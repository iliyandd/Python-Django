let notes  = [];
const noteBox = document.getElementById("display_notes");
const titleBox = document.getElementById("note-title");
const contentBox = document.getElementById("display_content");
const saveButton = document.getElementById("save-button");

let lastClickedNoteRow = -1;
let noteContent = "", titleContent = "";


[titleBox, contentBox].forEach(box => {
    box.addEventListener("input", function(){
        if(lastClickedNoteRow > -1){
            titleContent = titleBox.value;
            noteContent = contentBox.value;

            if(titleContent){
                saveButton.classList.remove("not-visible");
            }
            else{
                saveButton.classList.add("not-visible");
            }
        }
    });
});


saveButton.addEventListener("click", function(){
    $.ajax({
        type: "POST",
        url: "/edit-note/",
        data: {
            note_id: `${notes[lastClickedNoteRow].id}`,
            title: `${titleContent}`,
            content: `${noteContent}`
        },
        success: function(){
            notes[lastClickedNoteRow].title = `${titleContent}`;
            notes[lastClickedNoteRow].content = `${noteContent}`;
            setTimeout(saveButton.classList.add("not-visible"), 1000);
        },
        error: function(){
            alert("Error with deletion of the note!");
        }
    });
});


function loadNotesContent(){
    const noteRows = document.getElementsByClassName("note-row");

    for(let i = 0;  i < noteRows.length; i++){
        noteRows[i].addEventListener("click", function(){
            titleBox.value = notes[i].title;
            contentBox.value = notes[i].content;

            // lastClickedNoteRow = notes[i].id;
            lastClickedNoteRow = i;
            saveButton.classList.add("not-visible");
        });
    }
}


function loadDeleteButtons(){
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
                    notes.splice(i, 1);
                    if(lastClickedNoteRow === i){
                        contentBox.value = "";
                        titleBox.value = "";
                        lastClickedNoteRow = -1;
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
    if(notes.length > 0){
        titleBox.classList.remove("not-visible");
        contentBox.classList.remove("not-visible");

        noteBox.innerHTML = "";
        notes.forEach(note => {
        noteBox.innerHTML += `
            <span class="note-row">${note.title}</span>
            <button class="del-button">Delete</button><br><br><br>
            `;
        });

        loadNotesContent();
        loadDeleteButtons();
    }
    else{
        noteBox.innerHTML = "";
        titleBox.classList.add("not-visible");
        contentBox.classList.add("not-visible");
    }
}


function getNotes(){
    $.ajax({
        type: "GET",
        url: "/display-notes/",
        success: (response) => {
            notes = response.notes;
        },
        error: (error) => {
            console.log("error", error);
        }
    });
}



// function calls...

getNotes();
setInterval(displayNotes, 1000);
