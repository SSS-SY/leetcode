int myAtoi(char* str) {
    int ret=0;
    int len=strlen(str);
    int i=0,flag=1,temp;
    for(;i<len;i++){
        if(i==0&&str[i]==' ')continue;
        else if(str[i]==' '&&str[i-1]==' ')continue;
        else if((str[i]=='-'&&str[i+1]=='+')||(str[i]=='+'&&str[i+1]=='-'))return 0;
        else if(str[i]=='-')flag=-1;
        else if(str[i]=='+')flag=1;
        else if(((str[i]>'9'||str[i]<'0')&&i==0)) return 0;
        else if(((str[i]>'9'||str[i]<'0')&&str[i-1]==' ')||str[i]=='.') return ret*flag;
        else if((str[i]>'9'||str[i]<'0')) return ret*flag;
        else{
            temp=ret;
            ret=ret*10+str[i]-'0';
            if(((ret-str[i]+'0')/10)!=temp) return INT_MIN;
        }
    }
    return ret*flag;
}