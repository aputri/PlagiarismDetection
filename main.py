
# coding: utf-8

# In[58]:

import collections
from itertools import tee, islice

txt1 = raw_input("Enter file name of source text: ")
txt2 = raw_input("Enter file name of suspicious text: ")
n = input("Enter number for n-grams: ")

text = re.findall('\w+', open(txt1).read())
text += re.findall('\w+', open(txt2).read())

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

print(collections.Counter(ngrams(text, n)))


# 

# In[ ]:



