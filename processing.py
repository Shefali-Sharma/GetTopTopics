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
import sys
from collections import Counter
from pandas import DataFrame
#url = "https://t.lever-analytics.com/email-link?dest=http%3A%2F%2Fblog.rei.com%2Fcamp%2Fhow-to-introduce-your-indoorsy-friend-to-the-outdoors%2F&eid=e9d79a20-bead-481c-a9af-0c1ddd0bf411&idx=1&token=x_P0qIdOURCMBx_clbC1P1q9sJc"
#url="https://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster"
#url="https://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"

def top_keywords_from_url(url, no_of_relevant_topics):
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
        print ('NameError in this data: ' + str(err))
        return []
    except TypeError as err:
        print ('TypeError in this data: ' + str(err))
        return []
    except ValueError as err:
        print ('ValueError in this data: ' + str(err))
        return []
    except:
        print ('Error encountered for this data: ' + str(sys.exc_info()[0]))
        return []
