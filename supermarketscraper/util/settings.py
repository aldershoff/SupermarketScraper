"""
Global settings for the scraper. Also defining version numbers here
"""
# Verbose debug logging
verbose = False
debugging = False

# Database
mongoUrl = 'mongodb://localhost:27017/'
dbname = 'SupermarketScraper'
collection = 'data'
metacollection = 'metadata'

# Requests
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

# Parsing
maxErrors = 3 # Max errors per discount
maxFailedDiscounts = 5 # Max failed discounts per supermarket

"""
Applications specific static data
"""
version = '1.0.3'
url = 'https://github.com/tonsmets/SupermarketScraper'

def print_info():
	print("# =============================================================================== #")
	print("#     __                            __                                      ")
	print("#    / _\ _   _  _ __    ___  _ __ / _\  ___  _ __  __ _  _ __    ___  _ __ ")
	print("#    \ \ | | | || '_ \  / _ \| '__|\ \  / __|| '__|/ _` || '_ \  / _ \| '__|")
	print("#    _\ \| |_| || |_) ||  __/| |   _\ \| (__ | |  | (_| || |_) ||  __/| |   ")
	print("#    \__/ \__,_|| .__/  \___||_|   \__/ \___||_|   \__,_|| .__/  \___||_|   ")
	print("#               |_|                                      |_|                ")
	print("#   URL:", url)
	print("#   VERSION:", version)
	print("# =============================================================================== #\n")