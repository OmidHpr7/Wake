# -*- coding: utf-8 -*-
""" **************************************************************************
                           Created on 2021
                        @author: Omid Hajipoor
                    Email: hajipoor.omid@aut.ac.ir
                  Gmail: omid.hajipoor0770@Gmail.com
***************************************************************************"""



import nltk

class Pre_proc:
    def __init__(self,txt):
        self.txt=txt

    def makerule(self, context):
        data=self.txt
        rule_after = {}
        rule_befor = {}
        words = data.split(' ')
        index = context
     
        for word in words[index:]:
            key = ' '.join(words[index-context:index])
            if key in rule_after:
                rule_after[key].append(word)
            else:
                rule_after[key] = [word]
            index += 1
            if word in rule_befor:
                rule_befor[word].append(key)
            else:
                rule_befor[word] = [key]
            
        return rule_after,rule_befor

    def find_stopWord(self):
        file = nltk.word_tokenize(self.txt)
        dict_stopword={}
        stopWord=[]
        fin=open('utils\stopword With verb whtout dot.txt',encoding='utf8')
        
        for word in fin.readlines():
            stopWord.append(word.replace('\n', '').lower().replace(' ', '').lower().replace(' ', '').upper().replace('\ufeff', '').lower().replace('\ufeff', '').upper())

        for w in range(0,len(file)):
            word=file[w]
            word=word.replace(' ', '')
            if (word in stopWord) or (word.isdigit()):
                if word in dict_stopword:
                    if w-1<0 or w+1==len(file):
                        continue
                    else:
                        dict_stopword[word].append([file[w-1] , file[w+1]])
                        continue
                else:
                    dict_stopword[word]=[]
                    dict_stopword[word].append([file[w-1] , file[w+1]])
                    continue
        return dict_stopword 

    def PreProc(self):   
        def delete_Stopword(txt):
            def delete(txt):
                file = nltk.word_tokenize(txt)
                newFile=''
                dict_stopword={}
                stopWord=[]
                fin=open('utils\stopword With verb whtout dot.txt',encoding='utf8')
                
                for word in fin.readlines():
                    stopWord.append(word.replace('\n', '').lower().replace(' ', '').lower().replace(' ', '').upper().replace('\ufeff', '').lower().replace('\ufeff', '').upper())
        
                for w in range(0,len(file)):
                    word=file[w]
                    word=word.replace(' ', '')
                    if (word in stopWord) or (word.isdigit()):
                            continue
                    else:
                        newFile = newFile + ' ' + word
                    self.dict_stop=dict_stopword
                return newFile 
        
            #-----------------------------------------------------    
            if type(txt)==list:
                delStop=[]
                for line in txt:
                    delStop.append(delete(line))
                return(delStop)
            else:
                return delete(txt)
             
    
        def normalizer(txt):
            if type(txt)==list:
                normLine=[]
                for line in txt:
                    if line==[]:
                        continue
                    else:
                        file = nltk.word_tokenize(line)
                        newfile=''
                        for word in file:
                            word = word.replace("\u200c", " ").replace(".", ". ").upper().replace("\ufeff\n"," ").lower().replace(
                                "،", "، ").upper().replace('ة' , 'ه').replace('ي', 'ی').replace("؛" , '؛ ').upper().replace("؛" , ' ؛').lower().replace("." , ' .').lower().replace(
                                        "،", " ،").lower().replace('\xa0',' ')
                            newfile = newfile + ' ' + word
                        normLine.append(newfile)
                return normLine
        
            else:
                file = nltk.word_tokenize(txt)
                newfile=''
                for word in file:
                    word = word.replace("\u200c", " ").replace(".", ". ").upper().replace("\ufeff\n"," ").lower().replace(
                            "،", "، ").upper().replace('ة' , 'ه').replace('ي', 'ی').replace("؛" , '؛ ').upper().replace("؛" , ' ؛').lower().replace("." , ' .').lower().replace(
                                "،", " ،").lower().replace('\xa0',' ')
                    newfile = newfile + ' ' + word
                return newfile
    
        newtxt=normalizer(delete_Stopword(self.txt))
                
        return newtxt

# =============================================================================
#         ngram exraction
# =============================================================================
        
    def ngrams(input, n):
        input = nltk.word_tokenize(input)
        
        output = {}
        for i in range(len(input)-n+1):
            g = ' '.join(input[i:i+n])
            if ("." or" " or "-") in nltk.word_tokenize(g):
                    continue
            else:
                    output.setdefault(g, 0)
                    output[g] += 1
          
        return output 




     
