async function getAllUsers() {
    try {
        const response = await fetch('https://api.github.com/users/shreyanshumis')
        const data = await response.json()
        console.log(data);
    } catch (error) {
       console.log("E:", error);
    }
}

getAllUsers()

//-----------------------------------------------
fetch('https://api.github.com/users/shreyanshumis').then((response)=>{
    return response.json
})
.then((data) => {console.log(data);
})//thenable
.catch((error) => console.log(error))