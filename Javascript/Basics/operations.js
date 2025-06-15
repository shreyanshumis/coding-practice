//operations --- JUST FOR PRACTICE

let value = 3;
let negValue = -value;
// console.log(negValue);

//console.log(2+3) etc. all operations are supported.


//concat strings
let str1= "a";
let str2= "b";

let str3= str1 + str2;
console.log(str3);

//---------
//The result of the below operations is 12 since the datatype is converted to string
console.log("1" + 2);
console.log(1 + "2");

//The value returned is 122 due to the same reason
console.log("1" + 2 + 2);

//The below value returned is 32 and not 122 here due to a guideline - ToPrimitive website
console.log(1 + 2 + "2")

//returns 1
console.log(+true);

let gameCounter = 100
gameCounter++; //postfix 
++gameCounter; //prefix
console.log(gameCounter);

