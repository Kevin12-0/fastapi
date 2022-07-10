var form = document.querySelector("form");
form.onsubmit = e => {
    var id = document.querySelector("[id=id_cliente]").value;
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.open("GET","http://127.0.0.1:8000/cliente/"+id);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function() {
        const data = JSON.parse(xhr.response);
        console.log(data);
        const HttpResponse = document.querySelector("[id=datos]");
        const tpl = data.map((user) => `<tr><td>${user.id_cliente}</td><td>${user.nombre}</td><td>${user.email}</td></tr>`)
        HttpResponse.innerHTML = tpl;
    }
    xhr.send();
}