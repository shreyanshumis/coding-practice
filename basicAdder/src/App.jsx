import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import AdderComponent from './Components/AdderComponent'

function App() {
  let [calc, setCalc] = useState(0)
  
  const addition = ()=>{
    setCalc(calc+1);
  }

  const subtraction = ()=>{
    setCalc(calc-1);
  }

  return (
    <>
      
      <h3>Total:{calc} </h3>

      <button onClick={addition}>Add</button>
      <button onClick={subtraction}>Subtract</button>
    </>
  )
}

export default App
