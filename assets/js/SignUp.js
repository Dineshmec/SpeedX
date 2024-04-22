

function addUser(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const username = document.getElementById("signUpUsername").value;
    const email = document.getElementById("signUpUserEmail").value;
    const password = document.getElementById("signUpPasswordInput").value;
   // const workEmail = document.getElementById("signUpUserEmail").value; // Add this line to get work email

    const xhr = new XMLHttpRequest();
    xhr.open("POST", `${Appconfig.LOCALHOST}:${Appconfig.APP_PORT}/add_user`, true); // Replace with your actual API endpoint for adding a new user
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          alert(response.message);
          // You can redirect to another page or perform any other action here after successful sign up
        } else {
          const errorResponse = JSON.parse(xhr.responseText);
          alert(errorResponse.error);
        }
      }
    };
    const data = JSON.stringify({ username: username, email: email, password: password });
    xhr.send(data);
  }

  document.getElementById("signUpForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting normally
    addUser(event); // Call the addUser function
  });

  function togglePasswordVisibility() {
    const passwordInput = document.getElementById("signUpPasswordInput");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      hideShowBtn.style.opacity = "0.5";
    } else {
      passwordInput.type = "password";
      hideShowBtn.style.opacity = "1";
    }
  }

  const signUpScreen = document.getElementById("signUpScreen");
  const otpScreen = document.getElementById("otpScreen");
  const successScreen = document.getElementById("successScreen");

  const showEmailId = document.getElementById("showEmailId");
  const editEmail = document.getElementById("editEmail");

  // SignUp page form validations.
  const signUpUsername = document.getElementById("signUpUsername");
  const signUpUserEmail = document.getElementById("signUpUserEmail");
  const signUpPasswordInput = document.getElementById(
    "signUpPasswordInput"
  );

  function onSignInSumbitHandle(eve) {
    eve.preventDefault();
    homeValidateInputs();
  }

  function setErrorMessage(input, error_message) {
    // console.log("input", input);
    const inputControl = input.parentElement;
    const errorDisplay = inputControl.querySelector(".error_show");

    errorDisplay.innerText = error_message;
    inputControl.classList.add("error");
    inputControl.classList.remove("clear");
  }

  function setSuccessMessage(input) {
    // console.log("input", input);
    const inputControl = input.parentElement;
    const successDisplay = inputControl.querySelector(".error_show");

    successDisplay.innerText = " ";
    inputControl.classList.add("clear");
    inputControl.classList.remove("error");
  }

  function isValidEmail(email) {
    if (
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
        email
      )
    ) {
      return true;
    } else {
      return false;
    }
  }

  function homeValidateInputs() {
    // console.log("ok");
    var signUpUsername_value = signUpUsername.value.trim();
    //var signUpUserEmail_value = signUpUserEmail.value.trim();
    var signUpPasswordInput_value = signUpPasswordInput.value.trim();

    if (signUpUsername_value === "") {
      setErrorMessage(signUpUsername, "Please Enter a Username");
    } else {
      setSuccessMessage(signUpUsername);
    }

    // if (signUpUserEmail_value === "") {
    //   setErrorMessage(signUpUserEmail, "Please Enter a Email");
    // } else if (!isValidEmail(signUpUserEmail_value)) {
    //   setErrorMessage(signUpUserEmail, "Please Enter a 'Valid Email'");
    //   return false;
    // } else {
    //   setSuccessMessage(signUpUserEmail);
    // }

    if (signUpPasswordInput_value === "") {
      setErrorMessage(signUpPasswordInput, "Please Enter a Password");
    } else {
      setSuccessMessage(signUpPasswordInput);
    }

    if (
      signUpUsername_value &&
      signUpPasswordInput_value
    ) {
      // Make API call to send OTP
      fetch(`${Appconfig.LOCALHOST}:${Appconfig.APP_PORT}/send_otp`, { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'email': signUpUsername_value }),
      })
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Failed to send OTP');
          }
        })
        .then(data => {
          // Display OTP screen and other actions
          otpScreen.style.display = 'flex';
          signUpScreen.style.display = 'none';
          //showEmailId.innerText = signUpUserEmail_value;
          document.querySelectorAll('.otp-input')[0].focus();
        })
        .catch(error => {
          console.error('Error sending OTP:', error);
          // Handle error (e.g., show error message to the user)
        });
    }

  }

  let timer;
  let countdown = 15;
  function startResendTimer() {
    document.getElementById("resendBtn").disabled = true;
    timer = setInterval(updateTimer, 1000);
  }
  function updateTimer() {
    const timerElement = document.getElementById("timer");
    if (countdown > 0) {
      timerElement.textContent = `${countdown} seconds`;
      countdown--;
    } else {
      document.getElementById("resendBtn").disabled = false;
      timerElement.textContent = "";
      countdown = 15;
      clearInterval(timer);
    }
  }
  editEmail.addEventListener("click", () => {
    const timerElement = document.getElementById("timer");
    document.getElementById("resendBtn").disabled = false;
    timerElement.textContent = "";
    countdown = 15;
    clearInterval(timer);

    otpScreen.style.display = "none";
    signUpScreen.style.display = "flex";
  });
  const otpInputs = document.querySelectorAll(".otp-input");
  const refreshBtn = document.getElementById("resendBtn");

  otpInputs.forEach((input, index) => {
    input.addEventListener("input", (e) => {
      if (e.inputType === "deleteContentBackward" && index > 0) {
        otpInputs[index - 1].focus();
      } else if (index < otpInputs.length - 1) {
        otpInputs[index + 1].focus();
      }
      const allInputsFilled = Array.from(otpInputs).every(
        (input) => input.value.trim() !== ""
      );
      if (allInputsFilled) {
        // Gather OTP from inputs
        const otp = Array.from(otpInputs).map((input) => input.value.trim()).join('');
        var email = signUpUsername.value.trim();
        // var work_email = signUpUserEmail.value.trim();
        var password = signUpPasswordInput.value.trim();

        // Make API call to validate OTP
        fetch(`${Appconfig.LOCALHOST}:${Appconfig.APP_PORT}/validate_otp`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ 'otp':otp,'email':email,'password':password }),
        })
          .then(response => {
            if (response.ok) {
              return response.json();
            } else {
              throw new Error('Failed to validate OTP');
            }
          })
          .then(data => {
            // Handle validation success (e.g., show success screen)
            setTimeout(() => {
              otpScreen.style.display = "none";
              signUpScreen.style.display = "none";
              successScreen.style.display = "flex";
            }, 1000);
          })
          .catch(error => {
            console.error('Error validating OTP:', error);
            // Handle validation error (e.g., show error message to the user)
          });
      }
    });
  });

  refreshBtn.addEventListener("click", () => {
    otpInputs.forEach((input, index) => {
      input.value = "";
    });
  });