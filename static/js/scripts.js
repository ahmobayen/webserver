/*!
 * Start Bootstrap - Modern Business v5.0.5 (https://startbootstrap.com/template-overviews/modern-business)
 * Copyright 2013-2021 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('messages')) {
        let node = document.getElementById('messages');
        setTimeout(function() {
            node.parentNode.removeChild(node)
        }, 10000);

    }

    if (document.getElementById('blog_preview')) {
        load_abstract_posts();
    }

    if (document.getElementById('live_price')) {
        const tickers = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'BNBUSDT', 'SOLUSDT', ];
        setInterval(function() {
            for (let ticker of tickers) {
                get_realtime_price(ticker);
            }
        }, 2000)
    }


    if (document.getElementById('blog_home')) {
        let page = 2;
        load_posts();

        window.addEventListener('scroll', () => {
            const { scrollTop, clientHeight, scrollHeight } = document.documentElement;
            if ((scrollTop + clientHeight) >= scrollHeight) {

                if (load_posts(page)) {
                    page += 1;
                }
            }
        });
    }

})


function load_abstract_posts() {

    fetch(`/blogs?query=3`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            data.forEach(add_abstract_post);
        })
        .catch(error => console.error('Error:', error));
}

function load_posts(page_number) {
    if (!page_number) {
        page_number = 1;
    }
    fetch(`/blogs?page=${page_number}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            if (data.length) {
                data.slice(0, -1).forEach(add_post);
                return true;
            }

        })
        .catch(error => {
            console.error('Error:', error);
            return false
        });
}

function add_abstract_post(content) {
    const section = document.querySelector('#blogs');
    const post = document.createElement('div');
    post.classList.add('col-lg-4', 'mb-5');
    post.innerHTML = post_style(content, 100);

    section.appendChild(post);
}

function add_post(content) {
    const section = document.querySelector('#blog_home');
    const post = document.createElement('div');
    post.classList.add('card', 'border-0', 'shadow', 'rounded-3', 'overflow-hidden');
    post.innerHTML = post_style(content, 200);

    section.appendChild(post);
    section.appendChild(document.createElement('br'));
}

function post_style(content, slice_size) {
    return `<div class="card h-100 shadow border-0 bg-dark text-white">
                <div class="card-body p-4">
                    <div class="badge bg-dark-blue bg-gradient rounded-pill mb-2">${content.type}</div>
                    <a class="text-decoration-none link-dark stretched-link" href="${content.source}">
                        <h5 class="card-title mb-3 text-light">${content.title}</h5>
                    </a>
                    <p class="card-text mb-0" style="text-align: justify">${content.body.slice(0, slice_size)}...</p>
                </div>
                <div class="card-footer p-4 pt-0 bg-transparent border-top-0">
                    <div class="d-flex align-items-end justify-content-between">
                        <div class="d-flex align-items-center">
                            <div class="small">
                                <div class="fw-bold">${content.source.slice(0, 20)}</div>
                                <div class="text-muted">${content.timestamp}; ${Math.ceil(content.body.length / 100)} min read</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`
}

function get_realtime_price(ticker) {
    let price = document.querySelector(`#${ticker}`)
    fetch(`./load_prices/${ticker}`)
        .then(response => response.json())
        .then(data => {
            price.innerHTML = parseFloat(data.price).toFixed(4);
        });
}