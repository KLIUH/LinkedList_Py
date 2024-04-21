document.getElementById("loadFromFile").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var fileModal = new bootstrap.Modal(document.getElementById('fileModal'));
    fileModal.show();
});

// Add click event listener to "Input & add to the head" dropdown item
document.getElementById("openInputModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var inputModal = new bootstrap.Modal(document.getElementById('inputModal'));
    inputModal.show();
});

// Add click event listener to Submit button in input modal
document.getElementById("submitInput").addEventListener("click", function (event) {
    // Get form data
    var formData = new FormData(document.getElementById("inputForm"));

    // Do something with form data (e.g., send it to server)

    // Close the modal
    var inputModal = bootstrap.Modal.getInstance(document.getElementById('inputModal'));
    inputModal.hide();
});

// Add click event listener to "Search by tcode" dropdown item
document.getElementById("openSearchModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var searchModal = new bootstrap.Modal(document.getElementById('searchModal'));
    searchModal.show();
});

// Add click event listener to Search button in search modal
document.getElementById("submitSearch").addEventListener("click", function (event) {
    // Get tcode input value
    var tcode = document.getElementById("searchTcode").value;

    // Do something with the tcode value (e.g., perform search)

    // Close the modal
    var searchModal = bootstrap.Modal.getInstance(document.getElementById('searchModal'));
    searchModal.hide();
});

// Add click event listener to "Delete by tcode" dropdown item
document.getElementById("openDeleteModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
});

// Add click event listener to Delete button in delete modal
document.getElementById("submitDelete").addEventListener("click", function (event) {
    // Get tcode input value
    var tcode = document.getElementById("deleteTcode").value;

    // Do something with the tcode value (e.g., perform deletion)

    // Close the modal
    var deleteModal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
    deleteModal.hide();
});

// Add click event listener to "Add after position k" dropdown item
document.getElementById("openAddAfterModal").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of link

    // Show the modal
    var addAfterModal = new bootstrap.Modal(document.getElementById('addAfterModal'));
    addAfterModal.show();
});

// Add click event listener to Submit button in add after modal
document.getElementById("submitAddAfter").addEventListener("click", function (event) {
    // Get input values
    var positionK = document.getElementById("positionK").value;
    var tcode = document.getElementById("tcode").value;
    var trainName = document.getElementById("trainName").value;
    var seat = document.getElementById("seat").value;
    var booked = document.getElementById("booked").value;
    var departTime = document.getElementById("departTime").value;
    var departPlace = document.getElementById("departPlace").value;
    var availableSeat = document.getElementById("availableSeat").value;

    // Do something with the input values (e.g., add after position k)

    // Close the modal
    var addAfterModal = bootstrap.Modal.getInstance(document.getElementById('addAfterModal'));
    addAfterModal.hide();
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
    // Get input value
    var xCode = document.getElementById("xCode").value;

    // Do something with the input value (e.g., delete the node before the node having tcode = xCode)

    // Close the modal
    var deleteBeforeModal = bootstrap.Modal.getInstance(document.getElementById('deleteBeforeModal'));
    deleteBeforeModal.hide();
});