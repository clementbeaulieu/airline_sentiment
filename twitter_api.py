import re, tweepy, datetime, time, csv, html
from tweepy import OAuthHandler
from textblob import TextBlob
import utils
 
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self, args):
        '''
        Class constructor or initialization method.
        '''
        # Keys and Tokens from the Twitter Developper Console.
        consumer_key = args.consumer_key
        consumer_secret = args.consumer_secret
        access_token = args.access_token
        access_token_secret = args.access_token_secret
 
        # Attempt authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
            
        except:
            print("Error: Authentication Failed")
 
    # Cleaned Tweet (no link, @, etc...)
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    
    # Get a Tweet Sentiment using TextBlob
    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return analysis.sentiment.polarity, 'positive'
        elif analysis.sentiment.polarity == 0:
            return analysis.sentiment.polarity, 'neutral'
        else:
            return analysis.sentiment.polarity, 'negative'
 
    # Main function to fetch tweets and parse them
    def get_tweets(self, query, count, page, start, end):
        # empty list to store parsed tweets
        tweets = []
 
        try:
            for tweet in tweepy.Cursor(self.api.search, q=query, since=start, until=end, lang="en").items(count):
                
                # Dictionnary to store essential parameters of the parsed tweet
                parsed_tweet = {}

                #parsed_tweet['date'] = tweet.created_at
                parsed_tweet['text'] = html.unescape(tweet.text).replace('\n', ' ').replace('\r', '')
                parsed_tweet['sentiment_polarity'], parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                # Checking if no retweet
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            return tweets
 
        except tweepy.TweepError as e:
            print("Error : " + str(e))

    def writeToCSV(self, args):
        with open(args.file, 'a', newline='') as csvfile:    
            csvWriter = csv.writer(csvfile)
            tweets = self.get_tweets(query = args.query, count=args.count, page = args.page, start=args.start, end=args.end)

            if tweets==None:
                print('No Tweets')
            else:
                for tweet in tweets:
                    csvValue = tweet['text'], tweet['sentiment_polarity'], tweet['sentiment']
                    csvWriter.writerow(csvValue)

            # picking positive tweets from tweets
                ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
                positivePercent = 100*len(ptweets)/len(tweets)
            # percentage of positive tweets
                print("Positive tweets percentage:",positivePercent," %")
            # picking negative tweets from tweets
                ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
                negativePercent = 100*len(ntweets)/len(tweets)
            # percentage of negative tweets
                print("Negative tweets percentage: ",negativePercent," %")

                neutralPercent = 100*(len(tweets) - (len(ntweets) + len(ptweets)))/len(tweets)
            # percentage of neutral tweets
                print("Neutral tweets percentage:",neutralPercent,"%")
        csvfile.close()
 
def fetch_tweets(args):
    # creating object of TwitterClient Class
    api = TwitterClient(args)

    if args.real_time:
        while True:
            api.writeToCSV(args)
            time.sleep(args.sleep_time)
    else:
        api.writeToCSV(args)