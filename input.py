import requests
import json

api_key = ""  
query = "gym"
url = f"https://api.unsplash.com/search/photos?query={query}&client_id={api_key}"

data = None
raw_urls = []

try:
    print(f"Requesting data for query: '{query}' from {url}")  
    response = requests.get(url)
    response.raise_for_status()  

    data = response.json()

    if 'results' in data and isinstance(data['results'], list):
        results_list = data['results']
        raw_urls = [f'"{item["urls"]["raw"]}&w=600"' for item in results_list if 'urls' in item and 'raw' in item['urls']]

        if not results_list:  
            print(f"API returned successfully, but no results found for the query: '{query}'")
        elif not raw_urls:  
            print(f"Results found for '{query}', but no 'raw' URLs were present in the data.")
    else:
        print("Error: 'results' key not found or is not a list in the API response.")
        if data:
            print("Received data structure:")
            print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"\nError during API request: {e}")
except json.JSONDecodeError:
    print(f"\nError: Could not decode JSON response. Status code: {response.status_code if 'response' in locals() else 'N/A'}")
    if 'response' in locals():
        print("Response text:", response.text)
except KeyError as e:
    print(f"\nError: Missing expected key {e} in the API response data.")
    if data:
        print("Received data structure:")
        print(json.dumps(data, indent=2))
except Exception as e:  
    print(f"\nAn unexpected error occurred: {e}")

print("\n--- Extracted Raw Image URLs (600px width) ---")

if raw_urls:
    print("[")
    print(",\n".join(raw_urls))  
    print("]")
else:
    print("No raw URLs were extracted or available to print.")
