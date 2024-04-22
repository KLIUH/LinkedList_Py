document.getElementById("loadFromFile").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link
    // Show the modal
    var fileModal = new bootstrap.Modal(document.getElementById('fileModal'));
    fileModal.show();
});

function submitFile() {
    socket.send('2.1');
    const fileInput = document.getElementById('fileInput');
    const filePath = fileInput.value;
    const fileName = filePath.replace(/^.*[\\\/]/, '');

    console.log("Đường dẫn của tệp tin: " + fileName);
    var fileModal = bootstrap.Modal.getInstance(document.getElementById('fileModal'));
    fileModal.hide();
    socket.send(fileName)
}

function populateTable(data) {
    var tableBody = document.getElementById("customerListTable").getElementsByTagName('tbody')[0];
    tableBody.innerHTML = ""; // Clear existing data

    data.forEach(function (item) {
        var row = document.createElement("tr");
        row.innerHTML = "<td>" + item.ccode + "</td>" +
            "<td>" + item.name + "</td>" +
            "<td>" + item.phone + "</td>" 
        tableBody.appendChild(row);
    });
}

// Add click event listener to "Display data" dropdown item
document.getElementById("openDisplayDataModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    socket.send('2.3')
});

document.getElementById("openInputModal").addEventListener("click", function(event) {
    event.preventDefault(); // Ngăn chặn hành động mặc định của liên kết

    // Hiển thị modal
    var inputModal = new bootstrap.Modal(document.getElementById('inputModal'));
    inputModal.show();
});

document.getElementById("submitInput").addEventListener("click", function (event) {
    // Get form data
    socket.send('2.2')

    const ccode = document.getElementById("ccode").value;
    const name = document.getElementById("name").value;
    const phone = document.getElementById("phone").value;

    const cusData = {
        ccode,
        name,
        phone
    };
    const jsonData = JSON.stringify(cusData);
    // Close the modal
    const inputModal = bootstrap.Modal.getInstance(document.getElementById('inputModal'));
    inputModal.hide();

    console.log(jsonData);
    socket.send(jsonData)
});