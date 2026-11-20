import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:java+sort:stars"

headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "python-crash-course-app",
    # "Authorization": "Bearer YOUR-GITHUB-KEY",
}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dicts = r.json()

print(f"Total repositories: {response_dicts['total_count']}")
print(f"Completed results: {not response_dicts['incomplete_results']}")

repository_dicts = response_dicts["items"]
print(f"Repository returned: {len(repository_dicts)}")

print("\nReturned repositories overview:")
for repository_dict in repository_dicts:
    print(f"\nID: {repository_dict['id']}")
    print(f"Name: {repository_dict['name']}")
    print(f"Owner: {repository_dict['owner']['login']}")
    print(f"Stars: {repository_dict['stargazers_count']}")
    print(f"Url: {repository_dict['html_url']}")
    print(f"Created: {repository_dict['created_at']}")
    print(f"Last updated: {repository_dict['updated_at']}")
    print(f"Description: {repository_dict['description']}")
