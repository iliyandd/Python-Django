const helloWorldBox = document.getElementById("hello-world");
const postsBox = document.getElementById("posts-box");
const spinnerBox = document.getElementById("spinner-box");

// helloWorldBox.textContent = "Hello world";
// helloWorldBox.innerHTML = "Hello <b>world</b>";

$.ajax({
    type: "GET",
    url: "/data/",
    success: function (response) {
        const data = response.data;
        setTimeout(() => {
            spinnerBox.classList.add("not-visible");
            console.log(data);

            data.forEach(el => {
                // postsBox.innerHTML += `${el.title} - <b>${el.body}</b><br>`;

                postsBox.innerHTML += `
                    <div class="card mb-2">
                        <div class="card-body">
                            <h5 class="card-title">${el.title}</h5>
                            <p class="card-text">${el.body}</p>
                        </div>
                        <div class="card-footer">
                            <div class="row">
                                <div class="col-1">
                                    <a href="#" class="btn btn-primary">Details</a>
                                </div>
                                <div class="col-1">
                                    <a href="#" class="btn btn-primary">Like</a>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            });
        }, 100);

    },
    error: function (error) {
        console.log(error);
    }
})


$.ajax({
    type: 'GET',
    url: '/hello-world/',
    success: function (response) {
        console.log('success', response.text);
        helloWorldBox.textContent = response.text;
    },
    error: function (error) {
        console.log('error', error);
    }
})



// Fetch data every 5 seconds
// function f(){
//     $.ajax({
//         type: 'GET',
//         url: '/hello-world/',
//         success: function (response) {
//             // console.log('success', response);
//             console.log('success', response.text);
//             helloWorldBox.textContent = response.text;
//         },
//         error: function (error) {
//             console.log('error', error);
//         }
//     })
// }

// setInterval(f, 5000);