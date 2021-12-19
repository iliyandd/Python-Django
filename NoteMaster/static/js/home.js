const noteBox = document.getElementById("display_notes");
const contentBox = document.getElementById("display_content");


function prepareNotesContent(notes){
    var buttons = document.getElementsByClassName("note-row");

    for(let i = 0;  i < buttons.length; i++){
        buttons[i].onclick = () => {
            const title = `~~~ ${notes[i].title} ~~~\n\n`;
            contentBox.innerHTML = title;
            contentBox.innerHTML += notes[i].content;
        }
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
                    <button class="note-button">Edit</button>
                    <button class="note-button">Delete</button><br><br><br>
                `;
            });

            prepareNotesContent(notes);
        },
        error: (error) => {
            console.log("error", error);
        }
    })
}


// function calls...
displayNotes();
setInterval(displayNotes, 5000);
