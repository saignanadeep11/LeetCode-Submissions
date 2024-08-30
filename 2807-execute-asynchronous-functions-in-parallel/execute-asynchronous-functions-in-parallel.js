/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve,reject)=>{
    let arr=[]
    l=functions.length
    let ret=0;
    let rej=false
    for(let i=0;i<l;i++){
        functions[i]().then(res=>{
            if(!rej){arr[i]=res;
        ret+=1
        if(ret==l){
            resolve(arr)
        }}}).catch(err=>{
            if(!rej){
                rej=true;
            reject(err);
            }
        })
    }})
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */