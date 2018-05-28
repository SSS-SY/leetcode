int removeElement(int* nums, int numsSize, int val) {
    int* temp=(int*)malloc(numsSize*sizeof(int));
    int j=0;
    for(int i=0;i<numsSize;++i){
        if(nums[i]!=val){
            temp[j]=nums[i];
            j++;
        }
    }
    for(int k=0;k<j;++k){
        nums[k]=temp[k];
    }
    return j;
}