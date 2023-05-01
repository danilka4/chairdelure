import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "./gpt2_custom"
print('Loading Tokenizer')
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
print('Loading Model')
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_word_recommendations(prompt, extra_tokens=5):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    # Check if input_ids is empty or contains only special tokens
    if input_ids.size(1) == 0 or all(token in tokenizer.all_special_ids for token in input_ids[0]):
        return ''

    max_length = len(input_ids[0]) + extra_tokens

    # Create attention_mask
    attention_mask = input_ids.ne(tokenizer.eos_token_id).long()

    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=False,
        top_k=20,
        top_p=1.0,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id,  # Set pad_token_id to eos_token_id
        attention_mask=attention_mask,  # Pass attention_mask
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

def get_cases(data):
    cases = []
    for message in data:
        words = message.split()
        for i in range(1,len(words)):
            context = ' '.join(words[:i])
            word = words[i]
            cases.append((context, word))
    return cases

def evaluate_accuracy(test_file_path):
    total_count = 0
    correct_count = 0

    with open(test_file_path, 'r') as test_file:
        lines = test_file.readlines()
        cases = get_cases(lines)
        total_lines = len(cases)
        
        for idx, (prompt, expected_word) in enumerate(cases):
            print('Prompt: ', prompt)
            print('Expected Word: ', expected_word)
            p_len = len(prompt.split(' '))
            print('Prompt Length: ', p_len)
            generated_text = generate_word_recommendations(prompt)
            print('Generated Text: ', generated_text)
            generated_text = generated_text.replace('-',' ').replace('_',' ').replace('\n',' ').split()
            try:
                generated_word = generated_text[p_len]
            except IndexError:
                generated_word = ''

            print('Generated Words: ', generated_word)
            
            total_count += 1
            if expected_word == generated_word:
                correct_count += 1
            
            progress = (idx + 1) / total_lines * 100
            print(f"Progress: {progress:.2f}% | {idx+1}/{total_lines} | Correct: {correct_count} / {total_count}")

    accuracy = correct_count / total_count
    return accuracy

test_file_path = "data/molly_test.txt"
print('Evaluating Accuracy')
accuracy = evaluate_accuracy(test_file_path)
print(f"\nAccuracy: {accuracy:.2%}")
