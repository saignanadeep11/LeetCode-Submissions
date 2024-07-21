/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    memo={}
    return function(...args) {
        
        if(args in memo){
            return memo[args];
        }
        k=fn(...args);
        memo[args]=k;
        return k;
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