 //IF-ELSE

 if (true && 2===2 && 2=="2"){
    console.log(`true lol`);
} else {
    console.log(`not true lol`);
}

// === ->  doesn't execute (takes data types into account)
// 2 == "2" -> executed (despite string and number) 

//negative equivalent != and !==

//SWITCH

let month = 1;

switch (month) {
    case 1:
        console.log(`January!`);
        break;
    default:
        console.log(`Other months`);
        break;
}

// && - and
// || - or
// ?? - nullish coalescing operator (null and undefined)
let val1;
val1 = null ?? 10
val1 = undefined ?? 15
console.log(val1);

// Ternary Operator
condition ? true : false
