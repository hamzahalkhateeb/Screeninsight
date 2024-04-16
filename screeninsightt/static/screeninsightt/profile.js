document.addEventListener('DOMContentLoaded', function() {
    let navigation_bar = document.querySelector('#nav-cred');
    navigation_bar.style.opacity = '1';

    let watchButtons = document.querySelectorAll(".watchsymbol");
    watchButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            let movieid = button.id.split('_')[1];
            let difference = button.id.split('_')[0]
            let userid = document.querySelector(`#username_${movieid}`).value;
            let csrftoken = document.querySelector('#csrf_token').value;

            let data = {
                "movieid": movieid,
                "userid": userid,
                "LorW": "watchlist"
            };
            if(difference ==="watchedtv"){
                fetch('/deletetv', {
                    method: 'POST',
                    headers: {
                        'Content-Type': "application/json",
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    let deleted = data.deleted;

                    if (deleted == "true") {
                        div = document.querySelector(`#container2_${movieid}`);
                        div.style.opacity = "0";
                        setTimeout(function(){
                            div.remove();
                        }, 300);
                    }
                });

            }

            else if(difference ==="watched"){
                fetch('/delete', {
                        method: 'POST',
                        headers: {
                            'Content-Type': "application/json",
                            'X-CSRFToken': csrftoken
                        },
                        body: JSON.stringify(data)
                    })
                    .then(response => response.json())
                    .then(data => {
                        let deleted = data.deleted;

                        if (deleted == "true") {
                            div = document.querySelector(`#container2_${movieid}`);
                            div.style.opacity = "0";
                            setTimeout(function(){
                                div.remove();
                            }, 300);
                        }
                    });
            }
        });
    });

    let likeButtons = document.querySelectorAll(".likesymbol");
    likeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            
            let movieid = button.id.split('_')[1];
            let difference = button.id.split('_')[0]
            let userid = document.querySelector(`#username2_${movieid}`).value;
            let csrftoken = document.querySelector('#csrf_token2').value;
            

            let data = {
                "movieid": movieid,
                "userid": userid,
                "LorW": "likelist"
            };
            if(difference==="liked"){
            fetch('/delete', {
                    method: 'POST',
                    headers: {
                        'Content-Type': "application/json",
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    let deleted = data.deleted;

                    if (deleted == "true") {
                        div = document.querySelector(`#container3_${movieid}`);
                        div.style.opacity = "0";
                        setTimeout(function(){
                            div.remove();
                        }, 300);
                        
                    }
                });}
            else if(difference==="likedtv"){
                fetch('/deletetv', {
                    method: 'POST',
                    headers: {
                        'Content-Type': "application/json",
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    let deleted = data.deleted;

                    if (deleted == "true") {
                        div = document.querySelector(`#container3_${movieid}`);
                        div.style.opacity = "0";
                        setTimeout(function(){
                            div.remove();
                        }, 300);
                        
                    }
                });
            }
        });
    });


    let moviesbtn = document.querySelector("#movies");
    let tvbtn = document.querySelector("#tvshows");

    tvbtn.addEventListener('click', function(){

        moviesbtn.style.borderBottom = "none";
        tvbtn.style.borderBottom = "2px solid gray";
        
        let moviereviews = document.querySelectorAll(".reviewsss");
        moviereviews.forEach(review =>{
            review.style.display = "none";
            review.style.visibility = "hidden";
        })

        let tvreviews = document.querySelectorAll(".reviewstv");
        tvreviews.forEach(review =>{
            review.style.display = "flex";
            review.style.visibility = "visible";
        })

        let movieelements = document.querySelectorAll(".container2");
        movieelements.forEach(element =>{
            element.style.display = "none";
            element.style.visibility = "hidden";
        })

        let tvelements = document.querySelectorAll(".container99");
        tvelements.forEach(element =>{
            element.style.display = "flex";
            element.style.visibility = "visible";
        })

        let likedtitle = document.querySelector("#likedtitless");
        likedtitle.innerHTML = "Liked TV Shows <i class='fas fa-heart heart'>";
        let watchedtitle = document.querySelector("#watchedtitless");
        watchedtitle.innerHTML = "Watchlisted TV Shows <i class='fas fa-heart heart'>";
    })

    moviesbtn.addEventListener('click', function(){

        tvbtn.style.borderBottom = "none";
        moviesbtn.style.borderBottom = "2px solid gray";
        
        let moviereviews = document.querySelectorAll(".reviewsss");
        moviereviews.forEach(review =>{
            review.style.display = "flex";
            review.style.visibility = "visible";
        })

        let tvreviews = document.querySelectorAll(".reviewstv");
        tvreviews.forEach(review =>{
            review.style.display = "none";
            review.style.visibility = "hidden";
        })

        let movieelements = document.querySelectorAll(".container2");
        movieelements.forEach(element =>{
            element.style.display = "flex";
            element.style.visibility = "visible";
        })

        let tvelements = document.querySelectorAll(".container99");
        
        tvelements.forEach(element =>{
            element.style.display = "none";
            element.style.visibility = "hidden";
        })

        let likedtitle = document.querySelector("#likedtitless");
        likedtitle.innerHTML = "Liked Movies <i class='fas fa-heart heart'>";
        let watchedtitle = document.querySelector("#watchedtitless");
        watchedtitle.innerHTML = "Watchlisted Movies <i class='fas fa-heart heart'>";
    })
});
