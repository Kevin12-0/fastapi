const API_URL = "http://127.0.0.1:8000/clientes";
const xhr = new XMLHttpRequest();

function onRequestHandler() {
    if (xhr.readyState == 4 && xhr.status == 200) {
        const data = JSON.parse(this.response);
        console.log(data);
        const HttpResponse = document.querySelector("#datos");

        const tpl = data.map((user) => `<tr><td>${user.id_cliente}</td><td>${user.nombre}</td><td>${user.email}</td></tr>`);
        HttpResponse.innerHTML = tpl;
    }
}
xhr.addEventListener('load', onRequestHandler);
xhr.open("GET", API_URL);
xhr.send();
