const course = {
    courseName: "Javascript",
    price: "999",
    courseReview: "chai aur code is awesome"
}

// course.courseReview - NOTE !! if u want to print it multiple times and want to maintain a clean code then this may not be the ideal choice

const {courseReview : rev} = course
console.log(rev)


//React ! ! ! !
// const navbar = (/*{company} instead of props.company*/) => {

// }

// navbar(company = "shrey")


//Concept of API
// {
//     "name": "shrey",
//     "product": "gymapp",
//     "price": "free"
// }

