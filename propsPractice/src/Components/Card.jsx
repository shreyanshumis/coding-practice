import React from 'react'

// To receive values here we have props access by default in this component

// function Card(props) {
// const a = props.username --original syntax
// function Card({username, price=83748}) { //Directly giving username here no need to write props 
// price=20 is the default value

function Card({username, price}) { 
    return (
            <div
      className="flex flex-col rounded-xl  p-4"
      style={{
        border: "0.88px solid",

        backdropFilter: "saturate(180%) blur(14px)",
        background: " #ffffff0d",
      }}
    >
      <div>
        <img
          src="https://res.cloudinary.com/ddcg0rzlo/image/upload/v1652470298/9StaF0UBJfih_df0248.gif"
          alt="nft-gif"
          width="350"
          height="350"
          className="rounded-xl"
        />
      </div>
      <div className="flex flex-col  rounded-b-xl py-4 ">
        <div className="flex justify-between">
          <h1 className="font-RubikBold ">Name</h1>
          <h1 className="font-bold font-RubikBold">Price</h1>
        </div>
        <div className="flex  justify-between font-mono">
          <p>{username}</p>
          <p>{price}</p>
        </div>
      </div>
    </div>
    )
}

export default Card
