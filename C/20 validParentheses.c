bool isValid(char* s) {
    if(strlen(s)==0) return true;
    else if(strlen(s)%2==1) return false;
    else{
        char* stack=(char*)malloc(strlen(s)/2*sizeof(char));
        memset(stack,'\0',strlen(s));
        int j=0,i=0;
        for(;i<strlen(s);++i){
            if(s[i]=='('||s[i]=='['||s[i]=='{'){
                stack[j]=s[i];
                j++;
            }
            else if(s[i]==')'){
                if (stack[j-1]!='(') return false;
                j--;
            }
            else if(s[i]==']'){
                if (stack[j-1]!='[') return false;
                j--;
            }
            else if(s[i]=='}'){
                if (stack[j-1]!='{') return false;
                j--;
            }
        }
        if(i==strlen(s)&&j==0) return true;
    }
    return false;
}
