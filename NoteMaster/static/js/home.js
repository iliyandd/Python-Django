const noteBox = document.getElementById("display_notes");
const contentBox = document.getElementById("display_content");
let lastClickedNoteRow = -1;


function loadNotesContent(notes){
    const noteRows = document.getElementsByClassName("note-row");

    for(let i = 0;  i < noteRows.length; i++){
        noteRows[i].addEventListener("click", function(){
            const title = `~~~ ${notes[i].title} ~~~\n\n`;
            contentBox.innerHTML = title;
            contentBox.innerHTML += notes[i].content;

            lastClickedNoteRow = notes[i].id;
        });
    }
}


function loadDeleteButtons(notes){
    const deleteButtons = document.querySelectorAll(".del-button");

    for(let i = 0; i < deleteButtons.length; i++){

        deleteButtons[i].addEventListener("click", function(){
            console.log("Here 2");
            $.ajax({
                type: "POST",
                url: "/delete-note/",
                data: {
                    note_id: `${notes[i].id}`
                },
                success: function(){
                    if(lastClickedNoteRow == notes[i].id){
                        contentBox.innerHTML = "";
                    }
                },
                error: function(){
                    alert("Error with deletion of the note!");
                }
            });
        });
    }
}


function displayNotes(){
    $.ajax({
        type: "GET",
        url: "/display-notes/",
        success: (response) => {
            console.log("success", response);
            const notes = response.notes;
            
            noteBox.innerHTML = "";
            notes.forEach(note => {
                noteBox.innerHTML += `
                    <span class="note-row">
                        <span class="note">${note.title}</span>
                    </span>
                    <button class="note-button edit-button">Edit</button>
                    <button class="note-button del-button">Delete</button><br><br><br>
                `;
            });

            loadNotesContent(notes);
            loadDeleteButtons(notes);
        },
        error: (error) => {
            console.log("error", error);
        }
    });
}


// function calls...
displayNotes();
setInterval(displayNotes, 2000);
