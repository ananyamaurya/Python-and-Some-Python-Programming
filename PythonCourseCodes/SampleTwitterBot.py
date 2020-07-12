import tweepy
from time import time
from TwitterKeys import api_key, api_secret, access_token, access_secret

auth = tweepy.OAuthHandler(api_key(), api_secret())
auth.set_access_token(access_token(), access_secret())

api = tweepy.API(auth)
user = api.get_user("AprajitatijarpA")
# user_me = api.me()
# x = api.friends(user.id)
# for u in x:
#     print( u.name, u.screen_name, u.id)
# # varun = api.get_user('varun_bha000')
# # api.send_direct_message(varun.id, "this is a test message")
# #
stuff = api.user_timeline(user.screen_name, count=20, include_rts=True)

for s in stuff:
    print(s._json["text"])
    print("\n\n\n")


# def limit_handle(cursor):
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(1000)


# for tweet in tweepy.Cursor(api.search, 'ananya').items(2):
#     try:
#         tweet.favorite()
#         print('Tweet Liked')
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break
