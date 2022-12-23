// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
   
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
    })
  })()


// form submitting event enable and Disable the button dynamically using javascript 
  var textarea = document.getElementsByTagName("textarea");
  var inp = document.getElementsByTagName("input");
  var btn = document.getElementById("submitContact");
  // Disable the button dynamically using javascript
  btn.disabled = "disabled";

  function checkForm() {
      for (var i = 0; i < inp.length; i++) {
          if (inp[i].checkValidity() == false) {
              btn.disabled = "disabled";
          } else {
              btn.disabled = false;
          }
      }
      if(textarea[0].checkValidity()==false){
        btn.disabled = "disabled";
      }else {
        btn.disabled = false;
      }
  }
  
// Take first litters of the name and  creating profile image for comminuting 
var fullName1 = document.querySelectorAll('.fullName');
var fullName2 = document.querySelectorAll('.lastName');
var name1 = document.querySelectorAll('.name-fm');
      for(i=0; i<fullName1.length; i++){
        var initials = fullName1[i].textContent.charAt(0).toUpperCase() + '' + fullName2[i].textContent.charAt(0).toUpperCase(); name1[i].innerHTML = initials;
      }