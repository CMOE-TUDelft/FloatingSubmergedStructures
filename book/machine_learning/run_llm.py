import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, BitsAndBytesConfig
import gradio as gr


quant_config = BitsAndBytesConfig(load_in_8bit=True)
#
# gr.load_chat("http://localhost:11434/v1/", model="phi3", token="***").launch(share=True)

# Load your merged model
model_name = "microsoft/phi-3-mini-128k-instruct"
# model = AutoModelForCausalLM.from_pretrained("merged_model", device_map="auto", weights_only=True)
# tokenizer = AutoTokenizer.from_pretrained("merged_model")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quant_config,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.to("cuda")

# Create pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Gradio interface
def generate_text(prompt):
    output = pipe(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
    return output[0]["generated_text"]

gr.Interface(fn=generate_text, inputs="text", outputs="text").launch()