"""
Kata level 6
link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

"""
import string

def is_pangram(s):
    #fs stands for formated string
    fs = ''.join(e for e in s if e.isalnum()).lower()
    a = list("abcdefghijklmnopqrstuvwxyz")
    b = []
    for i in a:
        if i in fs:
            b.append(i)
    if a == b:
        return True
    return False

"""
kata level 6
link: https://www.codewars.com/kata/514b92a657cdc65150000006

"""
def solution(x):
  suma = 0
  if x > 1:
      for i in range(x):
        if (i%5==0 or i%3==0):
            suma = suma + i
  return suma       

"""
kata level 6
link: https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

"""
def find_it(seq):
    pairs = {}
    
    #this block creates a dictionary in which its key is the integer
    #and the value, the amount of ocurences for that integer in the list
    for i in  seq:
        if i not in pairs.keys():
            pairs[i] = 0
        pairs[i] = pairs[i] + 1
        
    key_list = list(pairs.keys())
    val_list = list(pairs.values())
    
    #if the module 2 of a element in the list of values
    #is different than 0 then return its key
    for i in range(len(val_list)):
        if(val_list[i]%2 != 0):
            return key_list[i]


"""
Kata level 8
link: https://www.codewars.com/kata/58f8a3a27a5c28d92e000144

"""
def first_non_consecutive(arr):
    if(len(arr)<=1):
        return None
    for i in range(0,len(arr)-1):
        if arr[i+1] - arr[i] > 1:
            return arr[i+1]
    return None


