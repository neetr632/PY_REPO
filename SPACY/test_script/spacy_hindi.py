import spacy
from spacy_transformers import Transformer
from transformers import AutoTokenizer, AutoModel

# Path to the local directory where the model is saved
local_model_path = "./ai4bharat_indic_bert"

# Load the tokenizer and model from the local directory
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
transformer_model = AutoModel.from_pretrained(local_model_path)

# Create a blank Hindi spaCy pipeline
nlp = spacy.blank("hi")

# Add the transformer model to the spaCy pipeline
transformer = Transformer(nlp.vocab, model=transformer_model)

# Add the transformer to the pipeline
nlp.add_pipe("transformer", config={"model": transformer})

# Process some text
doc = nlp("मेरा नाम नीरज है।")
for token in doc:
    print(token.text)
