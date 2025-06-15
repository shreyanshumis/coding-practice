//Js is dynamically typed

//Primitives Types - they're call by value

//7 Types: String, Number, Bool, null, undefined, Symbol, BigInt

//Reference Types(Non Primitives) - call by reference

//Arrays, Objects, Functions

const score =  100
const scoreValue =  100.3

const isLoggedIn = false
const temp = null
let userEmail;

const id = Symbol('123') //symbols
const newId = Symbol('123')
//their value will be different despite them looking the same. the return value is different

const bigNumber = 12343249328493n //bigint

//-----------
const heroes = ["Hero1", "Hero2", "Hero3"]//array

let myObj = {
    name: "shrey",
    age: 21,
} //object

const myFunc = function(){
    console.log("Hello world");
} //function

//---------MEMORY----------
//2 types - stack and heap

//Primitive type - Stack memory(call by value)
//Non Primitive type - heap memory(call by reference)

//Call by Value :-

let myName = "shrey"
let newName = myName
console.log(newName);
newName = "anshu"
//newName's value changed but myName's didn't cuz it's copy was given to newName and not the reference itself.

//Call by Reference :-

let user = {
    email:"user@hey.com",
    upi: "user@payhey"
}

let user2 = user
//This time you're getting the reference and not the copy of the same, hence the value in the original will change if u make changes in the 2nd one(user2)

user2.email = "anshu@hey.com"

console.log(user);
console.log(user2);