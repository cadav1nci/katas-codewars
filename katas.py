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