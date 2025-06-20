import urllib.request
import json

# Example REST API endpoint - GitHub API to get user information
url = "https://api.github.com/users/octocat"

print("Making request to:", url)

try:
    # Make the HTTP request
    response = urllib.request.urlopen(url)
    
    # Read the response data
    data = response.read()
    
    # Parse the JSON response
    user_info = json.loads(data)
    
    print(f"Status Code: {response.status}")
    print(f"Response length: {len(data)} characters")
    print("\nUser Information:")
    print(f"Username: {user_info['login']}")
    print(f"Name: {user_info['name']}")
    print(f"Location: {user_info['location']}")
    print(f"Public repos: {user_info['public_repos']}")
    print(f"Followers: {user_info['followers']}")
    print(f"Created at: {user_info['created_at']}")
    
except urllib.error.URLError as e:
    print(f"Error making request: {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
except KeyError as e:
    print(f"Missing key in response: {e}")

# Example with query parameters
print("\n" + "="*50)
print("Example with query parameters:")

# GitHub API to search repositories
search_url = "https://api.github.com/search/repositories?q=python&sort=stars&order=desc"

print("Making request to:", search_url)

try:
    response = urllib.request.urlopen(search_url)
    data = response.read()
    search_results = json.loads(data)
    
    print(f"Total repositories found: {search_results['total_count']}")
    print("\nTop 3 Python repositories by stars:")
    
    for i, repo in enumerate(search_results['items'][:3], 1):
        print(f"{i}. {repo['name']} by {repo['owner']['login']}")
        print(f"   Stars: {repo['stargazers_count']}")
        print(f"   Description: {repo['description']}")
        print()
        
except urllib.error.URLError as e:
    print(f"Error making request: {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
