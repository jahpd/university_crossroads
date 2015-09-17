"""
Minimal Example
===============
https://github.com/amueller/word_cloud
"""

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, '47_Douta_Ignorancia.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud().generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
