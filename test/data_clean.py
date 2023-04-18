import csv
from datetime import datetime
import json
import re

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

data = [row for row in data if row[0].year >= 2022]

# Cleaning methods
def remove_tags_links(s):
    s = re.sub(r"<(@|#)[!]?[0-9]+>", "", s)
    s = re.sub(r"(www|http[s]*)\S+\w?", "", s)
    return s

def is_not_wordle_message(s):
    return not re.match(r"Wordle [0-9]+.+", s)

data = [(timestamp, remove_tags_links(message)) for timestamp, message in data]
data = [row for row in data if is_not_wordle_message(row[1])]
data = [row for row in data if len(row[1]) > 0]

def to_prompt_response(message):
    message = message.split(' ')
    prompt = ' '.join(message[:len(message)//2])
    response = ' '.join(message[len(message)//2:])
    return prompt, response

data = [to_prompt_response(message) for _, message in data]

def to_dict(prompt, response):
    return {
        'instruction': 'Autocomplete',
        'input': prompt,
        'output': response
    }

data = [to_dict(prompt, response) for prompt, response in data]

with open(f'data/{filename}.json', 'w') as f:
    json.dump(data, f)
