import json

def format_to_json(financial_data):
    """
    Formats the extracted financial data into a structured JSON format.
    """
    formatted_data = {
        "company_name": financial_data.get("company_name", "N/A"),
        "report_date": financial_data.get("report_date", "N/A"),
        "net_profit": financial_data.get("net_profit", "N/A"),
        "revenue": financial_data.get("revenue", "N/A"),
        "total_assets": financial_data.get("total_assets", "N/A"),
        # Add other fields as needed
    }
    return json.dumps(formatted_data, indent=4)

if __name__ == "__main__":
    financial_data = {
        "company_name": "ABC Corp",
        "report_date": "2025-01-01",
        "net_profit": "5000000",
        "revenue": "20000000",
        "total_assets": "80000000"
    }
    formatted_json = format_to_json(financial_data)
    print(formatted_json)
