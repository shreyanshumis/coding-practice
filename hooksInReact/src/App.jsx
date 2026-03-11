import { useState } from 'react' //this one is for hooks too
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  
  let [counter, setCounter] = useState (1);//use state hooks - counter is the variable and setCounter is the function, with the use state default value given as 1.
  // let counter  = 0;
  const adder = () => {
    setCounter(counter + 1); // we update the counter using this method call
    // counter= counter+1;
  }

  return (
    <>
      <h1>Shreyanshu heheheh</h1>
      <h2>Counter {counter}</h2>
      <button onClick={adder}>
        Click this to say shrey is the best</button>
    </>
  )
}

export default App
