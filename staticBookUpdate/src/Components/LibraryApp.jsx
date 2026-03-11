import React from 'react'

function LibraryApp() {

    const books = [
        {
            id: 1,
            name: "Norwegian Wood",
            author: "Murakami",
            price: 300
        },
        {
            id: 2,
            name: "Atomic Habits",
            author: "James Clear",
            price: 700
        },
        {
            id: 3,
            name: "My Own book",
            author: "Shreyanshu",
            price: 100
        },
        {
            id: 4,
            name: "Hooked",
            author: "Nir Eyal",
            price: 400
        },
    ]

    // const alertingBooks = (book) => {
    //     alert(`Book Name: ${book.name}\nAuthor: ${book.author}`);
    // };

    function bookList() {
        return (
            <div>
                <table border="1" cellPadding="10">
                    <thead color='black'>
                        <tr>
                            <th>Name</th>
                            <th>Author</th>
                            <th>Price</th>
                            <th>Viewing Details</th>
                        </tr>
                    </thead>
                    <tbody>
                        {books.map(book => (
                            <tr key={book.id}>
                                <td>{book.name}</td>
                                <td>{book.author}</td>
                                <td>{book.price}</td>
                                <td><button onClick={() => alert(`Book Name: ${book.name}\nAuthor: ${book.author}`)}>View Details</button></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </ div>

        );
    }

    return (
        <>
            <h2>Library Book List</h2>
            {bookList()}
        </>
    )
}

export default LibraryApp
