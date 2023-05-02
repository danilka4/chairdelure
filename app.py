import flask
import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "./gpt2_custom"
print("Loading Tokenizer")
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
print("Loading Model")
model = GPT2LMHeadModel.from_pretrained(model_name)

app = flask.Flask(__name__)


def molly(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    print('test')
    # Check if input_ids is empty or contains only special tokens
    if input_ids.size(1) == 0 or all(
        token in tokenizer.all_special_ids for token in input_ids[0]
    ):
        return ""

    max_length = len(input_ids[0]) + 5

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
    return generated_text[len(prompt):]

# Run input on model
@app.route("/model", methods=["POST"])
def run_model():
    # Get form data
    selected_model = flask.request.form.get("model")
    text = flask.request.form.get("text")

    # Run model
    if selected_model == "molly":
        output = molly(text)
    elif selected_model == "daniel":
        output = daniel(text)
    elif selected_model == "chris":
        output = chris(text)
    else:
        output = "Error: Invalid model"
    # Return output as JSON
    return flask.jsonify({"output": output})

# Show about page
@app.route("/about")
def about():
    return flask.render_template("about.html")


@app.route("/")
def hello():
    return flask.render_template("index.html")


app.run()
