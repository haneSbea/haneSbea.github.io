var password = "itmesbe3";

function passcheck() {

if(document.getElementById('pass1').value != password){
alert('Wrong Password Try Again.');
return false;
}
if(document.getElementById('pass1').value == password){
    alert('Correct Password, Click OK to enter Webpage.');
    }
}