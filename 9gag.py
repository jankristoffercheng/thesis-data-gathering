# app.py

from nineapi.client import Client, APIException

client = Client()

try:
    client.log_in('jankristoffer96', 'Iamawesome1')
except APIException as e:
    print('Failed to log in:', e)
else:
    for post in client.get_posts(entry_types=['photo']):
        print(post.title)
        print(post.get_media_url())
    # last_post = None
    # for _ in range(5):
    #     posts = client.get_posts(olderThan=last_post)  # Pass `None` or ignore param to fetch first page.
    #     for post in posts:
    #         print(post.id, post.title)
    #     last_post = posts[-1]