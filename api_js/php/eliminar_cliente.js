var form = document.querySelector("form");
form.onsubmit = e => {
    var id = document.querySelector("[id=id_cliente]").value;
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE","http://127.0.0.1:8000/eliminar/"+id);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function() {
        const data = JSON.parse(xhr.response);
        console.log(data);
    }
    xhr.send();
}