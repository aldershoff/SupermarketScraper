"""
Global settings for the scraper. Also defining version numbers here
"""
mongoUrl = 'mongodb://localhost:27017/'
dbname = 'SupermarketScraper'


"""
Applications specific static data
"""
version = '1.0.1'
url = 'https://github.com/tonsmets/SupermarketScraper'

def print_info():
	print("#===============================================================================#")
	print("#  __                            __                                      ")
	print("# / _\ _   _  _ __    ___  _ __ / _\  ___  _ __  __ _  _ __    ___  _ __ ")
	print("# \ \ | | | || '_ \  / _ \| '__|\ \  / __|| '__|/ _` || '_ \  / _ \| '__|")
	print("# _\ \| |_| || |_) ||  __/| |   _\ \| (__ | |  | (_| || |_) ||  __/| |   ")
	print("# \__/ \__,_|| .__/  \___||_|   \__/ \___||_|   \__,_|| .__/  \___||_|   ")
	print("#            |_|                                      |_|                ")
	print("# URL:", url);
	print("# VERSION:", version)
	print("#===============================================================================#\n")