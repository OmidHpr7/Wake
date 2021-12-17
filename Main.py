# -*- coding: utf-8 -*-
""" **************************************************************************
                           Created on 2021
                        @author: Omid Hajipoor
                    Email: hajipoor.omid@aut.ac.ir
                  Gmail: omid.hajipoor0770@Gmail.com
************************************************************************** """


import Wake


# =============================================================================
# read data:
#   you most read a domain file and text file
# =============================================================================
news=open('Data\Sanad2030.txt' , 'r' , encoding='utf8').readlines()
domainTxt=news
txt=domainTxt[4]
numKey=5
word2vec_param=(5,2)

use_PreTrain_Model = 0

wake = Wake.wake(domainTxt , use_PreTrain_Model, word2vec_param)
key = wake.keyword_EXT(txt,numKey)
