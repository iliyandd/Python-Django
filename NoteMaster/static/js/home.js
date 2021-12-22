const noteBox = document.getElementById("display_notes");
const titleBox = document.getElementById("note-title");
const contentBox = document.getElementById("display_content");
const saveButton = document.getElementById("save-button");

let lastClickedNoteRow = -1;
let noteContent = "", titleContent = "";


contentBox.addEventListener("input", function(){
    if(lastClickedNoteRow > -1){
        saveButton.classList.remove("not-visible");
        noteContent = contentBox.value;
    }
});

titleBox.addEventListener("input", function(){
    if(lastClickedNoteRow > -1){
        saveButton.classList.remove("not-visible");
        titleContent = titleBox.textContent;
    }
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
            titleBox.textContent = notes[i].title;
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
                    note_id: `${notes[i].id}`
                },
                success: function(){
                    if(lastClickedNoteRow === notes[i].id){
                        contentBox.value = "";
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
setInterval(displayNotes, 2000);
