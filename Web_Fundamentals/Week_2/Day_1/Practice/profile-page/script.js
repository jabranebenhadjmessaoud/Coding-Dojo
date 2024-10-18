console.log("page loaded...");
var naaame=document.querySelector("#nametochange")
function changename(){
    
    naaame.innerHTML ="Jabrane" ;
}
var requestnumber=document.querySelector(".badge")
function decreaserequestcount(){

requestnumber.innerHTML --;
var nammetoremove=document.querySelector(".card-list-item") ;
nammetoremove.remove() ;
}

