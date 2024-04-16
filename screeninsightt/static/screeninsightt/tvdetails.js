document.addEventListener('DOMContentLoaded', function (){
    let navigation_bar = document.querySelector('#nav-cred');
    navigation_bar.style.opacity = '1';


    
    let userd = document.querySelector("#currentuser").value;
    let idd = document.querySelector('#datasid').value;

    colourbtns(userd, idd);


    let general = document.querySelector('#generaltab');
    let cast = document.querySelector('#casttab');
    general.addEventListener('click', function(){
        cast.setAttribute("style", "color: gray; background-color: rgb(41, 41, 41);");
        general.setAttribute("style", "color: white; background-color: rgb(51, 51, 51);");

        document.querySelector('#general').setAttribute("style", "display: block;");
        document.querySelector('#cast').setAttribute("style", "display: none;");
    })

    cast.addEventListener('click', function(){
        general.setAttribute("style", "color: gray; background-color: rgb(41, 41, 41);");
        cast.setAttribute("style", "color: white; background-color: rgb(51, 51, 51);");
        document.querySelector('#general').setAttribute("style", "display: none;");
        document.querySelector('#cast').setAttribute("style", "display: block;");
    })

    let number = document.querySelector("#number").innerHTML;
    let numberi = +number;
    findstars(numberi)
    



    let atlbtn = document.querySelector("#atl");
    let atwbtn = document.querySelector("#atw");
    atlbtn.addEventListener('click', function(){
        
        
        let moviename = document.querySelector("#mt").innerText;
        let posterpath = document.querySelector("#is").src;
        let user = document.querySelector("#currentuser").value;
        let id = document.querySelector('#datasid').value;
        

        let data = {
            'moviename': moviename,
            'posterpath': posterpath,
            'user': user,
            'movieid':id
        };
        
        fetch('/tvaddobjectsL', {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('#csrf_token').value
            },
            body: JSON.stringify(data)
        })
        .then(response =>response.json())
        .then(data =>{
            to_grey = data.to_grey;

            if (to_grey == true){
                atlbtn.style.color = "white"
            }
            else if(to_grey == false){
                atlbtn.style.color = "red"
            }
        })
        


    })
    
    atwbtn.addEventListener('click', function(){
        let moviename = document.querySelector("#mt").innerText;
        let posterpath = document.querySelector("#is").src;
        let user = document.querySelector("#currentuser").value;
        let id = document.querySelector('#datasid').value;
        

        let data = {
            'moviename': moviename,
            'posterpath': posterpath,
            'user': user,
            'movieid': id
        };
        
        fetch('/tvaddobjectsW', {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('#csrf_token').value
            },
            body: JSON.stringify(data)
        })
        .then(response =>response.json())
        .then(data =>{
            to_grey = data.to_grey;
            if (to_grey == true){
                atwbtn.style.color = "white"
            }
            else if(to_grey == false){
                atwbtn.style.color = "green"
            }
        })

    })

});

function findstars(number){
    let wholenumber = Math.floor(number);

    let decimal = number-wholenumber;

    if (decimal < 0.25 ){
        decimal = 0;
    } else if (decimal >= 0.25 && decimal < 0.75){
        decimal = 0.5;
    } else if (decimal >= 0.75 && decimal <= 0.99){
        decimal = 0;
        wholenumber = wholenumber + 1;
    };

    let wholestars = wholenumber;
    let halfstars = decimal;
    let offstars;

    if (halfstars === 0.5){
        offstars = 10 - (wholestars + 1);
    } else{
        offstars = 10-wholestars;
    }

    let actualstatement ="";

    


    for(let i = 0; i < wholestars; i++){
        actualstatement += "<i class='fas fa-star checked'></i>";
    };

    if(halfstars === 0.5){
        actualstatement += "<i class='fas fa-star-half-alt Hchecked'></i>";
    };

    for(let i = 0; i < offstars; i++){
        actualstatement += "<i class='fas fa-star unchecked'></i>";
    };
    
    document.querySelector('#number').innerHTML = actualstatement;

    
    


}

