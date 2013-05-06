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
        if 'delete' not in tweet.keys():
            if tweet['user']['location'] != None:
                tweets.append(tweet)
    return tweets

def tweet_mood(tw, sentiments):
    """ tweet_mood(str, dict) -> float
        if a word in the tweet is in the dict, then add the value to mood
        otherwise sentiment value is 0
    """
    mood = 0
    tweet = tw['text'].encode('utf-8').split()
    for key in sentiments.keys():
        if key in tweet:
            mood += sentiments[key]
    return mood

def limit_tweets_to_USA(twts, states):
    """ (list of dict, list of str) -> list of dict
        returns a subset of twts that only includes US tweets
    """
    
    USAtweets = []
    for tweet in twts:
        locale = tweet['user']['location'].split()
        if locale != [] and locale[-1].strip().upper() in states:
            USAtweets.append(tweet)
    return USAtweets

def update_state_mood(tweets, sentiments):
    """ (list of dicts, dict) -> dict
        returns a dict of state moods based on mood of tweets (based on sentiments
        file word moods) and the state of location,
        first limiting tweets to US states
    """
    state_moods = {'AK': 0, 'AL': 0, 'AR': 0, 'AZ': 0, 'CA': 0, 'CO': 0,
                   'CT': 0, 'DC': 0, 'DE': 0, 'FL': 0, 'GA': 0, 'HI': 0,
                   'IA': 0, 'ID': 0, 'IL': 0, 'IN': 0, 'KS': 0, 'KY': 0,
                   'LA': 0, 'MA': 0, 'MD': 0, 'ME': 0, 'MI': 0, 'MN': 0,
                   'MO': 0, 'MS': 0, 'MT': 0, 'NC': 0, 'ND': 0, 'NE': 0,
                   'NH': 0, 'NJ': 0, 'NM': 0, 'NV': 0, 'NY': 0, 'OH': 0,
                   'OK': 0, 'OR': 0, 'PA': 0, 'RI': 0, 'SC': 0, 'SD': 0,
                   'TN': 0, 'TX': 0, 'UT': 0, 'VA': 0, 'VT': 0, 'WA': 0,
                   'WI': 0, 'WV': 0, 'WY': 0}
    states = state_moods.keys()
    UStweets = limit_tweets_to_USA(tweets, states)
    for tweet in UStweets:
        mood = tweet_mood(tweet, sentiments)
        tweet_st = tweet['user']['location'].strip()[-2:].upper()
        state_moods[tweet_st] += mood
    return state_moods

def happiest_st(state_moods):
    """ (dict) -> str
        returns the two letter state that has the happiest rank in the dict
    """
    happiest_val = 0
    for key in state_moods:
        if state_moods[key] > happiest_val:
            happiest = key
            happiest_val = state_moods[key]
            
    return happiest


def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # load sentiments file into a dictionary
    sentiments = load_sentiment(sent_file)

    tweets = read_tweets(tweet_file)
    
    state_moods = update_state_mood(tweets, sentiments)
    happiest_state = happiest_st(state_moods)

    print happiest_state

if __name__ == '__main__':
    main()
