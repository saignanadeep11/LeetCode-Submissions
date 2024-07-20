/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    tn=[]
    for(let i=0;i<arr.length;i++){
        tn[i]=fn(arr[i],i);
    }
    return tn;
};