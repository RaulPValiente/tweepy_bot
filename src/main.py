import tweepy


# Credentials
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Auth
auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

# Calling API using Tweepy
api = tweepy.API(auth)

#Search Twitter for tweets with this keyword
search = ""

#Maximum limit of tweets to be interacted with
maxNumberOfTweets = 10

print('Retweet Bot Started!')

# Iterating the search and retweeting
for tweet in tweepy.Cursor(api.search_tweets, q=search).items(maxNumberOfTweets):
    try:
        # Retweet
        tweet.retweet()
        print('Retweeted the tweet')
        
        # Like
        api.create_favorite(tweet.id)
        print('Liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break