int newsum(int n){
    int res=0;
    while(n>0){
        res+=(n%10)*(n%10);
        n=n/10;
    }
    return res;
}

bool isHappy(int n) {
    int pool[20]={0},i;
    memset(pool,0,20);
    while(n!=1){
        for(i=0;pool[i]!=0;++i){
            if (pool[i]==n){
                return false;
            }
        }
        pool[i]=n;
        n=newsum(n);
    }
    return true;
}