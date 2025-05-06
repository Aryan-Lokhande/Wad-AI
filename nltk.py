#Write a program for the Information Retrieval System using appropriate NLP tools (such as
#NLTK, Open NLP, …)
#a. Text tokenization
#b. Count word frequency
#c. Remove stop words
#d. POS tagging

import nltk
from nltk import word_tokenize, FreqDist, pos_tag
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def text_tokenization(text):
    return word_tokenize(text)

def count_word_frequency(tokens):
    return FreqDist(tokens)

def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word.lower() not in stop_words]

def pos_tagging(tokens):
    return pos_tag(tokens)

# Get user input
text = input("Enter a sentence or a paragraph: ")

# Ask user which operation to perform
operation = input("Select operation (a. Tokenization, b. Word Frequency, c. Remove Stop Words, d. POS Tagging): ").lower()

# Perform the selected operation
if operation == 'a':    
    tokens = text_tokenization(text)
    print("Tokens:", tokens)
elif operation == 'b':
    tokens = text_tokenization(text)
    word_frequency = count_word_frequency(tokens)
    print("Word Frequency:", word_frequency)
elif operation == 'c':
    tokens = text_tokenization(text)
    tokens_without_stopwords = remove_stop_words(tokens)
    print("Tokens without Stop Words:", tokens_without_stopwords)
elif operation == 'd':
    tokens = text_tokenization(text)
    pos_tags = pos_tagging(tokens)
    print("POS Tags:", pos_tags)
else:
    print("Invalid operation. Please select a, b, c, or d.")

'''
***************
Output- 
Enter a sentence or a paragraph: I am John, IT student
Select operation (a. Tokenization, b. Word Frequency, c. Remove Stop Words, d. POS Tagging): a
Tokens: ['I', 'am', 'John', ',', 'IT', 'student']

Enter a sentence or a paragraph: Good game, Bye!
Select operation (a. Tokenization, b. Word Frequency, c. Remove Stop Words, d. POS Tagging): b
Word Frequency: <FreqDist with 5 samples and 5 outcomes>

Enter a sentence or a paragraph: The quick brown fox jumps over the lazy dog.
Select operation (a. Tokenization, b. Word Frequency, c. Remove Stop Words, d. POS Tagging): c
Tokens without Stop Words: ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog', '.']

Enter a sentence or a paragraph: The quick brown fox jumps over the lazy dog.
Select operation (a. Tokenization, b. Word Frequency, c. Remove Stop Words, d. POS Tagging): d
POS Tags: [('The', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'), ('fox', 'NN'), 
           ('jumps', 'VBZ'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'), 
           ('dog', 'NN'), ('.', '.')]
'''

