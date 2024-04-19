// Assuming you have a function that retrieves the response
function getResponse() {
    // Make a request to get the response
    let response = "This is the response from the AI";

    // Update the DOM with the response
    document.getElementById("response").innerText = response;
}

// Call the function when the page loads
window.onload = function() {
    getResponse();
};