//ARRAY SPECIFIC LOOPS
// ["","",""] - array of strings
// [{},{},{}] - array of objects


//-----------------forof loop

//Arrays

const arr = [1, 2, 3, 4, 5]

for (const num of arr) {
    console.log(num);
}

// const greetings = "hello world!"
// for (const greet of greetings) {
//     console.log(`The beginning: ${greetings}`);
// }

//Maps

const map = new Map() //Map is an obj that holds key value pair(unique values)(remembers the order of keys unlike objects)
map.set('IN', "India")
map.set('JP', "Japan")
map.set('ID', "Indonesia")

console.log(map);

// for (const codes of map) {
//     console.log(codes);
// }

for (const [key, value] of map) {
    console.log(key, ':-', value);
}

//-----------------forin loop

//obj

const myObject = {
    'game1' : 'GTA V',
    'game2' : 'Valorant'
}

// for (const key in myObject) {
//     console.log(myObject[key]); -> gives key's values
// }

for (const key in myObject) {
    console.log(`${key} game is ${myObject[key]} `);
}


//testing it in Arrays

const programming = ["js", "ruby", "py", "java", "cpp"]

for (const key in programming) {
    console.log(key);
}

//it doesnt print values, it prints keys only(0->....)
//type programming[key] instead to get the values
//in forof you directly get values
