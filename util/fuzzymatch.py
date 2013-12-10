---
This file unites three functions of the natural language toolkit: stemmer, tokenizing, and fuzzy matching. 
---


from nltk import metrics, stem, tokenize

### need to integrate this is current stemmer.py file
stemmer = stem.PorterStemmer()

def normalize(s):
    words = tokenize.wordpunct_tokenize(strip())
    return ' '.join([stemmer.stem(w) for w in words])

def fuzzy_match(s1, s2, max_dist=3):
    return metrics.edit_distance(normalize(s1), normalize(s2)) <= max_dist
