const noteBox = document.getElementById("display_notes");
const titleBox = document.getElementById("note-title");
const contentBox = document.getElementById("display_content");
const saveButton = document.getElementById("save-button");

let lastClickedNoteRow = -1;
let noteContent = "", titleContent = "";


[titleBox, contentBox].forEach(box => {
    box.addEventListener("input", function(){
        if(lastClickedNoteRow > -1){
            saveButton.classList.remove("not-visible");
            titleContent = titleBox.value;
            noteContent = contentBox.value;
        }
    });
});


saveButton.addEventListener("click", function(){
    $.ajax({
        type: "POST",
        url: "/edit-note/",
        data: {
            note_id: `${lastClickedNoteRow}`,
            title: `${titleContent}`,
            content: `${noteContent}`
        },
        success: function(){
            setTimeout(saveButton.classList.add("not-visible"), 1000);
        },
        error: function(){
            alert("Error with deletion of the note!");
        }
    });
});


function loadNotesContent(notes){
    const noteRows = document.getElementsByClassName("note-row");

    for(let i = 0;  i < noteRows.length; i++){
        noteRows[i].addEventListener("click", function(){
            titleBox.value = notes[i].title;
            contentBox.value = notes[i].content;

            lastClickedNoteRow = notes[i].id;
            saveButton.classList.add("not-visible");
        });
    }
}


function loadDeleteButtons(notes){
    const deleteButtons = document.querySelectorAll(".del-button");

    for(let i = 0; i < deleteButtons.length; i++){

        deleteButtons[i].addEventListener("click", function(){
            $.ajax({
                type: "POST",
                url: "/delete-note/",
                data: {
                    note_id: `${notes[i].id}`,
                },
                success: function(){
                    if(lastClickedNoteRow === notes[i].id){
                        contentBox.value = "";
                        titleBox.value = "";
                    }
                    lastClickedNoteRow = -1;
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
            const notes = response.notes;
            
            noteBox.innerHTML = "";
            notes.forEach(note => {
                noteBox.innerHTML += `
                    <span class="note-row">${note.title}</span>
                    <button class="del-button">Delete</button><br><br><br>
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
setInterval(displayNotes, 1000);
