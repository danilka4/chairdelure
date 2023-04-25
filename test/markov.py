import markovify

with open("../data/chris.txt") as f:
    text = f.read()

text_mod = markovify.Text(text)

for i in range(50):
    print(text_mod.make_sentence())
