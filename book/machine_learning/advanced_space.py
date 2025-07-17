from huggingface_hub import HfApi
repo_id = "Wauplin/my-cool-training-space"
api = HfApi()

# For example with a Gradio SDK
api.duplicate_space("huggingface/autotrain-advanced")