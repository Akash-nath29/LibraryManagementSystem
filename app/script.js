BOOK_LIST = 'http://127.0.0.1:5000/'
LEND_BOOK = 'http://127.0.0.1:5000/lend-book'
RETURN_BOOK = 'https://127.0.0.1:5000/return-book'

let container = document.querySelector('.container')

//lend book

const displayResult = (books) => {
    books.forEach(book => {
        const li = document.createElement("li");
        if(book.is_available = true){
            li.innerHTML = `<div class="card"><h1>${book.name}</h1><p class="author">${book.author}</p><p class="available availability">Available: ${book.is_available}</p><span class="buttonGroup"><button class="btn" onclick="lend(${book.id})">Borrow</button><button class="btn">Return</button></span></div>`;
        } else {
            li.innerHTML = `<div class="card"><h1>${book.name}</h1><p class="author">${book.author}</p><p class="available unavailability">Unavailable</p><span class="buttonGroup"><button class="btn" onclick="lend(${book.id})">Borrow</button><button class="btn">Return</button></span></div>`;
        }
        container.appendChild(li);
    });
}

const getResult = async () => {
    const response = await fetch(BOOK_LIST)
    const data = await response.json()
    displayResult(data)
}

const lend = async (id) => {
    const response = await fetch(`${LEND_BOOK}/${id}`)
    const data = await response.json()
    console.log(data)
    // document.querySelector('.available').classList.add = "unavailability";
}

window.onload = () => {
    getResult();
}