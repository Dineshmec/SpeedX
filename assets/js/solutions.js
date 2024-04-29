 document.addEventListener("DOMContentLoaded", function () {
    const useCasesLabel = document.getElementById('usecases1');
    if (useCasesLabel) {
        useCasesLabel.addEventListener('click', function () {
            fetch(`${Appconfig.LOCALHOST}:${Appconfig.SOLUTION_PORT}/get_use_cases1`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    const useCasesList1 = document.getElementById('useCasesList1');
                    useCasesList1.innerHTML = '';
                    data.forEach(useCase => {
                        const li = document.createElement('li');
                        li.textContent = useCase.use_case_name;
                        li.setAttribute('id', useCase.UCID);
                        li.setAttribute('onclick', `displayContext1('${useCase.UCID}')`);
                        useCasesList1.appendChild(li);
                    });
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        });
    } else {
        console.error("Element with ID  not found.");
    }
});

function displayContext1(UCID){
          
          console.log(UCID);
          const iframe=document.getElementById('iframe');
          const visit=document.getElementById('visit');
          iframe.setAttribute('src',`${Appconfig.LOCALHOST}:${Appconfig.WEB_RUN_PORT}/iframe/${UCID}.html`);
          visit.setAttribute('href',`${Appconfig.LOCALHOST}:${Appconfig.WEB_RUN_PORT}/iframe/${UCID}.html`)
//     console.log(UCID)
//     const url = `http://127.0.0.1:5007/?UCID=${UCID}`;

// fetch(url)
//   .then(response => {
//     if (!response.ok) {
//       throw new Error('Network response was not ok');
//     }
//     return response.text(); 
//   })
//   .then(html => {
//     // Assuming you want to display the HTML content
//     document.getElementById('container').innerHTML = html;
//   })
//   .catch(error => {
//     console.error('There was a problem with the Fetch request:', error);
//   });
}
