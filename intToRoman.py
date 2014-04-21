class Solution:
    # @return a string
    def intToRoman(self, num):
        s=''
        while num>=1000:
            num-=1000
            s=s+'M'
        if num>=900:
            s=s+'CM'
            num-=900
        if num>=500:
            s=s+'D'
            num-=500
        if num>=400:
            s=s+'CD'
            num-=400
        while num>=100:
            s=s+'C'
            num-=100
        if num>=90:
            s=s+'XC'
            num-=90
        if num>=50:
            s=s+'L'
            num-=50
        if num>=40:
            s=s+'XL'
            num-=40
        while num>=10:
            s=s+'X'
            num-=10
        if num>=9:
            s=s+'IX'
            num-=9
        if num>=5:
            s=s+'V'
            num-=5
        if num>=4:
            s=s+'IV'
            num-=4
        while num>=1:
            s=s+'I'
            num-=1
        return s
