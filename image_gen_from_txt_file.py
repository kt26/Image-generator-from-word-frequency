#pip install wordcloud 


import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
            
    frequencies = {}
    
    for i in file_contents.lower().split():
        if i in frequencies.keys():
            frequencies[i]+=1
        elif i not in punctuations and i not in uninteresting_words:
            frequencies[i]=1
            
    
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_file("myfile.jpg")


f = open("my_txt.txt", "r")
file_contents = f.read()
f.close()

myimage = calculate_frequencies(file_contents)
f = open(myimage , "w+")
f.close()
