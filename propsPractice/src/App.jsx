import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card from './Components/Card'

function App() {
  let [price, setPrice] = useState(20)

  const priceAddition = ()=>{
    setPrice(price+1);
  }

  let cardObject = {
    user: "shrey",
    price
  } //we need to pass this object incide the curly braces {} in the card component below -> someObj = {cardObject}

  let newArr = [1,2,3] //we can pass array too inside the curly braces {} (NOTE: Not the comment brackets but the one declared as someObj = {newArr}) only or else it will throw an error

  return (
    <> 
      <h1 className='bg-green-300 text-black p-4 rounded-2xl mb-4'>Tailwind Testing</h1>
      {/* <Card name="shreyanshu" someObj = {cardObject}/>
      <Card name="shreyanshu" someObj = {newArr}/> */}
      <Card username="shrey" price={price}/>
      <Card username="shrey"/>
      <button onClick={priceAddition}>If you're rich click here</button>
    </>
  )
}

export default App
