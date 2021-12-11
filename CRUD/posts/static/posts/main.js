const helloWorldBox = document.getElementById("hello-world");
const postsBox = document.getElementById("posts-box");

// helloWorldBox.textContent = "Hello world";
// helloWorldBox.innerHTML = "Hello <b>world</b>";

$.ajax({
    type: "GET",
    url: "/data/",
    success: function(response){
        const data = response.data;
        console.log(data);

        data.forEach(el => {
            postsBox.innerHTML += `${el.title} - <b>${el.body}</b><br>`;
        });
    },
    error: function(error){
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