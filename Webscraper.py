from TwitterOOP import twitter_bot

"""
    Below is a dictionary for pages to be scraped. 
    You can replace names with your own, but be 
    sure to find page id. 
    
    NOTE: Webpages can change so make sure to check whether 
          page format has changed. 
"""
author_dictionary = {"mencius":"406382",
                     'socrates':'275648',
                     'heraclitus':'77989',
                     'marcus_tullius_cicero':'13755',
                     'epicurus':'114041',
                     'herodotus':'901',
                     'seneca':'4918776'
                     }


for x in author_dictionary.keys():
    """Displays options available for selection from dictionary. """
    print("- " + x.capitalize())


scraper = input("Whose quotes would you like to get?\n")
scraper = str(scraper).lower()
number_of_pages = int(input("How many pages would you like to scrap?")) # Make sure not to exceed number of available pages!

webscraper_bot = twitter_bot(name=scraper, page_id=author_dictionary.get(scraper)) #Object is created.

for i in range(number_of_pages):
    soup = webscraper_bot.get_page(i)
    quotes = webscraper_bot.get_quote(soup)

cleaned_quotes = webscraper_bot.quote_cleaner(quotes)
webscraper_bot.print_quotes(cleaned_quotes)
webscraper_bot.create_text_file(scraper, cleaned_quotes)