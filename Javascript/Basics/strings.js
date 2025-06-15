// console.log("A" + "B"); - string concat

//backtics - string interpolation - it's like fstring in python.

let name = "Shrey"
console.log(`Hey! my name is ${name} and this is my codespace`);

//string as object

const gameName = new String('shrey_77')
//you can use length property and a lot more using it
//It's a key value pair of it's index and the character on that index.

console.log(gameName[1]);
// console.log(gameName.__proto__); //access objects //depricated feature

//Methods
console.log(gameName.length);
console.log(gameName.toUpperCase());
console.log(gameName.charAt(3));
console.log(gameName.indexOf('r'));

//slicing
const newString = gameName.substring(0,5);
console.log(newString);
const anotherString = gameName.slice(0,5);
console.log(anotherString);

//trim and replace
const newStringOne = "     shrey       ";
console.log(newStringOne);
console.log(newStringOne.trim()) //removes starting and ending spaces

const url = "https://shrey.com/hey%20shrey";

console.log(url.replace('%20','-'));

//includes
console.log(url.includes('shrey'));

//splitting
console.log(gameName.split('_'));