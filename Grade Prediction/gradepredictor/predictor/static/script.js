function getCSRFToken() {
    return document.querySelector("[name=csrfmiddlewaretoken]").value;
}

document.getElementById("predict-form").addEventListener("submit", function(event) {
    event.preventDefault();

    let socioeconomic_score = document.getElementById("socioeconomic_score").value;
    let sleep_hours = document.getElementById("sleep_hours").value;
    let study_hours = document.getElementById("study_hours").value;
    let attendance = document.getElementById("attendance").value;

    let requestData = {
        socioeconomic_score: parseFloat(socioeconomic_score),
        sleep_hours: parseFloat(sleep_hours),
        study_hours: parseFloat(study_hours),
        attendance: parseFloat(attendance)
    };

    fetch("/predict/", {
        method: "POST",
        body: JSON.stringify(requestData),
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        if (data.predicted_grade !== undefined) {
            document.getElementById("result").innerHTML = `Predicted Grade: <b>${data.predicted_grade}</b>`;
        } else {
            document.getElementById("result").innerHTML = `<span style="color: red;">Error: ${data.error}</span>`;
        }
    })
    .catch(error => console.error("Error:", error));
});





