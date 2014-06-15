#! /usr/bin/python
import wordladder
s=wordladder.Solution()
start='hit'
end='cog'
dict=['hot','dot','dog','lot','log']
print s.ladderLength(start,end,dict)
