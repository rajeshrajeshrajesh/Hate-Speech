function analyzeText() {
    let text = document.getElementById("textInput").value;

    if (!text) {
        document.getElementById("result").innerText = "Please enter some text.";
        return;
    }

    fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ text: text })
})

    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Prediction: " + data.prediction;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error connecting to server.";
    });
}
