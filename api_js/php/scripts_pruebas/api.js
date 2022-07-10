const API_URL = "http://127.0.0.1:8000";
const xhr = new XMLHttpRequest();

function onRequestHandler() {
    if (this.readyState == 4 && this.status == 200) {
        // 0 -> unset -> no se a llamado al metodo open
        // 1 -> opened -> se a llamado al metodo opene
        // 2. -> headers_recived -> se esta llamando al metodo send
        // 3. -> loandig -> esta recibiendo la respuesta
        // 4. -> Done -> se a completado la operacion
        const data = JSON.parse(this.response);
        console.log(data);
        const conv = JSON.stringify(data);
        document.getElementById("subtitulo").innerText = conv;
        //const HttpResponse = document.querySelector("#respuesta");
        // const tpl = data.map( (Hello) => '<label class="label">$Hello.World</label>')
        // HttpResponse.innerText = '<label class="label">'+tpl+'</label>';
    }
}

xhr.addEventListener('load', onRequestHandler);
xhr.open("GET", API_URL);
xhr.send();