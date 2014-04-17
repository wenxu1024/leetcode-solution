class Solution {
public:
    double pow(double x, int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        double y;
        if(x==1) return 1;
        if(x==-1) {if(n%2==0) return 1;else return -1;}
        if(n==0) return 1;
        if(n>0) {
        if(n%2==0) {y=pow(x,n/2);return y*y;}
        else {y=pow(x,n/2);return y*y*x;}
        }
        else {return 1.0/pow(x,-n);}
    }
};
