# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:58:42 2024

@author: CERN
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:45:14 2024

@author: CERN
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:26:16 2024

@author: CERN
"""

#import SW_Web_Scraper.main as scrape


import requests
from instabot import Bot

import time as t

import os

from PIL import Image, ImageDraw, ImageFont
import PIL


import textwrap
import math
import numpy as np

import warnings
warnings.filterwarnings("ignore")

path = "E:\Meme bot\Mischief\config\sticker_it_2_the_man_uuid_and_cookie.json"
dummy_folder = "E:\Meme bot\Mischief\dummy_folder"

if os.path.exists(dummy_folder) is False: 
    os.mkdir(dummy_folder)
else:
    pass

from bs4 import BeautifulSoup

from selenium import webdriver


import spacy

nlp = spacy.load("en_core_web_sm")


def summary(text):
    # extractive summary by word count

    # tokenize
    doc = nlp(text)

    # create dictionary
    word_dict = {}
    # loop through every sentence and give it a weight
    for word in doc:
        word = word.text.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # create a list of tuple (sentence text, score, index)
    sents = []
    # score sentences
    sent_score = 0
    for index, sent in enumerate(doc.sents):
        for word in sent:
            word = word.text.lower()
            sent_score += word_dict[word]
        sents.append((sent.text.replace("\n", " "), sent_score/len(sent), index))
    length = int(len(sents)/4)
        # sort sentence by word occurrences
    sents = sorted(sents, key=lambda x: -x[1])
    # return top n
    sents = sorted(sents[:length], key=lambda x: x[2])

    # compile them into text
    summary_text = ""
    for sent in sents[1:-2]:
        summary_text += sent[0] + " "
     
    return summary_text

def edit(image_path, title,category,subtitle):
    img = Image.open(r"E:\Meme bot\Mischief\template.png")
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype(r"C:\Users\CERN\Downloads\libre-franklin\fonts\TTF\LibreFranklin-ExtraBold.ttf", size=60)
    
    

  

    
    position = (1200,15)  
    box_width = 400
    box_height = 400
    font_size = 10
    
    


    # Convert text to uppercase
    text = title
    
    wrap_width = 15

    # Wrap the text
    lines = textwrap.wrap(text, width=wrap_width)

    # Calculate the height of the text to adjust if it doesn't fit
    while True:
        total_text_height = sum([font.getsize(line)[1] for line in lines])
        if total_text_height <= box_height:
            break
        font_size -= 1
        font = ImageFont.truetype(r"C:\Users\CERN\Downloads\libre-franklin\fonts\TTF\LibreFranklin-ExtraBold.ttf", size=font_size)
        
        lines = textwrap.wrap(text, width=wrap_width)

    # Draw each line of text
    y_text = position[1]
    for line in lines:
        width, height = draw.textsize(line, font=font)
        draw.text(((position[0] + box_width - width) / 2, y_text), line, font=font, fill="black")
        y_text += height

    
    
    position = (1100,400)  
    box_width = 500
    box_height = 200
    
    
    font_size = 30

    wrap_width = 15

    # Convert text to uppercase
    text = subtitle

    # Wrap the text
    lines = textwrap.wrap(text, width=50)

    # Calculate the height of the text to adjust if it doesn't fit
    while True:
        total_text_height = sum([font.getsize(line)[1] for line in lines])
        total_text_width = np.array([font.getsize(line)[0] for line in lines]).max()
        
        if total_text_width <= box_width:
            break
        font_size -= 1
        font = ImageFont.truetype(r"C:\Users\CERN\Downloads\libre-franklin\fonts\TTF\LibreFranklin-Light.ttf", size=font_size)
        
        lines = textwrap.wrap(text, width=50)

    # Draw each line of text
    y_text = position[1]
    for line in lines:
        width, height = draw.textsize(line, font=font)
        draw.text(((position[0] + box_width - width) / 2, y_text), line, font=font, fill=(25,25,25))
        y_text += height

    photo = Image.open(image_path)
    photo = photo.resize((455,455))
    
    img.paste(photo, (9,27))
    
    
    font = ImageFont.truetype(r"C:\Users\CERN\Downloads\libre-franklin\fonts\TTF\LibreFranklin-ExtraBold.ttf", size=60)
    draw.rectangle(((9,360),(463,427)),fill=(255,0,0))
    draw.text((25, 360), category, font=font, fill=(255, 255, 255))
  
    
    img.resize((1080,566))
    
    img = img.convert("RGB")

    
    img.save(image_path + '.jpg')
    os.remove(image_path)
    img.show()
    

    
    


def get_links():

    # Make a request
    page = requests.get(
        "https://socialistworker.co.uk/")
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Create top_items as empty list
    all_links = []
    
    # Extract and store in top_items according to instructions on the left
    links = soup.select('a')
    for ahref in links:
        text = ahref.text
        text = text.strip() if text is not None else ''
    
        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        all_links.append({"href": href, "text": text})
    
    #print(all_links)
    
    
    
    # List to store links with text 'News'
    news_links = []
    
    # Iterate over the response data
    for link_info in all_links:
        # Check if the 'text' key contains 'News'
        if link_info['href'].endswith('/'):
            if 'News' in link_info['text']:
                # Add the link to the list
                news_links.append(link_info['href'])
            elif link_info['text'] == '':
                # Add the link to the list
                news_links.append(link_info['href'])
    
    
    good_links = []
    # Print the news links
    for link in news_links:
        if link.endswith('uk/news/') == False:
            if link.endswith('https://socialistworker.co.uk/marxismfestival/') == False:
                if link.endswith('https://socialistworker.co.uk/breakfast-in-red/') == False:
                    if link.endswith('https://socialistworker.co.uk/') == False:
                        if link.endswith('https://www.instagram.com/socialist_workers_party/') == False:
                            good_links.append(link)
                            
    return good_links


username='sticker_it_2_the_man'
password='sticker'

if os.path.isfile(path):
    os.remove(path)

bot = Bot()
bot.login(username=username,
            password=password)

def caption(text,title,url):
    hashtags = '\n  #socialism #palestine #revolution #transrights #marxism #communism #peace #solidarity'
    
    caption = title + '\n \n' + text + 'Read the full article at: ' + url + '\n \n'+  hashtags 
    
    return caption

def get_image(url):
    img_data = requests.get(url).content
    filename = url.replace('/','') + '.png'
    filename = filename.replace(':','-')
    with open(dummy_folder + '/' + filename,'wb') as f:
        f.write(img_data)
        
    
    im = Image.open(dummy_folder + '/' + filename)
    newsize = (1080,566)
    im1 = im.resize(newsize)
    im1 = im1.convert("RGB")
    os.remove(dummy_folder + '/' + filename)
    im1.save(dummy_folder + '/' + filename)
    
    
    


            
            
def main():
    urls = get_links()
    # URL to scrape
    
    
    
    for url in urls:
        MATCH = False
        with open(r"E:\Meme bot\Mischief\urls.txt",'r') as f:
            veto = f.read().split('\n')
        for v in veto:
            if url == v:
                MATCH = True
        if MATCH == False:
            try:
              
                # Set up Selenium webdriver for Edge
                driver = webdriver.Edge()
                # Load the webpage
                driver.get(url)
                
                # Get the page source after JavaScript has rendered it
                page_source = driver.page_source
                
                # Close the Selenium webdriver
                driver.quit()
                
                
                
                # Parse the HTML using BeautifulSoup
                soup = BeautifulSoup(page_source, 'html.parser')
                
                # Find all image tags
                images = soup.find_all('img')
                
                # Extract image URLs
                image_urls = [img['src'] for img in images if 'src' in img.attrs]
                
                txt = summary(soup.body.text)
                
                title = soup.title.text
                
                captn = caption(txt,title,url)
                
                article_text = str(soup.body.text).strip()
                
                # Define the phrase to search for
                phrase = str(soup.title.text).strip()
                
                # Split the article text using the phrase as a delimiter
                parts = article_text.split(phrase)
                
                
                if len(parts) > 1:
                    # Extract the words before and after the phrase
                    category = parts[0].strip().split('\n')[-1]
                    subheader = parts[1].strip().split('\n')[0]
                else:
                    category = 'News'
                    subheader = 'Read the full article at www.socialistworker.co.uk'
                if category == 'Palestine 2023-24':
                    category = 'Palestine'
                elif category == 'General Election 2024':
                    category = 'Election'
                elif category == 'Reviews & Culture':
                    category = 'Culture'
                    
                    
                
                get_image(image_urls[2])
                
                files = os.listdir(dummy_folder)
                
                for name in files:
                    
                    edit(dummy_folder + '/' + name,title,category,subheader)
                   
                    bot.upload_photo(dummy_folder + '/' + name + '.jpg',caption=captn)
                    os.remove(dummy_folder + '/' + name + '.REMOVE_ME')
                    rnd = np.random.normal(2000,100)
                    t.sleep(rnd)
                
            except:
                files = os.listdir(dummy_folder)
                for name in files:
                    os.remove(dummy_folder + '/' + name)
                
            with open(r"E:\Meme bot\Mischief\urls.txt",'a') as f:
                f.write(url)
                f.write('\n')
            
            
    
            
        
            
            
    
            
        
while True:
    main()
