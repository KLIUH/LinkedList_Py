// Add click event listener to "Input & add to the head" dropdown item
document.getElementById("openInputModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var inputModal = new bootstrap.Modal(document.getElementById('inputModal'));
    inputModal.show();
});

document.getElementById("submitInput").addEventListener("click", function (event) {
    // Get form data
    socket.send('3.1')

    const tcode = document.getElementById("tcode").value;
    const ccode = document.getElementById("ccode").value;
    const numSeats = document.getElementById("num_seats").value;

    const bookingData = {
        tcode,
        ccode,
        num_seats: numSeats
    };
    const jsonData = JSON.stringify(bookingData);
    // Close the modal
    const inputModal = bootstrap.Modal.getInstance(document.getElementById('inputModal'));
    inputModal.hide();

    console.log(jsonData);
    socket.send(jsonData)
});

function populateTable(data) {
    var tableBody = document.getElementById("customerListTable").getElementsByTagName('tbody')[0];
    tableBody.innerHTML = ""; // Clear existing data

    data.forEach(function (item) {
        var row = document.createElement("tr");
        row.innerHTML = "<td>" + item.tcode + "</td>" +
            "<td>" + item.ccode + "</td>" +
            "<td>" + item.num_seats + "</td>"
        tableBody.appendChild(row);
    });
}

// Add click event listener to "Display data" dropdown item
document.getElementById("openDisplayDataModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    socket.send('3.2')
});

document.getElementById('openSort').addEventListener('click', (e) => {
    e.preventDefault();

    socket.send('3.3')
})