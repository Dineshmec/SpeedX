document.addEventListener("DOMContentLoaded", function () {
    const useCasesLabel = document.getElementById('aiusecases');
    if (useCasesLabel) {
        useCasesLabel.addEventListener('click', function () {
            fetch(`${Appconfig.LOCALHOST}:${Appconfig.MODEL_PORT}/get_aiuse_cases`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    const useCasesList = document.getElementById('AIuseCasesList');
                    useCasesList.innerHTML = '';
                    data.forEach(useCase => {
                        const li = document.createElement('li');
                        li.textContent = useCase.ai_use_case_name;
                        li.setAttribute('id', useCase.AI_ID);
                        li.setAttribute('onclick',`aiiframe('${useCase.notebook}')`)
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



function aiiframe(notebook){
const aiiframe=document.getElementById('aiiframe');
const webpage=document.getElementById('webpage');
const editor=document.getElementById('editor');
aiiframe.setAttribute('src',`/sources/html/${notebook}.html`);
webpage.setAttribute('href',`${Appconfig.LOCALHOST}:${Appconfig.WEB_RUN_PORT}/sources/html/${notebook}.html`);
editor.setAttribute('href',`https://jupyter.org/try-jupyter/lab/`);
}
