const obj1 = document.getElementById('hindi')
const obj2 = document.getElementById('english')
const obj11 = document.getElementById('hinditext')
const obj21 = document.getElementById('englishtext')

obj1.addEventListener('click', ()=>{
    obj21.style.display = 'none';
    obj11.style.display = 'block';
})

obj2.addEventListener('click', ()=>{
    obj11.style.display = 'none';
    obj21.style.display = 'block';
})

function check(){
    // console.log(scrollY)
    if(scrollY >= 1080){
        document.body.style.background = 'white';
    }
    else
        document.body.style.background = 'black';
}
setInterval(check, 300)
