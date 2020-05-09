#!/usr/bin/env python
"""
This file adapted from the Alice example at
https://github.com/amueller/word_cloud/blob/d1ec087a7f86e6dc14ed3771a9f8e84a5d384e0a/examples/masked.py
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read several arxiv preprints.
text1 = open(path.join(d, '1707.00391.txt')).read()
text2 = open(path.join(d, '1807.00461.txt')).read()
text3 = open(path.join(d, '1910.05625.txt')).read()

text = text1 + text2 + text3

# read the mask image
# hand-lettered by Sara :)
mask = np.array(Image.open(path.join(d, "mask.png")))


wc = WordCloud(background_color="white", max_words=3000, mask=mask,
               contour_width=3, contour_color='steelblue', width=1920, height=1080)

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "laura-raw.png"))
