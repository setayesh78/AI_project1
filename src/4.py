# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:31:22 2021

@author: Setayesh
"""
import re
from itertools import tee, islice
from collections import Counter


all_words_freq = 0
all_words_freq_pos = 0

def main():
    global all_words_freq
    global all_words_freq_pos
    negative_file_location = '.\\input\\rt-polarity.neg'
    #negative_file_location = '.\\input\\test.txt'
    positive_file_location = '.\\input\\rt-polarity.pos'
    
#    read_negative = open(negative_file_location, 'r')
#    neg_lines = read_negative.readlines()

#    read_positive = open(positive_file_location, 'r')
#    pos_lines = read_positive.readlines()
    
    
    
    #0. preprocessing : removing punctuation marks   
#    write_negative = open(".\\input\\no_punc.neg", 'w')
    punctuation = "!@#$%^&*()_=-+<>?:.,;{}[]/\\~\"\'"  
 
#    for line in neg_lines:
#        for char in line:
#            if char in punctuation:
#                line = line.replace(char, " ")
#        write_negative.write(line)
#    write_negative.close() 
    
    
#    write_positive = open(".\\input\\no_punc.pos", 'w')
#    for line in pos_lines:
#        for char in line:
#            if char in punctuation:
#                line = line.replace(char, " ")
#        write_positive.write(line)        
#    write_positive.close() 
    
    
        
    #1. dictionary : separating comment into + or - dictionaries    
    neg_dictionary = []  
    pos_dictionary = []  
    read_no_punc_neg = open(".\\input\\no_punc.neg", 'r')
    no_punc_neg = read_no_punc_neg.read()
    
    
    neg_dictionary = no_punc_neg.split()
        
    
    read_no_punc_pos = open(".\\input\\no_punc.pos", 'r')
    no_punc_pos = read_no_punc_pos.read()
    
    
    pos_dictionary = no_punc_pos.split()    
  
    
    
    #2. ONE words frequency
    one_word_freq_negative = open(".\\input\\one_word_freq.neg", 'w')
    one_word_freq_positive = open(".\\input\\one_word_freq.pos", 'w')
#    one_word_frequency = {}
    
#    for i in range(0,len(neg_dictionary)):
#        counter = 0
#        for j in range(0,len(neg_dictionary)):
#            if neg_dictionary[i] == neg_dictionary[j]:
#                counter += 1
#        if counter >= 2 :        
#            one_word_frequency[neg_dictionary[i]] = counter
      
#    one_word_sorted_freq = dict(sorted(one_word_frequency.items(), key=lambda item: item[1],reverse=True))    
    
#    one_word_most_repeated = dict(sorted(one_word_frequency.items(),key = lambda item: item[1],reverse=True)[:10])
    
    #delete 10 most repeted
#    one_word_freq_after_removing = {}
#    for key in one_word_sorted_freq.keys():
#        if key not in one_word_most_repeated:
#            one_word_freq_after_removing[key] = one_word_sorted_freq[key]
    
#    one_word_freq_negative.write(str(one_word_freq_after_removing))  
        
#    print("\n\n\n*************************************************")
#    print(one_word_freq_after_removing)
    
    count1 = Counter(ngrams(neg_dictionary,1))

    one_word_freq = {}
    i = -1
    for num in list(count1.values()):
        i += 1
        if num >= 2 :
            one_word_freq[list(count1.keys())[i]] = num
            all_words_freq += num
            
    one_word_sorted_freq = dict(sorted(one_word_freq.items(), key=lambda item: item[1],reverse=True)) 
    
    one_word_most_repeated = dict(sorted(one_word_sorted_freq.items(),key = lambda item: item[1],reverse=True)[:10])
    
    #delete 10 most repeted
    one_word_freq_after_removing = {}
    for key in one_word_sorted_freq.keys():
        if key not in one_word_most_repeated:
            one_word_freq_after_removing[key] = one_word_sorted_freq[key]
    
    one_word_freq_negative.write(str(one_word_freq_after_removing))  
 
    
    count1_pos = Counter(ngrams(pos_dictionary,1))

    one_word_freq_pos = {}
    i = -1
    for num in list(count1_pos.values()):
        i += 1
        if num >= 2 :
            one_word_freq_pos[list(count1_pos.keys())[i]] = num
            all_words_freq_pos += num
            
    one_word_sorted_freq_pos = dict(sorted(one_word_freq_pos.items(), key=lambda item: item[1],reverse=True)) 
    
    one_word_most_repeated_pos = dict(sorted(one_word_sorted_freq_pos.items(),key = lambda item: item[1],reverse=True)[:10])
    
    #delete 10 most repeted
    one_word_freq_after_removing_pos = {}
    for key in one_word_sorted_freq_pos.keys():
        if key not in one_word_most_repeated_pos:
            one_word_freq_after_removing_pos[key] = one_word_sorted_freq_pos[key]
    
    one_word_freq_positive.write(str(one_word_freq_after_removing_pos))     
    
    
    one_word_freq_negative.close()
    one_word_freq_positive.close()
    
 
    
   #2. TWO words frequency 
    two_word_freq_negative = open(".\\input\\two_word_freq.neg", 'w')
    two_word_freq_positive = open(".\\input\\two_word_freq.pos", 'w')
    
    count = Counter(ngrams(neg_dictionary,2))

    two_word_freq = {}
    i = -1
    for num in list(count.values()):
        i += 1
        if num >= 2 :
            two_word_freq[list(count.keys())[i]] = num
            
    two_word_sorted_freq = dict(sorted(two_word_freq.items(), key=lambda item: item[1],reverse=True)) 
#    print(two_word_sorted_freq)
    
    two_word_most_repeated = dict(sorted(two_word_sorted_freq.items(),key = lambda item: item[1],reverse=True)[:10])
    
    #delete 10 most repeted
    two_word_freq_after_removing = {}
    for key in two_word_sorted_freq.keys():
        if key not in two_word_most_repeated:
            two_word_freq_after_removing[key] = two_word_sorted_freq[key]
    
    two_word_freq_negative.write(str(two_word_freq_after_removing))  

   

    

    count_pos = Counter(ngrams(pos_dictionary,2))

    two_word_freq_pos = {}
    i = -1
    for num in list(count_pos.values()):
        i += 1
        if num >= 2 :
            two_word_freq_pos[list(count_pos.keys())[i]] = num
            
    two_word_sorted_freq_pos = dict(sorted(two_word_freq_pos.items(), key=lambda item: item[1],reverse=True)) 
    
    two_word_most_repeated_pos = dict(sorted(two_word_sorted_freq_pos.items(),key = lambda item: item[1],reverse=True)[:10])
    
    #delete 10 most repeted
    two_word_freq_after_removing_pos = {}
    for key in two_word_sorted_freq_pos.keys():
        if key not in two_word_most_repeated_pos:
            two_word_freq_after_removing_pos[key] = two_word_sorted_freq_pos[key]
    
    two_word_freq_positive.write(str(two_word_freq_after_removing_pos))  

    
    two_word_freq_negative.close()
    two_word_freq_positive.close()
   

    #3. calculating  
    #running the code : 
    landa1 = 1/3 
    landa2 = 1/3  
    landa3 = 1/3
    epsilon = 0.000000000001      
    sentence = input("enter your sentence : \n")
    while(sentence != "!q"):
        for char in sentence:
            if char in punctuation:
                sentence = sentence.replace(char, " ")        
        inpt = []
        inpt = sentence.split()
        print(inpt)
        
        #p for negative language model
        temp_p = 1 
        for i in range(1 , len(inpt)):
            if count1[(str(inpt[i-1]),)] !=0 and all_words_freq != 0:
                temp_p = temp_p *( landa1 * (count[(str(inpt[i-1]),str(inpt[i]))] / count1[(str(inpt[i-1]),)]) + landa2 * (count1[(str(inpt[i]),)] /all_words_freq) + landa3 * epsilon)
            else :
                print( "\"" + str(inpt[i-1]) + "\"" + " this word not trained")
                sentence = input("enter your sentence : \n")
                break;
                                                                 
        p_neg_total =  (count1[(str(inpt[0]),)] / all_words_freq) * temp_p 

        
        #p for positive language model
        temp_p = 1 
        for i in range(1 , len(inpt)):
            if count1_pos[(str(inpt[i-1]),)] !=0 and all_words_freq_pos != 0:
                temp_p = temp_p *( landa1 * (count_pos[(str(inpt[i-1]),str(inpt[i]))] / count1_pos[(str(inpt[i-1]),)]) + landa2 * (count1_pos[(str(inpt[i]),)] /all_words_freq_pos) + landa3 * epsilon)
            else :
                print( "\"" + str(inpt[i-1]) + "\"" + " this word not trained")
                sentence = input("enter your sentence : \n")
                break;                

                                                                             
        p_pos_total =  (count1_pos[(str(inpt[0]),)] / all_words_freq_pos) * temp_p 

        
        print("---------------------")
        print(p_neg_total)
        print(p_pos_total)
        print("---------------------")        
        
        if p_neg_total >= p_pos_total:
            print("filter this")
        else:
            print("not filter this")
        
        
        sentence = input("enter your sentence : \n")
        
         
    
    
def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break    


if __name__=="__main__":
    main()


#good websites : 
#https://stackoverflow.com/questions/12488722/counting-bigrams-pair-of-two-words-in-a-file-using-python/27180278
#    

  
    