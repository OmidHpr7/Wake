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

cntTxt = open('Data/mydata.txt' , 'r' , encoding='utf8').readlines()
shortTxt = cntTxt[10]

#initial Param
numKey=10
word2vec_param=(5,2)



# =============================================================================
# keyword extraction with pretrained model
# =============================================================================

use_PreTrain_Model = 1
model_add = 'Model/Model_Wed_Apr__3_16_32_06_2019'

wake = Wake.wake(cntTxt , use_PreTrain_Model, word2vec_param, model_add)
key = wake.keyword_EXT(shortTxt,numKey)

print(key)


'''
# =============================================================================
# keyword extraction with traning model
# =============================================================================

use_PreTrain_Model = 0

wake = Wake.wake(cntTxt , use_PreTrain_Model, word2vec_param)
key = wake.keyword_EXT(shortTxt,numKey)

print(key)
'''
