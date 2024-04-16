document.addEventListener('DOMContentLoaded', function (){
    let movie_info = document.querySelectorAll('.indexdiv .movie-info');
    setTimeout(function () {
        movie_info.forEach(function (movieInfo) {
            movieInfo.style.opacity = "1";
            movieInfo.style.paddingLeft = '3%';
        });
    }, 0);
    
    let trdmDisplayed = 0;
    let nextbtns = document.querySelectorAll('.nextbtn');
    let nextbtns2 = document.querySelectorAll('.nextbtn2');

    let trdmDisplayed2 = 0;
    let nextbtn3 = document.querySelector('.nextbtn3');
    let previousbtn3 = document.querySelector('.previousbtn3');

    let trdmDisplayed3 = 0;
    let nextbtn4 = document.querySelector('#nextbtn4');
    let previousbtn4 = document.querySelector('#previousbtn4');
    
    let trdmDisplayed4 = 0;
    let nextbtn5 = document.querySelector('#nextbtn5');
    let previousbtn5 = document.querySelector('#previousbtn5');

    let trdmDisplayed5 = 0;
    let nextbtn6 = document.querySelector('#nextbtn6');
    let previousbtn6 = document.querySelector('#previousbtn6');

    let trdmDisplayed6 = 0;
    let nextbtn7 = document.querySelector('#nextbtn7');
    let previousbtn7 = document.querySelector('#previousbtn7');

    let trdmDisplayed7 = 0;
    let nextbtn8 = document.querySelector('#nextbtn8');
    let previousbtn8 = document.querySelector('#previousbtn8');

    let trdmDisplayed8 = 0;
    let nextbtn9 = document.querySelector('#nextbtn9');
    let previousbtn9 = document.querySelector('#previousbtn9');

    nextbtns.forEach(function(nextbtn)
    {
        nextbtn.addEventListener('click', function(){
            
            trdmDisplayed += 1;
                        
            if(trdmDisplayed > 9){
                trdmDisplayed = 0;
            } else if(trdmDisplayed <= 0){
                trdmDisplayed = 9;
            };



            let element = document.getElementsByClassName('indexdiv')[0].getElementsByClassName('shading-div')[trdmDisplayed];
            let container = document.getElementsByClassName('indexdiv')[0];
            
            scrollleftvalue = element.offsetLeft - container.offsetLeft;

            
            container.scroll({
                left: scrollleftvalue,
                behavior: 'smooth'
            });

            
            

        });
    }); 

    nextbtns2.forEach(function(nextbtn2)
    {
        nextbtn2.addEventListener('click', function(){
            trdmDisplayed -= 1;
                        
            if(trdmDisplayed > 9){
                trdmDisplayed = 0;
            } else if(trdmDisplayed < 0){
                trdmDisplayed = 9;
            };

            
            let element = document.getElementsByClassName('indexdiv')[0].getElementsByClassName('shading-div')[trdmDisplayed];
            
            let container = document.getElementsByClassName('indexdiv')[0];
            
            scrollleftvalue = element.offsetLeft - container.offsetLeft;

            
            container.scroll({
                left: scrollleftvalue,
                behavior: 'smooth'
            });
            
        });
    

    });

    setInterval(function(){
            trdmDisplayed += 1;
                        
            if(trdmDisplayed > 9){
                trdmDisplayed = 0;
            } else if(trdmDisplayed <= 0){
                trdmDisplayed = 9;
            };



            let element = document.getElementsByClassName('indexdiv')[0].getElementsByClassName('shading-div')[trdmDisplayed];
            let container = document.getElementsByClassName('indexdiv')[0];
            
            scrollleftvalue = element.offsetLeft - container.offsetLeft;

            
            container.scroll({
                left: scrollleftvalue,
                behavior: 'smooth'
            });


        }, 20000);
    

    
    nextbtn4.addEventListener('click', function(){
        
        if(trdmDisplayed3 > 9){
            trdmDisplayed3 = 9;
        } else if(trdmDisplayed3 < 0){
            trdmDisplayed3 = 0;
        };

        let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[0].getElementsByClassName('containerC')[trdmDisplayed3];
        let container = document.getElementsByClassName('flow-into')[0];

        let numberofelements = document.getElementsByClassName('flow-into')[0].querySelectorAll('.containerC');
        
        
        
        let totalwidth = element.clientWidth * (numberofelements.length);

        let scrolled = container.scrollLeft;

        if (scrolled >= totalwidth){
            scrolled = totalwidth
        };

        
        scrolled += element.clientWidth;
        
        
        trdmDisplayed3 +=1;
        
        

        container.scroll({
            left: scrolled,
            behavior: 'smooth'
        });


    })

    previousbtn4.addEventListener('click', function(){
        
        if(trdmDisplayed3 > 9){
            trdmDisplayed3 = 9;
        } else if(trdmDisplayed3 < 0){
            trdmDisplayed3 = 0;
        };

        let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[0].getElementsByClassName('containerC')[trdmDisplayed3];
        let container = document.getElementsByClassName('flow-into')[0];

        let numberofelements = document.getElementsByClassName('flow-into')[0].querySelectorAll('.containerC');
        
        
        
        let totalwidth = element.clientWidth * (numberofelements.length);

        let scrolled = container.scrollLeft;

        if (scrolled >= totalwidth){
            scrolled = totalwidth
        };

        
        scrolled -= element.clientWidth;
        
        
        trdmDisplayed3 -=1;
        
        

        container.scroll({
            left: scrolled,
            behavior: 'smooth'
        });


    })
/////////////////////////////////////////////////
////////////////////////////////////////////////
nextbtn5.addEventListener('click', function(){
        
    if(trdmDisplayed4 > 9){
        trdmDisplayed4 = 9;
    } else if(trdmDisplayed4 < 0){
        trdmDisplayed4 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[1].getElementsByClassName('containerC')[trdmDisplayed4];
    let container = document.getElementsByClassName('flow-into')[1];
    

    let numberofelements = document.getElementsByClassName('flow-into')[1].querySelectorAll('.containerC');
    
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    

    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled += element.clientWidth;
    
    
    trdmDisplayed4 +=1;
    
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})

previousbtn5.addEventListener('click', function(){
        
    if(trdmDisplayed4 > 9){
        trdmDisplayed4 = 9;
    } else if(trdmDisplayed4 < 0){
        trdmDisplayed4 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[1].getElementsByClassName('containerC')[trdmDisplayed4];
    let container = document.getElementsByClassName('flow-into')[1];

    
    let numberofelements = document.getElementsByClassName('flow-into')[1].querySelectorAll('.containerC');
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    


    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled -= element.clientWidth;
    
    
    trdmDisplayed4 -=1;
    
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})
//////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////
nextbtn6.addEventListener('click', function(){
        
    if(trdmDisplayed5 > 9){
        trdmDisplayed5 = 9;
    } else if(trdmDisplayed5 < 0){
        trdmDisplayed5 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[2].getElementsByClassName('containerC')[trdmDisplayed5];
    let container = document.getElementsByClassName('flow-into')[2];
    

    let numberofelements = document.getElementsByClassName('flow-into')[2].querySelectorAll('.containerC');
    
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    

    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled += element.clientWidth;
    
    
    trdmDisplayed5 +=1;
    
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})

previousbtn6.addEventListener('click', function(){
        
    if(trdmDisplayed5 > 9){
        trdmDisplayed5 = 9;
    } else if(trdmDisplayed5 < 0){
        trdmDisplayed5 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[2].getElementsByClassName('containerC')[trdmDisplayed5];
    let container = document.getElementsByClassName('flow-into')[2];

   
    let numberofelements = document.getElementsByClassName('flow-into')[2].querySelectorAll('.containerC');
    
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    


    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled -= element.clientWidth;
    
    
    trdmDisplayed5 -=1;
    
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})
//////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////
nextbtn7.addEventListener('click', function(){
        
    if(trdmDisplayed6 > 9){
        trdmDisplayed6 = 9;
    } else if(trdmDisplayed6 < 0){
        trdmDisplayed6 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[3].getElementsByClassName('containerC')[trdmDisplayed6];
    let container = document.getElementsByClassName('flow-into')[3];
    

    let numberofelements = document.getElementsByClassName('flow-into')[3].querySelectorAll('.containerC');
   
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    

    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled += element.clientWidth;
    
    
    trdmDisplayed6 +=1;
   

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})

previousbtn7.addEventListener('click', function(){
        
    if(trdmDisplayed6 > 9){
        trdmDisplayed6 = 9;
    } else if(trdmDisplayed6 < 0){
        trdmDisplayed6 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[3].getElementsByClassName('containerC')[trdmDisplayed6];
    let container = document.getElementsByClassName('flow-into')[3];

    
    let numberofelements = document.getElementsByClassName('flow-into')[3].querySelectorAll('.containerC');
    
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    


    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled -= element.clientWidth;
    
    
    trdmDisplayed6 -=1;
    
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})
//////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////
nextbtn8.addEventListener('click', function(){
        
    if(trdmDisplayed7 > 9){
        trdmDisplayed7 = 9;
    } else if(trdmDisplayed7 < 0){
        trdmDisplayed7 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[4].getElementsByClassName('containerC')[trdmDisplayed7];
    let container = document.getElementsByClassName('flow-into')[4];
    
    let numberofelements = document.getElementsByClassName('flow-into')[4].querySelectorAll('.containerC');
   
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
  

    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled += element.clientWidth;
    
    
    trdmDisplayed7 +=1;
   
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})

previousbtn8.addEventListener('click', function(){
        
    if(trdmDisplayed7 > 9){
        trdmDisplayed7 = 9;
    } else if(trdmDisplayed7 < 0){
        trdmDisplayed7 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[4].getElementsByClassName('containerC')[trdmDisplayed7];
    let container = document.getElementsByClassName('flow-into')[4];

    
    let numberofelements = document.getElementsByClassName('flow-into')[4].querySelectorAll('.containerC');
   
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    


    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled -= element.clientWidth;
    
    
    trdmDisplayed7 -=1;
    
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})
//////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////
nextbtn9.addEventListener('click', function(){
        
    if(trdmDisplayed8 > 9){
        trdmDisplayed8 = 9;
    } else if(trdmDisplayed8 < 0){
        trdmDisplayed8 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[5].getElementsByClassName('containerC')[trdmDisplayed8];
    let container = document.getElementsByClassName('flow-into')[5];
   

    let numberofelements = document.getElementsByClassName('flow-into')[5].querySelectorAll('.containerC');
    
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    

    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled += element.clientWidth;
    
    
    trdmDisplayed8 +=1;
    
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})

previousbtn9.addEventListener('click', function(){
        
    if(trdmDisplayed8 > 9){
        trdmDisplayed8 = 9;
    } else if(trdmDisplayed8 < 0){
        trdmDisplayed8 = 0;
    };

    let element = document.getElementsByClassName('indexdiv2')[0].getElementsByClassName('flow-into')[5].getElementsByClassName('containerC')[trdmDisplayed8];
    let container = document.getElementsByClassName('flow-into')[5];

    
    let numberofelements = document.getElementsByClassName('flow-into')[5].querySelectorAll('.containerC');
    
    
    
    let totalwidth = element.clientWidth * (numberofelements.length);
    


    let scrolled = container.scrollLeft;

    if (scrolled >= totalwidth){
        scrolled = totalwidth
    };

    
    scrolled -= element.clientWidth;
    
    
    trdmDisplayed8 -=1;
    
    

    container.scroll({
        left: scrolled,
        behavior: 'smooth'
    });


})
}); 
