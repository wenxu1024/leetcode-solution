class Solution {
public:
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        int m,n;
        m=matrix.size();
        n=matrix[0].size();
        return sMatrix(matrix,target,0,m-1,0,n-1);
        }
    
    bool sMatrix(vector<vector<int> >&matrix, int target, int i, int j, int k, int l) {
        int m,n,q;
        q=matrix[0].size();
        if(i==j+1) {
            return false;
        }
        else if(i==j) {
            if(k==l+1) return false;
            else {
                n=(k+l)/2;
                if(target==matrix[i][n]) return true;
                else if(target>matrix[i][n]) return sMatrix(matrix,target,i,j,n+1,l);
                else return sMatrix(matrix,target,i,j,k,n-1);
            }
            
        }
        else {
            m=(i+j)/2;
            if(target==matrix[m][0]) return true;
            else if(target>matrix[m][0]) {
                if(target>matrix[m][q-1]) return sMatrix(matrix,target,m+1,j,k,l);
                else return sMatrix(matrix,target,m,m,k,l);
            }
            else {
                return sMatrix(matrix,target,i,m-1,k,l);
            }
        }
    }
};
