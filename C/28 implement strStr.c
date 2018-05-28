int strStr(char* haystack, char* needle) {
    if(strlen(needle)==0) return 0;
    if(strlen(haystack)<strlen(needle)) return -1;
    for(int i=0;i<strlen(haystack);++i){
        if(haystack[i]!=needle[0]) continue;
        int j;
        for(j=0;j<strlen(needle);j++){
            if(haystack[i+j]!=needle[j]) break;
        }
        if(j==strlen(needle)&&haystack[i+j-1]==needle[j-1]) return i;
    }
    return -1;
}