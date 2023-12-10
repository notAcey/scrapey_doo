function startScraping() {
    var url = document.getElementById('urlInput').value;
    fetch('/initialize_scraper', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ link: url }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Răspuns primit:', data);
        if (Array.isArray(data)) {
            displayProducts(data);
        } else {
            console.error('Răspunsul nu este un array:', data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

let currentPage = 1;
const perPage = 15;
let totalPages = 0;

function loadPage(page) {
    fetch(`/get_products?page=${page}`)
    .then(response => response.json())
    .then(data => {
        displayProducts(data.products);
        updatePaginationButtons(page, data.has_next);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function updatePaginationButtons(page, hasNext) {
    const prevButton = document.querySelector("#pagination button:first-child");
    const nextButton = document.querySelector("#pagination button:last-child");

    prevButton.className = page === 1 ? "btn btn-secondary" : "btn btn-primary";
    prevButton.disabled = page === 1;

    nextButton.className = hasNext ? "btn btn-primary" : "btn btn-secondary";
    nextButton.disabled = !hasNext;

    currentPage = page;
}

function displayProducts(products) {
    const productListElement = document.getElementById('productList');
    productListElement.innerHTML = '';

    products.forEach(product => {
        const productHTML = `
            <div class="card" style="margin-bottom: 20px;">
                <div class="card-header">
                    Produs
                </div>
                <div class="card-body">
                    <h5 class="card-title">${product['Product Name']}</h5>
                    <p class="card-text">Preț: ${product['Current Price']} lei.</p>
                    <p> Discount: ${product['Discount']}%</p>
                    <a href="${product['Link']}" class="btn btn-primary" target="_blank">Vezi produs</a>
                </div>
            </div>
        `;

        productListElement.innerHTML += productHTML;
    });
}


function sortProducts(sortType) {
    fetch('/sort_products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sort_type: sortType }),
    })
    .then(response => response.json())
    .then(data => {
        displayProducts(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function filterProducts(filterType, value) {
    fetch('/filter_products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filter_type: filterType, value: value }),
    })
    .then(response => response.json())
    .then(data => {
        displayProducts(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function clearFilters() {
    fetch('/clear_filters', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        displayProducts(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function exportProducts(exportType) {
    fetch(`/export_products?type=${exportType}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        if(data.fileUrl) {
            window.location.href = data.fileUrl;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

window.onload = () => {
    loadPage(1);
};