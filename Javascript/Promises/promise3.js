const promiseThree = new Promise(function(resolve, reject){
    setTimeout(function(){
        resolve({username: "Shrey", email: "shreyanshumishra.work@gmail.com"})
    }, 1000)
})

promiseThree.then(function(user){
    console.log(user);
})

const promiseFour = new Promise(function(resolve,reject){
    setTimeout(function(){
        let error = false
        if (!error){
            resolve({username: "Shrey"})
        }
        else {
            reject('ERROR: Something went wrong :(')
        }
    }, 1000)
})

// promiseFour.then().catch() //to catch errors
//chaining ->
promiseFour.then((user) => {
    console.log(user);
    return user.username
})
.then((username) => {
    console.log(username);
})
.catch(function(error){
    console.log(error);
})
.finally(() => console.log("The promise is either resolved or rejected")) //finally always executes

//---------------------------------------------------
const promiseFive = new Promise(function(resolve, reject){
    setTimeout(function(){
        let error = true
        if(!error){
            resolve({username:"Shrey", password:"xyz"})
        } else {
            reject('ERROR: JS Went wrong')
        }
    }, 1000)
});

// promiseFive.then()
async function consumePromiseFive(){
    try{
        const response = await promiseFive
        console.log(response);
    }
    catch(error){
        console.log(error);
        
    }
    //async await cant directly handle errors...so use try catch block
}

consumePromiseFive()

//--------------------------------------------