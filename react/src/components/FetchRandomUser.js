import React from 'react'

export default class FetchRandomUser extends React.Component {
  
    constructor(props){
        super(props)
        this.state = {
            loading: true,
            person: null
          } 
    }
     

//   async componentDidMount(){
//     const url = "https://api.randomuser.me/"
//     const response = await fetch(url);
//     const data = await response.json();
//     this.setState({person:data.results[0], loading: false})
//   }

  componentDidMount() {
      fetch("https://api.randomuser.me/")
      .then(res => res.json())
      .then(json => {
          this.setState({
              loading: false,
              person: json.results[0]
          })
      })
  }

  render() {
    return(
    <div>
        {this.state.loading || !this.state.person ? (
            <div>loading</div> 
        ) : (
            <div>{this.state.person.name.first}</div>
        )}
    </div>
    )}
    
}
