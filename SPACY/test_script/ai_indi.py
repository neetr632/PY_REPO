from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert")
model = AutoModelForSequenceClassification.from_pretrained("ai4bharat/indic-bert")

# Preprocess the text
text = "मेरा नाम नीरज है।"
inputs = tokenizer(text, return_tensors="pt")

# Get the model's predictions
outputs = model(**inputs)
predictions = outputs.logits.argmax(dim=-1)

# Print the predicted label (assuming a classification task)
print(predictions)