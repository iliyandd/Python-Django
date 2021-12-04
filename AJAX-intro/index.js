const url = "https://swapi.dev/api/people/";

// AJAX example
$.ajax({
    type: "GET",
    url: url,
    success: function(response){
        console.log(response);
    },
    error: function(error){
        console.log(error);
    }
})

// XMLHttpRequest example
const req = new XMLHttpRequest();

req.addEventListener('readystatechange', ()=>{
    if(req.readyState === 4){
        console.log('xhttp', JSON.parse(req.responseText));
    }
})

req.open('GET', url);
req.send();

// fetch example
fetch(url)
.then(resp=>resp.json()).then(data=>console.log('fetch', data))
.catch(error=>console.log(error));