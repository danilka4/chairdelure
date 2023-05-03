# chairdelure
Virginia Tech Capstone Project

If using `extract_messages.sh`, then put your discord data `package.zip` in your data folder.
That way it is not tracked by git and the shell script works.

# Running

1. Make sure you are running in a virtual environment (e.g., `python3 -m venv .env`)
2. Activate it (e.g. `source .env/bin/activate`)
3. Install the dependencies (e.g. `make install`)
4. Run the message extraction script (e.g. `./scripts/extract_messages.sh output.csv`)
5. Edit the name of your file in `test/data_clean.py` and run it (e.g. `cd test; python data_clean.py`)

## Markov Model - Chris
To run the markov model, change the file name in `test/markov.py` and run `cd test; python markov.py`. You will be given an output sentence based on 
your input "start words" for the model (1-2 words). To stop the model, type `n` into the input. Testing can be 

## GPT2 - Molly

When running `data_clean.py` create a txt file. In all files mentioned, update the file names to reflect your dataset. (Default value is `molly_{train/val/test}.txt`)

To train the model: `python3 ./test/gpt2.py`. This will save the model to `./gpt2_custom`

To run the default test: `python3 ./test/run.py`. This will give the accuracy of the model based on every permutation of messages in the text file.

To run the expiremental 3 word test: `python3 ./test/expirements.py`. This test generates three responses and checks to see if the right answer is in one of them.

## LLaMA User-LoRA Model - Daniel

If making your own train/test cases, use the process described in the GPT2 section with `data_clean.py` to create the needed txt files.

To run the LLaMA Model with custom LoRA user weights, it is recommended to run it inside google colab.
If following the colab notebook for this model (found in `notebooks/LoRa.ipynb`), essentially just follow all the steps in the "generation" section using a GPU.
First, download the appropriate transformers library, since the current one does not have LLaMA (yet). 
Then, download the LLaMA weights and add the LoRA user weights on top.
Daniel's are currently in a huggingface repo, otherwise upload your own and point the function to that.
Afterwards, it is a matter of calling `model.generate()` with some input text and the model will do its best to complete it.

# Non-ML Scripts

The model for the PCA can be found in the notebooks directory while the Markov model can be found in the test directory as "test.py."
Code on the discord bot can be found in the discord_bot directory.
Interaction with the gpt3 model can be found in "train_model.sh"

## Flask App

Run `appy.py`. Webpage will be at 127.0.0.1:5000
