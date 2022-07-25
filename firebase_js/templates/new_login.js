var form = document.querySelector("form");
form.onsubmit = e => {
    var email = document.querySelector("[id=correo]").value;
    var password = document.querySelector("[id=contraseña]").value;
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:8000/user/token/', true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Authorization", "Basic " + btoa(email.value + ":" + password.value));
    request.setRequestHeader("Content-Type", "application/json");
    request.onload= function() {
        const data = JSON.parse(request.response);
        if (request.status == 401 || response.status == 402){
            alert(data);
        }
        if(request.status == 202){
            const response = response.responseText;
            const json = JSON.parse(response);
            if (request.status == 202){
                sessionStorage.setItem("token",json.token);
                mensaje = "Bienvenido";
                alert(mensaje);
                document.querySelector("[id=inicio]").onclick=function(){
                    window.location.href = "bienvenida.html"
                };
            }
        }
    };
    request.send();
}