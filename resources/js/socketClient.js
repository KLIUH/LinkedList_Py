const socket = new WebSocket("ws://localhost:8000");

socket.onopen = function (event) {
    console.log("WebSocket connection established.");
};

socket.onmessage = function (event) {
    console.log(event.data);
    const data = JSON.parse(event.data);
    console.log(data);

    if (data && data.type === "alert") {
        const message = data.message;
    
        const alertDiv = document.createElement('div');
        alertDiv.classList.add('alert', 'alert-success');
        alertDiv.setAttribute('role', 'alert');
        alertDiv.textContent = message;
    
        const firstElement = document.body.firstChild;
        document.body.insertBefore(alertDiv, firstElement);
    
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 3000);
    }
    

    if (data && Array.isArray(data)) {
        populateTable(data)
    }
}
