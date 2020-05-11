from tf_idf_functions import readAndProcess,tokenize,stopWords,stem,calHashDocTokenFreq,calTfIdf,processQuery,calTfIdfQuery,calCosinSim
from PyQt5.QtWidgets import QApplication,QLabel, QWidget,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit, QTextEdit, QTextBrowser,QPushButton, QMessageBox
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QPixmap
import pickle
def textchanged():
    text=e1.text()
    print ("Contents of text box: "+str(text))
    q=str(text)

    global count

    #Process queries
    q2=processQuery(q)
    print(q2)
    query=[]
    query.append(q2)
    token_query=tokenize(query)
    filtered_query=stopWords(token_query)
    stem_query,unstem_query=stem(filtered_query)
    print(stem_query)
    dict4qWeight=calTfIdfQuery(stem_query,dict1,len(finalTokens))

    #Calculate the cosine similarity
    dict6coSim=calCosinSim(dict4qWeight,finalTokens,dict3Weight,dict5WSq)

    #Combine TF-IDF and page rank
    for q in dict6coSim:
        docs=dict6coSim[q]
        urls_score={ }
        for k in list(docs.keys()):
            urls_score[dictNumToUrl[k]]=((0.25)*docs[k]) + ((0.75)*node_scores[dictNumToUrl[k]])
    #print(urls_score)

    #Storing retrieved docs and similarity 
    global li
    li=list(sorted(urls_score.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
    #print(li)
    if(len(li)==0):
        msg = QMessageBox()
        msg.setWindowTitle("UIC Search Engine")
        msg.setText("No results to show!")
        msg.setIcon(QMessageBox.Question)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()   
        return  
    extend=[]
    extend_nums=[]
    j=0
    for k in li:
        if(j==30):
            break
        extend.append(k[0])
        extend_nums.append(dictUrlToNum[k[0]])
        j+=1
    print(extend_nums)

    final_dict={}
    for num in extend_nums:
        words_tfIdf=dict3Weight[num]
        for q in stem_query[0]:
            if q in words_tfIdf:
                words_tfIdf = {key:val for key, val in words_tfIdf.items() if key != q}
                  
                
        sorted_tfIdf=list(sorted(words_tfIdf.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
        
        sorted_tfIdf=sorted_tfIdf[:100]
        top_words=[]
        for word_score in sorted_tfIdf:
            if word_score[0] in final_dict.keys():
                sum1=final_dict[word_score[0]]
                sum1+=word_score[1]
                final_dict[word_score[0]]=sum1
            else:
                final_dict[word_score[0]]=word_score[1]
        
        final_sorted=list(sorted(final_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
        
    extended_query=[]
    k=0
    for pair in final_sorted:
        if(k==10):
            break
        extended_query.append(unstem[pair[0]])
        k+=1
    print(extended_query)
    lb0.show()
    lb1.setText(extended_query[0])
    lb2.setText(extended_query[1])
    lb3.setText(extended_query[2])
    lb4.setText(extended_query[3])
    lb5.setText(extended_query[4])
    lb6.setText(extended_query[5])
    lb7.setText(extended_query[6])
    lb8.setText(extended_query[7])
    lb9.setText(extended_query[8])
    lb10.setText(extended_query[9])
    #Printing the links in the text box
    i=0
    te.clear()
    count+=1
    for k in li:
        if(i==10):
            break
        contentOriginal=urlContent[k[0]]
        contentOriginal=contentOriginal.split()
        contentOriginal=contentOriginal[150:200]
        contentShow=' '.join(contentOriginal)
        te.append("<a href='"+k[0]+"'>"+k[0]+"</a><h4>"+urlTitle[k[0]]+"</h4> <small>"+"... "+contentShow+" ..." +"</small><br></br><br></br>")
        #te.append('<a href='+k[0]+'></a>')
        i+=1
    print("done")

def on_click():
    global count
    count+=1
    print("Count:"+str(count))
    end= count*10
    start= end-10
    print("Start: "+str(start)+" end: "+str(end))
    for i in range(start,end+1):
        if(i>=len(li)):
            msg = QMessageBox()
            msg.setWindowTitle("UIC Search Engine")
            msg.setText("No more results to show!")
            msg.setIcon(QMessageBox.Question)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_() 
            print(len(li))
            print("No more results to show!")
            break
        contentOriginal=urlContent[li[i][0]]
        contentOriginal=contentOriginal.split()
        contentOriginal=contentOriginal[150:200]
        contentShow=' '.join(contentOriginal)
        te.append("<a href='"+li[i][0]+"'>"+li[i][0]+"</a><h4>"+urlTitle[li[i][0]]+"</h4> <small>"+"... "+contentShow+" ..." +"</small><br></br><br></br>")
        #print("<a href='"+li[i][0]+"'>"+li[i][0]+"</a>")


if __name__ == "__main__":
    li=[]
    count=0

    dbfile = open('finalTokens.pickle', 'rb')      
    finalTokens = pickle.load(dbfile) 

    dbfile2 = open('dict1.pickle', 'rb')      
    dict1 = pickle.load(dbfile2) 

    dbfile3 = open('dict3Weight.pickle', 'rb')      
    dict3Weight = pickle.load(dbfile3) 

    dbfile4 = open('dict5WSq.pickle', 'rb')      
    dict5WSq = pickle.load(dbfile4) 

    dbfile5 = open('node_scores.pickle', 'rb')      
    node_scores = pickle.load(dbfile5) 

    dbfile6= open('dictNumToUrl.pickle', 'rb')      
    dictNumToUrl = pickle.load(dbfile6) 

    dbfile7= open('dictUrlToNum.pickle', 'rb')      
    dictUrlToNum = pickle.load(dbfile7)

    dbfile8= open('unstem.pickle', 'rb')      
    unstem = pickle.load(dbfile8) 

    

    dbfile10= open('urlContent.pickle', 'rb')      
    urlContent = pickle.load(dbfile10) 

    dbfile9= open('urlTitle.pickle', 'rb')      
    urlTitle = pickle.load(dbfile9) 

    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout2 = QHBoxLayout()
    layout3= QHBoxLayout()
    layout4= QHBoxLayout()
    lb0=QLabel('Consider adding the following to your query:')
    lb1=QLabel('')
    lb2=QLabel('')
    lb3=QLabel('')
    lb4=QLabel('')
    lb5=QLabel('')
    lb6=QLabel('')
    lb7=QLabel('')
    lb8=QLabel('')
    lb9=QLabel('')
    lb10=QLabel('')
    layout2.addWidget(lb1)
    layout2.addWidget(lb2)
    layout2.addWidget(lb3)
    layout2.addWidget(lb4)
    layout2.addWidget(lb5)

    layout3.addWidget(lb6)
    layout3.addWidget(lb7)
    layout3.addWidget(lb8)
    layout3.addWidget(lb9)
    layout3.addWidget(lb10)

    label_img = QLabel()
    pixmap = QPixmap("uic_v_small.png")
    print(pixmap.width())
    label_img.setPixmap(pixmap)

    #label_img.setGeometry(100,100,200,100)
    label = QLabel('Enter query:')
    layout4.addWidget(label_img)
    layout4.addWidget(label)
    lb0.hide()
    
    button=QPushButton('Show more results')
    e1 = QLineEdit()
    te = QTextBrowser()
    te.setOpenExternalLinks(True)
    button2=QPushButton('Search')
    button2.clicked.connect(textchanged)
    print("Here")
    button.clicked.connect(on_click)
    #e1.editingFinished.connect(textchanged)
    layout4.addWidget(e1)
    layout4.addWidget(button2)
    # layout.addWidget(label)
    # layout.addWidget(e1)
    layout.addLayout(layout4)
    layout.addWidget(lb0)
    layout.addLayout(layout2)
    layout.addLayout(layout3)
    layout.addWidget(te)
    layout.addWidget(button)
        
    window.setLayout(layout)
    window.setWindowTitle('UIC Search Engine')
    window.resize(800,600)
    window.show()
        
        #label.show()  
    app.exec_()       