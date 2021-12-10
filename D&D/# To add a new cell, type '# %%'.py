# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# For this exercise, you should start by reading in the text file produced from Exercise Three. This text file should already have the HTML code elements removed, 
# and primarily consist of text and other characters that we will remove through our processing. Store the input of your file in a string, 
# and convert the contents to lower case for consistency. 

f = open('hollywoodreviews.txt','r')
fileText = str(f.read().lower())
f.close()


# %%
# This week, we'll be using functions that we've already defined in our exercises. Try looking back through your code and notes from class. 
# Our first step is to import the regular expressions module and remove all non-alpha-numeric characters from the string, then save the string as an array of words ready for processing. 
# (Use the code in NormalizingText for reference)

def preprocess_text(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

word_bag = preprocess_text(fileText)
print(word_bag[0:50])


# %%
# Next, we'll use stop words to remove all the words that we don't want to include in our count. There are suggested words in this week's readings, 
# but you can also generate a custom list based on your topic. Define the stop words in an array, 
# and use a loop to remove any word in your bag of words that also appears on the stop words list (use the examples in Dictionaries for guidance.)

stop_words = ['is','a','on','the','in','aboutdoge','xca','xcb','x92','of','or','be','was','to','s','n','x88do','x8ad']

def removeStopWords(word_bag, stop_words):
    return [w for w in word_bag if w not in stop_words]

cleaned_words = removeStopWords(word_bag, stop_words)

print(cleaned_words[0:50])


# %%
# Now we're ready to count our words, and move from an array to a dictionary. Using the functions we've already built in the "Dictionaries.ipynb" file, 
# process your text by building a dictionary that zips words with their frequency, then removes redundancy by storing the data in the "dictionary" format.

def wordsToDictionary(word_bag):
    word_freq = [word_bag.count(word) for word in word_bag]
    return dict(list(zip(word_bag,word_freq)))

dict_words = wordsToDictionary(cleaned_words)

print(dict_words)


# %%
# Finally, explore what you can learn from this dictionary. Try: 
# A. Sorting your dictionary using our prebuilt method
def sortDictionary(words):
    aux = [(words[key], key) for key in words]
    aux.sort()
    aux.reverse()
    return aux

sort_dict = sortDictionary(dict_words)

# B. Printing the top five most frequent words from your data
x = 0
for pair in sort_dict:
    print(str(pair))
    x += 1
    if x==4:
        break

# C. Querying for certain key words and printing their frequency

print("Meme frequency: " + str(dict_words.get("meme")))
print("Tumblr frequency: " + str(dict_words.get("tumblr")))

# D. Comparing the relative frequency of words of interest

def compare_words(word_one, word_two):
    if not word_one in dict_words or not word_two in dict_words:
       print("Word(s) not found")
    elif dict_words[word_one] >  dict_words[word_two]:
        print(word_one + " appeared more often")
    elif dict_words[word_two] >  dict_words[word_one]:
        print(word_two + " appeared more often") 
    else:
        print("Words occurred with equal frequency")

compare_words("doge","meme")
compare_words("doge","fred")
compare_words("royalty","free")


