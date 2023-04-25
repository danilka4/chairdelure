from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "./gpt2_custom"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_word_recommendations(prompt, num_recommendations=5, max_length=20):
    # Encode the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate text using the model
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=num_recommendations,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=1.0,
    )

    # Decode the generated text
    generated_text = [tokenizer.decode(token, skip_special_tokens=True) for token in output]

    return generated_text

prompt = "Molly's favorite activity is"
recommendations = generate_word_recommendations(prompt)

for idx, rec in enumerate(recommendations):
    print(f"Option {idx + 1}: {rec}")
