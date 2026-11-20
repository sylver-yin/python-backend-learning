import urllib.request


def test_status_code_urllib_method():
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    with urllib.request.urlopen(url) as response:
        assert response.status == 200


# TODO: Redo this via requests module, not urllib.
