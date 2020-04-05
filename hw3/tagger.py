import nltk, re
from nltk.tag.brill import Template, Pos, Word
from nltk.corpus import brown


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
    (r'.*ing$', 'VBG'),				  # gerunds
	(r'.*ed$', 'VBD'),				  # simple past
	(r'.*es$', 'VBZ'),				  # 3rd singular present
	(r'.*ould$', 'MD'),				  # modals
	(r'.*\'s$', 'NN$'),				  # possessive nouns
	(r'.*s$', 'NNS'),				  # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),                  # cadinal numbers
	(r'.*', 'NN'), 				          # nouns (default)
	]

regexp_tagger = nltk.RegexpTagger(patterns)



## Part 2: Transformation-based learning and tagging

# Define rule templates
templates = [
            Template(Pos([-1])),              # previous  POS tag
            Template(Pos([-1]), Word([0]))    # previous POS tag + current word
             ]


# Train a error-driven, transformation-based tagger
tt = nltk.BrillTaggerTrainer(regexp_tagger, templates, trace=3)
brill_tagger = tt.train(train_data, max_rules=25)


## Part 3: Evalutation



## A unigram baseline tagger:
#unigram_tagger = nltk.UnigramTagger(train_data, backoff=nltk.DefaultTagger('NN'))
