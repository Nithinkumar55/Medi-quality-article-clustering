# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:35:34 2023

@author: nithi
"""

#web scrapping for single sheet

import os
os.chdir(r"C:\Users\nithi\OneDrive\Desktop\full stack data science & ai with chatgpt\9SEPTEMBER\26th-web scrapping (many xml files), R prog\25th,26th, - webscrapping\25th,26th, - webscrapping\14. NLP WEB SCRAPING\xml_single articles")

import xml.etree.ElementTree as ET

tree = ET.parse("769952.xml")
root = tree.getroot()

root = ET.tostring(root, encoding='utf8').decode('utf8')

root


import re, string, unicodedata
import nltk

from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = re.sub('  ','',text)
    return text

sample = denoise_text(root)
print(sample)



