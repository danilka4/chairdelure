import random

with open("./data/molly_train.txt") as f:
    words = [word for line in f for word in line.split(" ")]
with open("./data/molly_test.txt") as f:
    data = [line for line in f]


def random_guess(input):
    # Random word from the training data
    return random.choice(words)


def get_cases(data):
    cases = []
    for message in data:
        words = message.split()
        for i in range(len(words)):
            context = " ".join(words[:i])
            word = words[i]
            # cases.append((context, word, frequency))
            # json
            cases.append(
                {
                    "context": context,
                    "word": word,
                }
            )
    return cases


test_cases = get_cases(data)
results = [random_guess(case["context"]) for case in test_cases]
accuracy = sum(
    r == case["word"] for r, case in zip(results, test_cases)
) / len(test_cases)
print(f"Accuracy: {accuracy}")
