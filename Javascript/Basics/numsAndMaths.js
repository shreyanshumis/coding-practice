const score = 400; 
const balance = new Number(100) //new keywords - dedicated defined that it'll be a number only

console.log(score)
console.log(balance)

console.log(type(balance.toString()))//converts to string
console.log(type(balance.toFixed(2)))//decimal places are 2


const otherNumber = 123.8966
console.log(otherNumber.toPrecision(3))//precision - rounding off decimals

const hundreds = 100000
console.log(hundreds.toLocaleString()); //adds commas to the values such as 1,000,000
console.log(hundreds.toLocaleString('en-IN')); //adds commas but in Indian values instead of US

//_+_+_+_+_+_+_+_+_+_+_+_+--->Math library

console.log(Math);
console.log(Math.abs(-4)); //absolute value
console.log(Math.round(4.3)); //round off
console.log(Math.ceil(4.3)); //ceiling value
console.log(Math.round(4.2)); //floor value
console.log(Math.sqrt(25)); //square root
console.log(Math.pow(3,2)); //power
//Math.min - minimum value in an array
//Math.max - maximum value in an array

//Random
console.log(Math.random());//any random no. between 0 and 1(in decimals)
console.log((Math.random()*10) + 1);//multiplies the output by 10(+1 ensures the min value is 1 and not 0 incase we do Math.floor())

const min = 10;
const max = 20;

console.log(Math.floor(Math.random() * (max - min + 1)));
//simple formula for random number generation
