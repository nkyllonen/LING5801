'''
Nikki Kyllonen
LING 5801 - Computational Linguistics, Spring 2020

Python Assignment 2
2/23/2020
'''
import string
import nltk
nltk.download("reuters")
nltk.download("punkt")
from nltk.corpus import reuters

## GLOBAL VARIABLES ##
punc = set(string.punctuation)
sent1 = "It's a beautiful day in the neighborhood, please won't you be my beautiful " \
        "neighbor?"
sent2 = "We are inside the world of beautiful people, but that's not who we are; " \
        "we are not beautiful!"

## HELPER FUNCTIONS ##
# remove all punctuation
def remove_punc(s):
    return "".join( ch for ch in s if ch not in punc )

# turn all strings into sets of words
def q1(query):
    print("\n" + "~"*10 + " Q1 " + "~"*10)

    setA = set(sent1.split(" "))
    print("setA: " , setA)
    setB = set(sent2.split(" "))
    print("setB: " , setB)
    setC = set(query.split(" "))
    print("setC:" , setC)

    # return sets for q2
    return (setA, setB, setC)

# jaccard values
def q2(query, setA, setB, setC):
    print("\n" + "~"*10 + " Q2 " + "~"*10)
    
    # intersection and union between query and sent1
    insct1 = len(setA.intersection(setC))
    union1 = len(setA.union(setC))
    jaccard1 = insct1 / union1

    print("cardinality insct1: " , insct1)
    print("cardinality union1: " , union1)
    #print("1 WRONG!") if (jaccard1 != jaccard(query, sent1)) else print("Correct!")
    
    # intersection and union between query and sent2
    insct2 = len(setB.intersection(setC))
    union2 = len(setB.union(setC))
    jaccard2 = insct2 / union2

    print("cardinality insct2: " , insct2)
    print("cardinality union2: " , union2)
    #print("2 WRONG!") if (jaccard2 != jaccard(query, sent2)) else print("Correct!")
    
    # print highest jaccard value
    print("jaccard1: " , jaccard1) if (jaccard1 > jaccard2) else print("jaccard2: " , jaccard2)

# Q3: calculate jaccard value between two strings
def jaccard(query, doc):
    query = set(remove_punc(query).split(" "))
    doc = set(remove_punc(doc).split(" "))

    return len(query.intersection(doc)) / len(query.union(doc))


def q4(query):
    print("\n" + "~"*10 + " Q4 " + "~"*10)
    
    # retrieve seventh sentence and join into a string
    # also remove punctuation from it since they are separated out
    pick = " ".join( remove_punc(word) for word in reuters.sents()[7] if word not in punc)
    result = (pick, jaccard(query, pick))
    print(result)

if __name__ == '__main__':
    # pre-processing strings to remove all punctuation
    sent1 = remove_punc(sent1)
    sent2 = remove_punc(sent2)

    query = str(input("Please enter your query:\n"))
    
    (setA, setB, setC) = q1(query)
    q2(query, setA, setB, setC)
    q4(query)
