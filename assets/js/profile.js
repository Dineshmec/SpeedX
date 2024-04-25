// profile Screen
function showSelectField(selectValue) {
    const select = document.getElementById(selectValue);
    select.classList.toggle("d-block");
}
function handleIndustry() {
    showSelectField("industrySelect");
}
const industrySelectOption =
    document.querySelectorAll(".industryOptions");
industrySelectOption.forEach((element) => {
    element.addEventListener("click", (event) => {
        const clickedOption = event.target.innerHTML;
        const selectField = document.querySelector(".selectField");
        selectField.innerHTML = clickedOption;
        event.stopPropagation();
        showSelectField("industrySelect");
        // console.log(clickedOption);
    });
});
const profile = document.querySelector(".profile");
const profilePop = document.getElementById("profilePop");
profile.addEventListener("click", (e) => {
    e.stopPropagation();
    profilePop.classList.toggle("d-block");
});
// toogle
function toggleBtn(event) {
    const normalLabel = document.getElementById("normalLabel");
    const expertLabel = document.getElementById("expertLabel");

    if (event.target.checked) {
        normalLabel.classList.remove("activeClass");
        expertLabel.classList.add("activeClass");
    } else {
        expertLabel.classList.remove("activeClass");
        normalLabel.classList.add("activeClass");
    }
}
window.onclick = function (event) {
    if (!event.target.matches("#profilePop")) {
        profilePop.classList.remove("d-block");
    }
    if (!event.target.closest("#selectIndustryId")) {
        document.getElementById("industrySelect").classList.remove("d-block");
    }

};


//edit screen
const profileScreen = document.querySelector("[data-profileScreen]");
const editScreen = document.querySelector("[data-editScreen]");
function navEditScreen() {
    profileScreen.classList.add("d-none");
    editScreen.classList.replace("d-none", "d-flex");
}
function navProfileScreen() {
    profileScreen.classList.remove("d-none");
    editScreen.classList.replace("d-flex", "d-none");
}

//image upload
document.getElementById('upload-input').addEventListener('change', function (event) {
    const imageElement = document.getElementById("showProfile");
    imageElement.src = "assets/images/profile/edit/defaultimg.webp";
    const file = event.target.files[0];
    if (file) {
        // event.target.value = '';
        const reader = new FileReader();
        reader.onload = function (e) {
            const imageUrl = e.target.result;
            imageElement.src = imageUrl;
        };
        reader.readAsDataURL(file);
    }
});
document.getElementById('upload-input').addEventListener('click', function (event) {
    event.target.value = '';
})

const AddBtn = document.querySelector("[data-work-experience]");
const dynamicInputWrapper = document.querySelector(".dynamicInputWrapper");
let count = 1;
let selectedDateRanges = [null];
AddBtn.addEventListener("click", () => {
    count++;

    const temp = `<hr class="dividerDot" />
     <div class="dynamicInputSection" data-group-id=${count}>
                    <div class="inputAndErrPart">
                      <label class="selectLabel" for="workRoleSelectBox">Role</label>
                       <select class="customSelectOption"  data-select-input data-input-name="Role"   data-formate="array">
                        <option hidden selected disabled value=" ">Please Select Role</option>
                        <option value="Data Scientist">Data Scientist</option>
                        <option value="Front End">Front End</option>
                        <option value="Back End">Back End</option>
                        <option value="FullStack">FullStack</option>
                      </select>
                      <span class="error_show"></span>
                    </div>
                    <div class="inputAndErrPart">
                      <input class="input textInput" id="workDomain1" type="text" placeholder=" " data-text-input data-validation-type="text" data-input-name="Domain" data-formate="array" />
                      <span class="error_show"></span>
                      <label class="label" for="workDomain1">Domain</label>
                    </div>
                    <div class="inputAndErrPart">
                      <input class="input textInput" id="workCompany" type="text" placeholder=" " data-text-input data-validation-type="text" data-input-name="Company" data-formate="array" />
                      <span class="error_show"></span>
                      <label class="label" for="workCompany">Company</label>
                    </div>
                    <div class="inputAndErrPart">
                      <input class="input dateInput workDateInput" id="workDateInput${count}" type="date" placeholder=" " data-text-input data-validation-type="date" data-input-name="Experience" data-formate="array" />
                      <span class="error_show"></span>
                      <label class="label" for="workDateInput${count}">Experience</label>
                    </div>
                  </div> `;
    dynamicInputWrapper.insertAdjacentHTML("beforeend", temp);
    dynamicDateInputInit();
    dynamicSelectInputInit();
});

