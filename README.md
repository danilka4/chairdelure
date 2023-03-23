# chairdelure
Virginia Tech Capstone Project

If using `extract_messages.sh`, then put your discord data `package.zip` in your data folder.
That way it is not tracked by git and the shell script works.

## Development

1. Make sure you are running in a Python 3.10 virtual environment (e.g., `python3.10 -m venv .env`)
2. Activate it (e.g. `source .env/bin/activate`)

```shell
(.env) $ make install-dev
```

## Models

The model for the PCA can be found in the notebooks directory while the Markov model can be found in the test directory as "test.py"
