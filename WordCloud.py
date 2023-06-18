import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os
from PIL import Image
from stop_words import get_stop_words
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator, get_single_color_func


#read dataset
filepath = os.getcwd() + "\\Word Cloud\\" 

df = pd.read_excel(filepath + "Top 1000 Greatest Films.xlsx", sheet_name="Sheet1")
words = df['Title']
words = pd.Series.to_string(words)


#read shape image
shape = np.array(Image.open(filepath + "videocamera.jpg"))


#remove common words from word cloud
stopwords = get_stop_words('en')
stopwords.extend(["thou","thy","thee","dost","les"])
stopwords=set(stopwords)


#create wordcloud
wordcloud = WordCloud(max_words=50000,
                      stopwords=stopwords,
                      font_path='C:/Windows/Fonts/courbd.ttf',
                      prefer_horizontal=.7,
                      colormap='Reds',
                      min_font_size=5,
                      max_font_size=70,
                      background_color="Black",
                      width=3000,
                      height=3000,
                      margin=2,
                      collocations=False,
                      mask=shape,
                      repeat=False,
                      relative_scaling=0,
                      scale=1,
                      min_word_length=3,
                      include_numbers=False,
                      normalize_plurals=False,
                      font_step=1).generate(words)

print(wordcloud.layout_)

plt.figure(figsize=(30,30))
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()