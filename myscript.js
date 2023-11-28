var head=document.getElementsByClassName("hed")
function getRadomColor(){
    var letter="0123456789ABCDEF";
    var color ="#";
    for ( var i=0;i<6;i++){
        color+=letter[Math.floor(Math.random()*16)]
    }
    return color
}
function changeHeaderColor(){
Headers.style.color=getRadomColor();}
setInterval("changeHeaderColor()",500);