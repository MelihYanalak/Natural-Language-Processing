# -*- coding:utf-8 -*-
used = 0
total = 0
MAX = 15
dp = [[ ['#' for col in range(MAX)] for col in range(MAX)] for row in range(1000)]        # DEFINE 3D ARRAY
for i in range(1000):
       for j in range(MAX):
           for k in range(MAX):
               dp[i][j][k] = -1   # INITIALIZE ALL OF THE 3D ARRAY WITH -1 VALUE
def _3D_Edit_Distance(wordList,mainWord,dp):
    i = 0
    z = 1
    matchFound = 0
    resultList = {}
    while i < 1000 and i < len(wordList) and matchFound < 5:
        returnValue = (_2D_Edit_Distance(mainWord,wordList[i], len(mainWord), len(wordList[i]),z,i))
        if  returnValue != -2:
            if wordList[i] not in resultList:
                matchFound = matchFound + 1
                resultList[wordList[i]] = returnValue
        if i == len(wordList) - 1 and matchFound < 5 :
            z = z + 1
            i = -1
        i = i + 1
    return resultList
    

def _2D_Edit_Distance(str1, str2, m, n,z,x):  #z = limit  x = number of word
    global used
    global total
    total = total + (m * n)
    for i in range(m + 1): 
        for j in range(n + 1): 
            used = used + 1
            if i == 0:
                dp[x][i][j] = j   
  
            elif j == 0: 
                dp[x][i][j] = i  
  
            elif str1[i-1] == str2[j-1]: 
                dp[x][i][j] = dp[x][i-1][j-1] 
  
            else: 
                dp[x][i][j] = 1 + min(dp[x][i][j-1],dp[x][i-1][j],dp[x][i-1][j-1])

            if m > n:
                if i == j + (m - n):
                    if dp[x][i][j] > z:
                        return -2    
            else:
                if j == i + (n - m):
                    if dp[x][i][j] > z:
                        return -2  

                

    return dp[x][m][n]

    
    
def getWordsFromFile(inputFile):
    with open(inputFile, 'r', encoding='UTF-8') as f:    #read words from file
        words = f.read().splitlines()                           #split words 
    return words

def main():
    inputFile = input("Please enter the path of the input file\n")
    #inputFile = 'C:/Users/Dell/Desktop/NLP/HW1/input.txt'
    wordList = getWordsFromFile(inputFile)
    mainWord = input("Please enter the main word\n")
    resultList = _3D_Edit_Distance(wordList,mainWord,dp)
    print("\nTop 5 similar words are below")
    for key in resultList:
        print(key + " with the cost of " + str(resultList[key]))
    print("Usage percent of table is : ",end=""),
    print((float)(used/total)*100)
main()


