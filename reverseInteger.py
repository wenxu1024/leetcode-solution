class Solution:
    # @return an integer
    def reverse(self, x):
        if x>0:
            sign=1
        else:
            sign=-1
        x=abs(x)
        digits=[]
        while x:
            digits.append(x%10)
            x=x/10
        rx=0
        for d in digits:
            rx=rx*10+d
        return rx*sign
