#! /usr/bin/python
class Solution:
  #@param start, a string
  #@param end, a string
  #@param dict,a set of string
  #@return an integer
  def ladderLength(self,start,end,dict):
    dict=set(dict)
    q=Queue()
    q.push(start)
    l=0
    d={}
    visited={}
    dict.add(start)
    dict.add(end)
    d[start]=0
    for s in dict:
      visited[s]=False
    while q:
      item=q.pop()
      visited[item]=True
      if item==end:
        return d[item]+1
#      for s in dict:
#        if self.differone(s,item) and visited[s]==False:
#          q.push(s)
#          visited[s]=True
#          d[s]=d[item]+1
      print self.stos(item)
      for s in self.stos(item):
        if s in dict and visited[s]==False:
          q.push(s)
          visited[s]=True
          d[s]=d[item]+1
    return 0

  def differone(self,s,item):
    l=len(s)
    count=0
    for i in range(l):
      if not s[i]==item[i]:
        count+=1
    if count==1:
      return True
    else:
      return False

  def stos(self,s):
    listofs=[]
    l=len(s)
    for i in xrange(l):
      for c in map(chr,range(97,123)):
        stemp=s[:i]+c+s[i+1:]
        if not stemp==s:
          listofs+=[stemp]
    return listofs

class Node:
  def __init__(self,x):
    self.Value=x
    self.Next=None
    self.Prev=None
    return

class Queue:
  def __init__(self):
    self.n=0
    self.head=None
    self.tail=None
    return

  def __len__(self):
    return self.n

  def push(self,x):
    item=Node(x)
    temp=self.head
    self.head=item
    self.head.Next=temp
    if temp==None:
      self.tail=item
      self.tail.Prev=temp
    else:
      temp.Prev=self.head
    self.n=self.n+1
    return

  def pop(self):
    x=self.tail.Value
    temp=self.tail
    self.tail=self.tail.Prev
    if self.tail==None:
      self.head=None
    else:
      self.tail.Next=None
    self.n=self.n-1
    return x

  def __print__(self):
    item=self.head
    while item:
      print item.Value
      item=item.Next
    return
