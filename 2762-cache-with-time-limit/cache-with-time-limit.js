var TimeLimitedCache = function() {
    this.arr=new Map()
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let k=false
    if(this.arr.has(key)){
        k=true
        clearTimeout(this.arr.get(key).timeout)
    }
    this.arr.set(key,{
        value,
        timeout: setTimeout(()=>this.arr.delete(key),duration)
    })
    return k;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if(this.arr.has(key)){
        return this.arr.get(key).value
    }
    return -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.arr.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */