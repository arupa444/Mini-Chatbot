const text1= document.getElementById('textBox');
const submit1= document.getElementById('submitBox');
const output1= document.getElementById('outQue');

function clickOut(){
    output1.innerHTML=text1.value;
}

submit1.addEventListener('click',clickOut);