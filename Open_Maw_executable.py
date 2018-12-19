#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In[69]:


import numpy as np


# In[70]:


def throw_has_double(result_set):

    for die_val in range(1,11):
        double_throws = np.sum(result_set == die_val,axis=1) >= 2
        if die_val == 1:
            doubles_for_any_die_val = double_throws
        else:
            doubles_for_any_die_val = np.logical_or(doubles_for_any_die_val, double_throws)
    return doubles_for_any_die_val

##  Example when die_val = 6   
#    #check if each die equals given die value,
#    #sum true values to get count
#    result_set =   array([[9, 1, 8, 6, 3, 3],
#        [4, 7, 3, 9, 5, 2],
#        [1, 5, 2, 3, 3, 9],
#        ..., 
#        [6, 8, 8, 1, 6, 6],
#        [8, 4, 3, 9, 1, 3],
#        [4, 9, 9, 5, 8, 7]])   
#  die_val =6 
#  result_set == die_val
#  array([[False, False, False,  True, False, False],
#        [False, False, False, False, False, False],
#        [False, False, False, False, False, False],
#        ..., 
#        [ True, False, False, False,  True,  True],
#        [False, False, False, False, False, False],
#        [False, False, False, False, False, False]], dtype=bool)
# np.sum(result_set == die_val,axis=1) 
# array([1, 0, 0, ..., 3, 0, 0])
# np.sum(result_set == 6,axis=1) >=2
# array([False, False, False, ...,  True, False, False], dtype=bool)


# In[79]:


def print_card_result_probabilities(result_set,dice_num):
    doubles_for_any_die_val = throw_has_double(result_set)
    # get throws that aren't doubles
    throws_without_doubles = result_set[~doubles_for_any_die_val]
    sum_of_throw = np.sum(throws_without_doubles,axis=1)
    #convert sum of throw into one of the 6 card results
    # 1-7 = 1
    # 8-15 = 2 ,etc
    bins = np.array([1, 8, 16, 23, 32,40,max(41,(dice_num*10)+1)])
    final_card_results = np.digitize(sum_of_throw,bins,right=False)
    count_of_card_results = []
    print("Number of Dice:",dice_num)
    for card_result in range(1,7):
        count_of_card_results.append(sum(final_card_results == card_result))
        deaths = sum(doubles_for_any_die_val)/dice_throws
    print ("Deaths","{:.2%}".format(deaths))
    for card_result in range(6):
        percent_of_throws = count_of_card_results[card_result]/dice_throws
        print(card_result,    "{:.2%}".format(percent_of_throws))
    print()


# In[ ]:


if __name__ == '__main__':
    for dice_num in range(1,10):
        dice_throws = 100000
        result_set = np.random.randint(low=1, high=10, size=(dice_throws, dice_num))
        print_card_result_probabilities(result_set, dice_num)

