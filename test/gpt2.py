from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

def train_and_evaluate_gpt2_model(train_dataset_path, test_dataset_path):
    # Load pretrained GPT-2 model and tokenizer
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Load train and test datasets
    train_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=train_dataset_path,
        block_size=128
    )

    test_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=test_dataset_path,
        block_size=128
    )

    # Create data collator for language modeling
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir="./gpt2_custom",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
        evaluation_strategy="epoch"
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
        eval_dataset=test_dataset
    )

    # Train and evaluate the GPT-2 model
    trainer.train()
    trainer.evaluate()

    # Save the tokenizer, the model configuration, and the model weights to the same directory
    tokenizer.save_pretrained("./gpt2_custom")
    model.config.save_pretrained("./gpt2_custom")
    model.save_pretrained("./gpt2_custom")

if __name__ == "__main__":
    train_dataset_path = "data/molly_train.txt"
    val_dataset_path = "data/molly_val.txt"
    train_and_evaluate_gpt2_model(train_dataset_path, val_dataset_path)
