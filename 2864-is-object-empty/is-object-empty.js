/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    
    for(let k in obj){
        return false
    }
    return true
};