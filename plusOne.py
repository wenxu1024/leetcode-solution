class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits.reverse()
        newdigits=[]
        carry=1
        for d in digits:
            d=d+carry
            if d>=10:
                d=d-10
                carry=1
            else:
                carry=0
            newdigits.append(d)
        if carry:
            newdigits.append(carry)
        else:
            pass
        newdigits.reverse()
        return newdigits
            
