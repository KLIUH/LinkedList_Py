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
    localStorage.setItem('customers', JSON.stringify(data))
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

document.getElementById("openSaveFile").addEventListener("click", function() {
    // Mở modal
    var saveFileModal = new bootstrap.Modal(document.getElementById('saveFileModal'));
    saveFileModal.show();
});

// Xử lý khi người dùng nhấn vào nút "Save" trong modal
document.getElementById("saveToFileBtn").addEventListener("click", function() {
    socket.send('2.4')
    const fileName = document.getElementById("fileName").value;
    // Xử lý lưu file ở đây
    console.log("File name:", fileName);
    // Đóng modal sau khi lưu xong
    const saveFileModal = bootstrap.Modal.getInstance(document.getElementById('saveFileModal'));
    saveFileModal.hide();
    socket.send(fileName)
});

document.getElementById("openSearchModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var searchModal = new bootstrap.Modal(document.getElementById('searchModal'));
    searchModal.show();
});

// Add click event listener to Search button in search modal
document.getElementById("submitSearch").addEventListener("click", function (event) {
    socket.send('2.5')
    // Get tcode input value
    var ccode = document.getElementById("searchCcode").value;

    // Close the modal
    var searchModal = bootstrap.Modal.getInstance(document.getElementById('searchModal'));
    searchModal.hide();
    socket.send(ccode)
});

document.getElementById("openDeleteModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
});

// Add click event listener to Delete button in delete modal
document.getElementById("submitDelete").addEventListener("click", function (event) {
    socket.send('2.6')
    // Get tcode input value
    var ccode = document.getElementById("deleteCcode").value;


    // Close the modal
    var deleteModal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
    deleteModal.hide();
    socket.send(ccode)
});