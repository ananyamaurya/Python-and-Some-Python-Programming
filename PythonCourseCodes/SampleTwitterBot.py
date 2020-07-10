import tweepy

from TwitterKeys import api_key, api_secret, access_token, access_secret

auth = tweepy.OAuthHandler(api_key(), api_secret())
auth.set_access_token(access_token(), access_secret())

api = tweepy.API(auth)
user = api.get_user("AprajitatijarpA")
user_me = api.me()
x = api.friends(user.id)
varun = api.get_user('varun_bha000')
api.send_direct_message(varun.id, "this is a test message")

stuff = api.user_timeline(screen_name = 'AprajitatijarpA', count = 10, include_rts = True)
for status in stuff:
    print (status._json["text"])
    print("\n\n\n")

