# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:29:09 2019

@author: OmidHajipoor
"""

'''
**************************************************************************
*         Project: Design And Simulating Context-sensitive Lexicon       *
*                           For Persian Language                         *
*                         Programmer: OmidHajipoor                       *
*                   Gmail: Omid.Hajipoor0770@Gmail.com                   *
**************************************************************************
'''


import nltk
import gensim
import os
import time


class w2v:
    def __init__(self,domainTxt , windows , n ):
        self.domainTxt=domainTxt
        self.windows=windows
        self.n=n

    def sent_seprate(txt):
            sent=[] 
            if type(txt)==list:
                for line in txt:
                    if line==[]:
                        continue
                    else:
        
                        file = nltk.word_tokenize(line)
        
                        newfile = ''
                        j=0
                        for word in file:
                            j+=1
                            if len(word.split('.'))>1 or len(word.split("\n"))>1 or word=="." or j==len(file):
                                newfile=newfile+' '+word
                                sent.append(newfile)
                                newfile=''
                            else:
                                newfile=newfile+' '+word
        
            else:
                file = nltk.word_tokenize(txt)
                newfile = ''
                for word in file:        
                    if len(word.split('.'))>1 or len(word.split("\n"))>1 or word=="." :
                        newfile=newfile+' '+word
                        sent.append(newfile)
                        newfile=''
                    else:
                        newfile=newfile+' '+word
                
            return sent

    def learnW2v(self):
        sent=w2v.sent_seprate(self.domainTxt)
        sentences=[]
        for s in sent:
            sentences.append(nltk.word_tokenize(s))
        
        model = gensim.models.Word2Vec(sentences ,size=1000 , window=self.windows , min_count=self.n , workers=4 , alpha=0.025 )
        model.train(sentences, total_examples=len(sentences), epochs=1000)
        
        
        localtime = time.asctime( time.localtime(time.time()) )
        add='Model'
        if os.path.exists(add):
            newAdd=add+'/Model_'+localtime.replace(' ' , '_').replace(':' , '_')
            model.save(newAdd)
        else:
            os.makedirs(add)
            newAdd=add+'/Model_'+localtime.replace(' ' , '_').replace(':' , '_')
            model.save(newAdd)
            
            
        return model