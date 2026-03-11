import React, { Component } from 'react'
import Navbar from './components/Navbar'
import News from './components/News'

class App extends Component {
  // c  = 'some Text'; //we can initialize a variable here like this

  render() {
    return (
      <div>
      {/* we can display the content of the variable using this keyword {this.c} */}
      <Navbar />
      <News pageSize={20}/>
      </div>
    )
  }
}

export default App