//select skills checkbox
const skillsChecboxs = document.querySelectorAll(".skillsSelectCheckbox");
const skillLevelParentEle = document.querySelector("[data-skillLevelSection]");
skillsChecboxs.forEach((item) => {
    // console.log(item);
    item.addEventListener("change", (e) => {
        const inputName = (e.target.id).toLowerCase();
        const inputChecked = e.target.checked;
        const imgSrc = e.target.getAttribute("data-img-src");
        const titleText = e.target.getAttribute("data-title-text");
        if (inputChecked) {
            const temp = `  
                  <div class="skillLevelPart" data-${inputName}>
                        <div class="skillTitle">
                          <img
                            src="assets/images/profile/edit/${imgSrc}"
                            alt=${inputName}
                          />
                          <p>${titleText}</p>
                        </div>
                        <input  data-range-input
                          data-input-name="skillLevel"
                          data-skill-id="${inputName}" 
                          data-skill-name="${titleText}" 
                          class="rangeInputs"
                            type="range" 
                            min="0" 
                            max="100" />
                      </div>`;

            skillLevelParentEle.insertAdjacentHTML("beforeend", temp)
            // skillLevelParentEle.innerHTML += temp;
        } else {
            const skillLevelParentEle = document.querySelector("[data-skillLevelSection]");
            const removeEle = skillLevelParentEle.querySelector(`[data-${inputName}]`);
            removeEle.remove();
        }
    })
})

//chips input
function addChip() {
    var input = document.getElementById("textInput");
    var inputValue = input.value.trim();

    if (inputValue !== "") {
        var chipsContainer = document.getElementById("chipsContainer");
        var chip = document.createElement("div");
        chip.classList.add("chip");
        chip.textContent = inputValue;

        const imgClose = document.createElement("img");
        imgClose.classList.add("chip-close");
        imgClose.src = "assets/images/profile/edit/close.webp";
        imgClose.onclick = function () {
            chip.parentNode.removeChild(chip);
        };
        chip.appendChild(imgClose);
        chipsContainer.appendChild(chip);
        input.value = "";
    }
}

//live location 
const locationText = document.querySelector("#location");
function getLocation() {
    // Check for geolocation browser support and execute success method
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            geoLocationSuccess,
            geoLocationError,
            { timeout: 10000 }
        );
    } else {
        alert("Your browser doesn't support geolocation");
    }
}

