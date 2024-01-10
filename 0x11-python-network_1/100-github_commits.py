#!/usr/bin/python3
"""
Please list 10 commits (from the recent to the oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    repo = argv[1]
    repo_owner = argv[2]
    x = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(repo_owner, repo)

    res = get(URL)
    json = res.json()

    for el in json:
        if x > 9:
            break
        sha = el.get('sha')
        author = el.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        x += 1
