import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def load_sentiment(fp):
    """ (File) -> dict

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
    """ (file) -> list of str
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
    """ (list of str, dict) -> float
        if a word in the tweet is in the dict, then add the value to mood
        otherwise sentiment value is 0
    """
    mood = 0.0
    for key in sentiments.keys():
        if key in  tw:
            mood += sentiments[key]
    return mood

def split_tweet(tw):
    """ (str) -> list of str
        splits a single string into a list of strings, each list item a seperate
        word containing english characters
    """
    tweet = ''
    for word in ((tw.lower()).encode('utf-8')).split():
        if word.isalpha():
            tweet = tweet + word + ' '
    tweet = tweet.split()
    return tweet

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiments = load_sentiment(sent_file)
    all_tweets = read_tweets(tweet_file)
    

    for tweet in all_tweets:
        tw = split_tweet(tweet)
        tweet_mood_val = tweet_mood(tw, sentiments)
        for term in tw:
            if term not in sentiments.keys():
                term_mood = tweet_mood_val 
                sentiments[term] = term_mood
                print term, term_mood
        
    
    
if __name__ == '__main__':
    main()
