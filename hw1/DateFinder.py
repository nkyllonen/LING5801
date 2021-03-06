#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 9 2020

@author: breese

"""
import re
import codecs

################# FUNCTION DEFINITIONS -- DO NOT CHANGE #######################

def precision(system,gold):
    s = set(system)
    g = set(gold)
    tp = s.intersection(g)
    return len(tp)/len(s)

def recall(system,gold):
    s = set(system)
    g = set(gold)
    tp = s.intersection(g)
    return len(tp)/len(g)

def f1(p,r):
    return 2 * ((p * r)/(p + r))


def analyze(system,gold):
    p = precision(system,gold)
    r = recall(system,gold)
    f = f1(p,r)
    print("Precision: %f\tRecall: %f\tF1: %f" % (p,r,f))

################################################################################


# 0. Read the dates from the gold standard file into the list gold_dates.  These are 
# all of the dates in the dev.txt that your regular expression should match.  
gold_dates = [date.strip() for date in open("dev_gs.txt", "r").readlines() if date.strip()]


# 1. Read the contents of dev.txt into the string doc.  This is the file that your
# regular expression will scrape for date expressions.
doc = codecs.open("dev.txt", encoding='cp1251').read()


# 2. Define your regular expression in the string pattern.  The VERBOSE flag allows you to 
# leverage multi-line strings, whitespace, and comments within a regex definition.
s1 = r"(?:\b[0-9]{1,2}[.-]{1}\w+[.-]{1}[0-9]+\b)"       # #-month.# amd #.month.#
s2 = r"(?:\b[0-9]+[/]+[0-9]+[/]+[0-9]{2,}\b)"           # #/#/#
s3 = r"(?:\b[JFMASOND][^rf][a-z]{3,9}\s[0-9]+\b)"       # month # -- false positives matching incompleted dates such as # month #
#s3 = r"(?:\b[JFMASOND][aepuc][a-z]{3,9}\s[0-9]+\b)"
#s3 = r"(?:\b[JFMASOND][aepuc][nbrylgptvc][a-z]*\s[0-9]+\b)"
s4 = r"(?:[A-Z][a-z]{2,8}\s[0-9]{1,2}[tsrn]?[htd]?.\s[0-9]{4})" # month day(th, etc.) year

s5 = r"(?:\b[0-9]{1,2}\s[A-Z][a-z]+\s[0-9]{4}\b)"       # day month year -- no false positives
s6 = r"(?:\b[A-z][a-z]+.[-][0-9]{1,2}[-][0-9]{4}\b)"    # month -day-year -- account for extra space
#s6 = r"(?:\b[A-z][a-z]+.*[-].*[0-9]{1,2}.*[-].*[0-9]{4}\b)"  # month-day-year -- account for extra spaces between dashes

#pattern = r"{}|{}|{}".format(s1,s2,s4)
#pattern = r"{}|{}|{}|{}".format(s1,s2,s3,s4)
pattern = r"{}|{}|{}|{}|{}".format(s1,s2,s3,s4,s5)
#pattern = r"{}|{}|{}|{}|{}|{}".format(s1,s2,s3,s4,s5,s6)

regex = re.compile(pattern, re.VERBOSE)


# 3. Use the findall method to return a list of every occurrence of a date 
# in the development file.
dates = re.findall(regex, doc)


# 4. Evaluate your regex using the evaluate function.
print(analyze(dates, gold_dates))
