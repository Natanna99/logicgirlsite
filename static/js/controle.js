var btn1 = document.getElementById("sugestaoBtn");
var btn2 = document.getElementById("sobreBtn");
var btn3 = document.getElementById("downloadBtn");
var btn4 = document.getElementById("equipeBtn");

var nome = document.getElementById("navBar").attributes[1].textContent;

if(nome == "sobre"){
    btn2.className = "btn alert-info fs-4 fw-bold";
}else if(nome == "downloads"){
    btn3.className = "btn alert-info fs-4 fw-bold";
}else if(nome == "sugestao"){
    btn1.className = "btn alert-info fs-4 fw-bold";
}else if(nome == "equipe"){
    btn4.className = "btn alert-info fs-4 fw-bold";
}