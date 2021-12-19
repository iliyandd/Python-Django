
class NotesController
{
    constructor(){
        this.noteBox = document.getElementById("display_notes");
        this.contentBox = document.getElementById("display_content");
    }

    displayNotes(){
        $.ajax({
            type: "GET",
            url: "/display-notes/",
            success: (response) => {
                const notes = response.notes;
                
                this.noteBox.innerHTML = "";
                notes.forEach(note => {
                    this.noteBox.innerHTML += `
                        <span class="note-row">
                            <span class="note">${note.title}</span>
                        </span>
                        <button>Edit</button>
                        <button>Delete</button><br><br><br>
                    `;
                });
    
                this.prepareNotesContent(notes);
            },
            error: (error) => {
                console.log("error", error);
            }
        })
    }

    prepareNotesContent(notes){
        var buttons = document.getElementsByClassName("note-row");
    
        for(let i = 0;  i < buttons.length; i++){
            buttons[i].onclick = () => {
                const title = `~~~ ${notes[i].title} ~~~\n\n`;
                this.contentBox.innerHTML = title;
                this.contentBox.innerHTML += notes[i].content;
            }
        }
    }
}


// function calls...
const noteController = new NotesController();

noteController.displayNotes();
setInterval(noteController.displayNotes, 5000);
