#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:01:10 2019

@author: lix
"""

"""
Step 0: Preparation of the raw data set
"""
import csv

doc_complete = list()

AIRLINEREVIEW_CSV = "JetBlue.csv"

with open(AIRLINEREVIEW_CSV, 'rt', encoding='UTF-8') as airlinereview_data:
    airlinereviews = csv.reader(airlinereview_data, delimiter=',')
    line_count = 1 
    for row in airlinereviews:
        if line_count<=100:
            if row[2]=="negative":
                doc_complete.append(row[0])
                line_count += 1
        else:
            break

print('\n\nStep 0: Data\n\n')
print(len(doc_complete))
# print out the raw data of the 2nd row of the csv file
print(doc_complete[1])




"""
Step 1: Cleaning and Preprocessing of the data

Cleaning is an important step before any text mining task.
In this step, we will remove the punctuations, stopwords and normalize the corpus.

"""
# importing required libraries 
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string

# set of stopwords
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
exclude_words={'americanair','americanairlines','airline','realcandaceo','rt','phyllis51889108','flight'}

print(stop)

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in (stop)])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    test=' '.join(ch for ch in punc_free.lower().split() if ch not in exclude_words)
    normalized = " ".join(lemma.lemmatize(word) for word in test.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]    


print('\n\nStep 1: Cleaned Data\n\n')
# the cleaned data of the 2nd row
print(doc_clean)

"""
# visualize the word cloud
"""
# pip install WordCloud
# Import the wordcloud library
from wordcloud import WordCloud
    
long_string = ",".join([" ".join(sentence) for sentence in doc_clean])
# print('long_string: \n\n', long_string)

wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
wordcloud.generate(long_string)

wordcloud.to_image()


"""
Step 2: Preparing Document-Term Matrix

All the text documents combined is known as the corpus. 
To run any mathematical model on text corpus, it is a good practice to convert it into a matrix representation. 
LDA model looks for repeating term patterns in the entire DT matrix. 
Python provides many great libraries for text mining practices, 
“gensim” is one such clean and beautiful library to handle text data. 
It is scalable, robust and efficient. 
Following code shows how to convert a corpus into a document-term matrix.

"""
# Importing Gensim
import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(doc_clean)
# print(dictionary)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

print('\n\nStep 2: doc_term_matrix created!\n\n')

# Human readable format of corpus (term-frequency): doc_term_matrix
[[(dictionary[id], freq) for id, freq in cp] for cp in doc_term_matrix[0:]]
# [[(dictionary[id], freq) for id, freq in cp] for cp in doc_term_matrix[:1]]


"""
Step 3: Running LDA Model

Next step is to create an object for LDA model and train it on Document-Term matrix. 
The training also requires few parameters as input which are explained in the above section. 
The gensim module allows both LDA model estimation from a training corpus 
and inference of topic distribution on new, unseen documents.

"""

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
# num_topics is the key parameter that we need to set up
lda_model = Lda(corpus=doc_term_matrix, num_topics=3, id2word=dictionary, passes=10)

print('\n\nStep 3: LDA model trained!\n\n')


"""
Step 4: Print out results

Each line is a topic with individual topic terms and weights. 
"""
print(lda_model.print_topics(num_topics=3, num_words=10))

print('\n\nStep 4: results printed!\n\n')

from pprint import pprint
pprint(lda_model.print_topics(num_topics=3, num_words=10))

for idx, topic in lda_model.print_topics(num_topics=3, num_words=10):
    print('Topic {}: \nWord: {}'.format(idx, topic), '\n')
    
    
print('\n\nStep 4: results printed using pprint!\n\n')

## Can you distinguish different topics using the words in each topic and 
## their corresponding weights?



"""
Step 5: Compute Model Perplexity and Coherence Score

Model perplexity and topic coherence provide a convenient measure to judge 
how good a given topic model is. 
Topic coherence score, in particular, has been more helpful.
"""
# Compute Perplexity
# a measure of how good the model is. The lower, the better.
print('\nPerplexity: ', lda_model.log_perplexity(doc_term_matrix))  

# Compute Coherence Score.
# another measure. The higher, the better
from gensim.models import CoherenceModel
coherence_model_lda = CoherenceModel(model=lda_model, texts=doc_clean, dictionary=dictionary, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)




