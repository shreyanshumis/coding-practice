//singleton - single object if obj is created using constructor

//object literals 

// const jsUser = {} //Object created(empty object)
// Object.create //singleton Object created

const mySym = Symbol("key1")

const jsUser = {
    name: "Shrey",
    "full name": "Shrey M", //you cannot access using dot
    [mySym] : "mykey", //you need [] brackets to use the actual symbols
    age: 21,
    location: "Mumbai",
    email: "shrey@ggz.com",
    isLoggedIn: false,
    lastLoginDays:["Monday", "Saturday"]
}

// jsUser.name -> access object(using dot)
// jsUser["name"] -> another way to access objects

// overwrite values 
// jsUser.email = "newmail@ggz.com"

// how to lock/freeze an Object(won't propagate changes)
// Object.freeze(jsUser)

//Functions in JS
jsUser.greeting = function(){
    console.log("Hello world");
}

jsUser.greeting2 = function(){
    console.log(`Hello world! ${this.name}`); //same object reference
}

// console.log(jsUser.greeting()) //undefined
// console.log(jsUser.greeting) //function return back, reference

console.log(jsUser.greeting())
console.log(jsUser.greeting2())