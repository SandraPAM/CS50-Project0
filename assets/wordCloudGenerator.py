#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:41:59 2020

@author: Sandra

Script to build a WordCloud

For each language you must change lines:
    27 - "file = "
    46 - "words = re.findall"
    48 - "catchedStopWords"
    63 - "wc.to_file"
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
import re
import os

"""
0.1 Read file
"""
main_dir= os.getcwd() #Get current working directory
file ='/03_french.txt' #01_spanish, 02_english, 03_freanch, 04_lithuanian
    
text=''
with open(main_dir+file,'r', encoding='utf-8') as content_file:
    text = content_file.read()   
    
text = text.lower()

"""
0.2 Word list: skipping 'stopwords' and really short ones.
"""
# =============================================================================
# Regular expression: (general pattern that set a word)
# Spanish: [a-záéíóúñ]+
# English: [a-z]+
# French: [a-zàâçéèêëîïôûùüÿñæœ\']+
# Lithuanian: [a-ząčęėįšųū]+
# =============================================================================
#Look for ALL WORDS in the original text
words = re.findall('[a-zàâçéèêëîïôûùüÿñæœ\']+', text) 
#StopWords - Line '48' not working for Lihutanian language, use Line '49' instead
catchedStopWords = stopwords.words('french')  #spanish, english
#catchedStopWords = []
#Concatenate into a single text file
text =' '.join([word for word in words if word not in catchedStopWords and len(word)>3])


"""
0.3 WordCloud
"""
wc = WordCloud(background_color='white',width=1200,height=1000)

#Generate word cloud
wc.generate(text)

#Store to file
wc.to_file(main_dir+'/../src/french.png')
#Display the genereted word cloud
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')



