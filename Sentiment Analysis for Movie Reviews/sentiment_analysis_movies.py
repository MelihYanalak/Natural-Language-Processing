
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale

import numpy as np
import pandas as pd
import math
from gensim.models  import KeyedVectors
from gensim.models.word2vec import Word2Vec
import csv
import re 




def main():
    model,negatives,positives = load_model()
    probability_dict_forC0,probability_dict_forC1,p_c0,p_c1 = train(model,negatives,positives)
    result_labels,test_labels = test(probability_dict_forC0,probability_dict_forC1,p_c0,p_c1)
    accuracy = get_accuracy(result_labels,test_labels)
    print(accuracy)

def load_model():
    model = KeyedVectors.load_word2vec_format('wordvectors.bin', binary=True)
    with open('negative_train.txt', 'r', encoding='utf-8') as infile:
        negatives = infile.readlines()
    with open('positive_train.txt', 'r', encoding='utf-8') as infile:
        positives = infile.readlines()
    return model,negatives,positives


def train(model,negatives,positives):

    probability_dict_forC0 = dict()      
    probability_dict_forC1 = dict()
    for negative_comment in negatives:
        clean = re.sub(r"[,.:;@#?!&$]+\ *", " ", negative_comment)
        words = clean.split()
        
        if(len(words) >= 2):
            average = average_vector(model, negative_comment)
            for i in range(0,len(words)):
                if(words[i] in model.vocab):
                    sum = 1
                    for j in range(0,300):
                        if words[i] in model.vocab:
                            sum += abs(average[j] - (model[words[i]])[j])
                prob = sum / 1000
                if(words[i] in probability_dict_forC0):
                    probability_dict_forC0[words[i]] += prob
                else:
                    probability_dict_forC0[words[i]] = prob


    for posivite_comment in positives:
        clean = re.sub(r"[,.:;@#?!&$]+\ *", " ", posivite_comment)
        words = clean.split()
        if(len(words) >= 2):
            average = average_vector(model, posivite_comment)
            
            
            for i in range(0,len(words)):
                if(words[i] in model.vocab):
                    sum = 1
                    for j in range(0,300):
                        if words[i] in model.vocab:
                            sum += abs(average[j] - (model[words[i]])[j])

                    prob = sum / 1000
                    if(words[i] in probability_dict_forC1):
                        probability_dict_forC1[words[i]] += prob
                    else:
                        probability_dict_forC1[words[i]] = prob



    p_c1 = len(positives) / (len(positives) + len(negatives))
    p_c0 = len(negatives) / (len(positives) + len(negatives))
    return probability_dict_forC0,probability_dict_forC1,p_c0,p_c1

def train_with_cosine(model,negatives,positives):
    probability_dict_forC0 = dict()      
    probability_dict_forC1 = dict()
    for negative_comment in negatives:
        clean = re.sub(r"[,.:;@#?!&$]+\ *", " ", negative_comment)
        words = clean.split()
        
        if(len(words) >= 2):
            average = average_vector(model, negative_comment)
            for i in range(0,len(words)):
                if(words[i] in model.vocab):
                    sum = 1
                    for j in range(0,300):
                        if words[i] in model.vocab:
                            sum += abs(average[j] - (model[words[i]])[j])

            
                prob = sum / 1000
                if(words[i] in probability_dict_forC0):
                    probability_dict_forC0[words[i]] += prob
                else:
                    probability_dict_forC0[words[i]] = prob


    for posivite_comment in positives:
        clean = re.sub(r"[,.:;@#?!&$]+\ *", " ", posivite_comment)
        words = clean.split()
        if(len(words) >= 2):
            average = average_vector(model, posivite_comment)
            
            
            for i in range(0,len(words)):
                if(words[i] in model.vocab):
                    sum = 1
                    for j in range(0,300):
                        if words[i] in model.vocab:
                            sum += abs(average[j] - (model[words[i]])[j])
                    if(words[i] in model.vocab):
                        cosine_similarity = np.dot(model[words[i]], average)/(np.linalg.norm(model[words[i]])* np.linalg.norm(average))
                    else:
                        cosine_similarity = (float)(0.1)
                    if(words[i] in probability_dict_forC1):
                        probability_dict_forC0[words[i]] += cosine_similarity
                    else:
                        probability_dict_forC1[words[i]] = cosine_similarity



    p_c1 = len(positives) / (len(positives) + len(negatives))
    p_c0 = len(negatives) / (len(positives) + len(negatives))
    return probability_dict_forC0,probability_dict_forC1,p_c0,p_c1

def average_vector(model, comment):
    comment = re.sub(r"[,.:;@#?!&$]+\ *", " ", comment)
    words = comment.split()
    sum=[]
    sum = [0 for i in range(300)]
    count = 0
    for word in words:
        for i in range(300):
            if(word in model.vocab):
                    sum[i] += model[word][i]
                    count += 1
            
    for i in range(300):
        if(count != 0):
            sum[i] = sum[i] / count
            
    return sum

def average_vector_helper(model,word):
    sum = 0
    count = 0
    for i in range(300):
            if(word in model.vocab):
                sum += model[word][i]
                count += 1
    if(count != 0):
        sum = sum / count
    return sum
    



def test(probability_dict_forC0,probability_dict_forC1,p_c0,p_c1):
    test_comments,true_labels = get_test_labels('test_beyazperde.csv')
    predicted_labels = [] 
    for comment in test_comments:
        test_words = comment.split()
        p_w_c1 = 1
        p_w_c0 = 1
        for word in test_words:
            if(word in probability_dict_forC1):
                p_w_c1 *= probability_dict_forC1[word] * p_c1
            else:
                p_w_c1 *= (float)(0.2) * p_c1
            
            if(word in probability_dict_forC0):
                p_w_c0 *= probability_dict_forC0[word] * p_c0
            else:
                p_w_c0 *= (float)(0.2) * p_c0
        
        if(p_w_c1 > p_w_c0):
            predicted_labels.append("1")
        else:
            predicted_labels.append("0")
    return predicted_labels,true_labels

def get_accuracy(predicted_labels,true_labels):
    countMatch = 0
    for i in range(len(predicted_labels)):
        if true_labels[i] == predicted_labels[i]:
            countMatch += 1

    accuracy = (float)(countMatch / len(true_labels))
    return accuracy


def get_test_labels(fileName):
    test_comments = []
    test_labels = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                test_comments.append(row[1])
                test_labels.append(row[2])
            line_count += 1
    return test_comments,test_labels



main()