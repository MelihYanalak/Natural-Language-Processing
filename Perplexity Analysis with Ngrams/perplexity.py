# -*- coding: utf-8 -*-
import codecs
import nltk
import math
import pandas as pd 
from collections import defaultdict 
  

def controlChar(c):
    if((ord(c) <= 122 and ord(c) >= 97) or (c == ' ') or (ord(c) == 231) or (ord(c) == 287) or (ord(c) == 305) or (ord(c) == 246) or (ord(c) == 351) or (ord(c) == 252)):
        return True
    else:
        return False
        
# Utiliy function to create dictionary 
def multi_dict(K, type): 
    if K == 1: 
        return defaultdict(type) 
    else: 
        return defaultdict(lambda: multi_dict(K-1, type)) 
def  lower_Input(fileName,outputName):
    with open(fileName, 'r',encoding="utf-8",errors='ignore') as fileinput:
        with open(outputName, 'wb') as openFile:
            for line in fileinput:
                line = line.lower()
                openFile.write(line.encode("utf-8"))
        openFile.close()
    fileinput.close()
def countNgrams():
    dic1 = multi_dict(1,int)
    dic2 = multi_dict(2,int)
    dic3 = multi_dict(3,int)
    dic4 = multi_dict(4,int)
    dic5 = multi_dict(5,int)
    n1 = multi_dict(1,int)
    n2 = multi_dict(1,int)
    n3 = multi_dict(1,int)
    n4 = multi_dict(1,int)
    n5 = multi_dict(1,int)
    letterList = []
    with open('C:/Users/Dell/Desktop/NLP/HW2/data_lower.txt', 'r',encoding="utf-8") as fileInput:
        for line in fileInput:
            for ch in line:
                if(controlChar(ch)):
                    letterList.append(ch)
    fileInput.close()
    ch1 = letterList[0]
    ch2 = letterList[1]
    ch3 = letterList[2]
    ch4 = letterList[3]
    ch5 = letterList[4]
    dic1[ch1] = 1
    dic2[ch1][ch2] = 1
    dic3[ch1][ch2][ch3] = 1
    dic4[ch1][ch2][ch3][ch4] = 1
    dic5[ch1][ch2][ch3][ch4][ch5] = 1
    n1[1] = 1
    n2[1] = 1
    n3[1] = 1
    n4[1] = 1
    n5[1] = 1
    i = 5
    while i < len(letterList):
        ch1 = ch2
        ch2 = ch3
        ch3 = ch4
        ch4 = ch5
        ch5 = letterList[i]
        if dic1[ch1] == 0:
            dic1[ch1] = 1
            n1[1] = n1[1] + 1
        else:
            dic1[ch1] = dic1[ch1] + 1
            n1[(dic1[ch1])-1] = n1[(dic1[ch1])-1] - 1
            n1[(dic1[ch1])] = n1[(dic1[ch1])] + 1

        if dic2[ch1][ch2] == 0:
            dic2[ch1][ch2] = 1
            n2[1] = n2[1] + 1
        else:
            dic2[ch1][ch2] = dic2[ch1][ch2] + 1
            n2[(dic2[ch1][ch2])-1] = n2[(dic2[ch1][ch2])-1] -1
            n2[(dic2[ch1][ch2])] = n2[(dic2[ch1][ch2])] +1

        if dic3[ch1][ch2][ch3] == 0:
            dic3[ch1][ch2][ch3] = 1
            n3[1] = n3[1] + 1
        else:
            dic3[ch1][ch2][ch3] = dic3[ch1][ch2][ch3] + 1
            n3[(dic3[ch1][ch2][ch3])-1] =  n3[(dic3[ch1][ch2][ch3])-1]  -1
            n3[(dic3[ch1][ch2][ch3])] =  n3[(dic3[ch1][ch2][ch3])]  +1

        if dic4[ch1][ch2][ch3][ch4] == 0:
            dic4[ch1][ch2][ch3][ch4] = 1
            n4[1] = n4[1] + 1
        else:
            dic4[ch1][ch2][ch3][ch4] = dic4[ch1][ch2][ch3][ch4] + 1
            n4[(dic4[ch1][ch2][ch3][ch4])-1] = n4[(dic4[ch1][ch2][ch3][ch4])-1] - 1
            n4[(dic4[ch1][ch2][ch3][ch4])] = n4[(dic4[ch1][ch2][ch3][ch4])] + 1

        if dic5[ch1][ch2][ch3][ch4][ch5] == 0:
            dic5[ch1][ch2][ch3][ch4][ch5] = 1
            n5[1] = n5[1] + 1
        else:
            dic5[ch1][ch2][ch3][ch4][ch5] = dic5[ch1][ch2][ch3][ch4][ch5] + 1
            n5[(dic5[ch1][ch2][ch3][ch4][ch5])-1] =  n5[(dic5[ch1][ch2][ch3][ch4][ch5])-1] - 1
            n5[(dic5[ch1][ch2][ch3][ch4][ch5])] =  n5[(dic5[ch1][ch2][ch3][ch4][ch5])] + 1
        
        i = i+1

    if dic1[ch2] == 0:
            dic1[ch2] = 1
            n1[1] = n1[1] + 1
    else:
        dic1[ch2] = dic1[ch2] + 1
        n1[(dic1[ch2])-1] = n1[(dic1[ch2])-1] - 1
        n1[(dic1[ch2])] = n1[(dic1[ch2])] + 1

    if dic1[ch3] == 0:
            dic1[ch3] = 1
            n1[1] = n1[1] + 1
    else:
        dic1[ch3] = dic1[ch3] + 1
        n1[(dic1[ch3])-1] = n1[(dic1[ch3])-1] - 1
        n1[(dic1[ch3])] = n1[(dic1[ch3])] + 1

    if dic1[ch4] == 0:
            dic1[ch4] = 1
            n1[1] = n1[1] + 1
    else:
        dic1[ch4] = dic1[ch4] + 1
        n1[(dic1[ch4])-1] = n1[(dic1[ch4])-1] - 1
        n1[(dic1[ch4])] = n1[(dic1[ch4])] + 1

    if dic1[ch5] == 0:
            dic1[ch5] = 1
            n1[1] = n1[1] + 1
    else:
        dic1[ch5] = dic1[ch5] + 1
        n1[(dic1[ch5])-1] = n1[(dic1[ch5])-1] - 1
        n1[(dic1[ch5])] = n1[(dic1[ch5])] + 1

    
    if dic2[ch2][ch3] == 0:
            dic2[ch2][ch3] = 1
            n2[1] = n2[1] + 1
    else:
        dic2[ch2][ch3] = dic2[ch2][ch3] + 1
        n2[(dic2[ch2][ch3])-1] =  n2[(dic2[ch2][ch3])-1] -1
        n2[(dic2[ch2][ch3])] =  n2[(dic2[ch2][ch3])] +1

    if dic2[ch3][ch4] == 0:
            dic2[ch3][ch4] = 1
            n2[1] = n2[1] + 1
    else:
        dic2[ch3][ch4] = dic2[ch3][ch4] + 1
        n2[(dic2[ch3][ch4])-1] =  n2[(dic2[ch3][ch4])-1] -1
        n2[(dic2[ch3][ch4])] =  n2[(dic2[ch3][ch4])] +1

    if dic2[ch4][ch5] == 0:
            dic2[ch4][ch5] = 1
            n2[1] = n2[1] + 1
    else:
        dic2[ch4][ch5] = dic2[ch4][ch5] + 1
        n2[(dic2[ch4][ch5])-1] =  n2[(dic2[ch4][ch5])-1] -1
        n2[(dic2[ch4][ch5])] =  n2[(dic2[ch4][ch5])] +1

    
    if dic3[ch2][ch3][ch4] == 0:
            dic3[ch2][ch3][ch4] = 1
            n3[1] = n3[1] + 1
    else:
        dic3[ch2][ch3][ch4] = dic3[ch2][ch3][ch4] + 1
        n3[dic3[ch2][ch3][ch4]-1] = n3[dic3[ch2][ch3][ch4]-1] - 1
        n3[dic3[ch2][ch3][ch4]] = n3[dic3[ch2][ch3][ch4]] + 1

    if dic3[ch3][ch4][ch5] == 0:
            dic3[ch3][ch4][ch5] = 1
            n3[1] = n3[1] + 1
    else:
        dic3[ch3][ch4][ch5] = dic3[ch3][ch4][ch5] + 1
        n3[(dic3[ch3][ch4][ch5])-1] = n3[(dic3[ch3][ch4][ch5])-1] - 1
        n3[(dic3[ch3][ch4][ch5])] = n3[(dic3[ch3][ch4][ch5])] + 1

    
    if dic4[ch2][ch3][ch4][ch5] == 0:
            dic4[ch2][ch3][ch4][ch5] = 1
            n4[1] = n4[1] + 1
    else:
        dic4[ch2][ch3][ch4][ch5] = dic4[ch2][ch3][ch4][ch5] + 1
        n4[(dic4[ch2][ch3][ch4][ch5])-1] = n4[(dic4[ch2][ch3][ch4][ch5])-1] - 1
        n4[(dic4[ch2][ch3][ch4][ch5])] = n4[(dic4[ch2][ch3][ch4][ch5])] + 1
    n1[0] = (float)((n1[1]+1) / len(letterList))
    n2[0] = (float)((n5[1]+1) / (len(letterList) - 1))
    n3[0] = (float)((n5[1]+1) / (len(letterList) - 2))
    n4[0] = (float)((n5[1]+1) / (len(letterList) - 3))
    n5[0] = (float)((n5[1]+1) / (len(letterList) - 4))
    calculatePerplexity(dic1,dic2,dic3,dic4,dic5,n1,n2,n3,n4,n5,len(letterList))
