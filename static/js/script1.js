// Get the container element
var btnContainer = document.getElementById("myDIV");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("btt");

// Loop through the buttons and add the active class to the current/clicked button
$(function($) {
   
    let url = window.location.href;
    $('li a').each(function() {
      if (this.href === url) {
        $(this).closest('li').addClass('active');
      }
    });
});


(function() {
  console.log('here'); 
  let form = document.querySelector('.suscribe_form');
  form.addEventListener('submit',async (event) => {
    event.preventDefault();
    let postData = {
      "email" : form.email.value
    }

    let response = await fetch('http://localhost:8000/api/accounts/subscribers', {
         headers: {
           "Content-Type": "application/json",
         },
         method: "POST",
         body: JSON.stringify(postData)
     })
    
    // Handle success
    let responseData = await response.json();
    console.log('BAKC END RESPONCE AS JSON',responseData);
    if (response.ok){
      alert('you subscribe successfull')
    }else{
      alert(responseData.email)
    }
  
  });
  
  
})();
  
