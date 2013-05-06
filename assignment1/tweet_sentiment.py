import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def load_sentiment(fp):
    """ load_sentiments(File) -> dict

        provided a file of tab delimited words and sentiment values
        returns a dictionary with words as keys and the associated sentiment
        values
    """
    
    sentiments = {}
    # create a dictionary of sentiments and their related float values
    for sentiment in fp.readlines():
        L = sentiment.split("\t")
        sentiments[L[0]] = float(L[1])
    return sentiments

def read_tweets(fp):
    """ read_tweets(file) -> list of str
        given a file of tweets, return a list of strings containing
        each tweet's text
    """
    tweets = []
    for line in fp.readlines():
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            tweets.append(tweet['text'])
    return tweets

def tweet_mood(tw, sentiments):
    """ tweet_mood(str, dict) -> float
        if a word in the tweet is in the dict, then add the value to mood
        otherwise sentiment value is 0
    """
    tweet = ''
    for ch in (tw.lower()).encode('utf-8'):
        if ch.isalpha() or ch == ' ':
            tweet = tweet + ch
            
    mood = 0.0
    tweet = tweet.split()
    for key in sentiments.keys():
        if key in  tweet:
            mood += sentiments[key]
            
    return mood

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # load sentiments file into a dictionary
    sentiments = load_sentiment(sent_file)

    tweets = read_tweets(tweet_file)

    for tweet in tweets:
        print tweet_mood(tweet, sentiments)
    

if __name__ == '__main__':
    main()
