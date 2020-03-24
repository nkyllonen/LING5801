'''
Nikki Kyllonen
LING 5801 - Computational Linguistics, Spring 2020

Python Assignment 3
3/24/2020
'''
# IMPORT STATEMENTS #
import string
import nltk
from nltk.corpus import reuters
import re

# GLOBAL VARIABLES #
docs = []
query = ""

# HELPER FUNCTIONS #
def jaccard(query, doc):
    query = set(query.split())
    doc = set(doc.split())
    
    # check that the union does not yield the empty set
    if len(query.union(doc)) > 0:
        return len(query.intersection(doc)) / len(query.union(doc))
    else:
        return 0

# QUESTION FUNCTIONS #

# build a giant list of sentence strings
def q1():
    global docs
    
    # retrieve sentences from three genres
    docs = list(reuters.sents(categories='bop'))
    docs = docs + (reuters.sents(categories='cocoa'))
    docs = docs + (reuters.sents(categories='zinc'))
    #print(docs)

    # convert list of lists into list of strings
    doc = []
    for sent in docs:
        # case fold each sentence
        doc.append(" ".join([ word.lower() for word in sent if word not in set(string.punctuation) ]))
    docs = doc
    #print(docs)

# compare input sentence against each stored sentence in docs
def q2():
    global query
    query = str(input("Please enter a sentence: "))

    # calculate and store the jaccard value for query against every sentence
    jacValues = []
    for sent in docs:
        jacValues.append( (sent , jaccard(query, sent)) )

    return jacValues

# display top 10 "most similar" sentences
def q3(jaccardValues):
    print("\n" + "~"*10 + "Q3" + "~"*10)
    # sort tuples by their jaccard values (the second value in each tuple)
    jaccardValues.sort(key = lambda x : x[1])

    # print last 10 (top 10) values
    for i in range(10):
        print(jaccardValues[len(jaccardValues) - 1 - i])

def q4(jaccardValues):
    print("\n" + "~"*10 + "Q4" + "~"*10)
    # build regular expression
    regex = r'('
    for word in query.split(" "):
        regex = regex + "\\b" + word + '\\b|' # \b for word boundaries
    regex = regex[:-1] + ')'
    #print(regex)

    # substitute the matched words using a regular expression
    for i in range(10):
        result = jaccardValues[len(jaccardValues) - 1 - i]
        print((re.sub(regex, r'<\1>', result[0]) , result[1]))

# MAIN #
if __name__ == '__main__':
    q1()
    jaccardValues = q2()
    q3(jaccardValues)
    q4(jaccardValues)
