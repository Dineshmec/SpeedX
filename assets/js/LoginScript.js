function login(event) {
  event.preventDefault(); // Prevent the form from submitting normally

  const email = document.getElementById("loginUserEmail").value;
  const password = document.getElementById("loginUserPassword").value;

  const xhr = new XMLHttpRequest();
  xhr.open("POST", `${Appconfig.LOCALHOST}:${Appconfig.APP_PORT}/login`, true); // Replace with your actual API endpoint for login
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        const response = JSON.parse(xhr.responseText);
        // alert(response.message);
        window.location.href = "dashboard.html"; // Redirect to the dashboard page
      } else {
        const errorResponse = JSON.parse(xhr.responseText);
        alert(errorResponse.error);
      }
    }
  };
  const data = JSON.stringify({ email: email, password: password });
  xhr.send(data);
}

// Function to handle updating password
function updatePassword() {
  const email = prompt("Please enter your email address:");
  if (email) {
    const newPassword = prompt("Please enter your new password:");
    if (newPassword) {
      const xhr = new XMLHttpRequest();
      xhr.open("POST", `${Appconfig.LOCALHOST}:${Appconfig.APP_PORT}/update_password`, true); // Replace with your actual API endpoint for updating password
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            alert(response.message);
          } else {
            const errorResponse = JSON.parse(xhr.responseText);
            alert(errorResponse.error);
          }
        }
      };
      const data = JSON.stringify({ email: email, new_password: newPassword });
      xhr.send(data);
    }
  }
}



// Event listener for login button
// Event listener for login button
document.getElementById("loginForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the form from submitting normally
  login(event); // Call the login function
});


// Event listener for Forget Your Password link
// Event listener for Forget Your Password link
document.getElementById("forgotPasswordLink").addEventListener("click", function (event) {
  event.preventDefault(); // Prevent the default behavior of the anchor tag
  updatePassword(); // Call the updatePassword function
});

// Event listener for Sign Up link

function togglePasswordVisibility() {
  const passwordInput = document.getElementById("loginUserPassword");
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    hideShowBtn.style.opacity = "0.5";
  } else {
    passwordInput.type = "password";
    hideShowBtn.style.opacity = "1";
  }
}

// SignUp page form validations.
const loginUserEmail = document.getElementById("loginUserEmail");
const loginUserPassword = document.getElementById("loginUserPassword");

function onLoginInSumbitHandle(eve) {
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
  const loginUserEmail_value = loginUserEmail.value.trim();
  const loginUserPassword_value = loginUserPassword.value.trim();

  if (loginUserEmail_value === "") {
    setErrorMessage(loginUserEmail, "Please Enter a Email");
  } else if (!isValidEmail(loginUserEmail_value)) {
    setErrorMessage(loginUserEmail, "Please Enter a 'Valid Email'");
    return false;
  } else {
    setSuccessMessage(loginUserEmail);
  }

  if (loginUserPassword_value === "") {
    setErrorMessage(loginUserPassword, "Please Enter a Password");
  } else {
    setSuccessMessage(loginUserPassword);
  }

  if (loginUserEmail_value && loginUserPassword_value) {
    document.forms["loginForm"].reset();
    location.href = "dashboard.html";
    // window.location("dashboard.html");
    // otpScreen.style.display = "flex";
    // signUpScreen.style.display = "none";
    // showEmailId.innerText = signUpUserEmail_value;
  }
}
