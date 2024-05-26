# MarX
A project, using an Instagram API and web scraping to turn news articles into Instagram posts. Scraping images, headlines, sub-headlines and body of the text ,plus a little graphic design and natural language processing, aesthetic and informative instagram posts can be generated. This bot was developed using stories taken from www.socialistworker.co.uk , but could easily be adapted to pull from other sites.

# Dependencies

Instagram API is accessed through the python module instabot, which can be installed with 'pip install instabot'

The python module spacy is used for natural language processing (NLP), which can be installed with 'pip install spacy'

The specific NLP model used is 'en_core_web_sm', which can be installed with 'python -m spacy download en_core_web_sm'

Web scraping is done using the python module selenium, which also requires the microsoft edge web driver, or similar software for another browser. 
