//Immediately Invoked Function Expressions (IIFE)
//to remove pollution from global scope



//Normal Function
function chai(){
    console.log(`DB CONNECTED`)
}

chai()

//IIFE function

(function chai(){ //named IIFE.
    console.log(`DB CONNECTED`);
})(); //semicolon is needed here since IIFE doesnt know where to stop

// ()(); //IIFE function call


//IIFE function with arrow function

( () => { //simple IIFE
    console.log(`DB CONNECTED AGAIN`);
})();


//with arguments
( (name) => {
    console.log(`Hey ${name}`);
})("Shrey")