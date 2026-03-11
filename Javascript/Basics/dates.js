//Dates

let myDate = new Date();
console.log(myDate); //2024-07-28T05:52:07.788Z
console.log(myDate.toString()); //Sun Jul 28 2024 05:52:07 GMT+0000 (Coordinated Universal Time)
console.log(myDate.toDateString()); //Sun Jul 28 Jul 
console.log(myDate.toISOString());//2024-07-28T05:52:07.788Z 
console.log(myDate.toJSON()); //2024-07-28T05:52:07.788Z
console.log(myDate.toLocaleDateString()); // 7/28/24 
console.log(myDate.toLocaleString()); // 7/28/24 5:52:07 AM
console.log(myDate.toLocaleTimeString()); // 5:52:07 AM 
console.log(myDate.toTimeString()); //05:52:07 GMT+0000 (Coordinated Universal Time)
console.log(myDate.getTimezoneOffset()); //0

//---------------------
let myNewDate = new Date(2023, 0, 22) //Months in js start from 0
let myNewDate2 = new Date("2023-1-22") //Month starts from 1 in YYYY-MM-DD format however...
console.log(myNewDate.toDateString())
console.log(myNewDate2.toDateString())

let myTimeStamp = Date.now()
console.log(myTimeStamp) //it gives result in miliseconds from 1970
console.log(myNewDate2.getTime()) //it gives result from the aforementioned date
console.log(Math.floor(Date.now()/1000)) //value in seconds

console.log(myNewDate.getMonth() + 1)
console.log(myNewDate.getDay())

nuaDate = Date()
nuaDate.toLocaleString('default', {
    weekday: "long",
    }
)

console.log(nuaDate);

//getHours
//getMinutes
//getSeconds