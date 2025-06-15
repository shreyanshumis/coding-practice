//Arrow function and this keyword

const user = {
    username: "shrey",
    price: 999,

    welcomeMessage: function() {
        console.log(`${this.username}, Welcome to the website!`);
        console.log(this); //shows the current context - welcomeMessage in this case
    }

}

// user.welcomeMessage()
// user.username = "shrek"
// user.welcomeMessage()

// console.log(this); current context - empty object {}
//it's not an empty object in browser js, it's only empty in node environment

// function chai(){
//     let user = "hey"
//     console.log(this.user); //undefined cuz it works only in objects and not in functions
// }

// chai()

//BASIC Arrow function
const addTwo = (num1, num2) => {
    return num1 + num2
}

// console.log(addTwo(2,4));


//Implicit return - single line code without return keyword
const addTwo2 = (num1, num2) => (num1 + num2) //paranthesis is optional here

// console.log(addTwo2(2,4));

//Returning object

const addTwo3 = (num1, num2) => ({username:"shrey"})

// const myArray = [2, 5, 3, 7, 8]

// myArray.forEach( () => ())