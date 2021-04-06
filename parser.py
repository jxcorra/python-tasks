import requests


if __name__ == '__main__':
    response = requests.get('https://www.hackingwithswift.com/samples/friendface.json')

    users = response.json()

    import pprint
    pprint.pprint(users)