function colourbtns(user, id){

    
    let data = {
        "movieid": id, 
        "user": user
    }

    fetch('/tvexists', {
        method: 'POST',
        headers:  {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('#csrf_token').value
        },
        body: JSON.stringify(data)
    })
    .then(response=>response.json())
    .then(data =>{

        let in_likedlist = data.in_likedlist;
        let in_watchlist = data.in_watchlist;
        console.log( in_likedlist, in_watchlist)

        let atlbtn = document.querySelector("#atl");
        let atwbtn = document.querySelector("#atw");

        if (in_likedlist == true){
            atlbtn.style.color = "red";
        }
        if (in_watchlist == true){
            atwbtn.style.color = "green";
    }
    })
    

    
    
}

let submitrvu = document.querySelector("#srb");

submitrvu.addEventListener('click', function(){
    let heading = document.querySelector("#rvuheading").value;
    
    let body = document.querySelector("#rvubody").value;
    
    let rating = document.querySelector("#rating").value;
    
    let movie = document.querySelector("#datasid").value;
    
    let user = document.querySelector("#currentuser").value;
    let moviename = document.querySelector("#mt").innerText;
    let posterpath = document.querySelector("#is").src;

    if (heading == "" || body == "" || rating == ""){
        alert("please fill out all fields");
    }
    else{
        let data ={
            "reviewHeading": heading,
            "reviewBody": body,
            "rating": rating,
            "movieid": movie,
            "userid": user,
            "moviename": moviename,
            "posterpath":posterpath
        }

            fetch('/tvreview',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    'X-CSRFToken': document.querySelector("#csrf_token22").value
                },
                body:JSON.stringify(data)
                
            })

            

            .then(response => response.json())
            .then(data => {
                let success = data.success;
                let exists = data.exists;
                if (exists == "true"){
                    alert("You have already reviewed this movie");
                }
                else{
                    console.log("success");
                }
            })
    }
})

let edit = document.querySelector('#editbtn');
let save = document.querySelector('#savebtn');
edit.addEventListener('click', function(){
    edit.style.display = "none";
    save.style.display = "block";
    


    let user = document.querySelector("#currentuserinstance").value;
    let reviewid = document.querySelector("#reviewiddd").value;
    console.log(reviewid);
    let reviewcontent = document.querySelector(`#reviewcontent_${user}`);
    let headline = document.querySelector(`#headline_${reviewid}`).innerText;
    let body= document.querySelector(`#body_${reviewid}`).innerText;
    let stars = document.querySelector(`#rvustars_${reviewid}`).value;

    let formstring= `<form class="inputs">
                            <input type="hidden" id="csrf_token33" value="{{ csrf_token|safe }}">
                            <input type="text" id="rvuheading33" class="headinput" placeholder="Review Headline">
                            <input type="text" id="rvubody33" class="bodyinput" placeholder="Review body">
                            <div class="hinputs">
                                <input type="number" id="rating33" class="ratinginput" placeholder="Rate" min="1" max="10">
                                <span class="star"><i class="fas fa-star"></i></span>
                                
                            </div>
                    </form>`;

    reviewcontent.innerHTML = formstring;
    document.querySelector('#rvuheading33').value = headline;
    document.querySelector('#rvubody33').value = body;
    document.querySelector('#rating33').value = stars;

})



save.addEventListener('click', function(){
    let heading = document.querySelector("#rvuheading33").value;
    
    let body = document.querySelector("#rvubody33").value;
    
    let rating = document.querySelector("#rating33").value;
    
    let movie = document.querySelector("#datasid").value;
    
    let user = document.querySelector("#currentuser").value;
    let moviename = document.querySelector("#mt").innerText;
    let posterpath = document.querySelector("#is").src;

    if (heading == "" || body == "" || rating == ""){
        alert("please fill out all fields");
    }
    else{
        let data ={
            "reviewHeading": heading,
            "reviewBody": body,
            "rating": rating,
            "movieid": movie,
            "userid": user,
            "moviename": moviename,
            "posterpath":posterpath
        }

            fetch('/tvedit',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    'X-CSRFToken': document.querySelector("#csrf_token22").value
                },
                body:JSON.stringify(data)
                
            })
}});