/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeid;
    call=(...args)=>{
        if(timeid){
            clearTimeout(timeid)
        }
        timeid=setTimeout(()=>{
            fn(...args);
        },t)
    }
    return function(...args){
        call(...args)
    }
    
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */