// this code is just used for deleting the notes which we added
// and this is how we send a basic request to the backend from javascript  
function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}