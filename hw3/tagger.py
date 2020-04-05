import nltk, re
from nltk.tag.brill import Template, Pos, Word
from nltk.corpus import brown

# My computer requires that I download items from nltk
# I think it might have to do with my version of Python?
nltk.download('brown')

## Training and testing data:
data = brown.tagged_sents(categories=['news', 'editorial'])
train_data = []
test_data = []
for i, sent in enumerate(data):
    if i % 10 > 0:
        train_data.append(sent)
    else:
        test_data.append(sent)


## Development set (to test taggers before final evaulation on test_data):
dev_data = brown.tagged_sents(categories="government")


## A useful function:
def get_words(tagged_sentence):
    """Strip the POS tags from a tagged sentence."""
    return [word for word, tag in tagged_sentence]




# Part 1: Regular expression tagger

# These are the patterns from the NLTK text. Add 10 additional patterns to
# this list. Keep in mind that the order in which patterns are applied affects
# the performance of your tagger.  The last pattern is a default rule that
# assigns the singular noun tag NN to every token.

patterns = [
        (r'(?:\.|\?|\!)', '.'),                         # sentence terminator
        (r'(?:[Bb][Ee]\b)', 'BE'),                      # verb 'to be'
        (r'\b(([Aa]+[Nn]*)|([Nn][Oo])|([Tt][Hh][Ee])|([Yy][Ee])|([Ee]very))\b', 'AT'), # articles
        (r'(?:[Ww]ere[^n])','BED'),                     # verb 'to be' past tense 2nd sing
        (r'\b(?:[Ww][Aa][Ss])\b', 'BEDZ'),              # verb 'to be' past tenst 1st/3rd sing
        (r'\b(?:[Aa][Mm])\b', 'BEM'),                   # verb 'to be' present tense 1st sing
        (r'\b(?:[Ii][Ss])\b', 'BEZ'),                   # verb 'to be' present tense 3rd sing
        (r'\b(?:([Aa][Nn][Dd])|([Oo][Rr])|([Bb]ut)|([Pp]lus)|([Nn]*[Ee]ither)|([Nn]or)|([Yy]et)|([Mm]inus))\b','CC'),                                        # conjuctions, coordinating
        (r'\b(?:[Bb][Ee]+[Nn])\b','BEN'),               # verb 'to be', past part
        (r'\b(?:([Ff][Oo][Rr])|([Ii][Nn]([Tt][Oo])*)|([Oo]([Ff]|[Nn]|(ut)|(ver)))|([Bb]([Yy]|efore|etween))|((([Cc]onsider)|([Rr]egard)|([Aa]ccord)|([Ii]nclud))ing)|([Aa]((mong)|(gainst)|([Ss])|(fter)|([Tt])))|([Tt](([Oo])|(hrough)|(han)|(oward)))|([Ww]ith(out)*)|([Uu]((nder)|(pon)))|([Dd](uring|espite))|([Ss]ince)|([Pp]er)|([Ee]xcept))\b','IN'),          # prepositions 
        (r'\b(?:([Nn](one|othing|obody|o-one|othin)|([Ss](omething|omeone))|([Aa](nyone|nybody|nything)))|([Ee]very(thing|body|one))|[Oo]ne)\b','PN'),      # pronoun, nominal
        (r'\b(?:([Ii][Tt])|([Tt]*[Ss]*[Hh][Ee]+))\b','PPS'),    # pronoun, personal, nominative

        # original patterns
        (r'.*ing$', 'VBG'),				# gerunds
	(r'.*ed$', 'VBD'),				# simple past
	(r'.*es$', 'VBZ'),				# 3rd singular present
	(r'.*ould$', 'MD'),				# modals
	(r'.*\'s$', 'NN$'),				# possessive nouns
	(r'.*s$', 'NNS'),				# plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),                # cadinal numbers
	(r'.*', 'NN'), 				        # nouns (default)
	]

regexp_tagger = nltk.RegexpTagger(patterns)



## Part 2: Transformation-based learning and tagging

# Define rule templates
#templates = [
#            Template(Pos([-1])),              # previous  POS tag
#            Template(Pos([-1]), Word([0]))    # previous POS tag + current word
#             ]
#
#
## Train a error-driven, transformation-based tagger
#tt = nltk.BrillTaggerTrainer(regexp_tagger, templates, trace=3)
#brill_tagger = tt.train(train_data, max_rules=25)


## Part 3: Evaluation
print("Regexp_tagger accuracy with dev_data: {}".format(regexp_tagger.evaluate(dev_data)))


## A unigram baseline tagger:
#unigram_tagger = nltk.UnigramTagger(train_data, backoff=nltk.DefaultTagger('NN'))
