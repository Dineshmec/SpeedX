

function addUser(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const email = document.getElementById("signUpUsername").value;
   // const email = document.getElementById("signUpUserEmail").value;
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
    const data = JSON.stringify({ email: email, password: password });
    xhr.send(data);
  }

  document.getElementById("signUpForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting normally
    addUser(event); // Call the addUser function
  });

  