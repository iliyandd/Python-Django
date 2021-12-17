const noteBox = document.getElementById("display_notes");
 
const displayNotes = ()=>{
    $.ajax({
        type: "GET",
        url: "/display-notes/",
        success: function(response){
            const notes = response.notes;
            console.log("success", notes);

            noteBox.innerHTML = "";
            notes.forEach(note => {
                noteBox.innerHTML += `<p>${note.title}</p>`;
            });
        },
        error: function(error){
            console.log("error", error);
        }
    })
}

displayNotes();
setInterval(displayNotes, 5000);