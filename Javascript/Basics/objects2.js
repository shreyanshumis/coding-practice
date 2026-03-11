// const tinderUser = new Object() -> Singleton obj
// const tinderUser = {} -> non-Singleton obj

const tinderUser = {}

tinderUser.id = "123abc"
tinderUser.name = "Anshu"
tinderUser.isLoggedIn = false


// console.log(tinderUser)

const regularUser = {
    email: "some@gmail.com",
    fullName: {
        userFullName: {
            firstName : "Shrey",
            lastName : "Mis"
        }
    }
}

// console.log(regularUser.fullName.userFullName.firstName) //You can access all the nested objects using successive dots and names like this

// console.log(regularUser.fullName?.userFullName.firstName) // Use ? if unsure if fullname exists or not, better than using if-else literally everywhere

const obj1 = {1: "a", 2: "b"}
const obj2 = {3: "a", 4: "b"}
const obj4 = {5: "a", 6: "b"}

// const obj3 = { obj1, obj2 } //objects inside an object as a whole, same problem as array

// const obj3 = Object.assign(obj1, obj2) //returns a target object
// const obj3 = Object.assign({},obj1, obj2, obj4) //same + giving {} is a good practice, guarantees result.
const obj3 = {...obj1, ...obj2, ...obj4} //SPREAD - easy spread and adds all individual elements to obj3

// console.log(obj3)


//If the data comes from a database (Array of objects)

const users = [
    {
        id:1,
        email: "psf@ggz.com"
    },
    {
        id:2,
        email: "hgfri@ggz.com"
    },
    {
        id:3,
        email: "ze@ggz.com"
    }
]

// users[1].email //accessing values using arrays, u can use loops too

console.log(tinderUser);

console.log(Object.keys(tinderUser)) //keys //output is an array
//Syntax Object.keys(object name)

console.log(Object.values(tinderUser)); //values

console.log(Object.entries(tinderUser)) //key value pairs returned //2D array returned

//if a value doesnt exist while u loop it - it may crash
//in such scenarios:

console.log(tinderUser.hasOwnProperty('isLoggedIn')); //returns bool
console.log(tinderUser.hasOwnProperty('isLogged')); //returns bool