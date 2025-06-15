const progLangs = ["Python", "Java", "C++"]
const humanLangs = ["Odia","English","Japanese"]

progLangs.push(humanLangs) //it adds the array itself as a single element into the other array instead of adding the elements separately.

// console.log(progLangs)
// console.log(progLangs[3][1])

const newLang = progLangs.concat(humanLangs) //combines 2 or more arrays and returns a new array
// console.log(newLang)

const allNewLangs = [...progLangs,...humanLangs] //all the elements are split and not like the first case
// console.log(allNewLangs)

const newArr = [1, 2, 3, [4, 5, 6], 7, [6, 7, [4, 5]]]

const fixedArr = newArr.flat(Infinity) //returns a new array with all sub array elements
// console.log(fixedArr)

// Array.isArray("Shrey")  --> false
// Array.from("Shrey")  --> converts it into an array(S,h,r,e,y)

//if u give something like Array.from({name: "Shrey"})
//It returns an empty array since it is NOT able to decide which one to make an array out of, key or value

let score1 = 100
let score2 = 200
let score3 = 300

console.log(Array.of(score1, score2, score3))
