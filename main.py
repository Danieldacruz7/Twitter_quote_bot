import tweepy # import library for interacting with Twitter
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
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Handles user authentication
auth.set_access_token(key, secret) # assigns access token to interact with API
api = tweepy.API(auth) # stores API information 

author_list = [i for i in author_dictionary]
number_of_authors = len(author_list)

def automate_tweet(quotes_file, name_in_list):
    """
    Retrieves quote and its author for the text file, 
    and uploads the data using the Twitter API. 

    Args: 
        quotes_file - the file containing a quote. 
        name_in_list - name of randomly selected author. 

    Returns: 
        None
    """
    api.update_status('{}\n\n - {}'.format(quotes_file[y], name_in_list))

def test_tweet(quotes_file, name_in_list):
    """
    Retrieves quote and its author for the text file, 
    and uploads the data without using the Twitter API. 

    Args: 
        quotes_file - the file containing a quote. 
        name_in_list - name of randomly selected author. 

    Returns: 
        None
    """
    print("{}\n\n - {}".format(quotes_file[y], name_in_list))

while True:
    """
    Main portion of tweet automation. 
    This code is hosted on pythonanywhere.com.
    
    A while loop is implemented for continous deployment,
    and is scheduled to tweet automatically every 6 hours.  
    It will randomly select a file of quotes, and select a random 
    quote from the aforementioned text file. 
    """

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
