/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return{
        toBe:(k)=>{
        if (val===k){
            return true;
        }
            throw new Error("Not Equal");
    },
        notToBe:(k)=>{
        if (k===val){
            throw new Error("Equal")
        }
        return true
    }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */