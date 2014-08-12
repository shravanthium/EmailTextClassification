import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import re
import string
regex = re.compile('[%s]' % re.escape(string.punctuation))


#remove unnecessary punctuation marks from the mail text
def remove_punctuation(mail):
    new_review=[]	
    for token in mail:
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    return new_review

#remove stop words from the mail text
def remove_stopwords(striptext):
    new_term_vector = []
    for word in striptext:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    return new_term_vector    
            
#remove mailbody words
mail_words=['hi','hello','regards','please','dear']
