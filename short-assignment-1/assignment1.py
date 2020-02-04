'''
Nikki Kyllonen
LING 5801 - Computational Linguistics, Spring 2020

Python Assignment 1
2/4/2020
'''

# use just the slice and concatenation operations
def q1():
    s = "colorless"
    return s[:4] + "u" + s[4:]

# use the slice notation to remove the affixes from given words
def q2():
    print("dishes"[:-2])
    print("running"[:-4])
    print("nationality"[:-5])
    print("undo"[:-2])
    print("preheat"[:-4])

# store the lengths of the words in a list
def q3():
    chomsky = ["Colorless", "green", "ideas", "sleep", "furiously"]

    # using a for loop
    lengths = []
    for word in chomsky:
        lengths.append(len(word))
    print(lengths)

    # using a list comprehension
    lengths = [ len(word) for word in chomsky ]
    print(lengths)

# process a silly string
def q4():
    silly = "newly formed bland ideas are inexpressible in an infuriating way"
    
    # (a)
    bland = silly.split()
    print(bland)
    
    # (b)
    longwords = list(filter( lambda x : len(x) > 4 , bland )) 
    print(longwords)
    
    # (c)
    seconds = ''.join(list(map( lambda x : x[1], bland)))
    print(seconds)
    
    # (d)
    rejoined = " ".join(bland)
    print(rejoined)
    
    # (e)
    for word in sorted(bland):
        print(word)

if __name__ == '__main__':
    print(q1())
    q2()
    q3()
    q4()
