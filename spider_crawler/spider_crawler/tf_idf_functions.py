import math
import json
import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 


def readAndProcess():
    dictUrlToNum={}
    dictNumToUrl={}
    with open('D:\Sem2\IR\SearchEngineProject\spider_crawler\spider_crawler\output.json', 'r') as openfile: 
          # Reading from json file 
        json_objects = json.load(openfile)

    #Perform preprocessing 
    urlTitle={}
    urlContent={}
    lines=[]
    index=1
    for obj in json_objects:
        #print(obj['url'])
        urlTitle[obj['url']]=obj['title']
        obj['content']=obj['content'].replace('\n',' ')
        urlContent[obj['url']]=obj['content']
        obj['content']= obj['content'].lower()
        
        obj['content']=re.sub(r'[^A-Za-z0-9 ]+', ' ', obj['content'])
        obj['content'] = re.sub("^\d+\s|\s\d+\s|\s\d+$", '', obj['content'])
        #print(obj['content'])
        lines.append(obj['content'])
        
        dictNumToUrl[index]=obj['url']
        dictUrlToNum[obj['url']]=index
        index+=1
    #print(dictUrlToNum)
    return json_objects,lines,dictUrlToNum,dictNumToUrl,urlTitle,urlContent

def tokenize(lines):
    tokens=[]
    for line in lines:
        tokens.append(word_tokenize(line)) 
    return tokens

def stopWords(final_tokens):
    stop_words = set(stopwords.words('english'))
    filtered_words = []
    for list_item in final_tokens:
        temp=[]
        for word in list_item:
            if word not in stop_words:
                temp.append(word)
        filtered_words.append(temp)
    
    return filtered_words

unstem={}
#Function to stem words 
def stem(filtered_words):
    ps = PorterStemmer()
    stem=[]
    for list in filtered_words:
        temp=[]
        for word in list:
           temp.append(ps.stem(word))
           unstem[ps.stem(word)] = word
        stem.append(temp)
     
    '''               
    for w in filtered_words:
        stem.append(ps.stem(w))
    '''
    return stem,unstem 

def calHashDocTokenFreq(finalTokens):
    dict1={}
    i=1
    for doc in finalTokens:
        for token in doc:
            if token not in dict1.keys():
                dict2={}
                dict2[i] = 1
                dict1[token]=dict2
            else:
                temp_dict=dict1.get(token)
                if i not in temp_dict.keys():
                    temp_dict[i]=1
                else:
                    temp_dict[i]+=1
        i=i+1
    return dict1

def calTfIdf(dict1,finalTokens):
    dict3Weight={}
    dict5WSq={}
    j=1
    for doc in finalTokens:
        weights={}
        sumW=0
        for token in set(doc):
            idf=math.log2(len(finalTokens)/len(dict1.get(token)))
            tf=((dict1.get(token).get(j)) /len(doc))
            weight=tf*idf
            #print(weight)
            weights[token]=weight
            sumW=sumW+(weight*weight)
        dict3Weight[j]=weights
        dict5WSq[j]=sumW
        j=j+1
    return dict3Weight,dict5WSq 

def processQuery(q):
    q=q.lower()
    q=q.replace('\n',' ')
    q=re.sub(r'[^A-Za-z0-9 ]+', '', q)

    return q

def calTfIdfQuery(stem_query,dict1,numOfDocs):
    k=1
    dict4qWeight={}
    for q in stem_query:
        weights={}
        for token in q:
            if token in dict1.keys():
                idf=math.log2(numOfDocs/len(dict1.get(token)))
                tf=(q.count(token)/len(q))
                weight=idf*tf
                weights[token]=weight
        dict4qWeight[k]=weights
        k=k+1
    return dict4qWeight

def calCosinSim(dict4qWeight,finalTokens,dict3Weight,dict5WSq):
    dict6coSim={}
    i=1
    j=1
    for q in dict4qWeight:
        i=1
        temp={}
        for doc in finalTokens:
            num=0
            if not (set(dict4qWeight[q].keys()).isdisjoint(set(doc))):    #Terms match in query and document
                common=[]
                common=set(dict4qWeight[q].keys()).intersection(set(doc))
                for word in common:
                    num=num+(dict4qWeight[q].get(word)*dict3Weight[i].get(word))
                den=math.sqrt(dict5WSq.get(i))
                cosim=num/den
                temp[i]=cosim
            i+=1
        dict6coSim[j]=temp
        j+=1
    return dict6coSim

