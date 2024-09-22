from transformers import AutoTokenizer, AutoModel

# Specify a directory to save the model locally
local_model_path = "./ai4bharat_indic_bert"

# Download the model and tokenizer and save them to the specified path
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert", cache_dir=local_model_path)
model = AutoModel.from_pretrained("ai4bharat/indic-bert", cache_dir=local_model_path)

print("Model downloaded and saved locally.")
