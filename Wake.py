# -*- coding: utf-8 -*-
""" **************************************************************************
                           Created on 2021
                        @author: Omid Hajipoor
                    Email: hajipoor.omid@aut.ac.ir
                  Gmail: omid.hajipoor0770@Gmail.com
************************************************************************** """


import nltk
import learnWord2vec
import math
import Helper
from gensim.models import Word2Vec


class wake:
    def __init__(self,*args, **kwargs):
        domainTxt = args[0]
        preTrainModel = args[1]
        t = Helper.Pre_proc(domainTxt)
        domainTxt = t.PreProc()
        self.domainTxt=domainTxt
        if preTrainModel==1 and len(args)==2:
            print('Error: '+"Addres for load model is not defined")
        elif preTrainModel==0:
            param=args[2]
            creatMod=learnWord2vec.w2v(domainTxt,param[0],param[1])
            self.model =creatMod.learnW2v()
        else:
            try:
                addLoad=args[3]
                self.model= Word2Vec.load(addLoad)
                print('Model Was loaded...')
            except NameError:
              print("Addres for load model is not defined")
# =============================================================================
#     input: txt , number of keyword
#     output: keywords and score
# =============================================================================
    
    def keyword_EXT(self,txt , numKey):
        t = Helper.Pre_proc(txt)
        doc=t.PreProc()
        vocab = self.model.wv.vocab
        

        token=nltk.word_tokenize(doc)
        final_word=[]
        for word in token:
            if word not in vocab:
                continue
            else:
                final_word.append(word)
                
                
        
        dis=[]
        for i in range(1,len(final_word)-1):
            s=[]
            s.append(final_word[i])
            s.append(self.model.wv.distance(final_word[i+1] ,final_word[i] ))
            s.append(self.model.wv.distance(final_word[i-1] ,final_word[i] ))
            dis.append(s)
        
        disSum={}
        co={}
        for line in dis:
            if line[0] in disSum:
                disSum[line[0]]+=line[1]
                co[line[0]]+=1
                disSum[line[0]]+=line[2]
                co[line[0]]+=1
            else:
                disSum[line[0]]=line[1]
                co[line[0]]=1
                disSum[line[0]]+=line[2]
                co[line[0]]+=1
        
        score={}
        n = Helper.Pre_proc.ngrams(doc,1)
        
        countN=0
        for w in n:
            countN+=n[w]
            
        
        pw={}
        for w in n:
            pw[w]=n[w]/countN
        
        for word in disSum:
            if word=='.':
                continue
            else:
                score[word]=disSum[word]*pw[word]/co[word]
        
        
        
        sorted_by_value_ngram = sorted(n.items(), key=lambda kv: kv[1])
        com={}
        ls=[]
        for w in sorted_by_value_ngram:
            w1=w[0]
            if w1 not in vocab:
                continue
            else:
                dist=0
                coo=0
                for i in range(len(final_word)):
                    if final_word[i] not in vocab:
                        continue
                    else:
                        dist+=self.model.wv.distance(w1,final_word[i] )
                        coo+=1
                com[w1]=dist/coo
                ls.append(com[w1])
        
        newScore={}
        for w in com:
            if (w in pw) and (w in com):
                
                if pw[w]==0:
                    newScore[w]=abs(math.log2(0.99)*com[w])
                else:
                    newScore[w]=abs(math.log2(pw[w])*com[w])
                
            else:
                continue
        
        sorted_by_value_com = sorted(newScore.items(), key=lambda kv: kv[1])
        
        selectedDoc=[]
        selectedDoc=sorted_by_value_com[0:numKey]#len(realKey[ss])numOfWord
        return selectedDoc