function geoLocationSuccess(pos) {
    const myLat = pos.coords.latitude;
    const myLng = pos.coords.longitude;
    let loadingTimeout;

    const loading = function () {
        locationText.value = "Finding...";
    };
    loadingTimeout = setTimeout(loading, 600);

    fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${myLat}&lon=${myLng}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (loadingTimeout) {
                clearTimeout(loadingTimeout);
                loadingTimeout = null;
                locationText.value = data.address.city;
                console.log("data", data.address.city);
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function geoLocationError(error) {
    const errors = {
        1: "Permission denied",
        2: "Position unavailable",
        3: "Request timeout"
    };
    alert("Error: " + errors[error.code]);
}
const getLocationButton = document.getElementById("getLocationButton");
getLocationButton.addEventListener("click", getLocation);

//validation function
function onProfileSumbitHandle(eve) {
    eve.preventDefault();
    homeValidateInputs();
}

function setErrorMessage(input, error_message) {
    const inputControl = input.parentElement;
    const errorDisplay = inputControl.querySelector(".error_show");
    errorDisplay.innerText = error_message;
    inputControl.classList.add("error");
    inputControl.classList.remove("clear");
}

function setSuccessMessage(input) {
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
function isValidNumber(phoneno) {
    if (phoneno.length == 10) {
        return true;
    }
    else {
        return false;
    }
}
const experienceArr = [];
let dataArr = {};
const technologyExpertise = [];
function homeValidateInputs() {
    experienceArr.length = 0
    const textInput = document.querySelectorAll("[data-text-input]")
    const selectInput = document.querySelectorAll("[data-select-input]")
    const fileInput = document.querySelectorAll("[data-file-input]")
    const rangeInput = document.querySelectorAll("[data-range-input]")
    let setOne = true;
    let setTwo = true;
    let setthree = true;
    dataArr = {};

    textInput.forEach((item) => {
        const trimItem = item.value
        const inputName = item.getAttribute("data-input-name")
        const inputType = item.getAttribute("data-validation-type")
        const dataFormte = item.getAttribute("data-formate")
        // console.log(inputName);
        if (trimItem === "") {
            if (inputType == "text" || inputType == "phoneNumber") {
                setErrorMessage(item, `Please Enter a ${inputName}`);
                setOne = false;
            }
            if (inputType == "date") {
                setErrorMessage(item, `Please Select a ${inputName}`);
                setOne = false;
            }
        } else {
            setSuccessMessage(item);
            if (dataFormte == "array") {
                const indexNum = item.closest(".dynamicInputSection").getAttribute("data-group-id")

                const obj = { id: indexNum, [inputName]: trimItem };
                if (experienceArr.length >= 0) {
                    experienceArr.push(obj)
                }
            }
            else {
                dataArr = { ...dataArr, [inputName]: trimItem }
            }

        }
        if (inputType == "phoneNumber") {
            console.log(trimItem.length);
            if (!isValidNumber(trimItem)) {
                setErrorMessage(item, "Please Enter a 'Valid Number'");
                setOne = false;
                return false
            }
        }

    });

    selectInput.forEach((item) => {
        const trimItem = item.value
        const inputName = item.getAttribute("data-input-name")
        const dataFormte = item.getAttribute("data-formate")
        if (trimItem === " ") {
            setErrorMessage(item, `Please Select a ${inputName}`);
            setTwo = false;
        } else {
            setSuccessMessage(item);

            if (dataFormte == "array") {
                const indexNum = item.closest(".dynamicInputSection").getAttribute("data-group-id")
                const obj = { id: indexNum, [inputName]: trimItem };
                if (experienceArr.length >= 0) {
                    experienceArr.push(obj)
                }
            } else {
                dataArr = { ...dataArr, [inputName]: trimItem }
            }

        }

    });
    // fileInput
    fileInput.forEach((item) => {
        const trimItem = item.files[0];
        const inputName = item.getAttribute("data-input-name")
        // console.log("file-->", trimItem);
        if (!trimItem) {
            setErrorMessage(item, `Please Upload a ${inputName}`);
            setthree = false;
        } else {
            if (!trimItem.type.startsWith("image/")) {
                setErrorMessage(item, `Please Upload a Valid ${inputName}`);
                setthree = false;
            } else {
                setSuccessMessage(item);
                dataArr = { ...dataArr, [inputName]: trimItem }

            }
        }
    })

    rangeInput.forEach((item) => {
        const inputName = item.getAttribute("data-skill-name")
        const inputType = item.getAttribute("data-validation-type")
        console.log("rangeInput", item.value, inputName);
        // dataArr = { ...dataArr, technologyExpertise:  }
        // technologyExpertise.push();
    });

    const groupById = (data) => {
        const groupedData = {};
        data.forEach((item) => {
            if (!groupedData[item.id]) {
                groupedData[item.id] = [];
            }
            groupedData[item.id].push(item);
        });
        return Object.values(groupedData);
    };

    const transformedData = groupById(experienceArr);
    console.log("transformedData", transformedData);
    console.log("dataArr---->", dataArr);
    console.log(setOne,
        setTwo,
        setthree);
    if (setOne &&
        setTwo &&
        setthree) {
        // console.log("done")
        dataArr = { ...dataArr, workExperience: transformedData }
        // console.log("final---->", dataArr);
        navProfileScreen()
    }

}

//others
//custom select
$(document).ready(function () {
    dynamicDateInputInit();
    flatpickr(".brithdayDateInput", {
        dateFormat: "M d, Y",
    });
    $(".customSelectOption").select2({
        minimumResultsForSearch: Infinity,
    });
});
//custom Calender
function dynamicSelectInputInit() {
    $(".customSelectOption").select2({
        minimumResultsForSearch: Infinity,
    });
}

function dynamicDateInputInit() {
    const dateInputs = document.querySelectorAll(".workDateInput");
    dateInputs.forEach((input, index) => {
        flatpickr(input, {
            dateFormat: "Y-m-d", // Date format for input[type=date]
            mode: "range",
            defaultDate: selectedDateRanges[index], // Set the default date range
            onChange: function (selectedDates) {
                selectedDateRanges[index] = selectedDates; // Update selected date range for the input
            }
        });
    });
}
