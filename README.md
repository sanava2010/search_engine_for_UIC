# search_engine_for_UIC
#Download necessary libraries.
Libraries and packages such as nltk, PyQt5, bs4 (for BeautifulSoup), scrapy should be installed.
Python 3 should be installed.
#Place all the files in the working directory.
All the files should follow the same directory structure as given. 
To run the project, the working directory should be the same as the directory where main.py is installed. 
The scraping has already been done and all the scrapped output is present in output.json file. All preprocessing has also already been done.
The user should run the main.py file. 
#To run the scraper and to do preprocessing
1) Delete the existing output.json file.
2) If the user wants to scrape more documents, the following command should be run from the command line where the command line is opened in spiders folder.
'scrapy crawl uic_crawler -o output.json'
3) Move the output.json file to the same location as the main.py file.
4) Run preprocessing.py file to calculate the inverted index and generate the required pickle files. 
5) Run main.py


