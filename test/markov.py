# Markov model testing by Chris Bonner
import markovify

file_name = "output"

with open(f"../data/{file_name}_train.txt") as f:
    text = f.read()

training_model = markovify.NewlineText(text, state_size=3)

while True:
    args = input("To stop model, type [n]\nStart sentence (1-2 words): ")
    if args == "n":
        break
    try:
        output = training_model.make_sentence_with_start(args, max_chars=180)
        print(output)
    except Exception as e:
        if str(e).split()[-1] == args:
            print(f"Model did not return an output with start words '{args}'")
        else:
            print(f"Model returned an invalid run with start words '{args}'")
