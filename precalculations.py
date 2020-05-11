from tf_idf_functions import readAndProcess,tokenize,stopWords,stem,calHashDocTokenFreq,calTfIdf,processQuery,calTfIdfQuery,calCosinSim
from pageRank import pageRank
import pickle 


if __name__ == "__main__":

    li=[]
    count=0
    #Preprocess the webpages
    jsonArray,lines,dictUrlToNum,dictNumToUrl,urlTitle,urlContent=readAndProcess()
    tokens=tokenize(lines)
    filteredWords=stopWords(tokens)
    stemmed_words,unstem=stem(filteredWords)
    finalTokens=stopWords(stemmed_words)

    #cdprint(unstem)
    
        
    #Calculating hash table consisting of terms doc and freq term-> doc1:4,doc2:5...
    dict1=calHashDocTokenFreq(finalTokens)
    
    #Calculting tf-idf of docs and storing it in hash table doc-> term,weight
    dict3Weight,dict5WSq=calTfIdf(dict1,finalTokens)
    #print(dictNumToUrl[2])

    #Calculate PageRank
    node_scores=pageRank(jsonArray)
    counter=0
    for obj in jsonArray:
        counter=counter+len(obj['out_links'])
    print("Total number of outlinks:"+str(counter))

    dictNumToUrlFile = open('dictNumToUrl.pickle', 'wb') 
    # source, destination 
    pickle.dump(dictNumToUrl, dictNumToUrlFile)                      
    dictNumToUrlFile.close() 


    finalTokensFile = open('finalTokens.pickle', 'wb') 
    # source, destination 
    pickle.dump(finalTokens, finalTokensFile)                      
    finalTokensFile.close() 
    

    dict1File = open('dict1.pickle', 'wb') 
    # source, destination 
    pickle.dump(dict1, dict1File)                      
    dict1File.close() 
    

    dict3WeightFile = open('dict3Weight.pickle', 'wb') 
    # source, destination 
    pickle.dump(dict3Weight, dict3WeightFile)                      
    dict3WeightFile.close() 
    
    dict5WSqFile = open('dict5WSq.pickle', 'wb') 
    # source, destination 
    pickle.dump(dict5WSq, dict5WSqFile)                      
    dict5WSqFile.close() 

    nodeScoresFile = open('node_scores.pickle', 'wb') 
    # source, destination 
    pickle.dump(node_scores, nodeScoresFile)                      
    nodeScoresFile.close() 

    dictUrlToNumFile = open('dictUrlToNum.pickle', 'wb') 
    # source, destination 
    pickle.dump(dictUrlToNum, dictUrlToNumFile)                      
    dictUrlToNumFile.close() 

    unstemFile = open('unstem.pickle', 'wb') 
    # source, destination 
    pickle.dump(unstem, unstemFile)                      
    unstemFile.close() 

    urlTitleFile = open('urlTitle.pickle', 'wb') 
    # source, destination 
    pickle.dump(urlTitle, urlTitleFile)                      
    urlTitleFile.close()

    urlContentFile = open('urlContent.pickle', 'wb') 
    # source, destination 
    pickle.dump(urlContent, urlContentFile)                      
    urlContentFile.close()

    
     
    print("Done!")

    
    
    