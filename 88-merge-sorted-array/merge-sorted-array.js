/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    p1=m-1
    p2=n-1
    n+=m-1
    while(p1>=0 && p2>=0){
        if(nums1[p1]>nums2[p2]){
            nums1[n]=nums1[p1];
            nums1[p1]=0
            p1--;n--;
        }
        else{
            nums1[n]=nums2[p2];
            p2-=1
            n--;
        }
    }
    while(p2>=0){
        nums1[n--]=nums2[p2--];
    }
};