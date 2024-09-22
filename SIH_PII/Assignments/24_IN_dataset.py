from faker import Faker
import random
import string
import re
import pandas as pd
# Initialize Faker
fake = Faker()
resultant_dataset = []
def random_uppercase_string(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def clean_phone_number(phone_number):
    digits = re.sub(r'\D', '', phone_number)  # Remove non-digit characters
    if len(digits) >= 10:
        return f"+91{digits[-10:]}"  # Return last 10 digits with +91 prefix
    return phone_number

def generate_pii():
    return {
        "Name": fake.name(),
        "Address": fake.address().replace("\n", ", "),  # Replace newlines in address for better formatting
        "Email": fake.email(),
        "Phone Number": clean_phone_number(fake.phone_number()),  # Format phone number
        "Aadhaar Number": f"{random.randint(100000000000, 999999999999)}",  # 12-digit Aadhaar number
        "PAN": f"{random_uppercase_string(5)}{random.randint(1000, 9999)}{random_uppercase_string(1)}",  # PAN format
        "Driving License": f"{random_uppercase_string(2)}-{random.randint(10000000000000, 99999999999999)}",  # Driving License format
        "Voter ID": f"{random_uppercase_string(2)}-{random.randint(1000000000, 9999999999)}"  # Voter ID format
    }

for _ in range(5000):
    pii_data = generate_pii()
    resultant_dataset.append(pii_data)
print("Sample PII Data:")
df = pd.DataFrame(resultant_dataset)
df.to_excel("output.xlsx", index=False)
