import sys
import json


def read_tweets(fp):
    """ (file) -> list of dict
        given a file of tweets, return a list of strings containing
        each tweet's text
    """
    tweets = []
    for line in fp.readlines():
        tweet = json.loads(line)
        tweets.append(tweet)
    return tweets


def count_hashtags(tw, hashtags):
    """ (dict, dict) -> int
        modify dictionary of hashtags and individual counts and return the count
        of hashtags in this tweet
    """
    hashtag_count = 0
    for tweet in tw:
        if u'entities' in tweet.keys() and u'hashtags' in tweet[u'entities'].keys():
            for tags in tweet[u'entities'][u'hashtags']:
                if tags['text'] in hashtags.keys():
                    hashtags[tags['text']] += 1
                else:
                    hashtags[tags['text']] = 1
                    hashtag_count += 1
    return hashtag_count

def create_sorted_list(hashtags):
    """ (dict) -> descending list of list of [float, str]
        returns a sorted list of lists in descending order,
        [float value, str hashtag)
    """
    L_tags = []
    for key in hashtags.keys():
        L_tags.append([float(hashtags[key]), key])
    L_tags.sort(reverse=True)
    return L_tags

def print_top_of_list(L, num):
    """ (list of (float, str), int) -> None
        prints first num of tuples in format "str float"
    """
    if num > len(L):
        raise ArgumentError, 'Less than top number of items in list'
    for i in range(num):
        print L[i][1].encode('utf-8'), L[i][0]
        
def main():
    tweet_file = open(sys.argv[1])
    tweets = read_tweets(tweet_file)
    
    tops = 10
    hashtag_count = 0
    tags = {}

    # get number of terms in each tweet, add new terms to dict & increase val
    hashtag_count += count_hashtags(tweets, tags)

    tag_list = create_sorted_list(tags)
    print_top_of_list(tag_list, tops)
        


if __name__ == '__main__':
    main()

