import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

base_url = 'https://vnexpress.net/'

try:
    print("Fetching vnexpress.net...")
    response = requests.get(base_url, headers=headers, timeout=10)
    response.raise_for_status()
    
    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all links
    all_links = soup.find_all('a', href=True)
    seen_urls = set()
    
    print("Extracting links...")
    for link in all_links:
        href = link.get('href')
        text = link.get_text().strip()
        
        if href and href not in seen_urls:
            full_url = urljoin(base_url, href)
            print(f"\nText: {text}")
            print(f"URL: {full_url}")
            seen_urls.add(href)
    
    print(f"\nTotal unique links found: {len(seen_urls)}")
    
except requests.RequestException as e:
    print(f"Error fetching the webpage: {e}")
except Exception as e:
    print(f"Error parsing the webpage: {e}")
