import os
import requests
from dotenv import load_dotenv

# Environment variables load karein
load_dotenv()

class PhoneLookup:
    def __init__(self):
        self.api_key = os.getenv("ABSTRACT_API_KEY")
        self.url = "https://phoneintelligence.abstractapi.com/v1/"

    def fetch_info(self, number):
        if not self.api_key:
            return "❌ Error: API Key nahi mili! .env file check karein."
        
        params = {"api_key": self.api_key, "phone": number}
        
        try:
            response = requests.get(self.api_key, params=params) # Corrected logic
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Simple Output
            print(f"\n✅ Results for: {data.get('format').get('international')}")
            print(f"📍 Location: {data.get('location')}")
            print(f"🏢 Carrier:  {data.get('carrier')}")
            print(f"📱 Type:     {data.get('type')}")
            print(f"🌍 Country:  {data.get('country').get('name')}")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("--- Phone Info Repo (Abstract API) ---")
    target = input("Enter phone number with country code (e.g., +91...): ")
    
    bot = PhoneLookup()
    bot.fetch_info(target)
