from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load base model and LoRA adapter
model_name = "MBZUAI/MobiLlama-05B"
base_model = AutoModelForCausalLM.from_pretrained(model_name)
peft_model = PeftModel.from_pretrained(base_model, ".mobilama-lora")
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Merge LoRA into base model
merged_model = peft_model.merge_and_unload()
merged_model.save_pretrained("merged_model")
tokenizer.save_pretrained("merged_model")
