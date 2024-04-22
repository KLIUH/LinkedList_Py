document.getElementById("loadFromFile").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link
    // Show the modal
    var fileModal = new bootstrap.Modal(document.getElementById('fileModal'));
    fileModal.show();
});

function submitFile() {
    socket.send('1.1');
    const fileInput = document.getElementById('fileInput');
    const filePath = fileInput.value;
    const fileName = filePath.replace(/^.*[\\\/]/, '');

    console.log("Đường dẫn của tệp tin: " + fileName);
    var fileModal = bootstrap.Modal.getInstance(document.getElementById('fileModal'));
    fileModal.hide();
    socket.send(fileName)
}

// Add click event listener to "Input & add to the head" dropdown item
document.getElementById("openInputModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var inputModal = new bootstrap.Modal(document.getElementById('inputModal'));
    inputModal.show();
    socket.send('1.2')
});

// Add click event listener to Submit button in input modal
document.getElementById("submitInput").addEventListener("click", function (event) {
    // Get form data
    const formData = new FormData(document.getElementById("inputForm"));

    const tcode = document.getElementById("tcode").value;
    const trainName = document.getElementById("trainName").value;
    const seat = document.getElementById("seat").value;
    const booked = document.getElementById("booked").value;
    const departTime = document.getElementById("departTime").value;
    const departPlace = document.getElementById("departPlace").value;
    const availableSeat = parseInt(seat) - parseInt(booked);

    const trainData = {
        tcode: tcode,
        tname: trainName,
        seat: seat,
        booked: booked,
        depart_time: departTime,
        depart_place: departPlace,
        available_seat: availableSeat
    };
    const jsonData = JSON.stringify(trainData);
    // Close the modal
    const inputModal = bootstrap.Modal.getInstance(document.getElementById('inputModal'));
    inputModal.hide();

    socket.send(jsonData)
});

// Add click event listener to "Search by tcode" dropdown item
document.getElementById("openSearchModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var searchModal = new bootstrap.Modal(document.getElementById('searchModal'));
    searchModal.show();
    socket.send('1.5')
});

// Add click event listener to Search button in search modal
document.getElementById("submitSearch").addEventListener("click", function (event) {
    // Get tcode input value
    var tcode = document.getElementById("searchTcode").value;

    // Close the modal
    var searchModal = bootstrap.Modal.getInstance(document.getElementById('searchModal'));
    searchModal.hide();
    socket.send(tcode)
});

// Add click event listener to "Delete by tcode" dropdown item
document.getElementById("openDeleteModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
    socket.send('1.6')
});

// Add click event listener to Delete button in delete modal
document.getElementById("submitDelete").addEventListener("click", function (event) {
    // Get tcode input value
    var tcode = document.getElementById("deleteTcode").value;


    // Close the modal
    var deleteModal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
    deleteModal.hide();
    socket.send(tcode)
});

// Add click event listener to "Add after position k" dropdown item
document.getElementById("openAddAfterModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var addAfterModal = new bootstrap.Modal(document.getElementById('addAfterModal'));
    addAfterModal.show();
    socket.send('1.8')
});

// Add click event listener to Submit button in add after modal
document.getElementById("submitAddAfter").addEventListener("click", function (event) {
    // Get input values
    const positionK = document.getElementById("positionK").value;
    const tcode = document.getElementById("tcodeK").value;
    const trainName = document.getElementById("trainNameK").value;
    const seat = document.getElementById("seatK").value;
    const booked = document.getElementById("bookedK").value;
    const departTime = document.getElementById("departTimeK").value;
    const departPlace = document.getElementById("departPlaceK").value;
    const availableSeat = parseInt(seat) - parseInt(booked);

    const trainData = {
        k: positionK,
        tcode: tcode,
        tname: trainName,
        seat: seat,
        booked: booked,
        depart_time: departTime,
        depart_place: departPlace,
        available_seat: availableSeat
    };
    const jsonData = JSON.stringify(trainData);

    // Close the modal
    const addAfterModal = bootstrap.Modal.getInstance(document.getElementById('addAfterModal'));
    addAfterModal.hide();
    console.log(jsonData);
    socket.send(jsonData)
});

// Add click event listener to "Delete the node before the node having tcode = xCode" dropdown item
document.getElementById("openDeleteBeforeModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var deleteBeforeModal = new bootstrap.Modal(document.getElementById('deleteBeforeModal'));
    deleteBeforeModal.show();
});

// Add click event listener to Submit button in delete before modal
document.getElementById("submitDeleteBefore").addEventListener("click", function (event) {
    socket.send('1.9')
    var xCode = document.getElementById("xCode").value;

    // Do something with the input value (e.g., delete the node before the node having tcode = xCode)

    // Close the modal
    var deleteBeforeModal = bootstrap.Modal.getInstance(document.getElementById('deleteBeforeModal'));
    deleteBeforeModal.hide();
    socket.send(xCode)
});

// Function to populate existing table with data
function populateTable(data) {
    var tableBody = document.getElementById("trainListTable").getElementsByTagName('tbody')[0];
    tableBody.innerHTML = ""; // Clear existing data

    data.forEach(function (item) {
        var row = document.createElement("tr");
        row.innerHTML = "<td>" + item.tcode + "</td>" +
            "<td>" + item.train_name + "</td>" +
            "<td>" + item.seat + "</td>" +
            "<td>" + item.booked + "</td>" +
            "<td>" + item.depart_time + "</td>" +
            "<td>" + item.depart_place + "</td>" +
            "<td>" + item.available_seat + "</td>";
        tableBody.appendChild(row);
    });
}

// Add click event listener to "Display data" dropdown item
document.getElementById("openDisplayDataModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    socket.send('1.3')
});
document.getElementById("openSaveFile").addEventListener("click", function() {
    // Mở modal
    var saveFileModal = new bootstrap.Modal(document.getElementById('saveFileModal'));
    saveFileModal.show();
});

// Xử lý khi người dùng nhấn vào nút "Save" trong modal
document.getElementById("saveToFileBtn").addEventListener("click", function() {
    socket.send('1.4')
    const fileName = document.getElementById("fileName").value;
    // Xử lý lưu file ở đây
    console.log("File name:", fileName);
    // Đóng modal sau khi lưu xong
    const saveFileModal = bootstrap.Modal.getInstance(document.getElementById('saveFileModal'));
    saveFileModal.hide();
    socket.send(fileName)
});




document.getElementById("openSortByTcode").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link
    socket.send('1.7')
});