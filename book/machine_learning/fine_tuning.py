from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from peft import get_peft_model, LoraConfig, TaskType
import numpy as np
from datasets import Dataset
from peft import PeftModel

import torch
print(torch.cuda.is_available())  # Should print True if CUDA is set up correctly

model_name = "MBZUAI/MobiLlama-05B"
# Load the model configuration first
config = AutoConfig.from_pretrained(model_name)

# Load the model using the correct configuration
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

loaded = np.load('data/text.npz')
text = loaded['a']
print(text)

text_data = [{"text": t} for t in text]
print(text_data)
dataset = Dataset.from_list(text_data)

def tokenize_and_add_labels(example):
    encoding = tokenizer(example["text"], truncation=True, padding="max_length", max_length=512)
    encoding["labels"] = encoding["input_ids"]  # Set labels as the same as input_ids for causal LM
    return encoding

tokenized_dataset = dataset.map(tokenize_and_add_labels)

from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./mobilama-lora",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    num_train_epochs=3,
    learning_rate=2e-4,
    logging_dir="./logs",
    save_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator,  # you may need to define a data_collator
    tokenizer=tokenizer,
    label_names=["input_ids"],  # explicitly set label_names
)

trainer.train()

# # Load base model and LoRA adapter
# base_model = AutoModelForCausalLM.from_pretrained(model_name)
# peft_model = PeftModel.from_pretrained(model, "-academic/checkpoint-3")
#
# # Merge LoRA into base model
# merged_model = peft_model.merge_and_unload()
# merged_model.save_pretrained("merged_model_2")
# tokenizer.save_pretrained("merged_model_2")
