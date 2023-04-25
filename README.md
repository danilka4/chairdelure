# chairdelure
Virginia Tech Capstone Project

If using `extract_messages.sh`, then put your discord data `package.zip` in your data folder.
That way it is not tracked by git and the shell script works.

## Development

1. Make sure you are running in a virtual environment (e.g., `python3 -m venv .env`)
2. Activate it (e.g. `source .env/bin/activate`)

```shell
(.env) $ make install-dev
```

## Models

The model for the PCA can be found in the notebooks directory while the Markov model can be found in the test directory as "test.py."
Code on the discord bot can be found in the discord_bot directory.
Interaction with the gpt3 model can be found in "train_model.sh"

The one version of these open source/open source adjacent LLM's that we were able to run was [alpaca.cpp](https://github.com/antimatter15/alpaca.cpp).
Alpaca.cpp 
