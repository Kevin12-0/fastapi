var form = document.querySelector("form");
form.onsubmit = e => {
    var nombre = document.querySelector("[id=nombre]").value;
    var email = document.querySelector("[id=correo]").value;
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.open("POST","http://127.0.0.1:8000/insertar/"+nombre+"/"+email)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function() {
        const data = JSON.parse(xhr.response);
        console.log(data);
    }
    xhr.send();
}