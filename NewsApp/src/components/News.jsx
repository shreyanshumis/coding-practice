import React, { Component } from 'react'
import NewsItem from './NewsItem'

class News extends Component {

    constructor() {
        super();
        this.state = {
            articles: [],
            loading: false,
            page: 1
        }
    }
    async componentDidMount() {//runs after render
        let url = `https://newsapi.org/v2/everything?q=computer+science&sortBy=popularity&apiKey=4a471f5a377d43fc8638cae06c9d1542&page=1&pageSize=${this.props.pageSize}`
        let data = await fetch(url);
        let parsedData = await data.json();
        this.setState({ articles: parsedData.articles, totalResults: parsedData.totalResults })
    }

    handlePrevClick = async () => {
        let url = `https://newsapi.org/v2/everything?q=computer+science&sortBy=popularity&apiKey=4a471f5a377d43fc8638cae06c9d1542&page=${this.state.page - 1}&pageSize=${this.props.pageSize}`;
        let data = await fetch(url);
        let parsedData = await data.json();
        this.setState({
            page: this.state.page - 1,
            articles: parsedData.articles
        })
    }

    handleNextClick = async () => {

    const maxPage = Math.min(
        Math.ceil(this.state.totalResults / this.props.pageSize),
        5
    );

    if (this.state.page >= maxPage) return;

    let url = `https://newsapi.org/v2/everything?q=computer+science&sortBy=popularity&apiKey=4a471f5a377d43fc8638cae06c9d1542&page=${this.state.page + 1}&pageSize=${this.props.pageSize}`;

    let data = await fetch(url);
    let parsedData = await data.json();

    this.setState({
        page: this.state.page + 1,
        articles: parsedData.articles
    });
}

    render() {
        return (
            <div className='container my-3'>
                <h1 className='text-center'>Today's been pretty eventful!</h1>
                <div className="row">
                    {this.state.articles.map((element) => {
                        return <div className="col-md-4" key={element.url}>
                            <NewsItem title={element.title} description={element.description ? element.description.slice(0, 20) : ""} imageUrl={element.urlToImage} newsUrl={element.url} />
                        </div>
                    })}
                </div>
                <div className="container d-flex justify-content-between">
                    <button disabled={this.state.page <= 1} type="button" className="btn btn-outline-dark" onClick={this.handlePrevClick}>&larr; Previous</button>

                    <button disabled={this.state.page + 1 > Math.min(Math.ceil(this.state.totalResults / this.props.pageSize), 5)} type="button" className="btn btn-outline-dark" onClick={this.handleNextClick}>Next &rarr; </button>
                </div>
            </ div>
        ) 
    }
}

export default News