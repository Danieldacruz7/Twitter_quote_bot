import tweepy
import time
import random
from Webscraper import author_dictionary

"""
    The consumer key and secret are provided by Twitter
    when application for API is approved. 
    
    Each key and secret are unique. 
    Replace x's with your own. 
"""
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

key = "xxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

"""Below is the code for using Twitter API"""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

author_list = []
for i in author_dictionary:
    author_list.append(i)
number_of_authors = len(author_list)

def automate_tweet(quotes_file, name_in_list):
    """Function for sending Tweet via API. """
    api.update_status('{}\n\n - {}'.format(quotes_file[y], name_in_list))

def test_tweet(quotes_file, name_in_list):
    """Function is used to test the output of each tweet. """
    print("{}\n\n - {}".format(quotes_file[y], name_in_list))

"""
    Main portion of tweet automation. 
    This code is hosted on pythonanywhere.com.
    
    A while loop is implemented for continous deployment,
    and is scheduled to tweet automatically every 6 hours.  
    It will randomly select a file of quotes, and select a random 
    quote from the aforementioned text file. 
"""

while True:
    """This loop continues indefinitely. """

    x = random.randint(0, number_of_authors-1)
    author_name = author_list[x]
    file = r"{}.txt".format(author_name)
    with open(file, encoding='UTF-8') as f: # Encoding is necessary for normalization of text format.
        count = sum(1 for _ in f)
    y = random.randint(0, count-1)
    with open(file, encoding='UTF-8') as f:
        quote_file = f.readlines()
        automate_tweet(quote_file, author_name)
    time.sleep(21600) # Sleep puts while loop to rest for 6 hours.
