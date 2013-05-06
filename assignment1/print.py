import urllib2 as urllib
import json

##for page in range(1, 10):
##    print "Page number %d" %page
##    response = urllib.urlopen(("http://search.twitter.com/search.json?q=microsoft&page=" + str(page)))
##    results = json.load(response)["results"]
##    for i in range(len(results)):
##        print("From user: %s => %s") %(results[i]['from_user_name'], results[i]['text'])
##    


in_file = open('problem1.txt')
results = json.load(in_file)
print type(results)
