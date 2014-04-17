class Solution {
public:
        vector<int> getRow(int rowIndex) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> prev,curr;
        int i,j;
        rowIndex++;
        for(i=0;i<rowIndex;i++) {
          for(j=0;j<=i;j++) {
              if(j==0||j==i) curr.push_back(1);
              else curr.push_back(prev[j-1]+prev[j]);
          }       
          while(prev.size()) prev.pop_back();
          while(curr.size()) {prev.push_back(curr.back());curr.pop_back();}
        }       
        return prev;
    }

};
