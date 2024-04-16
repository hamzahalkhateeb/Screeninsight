document.addEventListener('DOMContentLoaded', function (){
    let navigation_bar = document.querySelector('#nav-cred');
    navigation_bar.style.opacity = '1';



    let actionbtn = document.querySelector('#actionbtn');
    let comedybtn = document.querySelector('#comedybtn');
    let dramabtn = document.querySelector('#dramabtn');
    let fantasybtn = document.querySelector('#fantasybtn');
    let horrorbtn = document.querySelector('#horrorbtn');
    let romancebtn = document.querySelector('#romancebtn');

    actionbtn.addEventListener('click', function(){
        let targetdiv = document.getElementsByClassName('flowParent')[0];
        targetdiv.scrollIntoView({behavior: 'smooth', block: 'center'});
    })

    comedybtn.addEventListener('click', function(){
        let targetdiv = document.getElementsByClassName('flowParent')[1];
        targetdiv.scrollIntoView({behavior: 'smooth', block: 'center'});
    })

    dramabtn.addEventListener('click', function(){
        let targetdiv = document.getElementsByClassName('flowParent')[2];
        targetdiv.scrollIntoView({behavior: 'smooth', block: 'center'});
    })

    fantasybtn.addEventListener('click', function(){
        let targetdiv = document.getElementsByClassName('flowParent')[3];
        targetdiv.scrollIntoView({behavior: 'smooth', block: 'center'});
    })

    horrorbtn.addEventListener('click', function(){
        let targetdiv = document.getElementsByClassName('flowParent')[4];
        targetdiv.scrollIntoView({behavior: 'smooth', block: 'center'});
    })

    romancebtn.addEventListener('click', function(){
        let targetdiv = document.getElementsByClassName('flowParent')[5];
        targetdiv.scrollIntoView({behavior: 'smooth', block: 'center'});
    })
});