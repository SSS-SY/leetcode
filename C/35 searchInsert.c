int searchInsert(int* nums, int numsSize, int target) {
    int first=0,last=numsSize-1;
    if(nums[0]>target) return 0;
    if(nums[last]<target) return numsSize;
    while(first<=last){
        int mid=(first+last)/2;
        if (nums[mid]==target) return mid;
        else if (nums[mid]<target) first=mid+1;
        else last=mid-1;
    }
    return first;
}