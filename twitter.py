import tweepy

from database import ConnectionFactory

TWITTER_APP_KEY = 'Xrg9vh1qY5VVLynuflDBlJWza'
TWITTER_APP_SECRET = 'gNCxHsfEJF61h4lXyvc33YtwcSTq8l3FHWD96bMHR5483JIg68'
TWITTER_KEY = '2373607303-EUazPZlTqcbAEZYar5rMeLopnTlcl9XGjaU935A'
TWITTER_SECRET = 'bcQO93Og3XAPSNuaY5Qw4VSRhVugJT7qHSbKa0ZfPCALX'

class StreamListener(tweepy.StreamListener):

    def __init__(self):
        super(StreamListener, self).__init__()
        self._conn = ConnectionFactory().getConnectionThesis()
        self._conn.set_charset('utf8mb4')
        self._cursor = self._conn.cursor()


    def on_status(self, status):
        if (status.lang == "en") and (not status.retweeted) and ('RT @' not in status.text):

            try:
                if len(status.text) != 0 and len(status.extended_entities['media']) == 1 and status.extended_entities['media'][0]['type'] == 'photo':
                    screenName = status.author.screen_name
                    date = status.created_at
                    text = status.text.replace(status.extended_entities['media'][0]['url'], '')
                    image = status.extended_entities['media'][0]['media_url_https']
                    url = status.extended_entities['media'][0]['expanded_url']

                    print(screenName)
                    print(date)
                    print(text)
                    print(image)
                    print(url)

                    self._cursor.execute("INSERT INTO twitter (screen_name, date, text, image_url, url) VALUES (%s, %s, %s, %s, %s)", (screenName, date, text, image, url))

            except AttributeError:
                pass

    def on_error(self, status_code):
        if status_code == 420:
            return False

auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)

api = tweepy.API(auth)

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#stream.sample()
stream.filter(locations=[117.17427453, 5.58100332277, 126.537423944, 18.5052273625])
# stream.filter(track=['#humor', '#sarcasm'])