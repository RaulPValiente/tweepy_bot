# Twitter Retweet Bot

This Python program utilizes the Tweepy library to search for tweets containing a specific keyword on Twitter and retweet them. It is designed to be used with a Twitter developer account and the appropriate API keys.

## Requirements

- Python 3.x
- Tweepy library

## Installation

1. Clone or download this repository.
2. Install the Tweepy library using pip:
3. Replace the placeholder credentials in the code with your own Twitter API credentials.

## Usage

1. Run the program in your preferred Python environment.
2. The program will search Twitter for tweets containing the specified keyword.
3. It will then retweet a maximum number of tweets (specified by `maxNumberOfTweets`) that match the search query.

## Configuration

- `CONSUMER_KEY`: Your Twitter app's consumer key.
- `CONSUMER_SECRET`: Your Twitter app's consumer secret.
- `ACCESS_TOKEN`: Your Twitter account's access token.
- `ACCESS_TOKEN_SECRET`: Your Twitter account's access token secret.
- `search`: The keyword to search for on Twitter.
- `maxNumberOfTweets`: The maximum number of tweets to interact with.

## Disclaimer

This program is provided as-is. Use it responsibly and ensure compliance with Twitter's API usage policies and guidelines.

## Note

Please note that depending on the usage limits and restrictions of the Twitter API, you may need elevated permissions or access levels which may not be available with the free tier.