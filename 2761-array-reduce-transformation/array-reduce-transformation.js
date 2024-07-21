/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let k=init;
    nums.forEach((i)=>{
        k=fn(k,i);
    })
    return k;
};