//all three(let, const, var) have different scopes
// var c = 300
// if (true){
//     let a = 10
//     const b = 20
//     // var c = 30
// }

// console.log(a);
// console.log(b);
// console.log(c);

// function one(){
//     const username = "shrey"

//     function two(){
//         const website  = "github"
//         console.log(username);
//     }
//     // console.log(website); js executes line by line

//     two()
// }

// one()

// if (true){
//     const username = "shrey"
//     if(username === "shrey"){
//         const website = " youtube"
    
//         console.log(username + website)
//     }
//     // console.log(website); out of scope
// }
// console.log(username); out of scope too lol

// Example

function addOne(num) { //declaration of function
    return num + 1
}

addOne(5)

const addTwo = function(num){ //declared and stored in a variable too
    return num + 2
}

addTwo(5)

//search up hoisting in js