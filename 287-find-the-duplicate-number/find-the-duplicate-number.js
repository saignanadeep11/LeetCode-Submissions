/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let fast=nums[nums[0]]
    let slow=nums[0]
    while(fast!=slow){
        fast=nums[nums[fast]]
        slow=nums[slow]
    }
    fast=0
    while(fast!=slow){
        fast=nums[fast]
        slow=nums[slow]
    }
    return fast
};