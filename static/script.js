function maisinfo(){
    var mais=document.getElementById('mais')
    var button=document.getElementById('button')
    if(mais.style.display === "none"){
        mais.style.display="inline"
        button.innerHTML="&#10548;"}
    else{
        mais.style.display="none"
        button.innerHTML="&#10549;"
    }
}
setTimeout(function clim(){
    var tes=document.getElementById('teste')
    var clima=document.getElementById('clima_um').innerText
    if(clima === "Céu Limpo"){
        tes.setAttribute('src',"/static/sun.png")}
    else if(clima == "Nublado"||clima == "Algumas Nuvens"||clima == "Nuvens Dispersas"){
        tes.setAttribute('src', "/static/nublado.png")}
    else if(clima == "Garoa De Leve Intensidade"|| clima == "Chuva Leve"|| clima == "Chuva Moderada"){
        tes.setAttribute('src', "/static/rain.png")
    }
    else if(clima == "Névoa"){
        tes.setAttribute('src',"/static/nevoa.png")
    }

},3000)