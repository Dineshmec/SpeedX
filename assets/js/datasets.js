document.addEventListener("DOMContentLoaded", function () {
    const useCasesLabel = document.getElementById('insurance');
    if (useCasesLabel) {
        useCasesLabel.addEventListener('click', function () {
            fetch(`${Appconfig.LOCALHOST}:${Appconfig.INSURANCE_PORT}/schema/techinsurance`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    
                    const useCasesList = document.getElementById('insurancetable');
                    useCasesList.innerHTML = '';
                    data.forEach(list => {
                        const li = document.createElement('li');
                        li.textContent = list;
                        li.setAttribute('id', list);
                        const table=list;
                        console.log(typeof(table))
                        li.setAttribute('onclick', `displayTable('${table}')`);
                        useCasesList.appendChild(li);
                    });
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        });
    } else {
        console.error("Element with ID 'usecases' not found.");
    }
});

function displayTable(table){
    console.log(table);
    const url = `${Appconfig.LOCALHOST}:${Appconfig.INSURANCE_PORT}/schema/techinsurance/${table}`;
    
        fetch(url)
        .then(response => response.json())
        .then(data => {
            const table = document.getElementById('schemaTable').getElementsByTagName('tbody')[0];
            while (table.firstChild) {
                table.removeChild(table.firstChild);
            }
            data.forEach(item => {
                let row = table.insertRow();
                let fieldName = row.insertCell(0);
                fieldName.innerHTML = item.Field;
                let fieldType = row.insertCell(1);
                fieldType.innerHTML = item.Type;
            });
        })
        .catch(error => console.error('Error fetching data:', error));
    }


document.addEventListener('DOMContentLoaded', (event) => {   
    const insurance=document.getElementById('insurance');
    const er=document.getElementById('er');
    const insuranceER=document.getElementById('insuranceER');
    const insurancetable=document.getElementById('insurancetable');
    const table=document.getElementById('table');
    
    insurance.addEventListener('click',()=>{
        console.log("success");
        er.setAttribute('src',`${Appconfig.LOCALHOST}:${Appconfig.WEB_RUN_PORT}/iframe/insurance.html`);
        insuranceER.setAttribute('href',`${Appconfig.LOCALHOST}:${Appconfig.WEB_RUN_PORT}/iframe/insurance.html`);
        console.log("success");
        er.style.display="block";
        table.style.display="none"
    })
    
    insurancetable.addEventListener('click',()=>{
        er.style.display="none";
        table.style.display="block"
    })

});