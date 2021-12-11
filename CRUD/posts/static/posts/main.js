const helloWorldBox = document.getElementById("hello-world");

// helloWorldBox.textContent = "Hello world";
// helloWorldBox.innerHTML = "Hello <b>world</b>";

$.ajax({
    type: 'GET',
    url: '/hello-world/',
    success: function (response) {
        // console.log('success', response);
        console.log('success', response.text);
        helloWorldBox.textContent = response.text;
    },
    error: function (error) {
        console.log('error', error);
    }
})


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