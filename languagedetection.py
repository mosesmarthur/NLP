from nltk import *
from nltk.corpus import *
def lang_ratio(input):
    lang_ratio = {}
    tokens = wordpunct_tokenize(input)
    words = [word.lower() for word in tokens]
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        lang_ratio[language] = len(common_elements)
    return lang_ratio

def detect_language(input):
    ratios = lang_ratio(input)
    language = max(ratios, key=ratios.get)
    return language

input1 ="Jeg er fra Danmark. Jeg snakker Dansk"

language = detect_language(input1)
print(input1 +"\t Language of the sentence:" +language)

