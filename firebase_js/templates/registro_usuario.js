var form = document.querySelector("form");
form.onsubmit=e=>{
    var correo = document.querySelector("[id=correo]").value;
    var password = document.querySelector("[id=password]").value;
    var confirmacion = document.querySelector("[id=confirmacion]").value;
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:8000/registro/"+correo+"/"+password+"/"+confirmacion);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onload = function() {
        const data = JSON.parse(xhr.response);
        console.log(data);
        const response = JSON.stringify(data);
        alert(response);
    }
    xhr.send();
}