def calculatePerplexity(dic1,dic2,dic3,dic4,dic5,n1,n2,n3,n4,n5,wordNum):
    letterList = []
    with open('C:/Users/Dell/Desktop/NLP/HW2/test_lower.txt', 'r',encoding="utf-8") as fileInput:
        for line in fileInput:
            for ch in line:
                if(controlChar(ch)):
                    letterList.append(ch)
    fileInput.close()
    i = 0
    while i + 25 < len(letterList):
        perplexity(letterList[i : i+25],dic1,dic2,dic3,dic4,dic5,n1,n2,n3,n4,n5,wordNum)
        i = i + 25
    
    


def perplexity(sentence,dic1,dic2,dic3,dic4,dic5,n1,n2,n3,n4,n5,wordNum):
    
    openFile = open('C:/Users/Dell/Desktop/NLP/HW2/output.txt', 'ab')
    ch1 = sentence[0]
    ch2 = sentence[1]
    ch3 = sentence[2]
    ch4 = sentence[3]
    ch5 = sentence[4]
    i = 5
    count = 5
    
    openFile.write(ch1.encode("utf-8"))
    openFile.write(ch2.encode("utf-8"))
    openFile.write(ch3.encode("utf-8"))
    openFile.write(ch4.encode("utf-8"))
    openFile.write(ch5.encode("utf-8"))
    
    if dic1[ch1] == 0:
        pw1 = n1[0]
    else:
        pw1 = (float)((dic1[ch1] + 1) * (n1[dic1[ch1] + 1] +1) / (n1[dic1[ch1]]+1))
        pw1 = (float)(pw1 / wordNum)
        #pw1 = (float)(1/pw1)
        #print("pw1 = " + (str)(pw1))
    perpForUniGram = math.log2(pw1)
    #print("perpForUniGram "+(str)(perpForUniGram))
    if dic2[ch1][ch2] == 0:
        pw2w1 = n2[0]
    else:
        pw2w1 = (float)((dic2[ch1][ch2] + 1) * (n2[dic2[ch1][ch2] + 1]+1) / (n2[dic2[ch1][ch2]]+1))
        pw2w1 = (float)(pw2w1 / ((dic1[ch1] + 1) * (n1[dic1[ch1] + 1]+1) / (n1[dic1[ch1]]+1)))
        #pw2w1 = (float)(1/pw2w1)
        #print("pw2w1 = " + (str)(pw2w1))
    perpForBiGram = math.log2(pw1) + math.log2(pw2w1)
    #print("perpForBiGram "+(str)(perpForBiGram))

    if dic3[ch1][ch2][ch3] == 0:
        pw3w2w1 = n3[0]
    else:
        pw3w2w1 = (float)((dic3[ch1][ch2][ch3] + 1) * (n3[dic3[ch1][ch2][ch3] + 1]+1) / (n3[dic3[ch1][ch2][ch3]]+1))
        pw3w2w1 = (float)(pw3w2w1 / ((dic2[ch1][ch2] + 1) * (n2[dic2[ch1][ch2] + 1]+1) / (n2[dic2[ch1][ch2]]+1)))
        #pw3w2w1 = (float)(1/pw3w2w1)
        #print("pw3w2w1 = " + (str)(pw3w2w1))
    perpForTriGram = math.log2(pw1) + math.log2(pw2w1) + math.log2(pw3w2w1)

    if dic4[ch1][ch2][ch3][ch4] == 0:
        pw4w3w2w1 = n4[0]
    else:
        pw4w3w2w1 = (float)((dic4[ch1][ch2][ch3][ch4] + 1) * (n4[dic4[ch1][ch2][ch3][ch4] + 1]+1) / (n4[dic4[ch1][ch2][ch3][ch4]]+1))
        pw4w3w2w1 = (float)(pw4w3w2w1 / ((dic3[ch1][ch2][ch3] + 1) * (n3[dic3[ch1][ch2][ch3] + 1]+1) / (n3[dic3[ch1][ch2][ch3]]+1)))
        #pw4w3w2w1 = (float)(1/pw4w3w2w1)
        #print("pw4w3w2w1 = " + (str)(pw4w3w2w1))
    perpForFourGram = math.log2(pw1) + math.log2(pw2w1) + math.log2(pw3w2w1) + math.log2(pw4w3w2w1)

    if dic5[ch1][ch2][ch3][ch4][ch5] == 0:
        pw5w4w3w2w1 = n5[0]
    else:
        pw5w4w3w2w1 = (float)((dic5[ch1][ch2][ch3][ch4][ch5] + 1) * (n5[dic5[ch1][ch2][ch3][ch4][ch5] + 1]+1) / (n5[dic5[ch1][ch2][ch3][ch4][ch5]]+1))
        pw5w4w3w2w1 = (float)(pw5w4w3w2w1 / ((dic4[ch1][ch2][ch3][ch4] + 1) * (n4[dic4[ch1][ch2][ch3][ch4] + 1]+1) / (n4[dic4[ch1][ch2][ch3][ch4]]+1)))
        #pw5w4w3w2w1 = (float)(1/pw5w4w3w2w1)
        #print("pw5w4w3w2w1 = " + (str)(pw5w4w3w2w1))
    perpForFiveGram = math.log2(pw1) + math.log2(pw2w1) + math.log2(pw3w2w1) + math.log2(pw4w3w2w1) + math.log2(pw5w4w3w2w1)

    while i < len(sentence):
        if count >= 24:
            #2**(-L/toplam_letter)
            #p = 1 / markov
            #return math.pow(p, 1 / n)
            
            x = (math.pow(10,9))
            perpForUniGram = math.pow(2,((float)(perpForUniGram*(-1) / wordNum))) * x 
            perpForUniGram = (perpForUniGram % (x))
            perpForBiGram = math.pow(2,((float)(perpForBiGram*(-1) / (wordNum-1))))  * x
            perpForBiGram = (perpForBiGram % (x))
            perpForTriGram = math.pow(2,((float)(perpForTriGram*(-1) / (wordNum-2)))) *x 
            perpForTriGram = (perpForTriGram % (x))
            perpForFourGram = math.pow(2,((float)(perpForFourGram*(-1) / (wordNum-3)))) *x
            perpForFourGram = (perpForFourGram % (x))
            perpForFiveGram = math.pow(2,((float)(perpForFiveGram*(-1) / (wordNum-4)))) *x
            perpForFiveGram = (perpForFiveGram % (x))
            string = "  p1 = " + (str)(perpForUniGram)  + "  p2 = " + (str)(perpForBiGram)  + "  p3 = " + (str)(perpForTriGram) + "  p4 = " + (str)(perpForFourGram) + "  p5 = " + (str)(perpForFiveGram) + "\n"
            openFile.write(string.encode("utf-8"))
            count = 0
        ch1 = ch2
        ch2 = ch3
        ch3 = ch4
        ch4 = ch5
        ch5 = sentence[i]
        count = count + 1
        '''
        openFile.write(ch1.encode("utf-8"))
        openFile.write(ch2.encode("utf-8"))
        openFile.write(ch3.encode("utf-8"))
        openFile.write(ch4.encode("utf-8"))
        '''
        openFile.write(ch5.encode("utf-8"))
        
        if dic1[ch1] == 0:
            pw1 = n1[0]
        else:
            pw1 = (float)((dic1[ch1] + 1) * (n1[dic1[ch1] + 1]+1) / (n1[dic1[ch1]]+1))
            pw1 = (float)(pw1 / wordNum)
            #print("pw1 = " + (str)(pw1))
            #pw1 = (float)(1/pw1)
        perpForUniGram = perpForUniGram + math.log2(pw1)
        if dic2[ch1][ch2] == 0:
            pw2w1 = n2[0]
        else:
            pw2w1 = (float)((dic2[ch1][ch2] + 1) * (n2[dic2[ch1][ch2] + 1]+1) / (n2[dic2[ch1][ch2]]+1))
            pw2w1 = (float)(pw2w1 / ((dic1[ch1] + 1) * (n1[dic1[ch1] + 1]+1) / (n1[dic1[ch1]]+1)))
            #print("pw2w1 = " + (str)(pw2w1))
            #pw2w1 = (float)(1/pw2w1)
        perpForBiGram = perpForBiGram + math.log2(pw2w1)
        if dic3[ch1][ch2][ch3] == 0:
            pw3w2w1 = n3[0]
        else:
            pw3w2w1 = (float)((dic3[ch1][ch2][ch3] + 1) * (n3[dic3[ch1][ch2][ch3] + 1]+1) / (n3[dic3[ch1][ch2][ch3]]+1))
            #print("n3[dic3[ch1][ch2][ch3] + 1]+1 = "+(str)(n3[dic3[ch1][ch2][ch3] + 1]+1))
            #print("(n3[dic3[ch1][ch2][ch3]]+1) = "+(str)((n3[dic3[ch1][ch2][ch3]]+1)))
            pw3w2w1 = (float)(pw3w2w1 / ((dic2[ch1][ch2] + 1) * (n2[dic2[ch1][ch2] + 1]+1) / (n2[dic2[ch1][ch2]]+1)))
            #print("pw3w2w1 = " + (str)(pw3w2w1))
            #pw3w2w1 = (float)(1/pw3w2w1)
        perpForTriGram = perpForTriGram + math.log2(pw3w2w1)
        if dic4[ch1][ch2][ch3][ch4] == 0:
            pw4w3w2w1 = n4[0]
        else:
            pw4w3w2w1 = (float)((dic4[ch1][ch2][ch3][ch4] + 1) * (n4[dic4[ch1][ch2][ch3][ch4] + 1]+1) / (n4[dic4[ch1][ch2][ch3][ch4]]+1))
            pw4w3w2w1 = (float)(pw4w3w2w1 / ((dic3[ch1][ch2][ch3] + 1) * (n3[dic3[ch1][ch2][ch3] + 1]+1) / (n3[dic3[ch1][ch2][ch3]]+1)))
            #print("pw4w3w2w1 = " + (str)(pw4w3w2w1))
            #pw4w3w2w1 = (float)(1/pw4w3w2w1)
        perpForFourGram = perpForFourGram + math.log2(pw4w3w2w1)
        if dic5[ch1][ch2][ch3][ch4][ch5] == 0:
            pw5w4w3w2w1 = n5[0]
        else:
            pw5w4w3w2w1 = (float)((dic5[ch1][ch2][ch3][ch4][ch5] + 1) * (n5[dic5[ch1][ch2][ch3][ch4][ch5] + 1]+1) / (n5[dic5[ch1][ch2][ch3][ch4][ch5]]+1))
            pw5w4w3w2w1 = (float)(pw5w4w3w2w1 / ((dic4[ch1][ch2][ch3][ch4] + 1) * (n4[dic4[ch1][ch2][ch3][ch4] + 1]+1) / (n4[dic4[ch1][ch2][ch3][ch4]]+1)))
            #print("pw5w4w3w2w1 = " + (str)(pw5w4w3w2w1))
            #pw5w4w3w2w1 = (float)(1/pw5w4w3w2w1)
        perpForFiveGram = perpForFiveGram + math.log2(pw5w4w3w2w1)
        
        i = i + 1

    
        
  
def main():
    lower_Input('C:/Users/Dell/Desktop/NLP/HW2/data.txt','C:/Users/Dell/Desktop/NLP/HW2/data_lower.txt')
    lower_Input('C:/Users/Dell/Desktop/NLP/HW2/test.txt','C:/Users/Dell/Desktop/NLP/HW2/test_lower.txt')
    countNgrams()
    

main()
