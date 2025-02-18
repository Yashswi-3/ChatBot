from transformers import pipeline
import re

def extract_financial_data(text):
    # Load an improved financial NER model
    nlp_ner = pipeline(
        "ner",
        model="Jean-Baptiste/roberta-large-ner-english",  # Better for ORG extraction
        tokenizer="Jean-Baptiste/roberta-large-ner-english",
        grouped_entities=True  # ✅ Ensures full words are merged correctly
    )

    entities = nlp_ner(text)
    print("Extracted Entities:", entities)  # Debugging step

    financial_data = {
        "company_name": "N/A",
        "report_date": "N/A",
        "profit_before_tax": "N/A"
    }

    for entity in entities:
        entity_type = entity.get("entity_group", "")
        entity_text = entity["word"].replace("##", "")  # Fix token splitting

        if entity_type == "ORG":
            financial_data["company_name"] = entity_text
        elif entity_type == "DATE":
            financial_data["report_date"] = entity_text

    # Use regex to extract financial values
    profit_match = re.search(r"profit before tax.*?₹?([\d.,]+)", text, re.IGNORECASE)
    if profit_match:
        financial_data["profit_before_tax"] = profit_match.group(1)

    return financial_data

# Example Usage
sample_text = """
Eveready Industries India Ltd. released its financial report on 5th February 2025.
The profit before tax for the quarter was ₹86.25 Crores.
"""

result = extract_financial_data(sample_text)
print("Final Extracted Financial Data:", result)
