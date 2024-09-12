/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    n=arr.length;
    if(n==0){
        return []
    }
    if(size>=n){
        return [arr]
    }
    ret=[]
    sub=[]
    for(let i=0;i<n;i+=size){
        let k=i+size
        for(let j=i;j<k;j+=1){
            if(j>=n){
                break;
            }
            // console.log(sub,j,size,k)
            sub.push(arr[j])
            // console.log(sub)
        }
        ret.push(sub)
        sub=[]
    }
    return ret
};
