/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    var k=new Promise(res=>setTimeout(res,millis));
    return k;
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */