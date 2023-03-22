if [[ -z "$OPEN_API_KEY" ]]; then
    read -p "Open AI Key: " OPEN_API_KEY
fi
openai tools fine_tunes.prepare_data -f $1
# We will want to update to a more sofisticated model later
openai api fine_tunes.create -t data_prepared.jsonl -m ada