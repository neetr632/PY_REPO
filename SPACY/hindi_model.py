import spacy

# Create a blank Hindi model
nlp = spacy.blank("hi")

# Add the 'ner' pipeline to the blank model
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("feature-extraction", model="monsoon-nlp/hindi-bert")   
# Load model directly
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("monsoon-nlp/hindi-bert")
model = AutoModel.from_pretrained("monsoon-nlp/hindi-bert")