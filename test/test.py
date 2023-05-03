import markovify

with open("../data/output_train.txt") as f:
    text = f.read()

text_mod = markovify.Text(text)


for i in range(5):
    print(text_mod.make_sentence())

for i in range(3):
    print(text_mod.make_short_sentence(280))
