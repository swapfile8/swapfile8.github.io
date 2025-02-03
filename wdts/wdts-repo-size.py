import requests
def get_size(user, repo):
    resp = requests.get(f'https://api.github.com/repos/{user}/{repo}')
    if resp.status_code == 200:
        kb = resp.json()['size']
        print(f'Size: {round(kb/1024,1)}M')
