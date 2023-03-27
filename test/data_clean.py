import csv
from datetime import datetime
import json

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

'''
convert str formatted 2023-01-13 21:21:11.750000+00:00 to datetime
'''
def to_time(str):
    str = str.split('+')[0].split('.')[0]
    # print(str)
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')

data = read_csv('data/molly.csv')
data = [row[1:3] for row in data[1:]]
data = [(to_time(timestamp),message) for timestamp, message in data]

data = [row for row in data if row[0].year >= 2022]

'''
turn string into prompt and response

does this by splitting on spaces and taking the first half as the prompt
and the remainder as the response
'''
def to_prompt_response(message):
    message = message.split(' ')
    prompt = ' '.join(message[:len(message)//2])
    response = ' '.join(message[len(message)//2:])
    return prompt, response

data = [to_prompt_response(message) for _, message in data]

def to_dict(prompt, response):
    return {
        'prompt': prompt,
        'completion': response
    }

data = [to_dict(prompt, response) for prompt, response in data]

with open('data/molly_data.json', 'w') as f:
    json.dump(data, f)