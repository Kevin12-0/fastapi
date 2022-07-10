var form = document.querySelector("form");
form.onsubmit = e => {
    var id = document.querySelector("[id=id_cliente]").value;
    var nombre = document.querySelector("[id=nombre_cliente]").value;
    var email = document.querySelector("[id=email]").value;
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.open("PUT","http://127.0.0.1:8000/actulizar/"+id+"/"+nombre+"/"+email);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function() {
        const data = JSON.parse(xhr.response);
        console.log(data);
    }
    xhr.send();
}
