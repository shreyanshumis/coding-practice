// function sayMyName() {
//     console.log("Hello world");
//     console.log("My name is Shrey");
// }

// sayMyName() -> executes it
// sayMyName -> reference 

// function addTwoNum(num1, num2){ //function functionName(parameters)
//     console.log(num1 + num2);
// }

function addTwoNum(num1, num2){ //function functionName(parameters)
    let num3 = num1 + num2
    return num3
}

// const result = addTwoNum(3,4) //you need to give arguments in order for the functions to work
//in the above line of code, result will be undefined since the function is only executing but not returning anything. use return statement.
//but once u use the return keyword like in Line 15, the result will be stored in "const result".

// console.log(result);

function loginUserMessage(username){
    if(username === undefined){ //or !username or undefined works.
        console.log("Please enter ur username")
    }

    return `${username} logged in successfully!`
}

// let msg = loginUserMessage("Shrey")

// console.log(msg);

function calcCartPrice(...num1) { //in case you dont know how many arguments come - use rest operator(same syntax as spread operator(triple dots))
    return num1
}

console.log(calcCartPrice(2,34,45,654))

const user = {
    username: "shrey",
    price: 99
}

function handleObj(anyobject){
    console.log(`Username is ${anyobject.username} and price is ${anyobject.price}`);
}

// handleObj(user)
// handleObj({
//     username:"yo",
//     price:23
// })

const myArr = [200, 245, 435]

function returnSecondValue(getMyArr){
    return getMyArr[1]
}

console.log(returnSecondValue(myArr));