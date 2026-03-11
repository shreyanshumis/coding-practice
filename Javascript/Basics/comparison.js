// console.log( 2 > 1 );
// console.log( 2 < 1 );
// console.log( 2 >= 1 );
// console.log( 2 <= 1 );
// console.log( 2 == 1 );
// console.log( 2 != 1 );

console.log("2" > 1); //js converts 2 to number- make sure the types are same

console.log(null > 0); //res - false
console.log(null == 0); //res - false
console.log(null >= 0 ); //res - true
//The reason is that the equality check == and comparisons > < >= <= work differently. 
//comparisons convert null into a number, treating it as 0. That's why 3rd null >= 0 is true and 1st one is false

// === strict check -  it checks the datatypes as well. The below examples will be treated differently.
console.log("2" == 2);
console.log("2" === 2);