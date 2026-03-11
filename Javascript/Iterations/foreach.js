const coding = ["js", "ruby", "java", "py", "cpp"]

coding.forEach( function (val) {
    console.log(val);
} ) 
//since it's callback function, it doesnt have name ^
//it will automatically execute all values

//using arrow function
coding.forEach( (val) => {
    console.log(val)
})

//another way

function printMe(item){
    console.log(item);
}

coding.forEach(printMe) //gave func reference.

//a scenario - array of objects

const myCoding = [
    {
        languageName: "javascript",
        languageFileName: "js"
    },
    {
        languageName: "java",
        languageFileName: "java"
    },
    {
        languageName: "python",
        languageFileName: "py"
    }
]

myCoding.forEach( (item) => {
    console.log(item.languageName); //took a value out of array of objects
} )

//foreach doesnt return anything

const myNums = [1,2,3,4,5,6,7,8,9,10]

myNums.filter((myNums) => num > 4)//filter takes callback 
//this returns values, not foreach
//if u use parenthesis then it's implicit return(auto return)
//if u use curly braces then it's explicit return(manually write return keyword)

const newNums = myNums.filter( (num) => {
    return num > 4;
})


//using foreach instead of filter
const newNums2 = []

myNums2.forEach( (num) => {
    if (num > 4){
        newNums2.push(num)
    }
} )

console.log(newNums2);