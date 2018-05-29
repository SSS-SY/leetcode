class Solution {
public:
    string intToRoman(int num) {
        if(num <= 0) return "";  
        string ret = "";  
        static int number[13] = {1000, 900, 500, 400, 100,90, 50, 40, 10, 9, 5, 4, 1};  
        static string flags[13] = {"M","CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};  
        for(int i = 0; i < 13 && num > 0; i++){   
            if(num < number[i]) continue;  
            while(num >= number[i]){  
                num-= number[i];  
                ret += flags[i];  
            }  
        }  
        return ret;   
    }
};