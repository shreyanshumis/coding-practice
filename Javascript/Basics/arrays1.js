// arrays

// const mrArr = [0, 1, 2, 3, 4, 5, false, "shrey"] 
//it can have any datatypes
//it can be resized
//it can be accessed by Index. zero based


//2 ways to declare arrays
const myArr = [0, 1, 2, 3, 4, 5]
const myArr2 = new Array(1, 2, 3, 4)

// console.log(myArr[1]);

//Array methods
// myArr.push(6)
// myArr.pop()
// myArr.unshift(0) //element is placed at the beginning of the array, shifting all the other elements. NOT recommnded.
// myArr.shift()

// console.log(myArr.includes(9)) //includes a element or not- keep in mind the datatype of the result.
// console.log(myArr.indexOf(3)) //index of a particular element 

const newArr = myArr.join()
// console.log(newArr) //type changed into a string after .join() function

//slice, splice

console.log("A - ", myArr)

const myn1 = myArr.slice(1,3) //returns a section of an array without manipulating original array
console.log(myn1)
console.log("B - ", myArr)

const myn2 = myArr.splice(1,3) //splice actually manipulates the original array too
console.log(myn2)
console.log("C - ", myArr)

