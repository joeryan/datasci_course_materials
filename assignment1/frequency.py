import sys
import json


def read_tweets(fp):
    """ (file) -> list of str
        given a file of tweets, return a list of strings containing
        each tweet's text
    """
    tweets = []
    for line in fp.readlines():
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            tweets.append((tweet['text']))
    return tweets


def count_terms(tw, terms):
    """ (str, dict) -> int
        modify dictionary of terms and individual counts and return the count
        of terms in this tweet
    """
    term_count = 0
    max_freq = 0
    for tweet in tw:
        for word in tweet.split():
            if word in terms:
                terms[word] += 1
            else:
                terms[word] = 1
                term_count += 1
           
    
    return term_count


def main():
    tweet_file = open(sys.argv[1])
    tweets = read_tweets(tweet_file)
    
    
   
    terms = {}

    # get number of terms in each tweet, add new terms to dict & increase val
    term_count = count_terms(tweets, terms)
     
    for key in terms:
        # print out each term and the frequency
        term_freq = (float(terms[key])) / (float(term_count))
        print key.encode('utf-8'), term_freq
        


if __name__ == '__main__':
    main()

