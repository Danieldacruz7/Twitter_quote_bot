# Twitter_quote_bot
A project for webscraping Goodreads for quotes, and automatically posting them on Twitter. 

This was a fun project to practice webscraping using BeautifulSoup, parsing through webpage contents and interacting with Twitter API. The code is run indefinitely on pythonanywhere.com. You can find my implementation at https://twitter.com/PhilosClassica.

## Instructions:
1. Run the Webscraper.py. Add your own authors, and make sure to scan webpapge URLs to obtain the specific page ID. Add them to the author dictionary. After making HTTP requests, it will compile all quotes into a list. Once cleaned, it will then create text files with all the quotes that have been wrangled. 
2. Apply for Twitter API access. This will allow you to post quotes on Twitter without violating terms and conditions - like spamming. This should take a day or two.
4. Upload the text files and the main.py file onto pythonanywhere.com. This will run your code indefinitely on their servers. 

Note: Webpages can change. You may have to make alterations based on the changes of the webpages. 
