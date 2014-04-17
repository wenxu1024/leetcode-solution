class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int i,n,total,k;
        n=gas.size();
        k=0;
        while(true) {
        total=0;
        for(i=k;i<n+k&&total>=0;i++) {
            total+=gas[i%n]-cost[i%n];
        }
        if(total>=0) return k;
        else {
            if(i>=n) return -1;
            k=i;
        }
        }
    }
};
