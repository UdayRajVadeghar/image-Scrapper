import requests
import json 
api_key = ""
query = "shirt"
url = f"https://api.unsplash.com/search/photos?query={query}&client_id={api_key}"


data = None 
raw_urls = []
regular_urls = []
small_urls = []
thumb_urls = []

try:
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json() 

    
    if 'results' in data and isinstance(data['results'], list):
        results_list = data['results']

        raw_urls = [item['urls']['raw'] for item in results_list if 'urls' in item and 'raw' in item['urls']]
        regular_urls = [item['urls']['regular'] for item in results_list if 'urls' in item and 'regular' in item['urls']]
        small_urls = [item['urls']['small'] for item in results_list if 'urls' in item and 'small' in item['urls']]
        thumb_urls = [item['urls']['thumb'] for item in results_list if 'urls' in item and 'thumb' in item['urls']]

        if not results_list:
            print(f"API returned successfully, but no results found for the query: '{query}'")

    else:
        print("Error: 'results' key not found or not a list in the API response.")
        if data:
            print("Received data structure:")
            print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"Error during API request: {e}")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON response from the API. Status code: {response.status_code}")
    print("Response text:", response.text) 
except KeyError as e:
     print(f"Error: Missing expected key {e} in the API response data.")
     if data: 
         print("Received data structure:")
         print(json.dumps(data, indent=2))


print("\n--- Extracted Image URLs ---")

print("\nRaw Image URLs:")
if raw_urls:
    for url in raw_urls:
        print(url)

    print("lasdasmdklaskldmaklmdaklmdaklmkl mklmk ")   
    for url in regular_urls:
        print(regular_urls)    
else:
    print("No raw URLs were extracted.")

