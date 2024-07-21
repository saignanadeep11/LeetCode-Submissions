/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    memo={}
    return function(...args) {
        ans=[]
        // console.log(args,memo);
        if(args in memo){
            ans.push(memo[args])
        }
        else{
        k=fn(...args);
        memo[args]=k;
        ans.push(k);
        }
        return ans;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */