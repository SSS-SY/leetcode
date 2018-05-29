class Solution {
public:
    std::string countAndSay(int n) {
        std::string ret="1";
        for(int i=1;i<n;i++){
            std::string temp=ret;
            ret="";
            int len=temp.length();
            int times=0;
            int j;
            for(j=0;j<len;j++){
                if(j>0&&temp[j]!=temp[j-1]){
                    ret+=std::to_string(times)+temp[j-1];
                    times=1;
                }
                else{
                    times++;
                }
            }
            ret+=std::to_string(times)+temp[j-1];
        }
        return ret;
    }
};