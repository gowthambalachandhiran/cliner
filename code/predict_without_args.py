# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 08:37:30 2019

@author: balacg1
"""

from predict import predict

predict('C://Users//balacg1//Desktop//Cliner//data//examples//ex_doc.txt', 'C://Users//balacg1//Desktop//Cliner//models//silver.crf', 'data//predictions', format='i2b2',use_lstm=False)