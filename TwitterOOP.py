from bs4 import BeautifulSoup
import requests

class twitter_bot:
    """Class created to scrape data from webpage. """
    def __init__(self, name, page_id):
        self.name = name
        self.page_id = page_id

    def get_page(self, iteration):
        """Function to make http request from Goodreads.com, and pull webpage contents. """
        page = requests.get("https://www.goodreads.com/author/quotes/" + self.page_id + "." + self.name + "?page={}".format(iteration))
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def get_quote(self, soup):
        """Function to parse webpage contents to find quotes. """
        short_descs = [i.get_text() for i in soup.select(".quoteText")]
        return short_descs

    def quote_cleaner(self, quotes):
        """Function to format quotes for easier addition to text file. """
        clean_quotes = []
        for i in range(len(quotes)):
            x = quotes[i].split()
            try:
                x = ' '.join(x)
                if len(x) > 240: # Tweets have a limit of characters per tweet (280). 240 is an arbitrary number
                    continue # Quotes longer than 240 are automatically excluded.
                else:
                    clean_quotes.append(x) # Quotes are added to a new list.
            except:
                continue
        return clean_quotes

    def print_quotes(self, cleaned_quotes):
        """Function is not necessary. Only to display quotes that will be added to a text file. """
        for i in cleaned_quotes:
            print(i)

    def create_text_file(self, name, cleaned_quotes):
        """Function to create a text file with specified name, and quotes are added. """
        with open(name.capitalize() + ".txt", 'w+', encoding="utf-8") as f:
            for i in cleaned_quotes:
                f.write(i + "\n")

