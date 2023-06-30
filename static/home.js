(function() {
  window.addEventListener("load", initialize)
  //used to ensure the user selected a file.

  function initialize() {
    document.getElementById("uploadForm").addEventListener("submit", validate);
  }

  function validate() {
    valid = true;

    var fileInput = document.querySelector(".select");
      if (fileInput.files.length === 0) {
        alert("Please select a file before uploading.");
        event.preventDefault();  // stop form from submitting
      }

    return valid;
  }
})();
