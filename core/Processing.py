import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.util import ngrams
import re
from core.Logger import Logger
import sys
import os
from collections import Counter
from pandas import DataFrame

class Processing:
    def __init__(self):
        self.loggerObj = Logger()

    def top_keywords_from_url(self, url, no_of_relevant_topics):
        try:
            REMOVE = {'style', 'script', 'head', 'title','[document]'}
            def visible_texts(soup):
                return re.compile(r'\s{3,}').sub('  ', ' '.join([s for s in soup.strings if s.parent.name not in REMOVE]))
            html = request.urlopen(url).read()
            soup = BeautifulSoup(html,"lxml")
            text = visible_texts(soup)
            lmtzr = WordNetLemmatizer()
            word_tokens = word_tokenize(text)
            stop_words = set(stopwords.words('english'))
            filtered_sentence = [lmtzr.lemmatize(w.lower()) for w in word_tokens if not w in stop_words and len(w) >= 4]
            Bigram = list(zip(filtered_sentence[::2], filtered_sentence[1::2]))
            countUnigram = Counter(filtered_sentence)
            countBigram = Counter([i[0].strip() + " " + i[1].strip() for i in Bigram])

            df_unigram = DataFrame.from_dict(countUnigram, orient='index').sort_values(by=0,ascending=False).reset_index()
            df_bigram = DataFrame.from_dict(countBigram, orient='index').sort_values(by=0,ascending=False).reset_index()
            bigram_weight = df_unigram[0][0]/df_bigram[0][0]
            df_bigram[0] = df_bigram[0]*bigram_weight
            return df_unigram.append(df_bigram).sort_values(by=0,ascending=False).reset_index(drop=True)[:no_of_relevant_topics]
        except NameError as err:
            message = 'NameError in this data: ' + str(err)
            self.loggerObj.error(os.path.basename(__file__), message)
            return []
        except TypeError as err:
            message = 'TypeError in this data: ' + str(err)
            self.loggerObj.error(os.path.basename(__file__), message)
            return []
        except ValueError as err:
            message = 'ValueError in this data: ' + str(err)
            self.loggerObj.error(os.path.basename(__file__), message)
            return []
        except AttributeError as err:
            message = 'AttributeError in this data: ' + str(err)
            self.loggerObj.error(os.path.basename(__file__), message)
            return []
        except:
            message = 'Error encountered for this data: ' + str(sys.exc_info()[0])
            self.loggerObj.error(os.path.basename(__file__), message)
            return []
