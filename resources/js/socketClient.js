const socket = new WebSocket("ws://localhost:8000");

socket.onopen = function (event) {
    console.log("WebSocket connection established.");
};

socket.onmessage = function (event) {
    console.log(event.data);
    const data = JSON.parse(event.data);
    console.log(data);

    if (data && data.type !== undefined) {
        const message = data.message;
    
        const alertDiv = document.createElement('div');
        alertDiv.classList.add('alert', `alert-${data.type}`);
        alertDiv.setAttribute('role', 'alert');
        alertDiv.textContent = message;
    
        document.querySelector('.notice').appendChild(alertDiv);
    
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 3000);
    }
    

    if (data && Array.isArray(data)) {
        populateTable(data)
    }
}
