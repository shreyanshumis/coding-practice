//promise is an object -> eventual completion
//promise created
const promiseOne = new Promise(function(resolve, reject){
    //Do an async task
    //Database calls, cryptography tasks, network calls etc.
    setTimeout(function(){
        console.log('Async task is complete');
        resolve() //resolve connected
    }, 3000) 
}) 

//promise consume
promiseOne.then(function(){
    console.log('Promise consumed');
})//then is related to 'resolve'

//first async task is completed and then the promise is consumed.
// ------------------------------------------------------------------
new Promise(function(resolve,reject){
    setTimeout(function(){
        console.log("Async task 2");
        resolve()
    }, 1000)
}).then(function(){
    console.log("Async 2 resolved too");
})
//we did it in one piece and not in 2 pieces like above