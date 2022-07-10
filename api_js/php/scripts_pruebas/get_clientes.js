let API_URL = "http://127.0.0.1:8000/clientes"
fetch(API_URL)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))

const mostrarDatos = (data) => {
    console.log(data)
    for (let i = 0; i < data.length; i++) {
        document.getElementById("datos").innerHTML = "<tr><td>1</td></tr>";
    }
}
