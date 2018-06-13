import requests

with open('pic1.jpg', 'wb') as handle:
    response = requests.get('https://pbs.twimg.com/media/Dd3UCPzUwAACVd4.jpg', stream=True)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)