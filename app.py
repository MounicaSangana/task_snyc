import requests

# Hardcoded values
DATABASE_PASSWORD = "admin123456"
API_KEY = "sk-1234567890abcdef1234567890abcdef"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_to_api():
    """Function using hardcoded API key"""
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get("https://api.example.com/data", headers=headers)
    return response.json()

def get_database_connection():
    """Function with hardcoded database password"""
    connection_string = f"postgresql://admin:{DATABASE_PASSWORD}@localhost/mydb"
    print(f"Connecting with password: {DATABASE_PASSWORD}")
    return connection_string

if __name__ == "__main__":
    print("App with hardcoded secrets")
    print(f"Database Password: {DATABASE_PASSWORD}")
    print(f"API Key: {API_KEY}")