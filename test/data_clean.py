import csv
from datetime import datetime
import json
import re
import emoji

filename = 'molly'

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def to_time(str):
    str = str.split('+')[0].split('.')[0]
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')

data = read_csv(f'data/{filename}.csv')
data = [row[1:3] for row in data[1:]]
data = [(to_time(timestamp), message) for timestamp, message in data]

data = [msg for time, msg in data if time.year >= 2022]

# Cleaning methods
def remove_tags_links(s):
    s = re.sub(r"<(@|#)[!]?[0-9]+>", "", s)
    s = re.sub(r"(www|http[s]*)\S+\w?", "", s)
    return s

data = [remove_tags_links(message) for message in data]

def is_not_wordle_message(s):
    return not re.match(r"Wordle [0-9]+.+", s)

data = [message for message in data if is_not_wordle_message(message)]

def demojify(message):
    # Replace Discord emotes with names
    emote_pattern = r'<a?(:\w+:)\d+>'
    message = re.sub(emote_pattern, r'\1', message)
    # Replace Unicode emojis with names
    message = emoji.demojize(message, delimiters=(':', ':'))
    # Ensure spaces around emoji names without adding extra spaces
    message = re.sub(r'(?<=\w)(:[^:\s]+:)|(:[^:\s]+:)(?=\w)', r' \1\2 ', message)
    message = re.sub(r'\s{2,}', ' ', message).strip()
    return message

data = [demojify(message) for message in data]

def replace_regional_indicators(message):
    result = []
    for char in message:
        code_point = ord(char)
        if 0x1F1E6 <= code_point <= 0x1F1FF:
            result.append(chr(code_point - 0x1F1A5))
        else:
            result.append(char)
    return ''.join(result)

def replace_fancy(s):
    s = re.sub(r'“', '"', s)
    s = re.sub(r'”', '"', s)
    s = re.sub(r'‘', "'", s)
    s = re.sub(r'’', "'", s)
    s = re.sub(r'—', '-', s)
    s = re.sub(r'–', '-', s)
    s = re.sub(r'…', '...', s)
    # Replace non english characters with english characters
    s = re.sub(r'é', 'e', s)
    s = re.sub(r'å', 'a', s)
    # Replace independent regional indicator with letter
    s = replace_regional_indicators(s)
    return s

data = [replace_fancy(message) for message in data]

# Not all characters are ascii
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

data = [message for message in data if is_ascii(message)]

# Put spaces around punctuation
def add_spaces_around_punctuation(s):
    s = re.sub(r'([.,!?()])', r' \1 ', s)
    s = re.sub(r'\s{2,}', ' ', s)
    return s.strip()

data = [add_spaces_around_punctuation(message) for message in data]

# Remove extra spaces
def remove_extra_spaces(s):
    s = re.sub(r'\s{2,}', ' ', s)
    return s.strip()

data = [remove_extra_spaces(message) for message in data]

# lowercase
data = [message.lower() for message in data]

# Shuffle data
import random
random.seed(369)
random.shuffle(data)

# Split into a training, and test set
train = data[:int(len(data) * 0.8)]
test = data[int(len(data) * 0.8):]


# Get word frequencies
def get_word_frequencies(data):
    word_frequencies = {}
    for message in data:
        for word in message.split():
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1
    return word_frequencies

word_frequencies = get_word_frequencies(data)

# Take each message and create every case
# For example "Hello my name is Molly." ->
# - ("", "Hello")
# - ("Hello", "my")
# - ("Hello my", "name")
# - ("Hello my name", "is")
# - ("Hello my name is", "Molly")
# - ("Hello my name is Molly", ".")
def get_cases(data, frequencies):
    cases = []
    for message in data:
        words = message.split()
        for i in range(len(words)):
            context = ' '.join(words[:i])
            word = words[i]
            frequency = frequencies[word]
            cases.append((context, word, frequency))
    return cases

if input('Create unique cases?') == 'y':
    train_cases = get_cases(train)
    val_cases = get_cases(val)
    test_cases = get_cases(test)

    print(f'Train: {len(train_cases)}')
    print(f'Val: {len(val_cases)}')
    print(f'Test: {len(test_cases)}')

file_type = input('File Type: ')

if file_type == 'txt':
    with open(f'data/{filename}_train.txt', 'w') as f:
        f.write('\n'.join(train))
    with open(f'data/{filename}_test.txt', 'w') as f:
        f.write('\n'.join(test))
else:
    print('Invalid file type')
