class Solution {
public:
       vector<vector<int> > generate(int numRows) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> d;
        vector<vector<int> > temp; 
        int i,j;
        for(i=0;i<numRows;i++) {
            for(j=0;j<=i;j++) {
                if(j==0||j==i) d.push_back(1);
                else d.push_back(temp[i-1][j-1]+temp[i-1][j]);
                }       
                temp.push_back(d);
                while(d.size()) {d.pop_back();}
        }       
        return temp;
    }

};
