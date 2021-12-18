const noteBox = document.getElementById("display_notes");
const contentBox = document.getElementById("display_content");
 
const displayNotes = ()=>{
    $.ajax({
        type: "GET",
        url: "/display-notes/",
        success: function(response){
            const notes = response.notes;
            console.log("success", notes);

            noteBox.innerHTML = "";
            notes.forEach(note => {
                noteBox.innerHTML += `
                    <span class="note-row">
                        <span class="note">${note.title}</span>
                    </span>
                    <button>Edit</button>
                    <button>Delete</button><br><br><br>
                `;
            });

            var buttons = document.getElementsByClassName("note-row");
            for(let i = 0;  i < buttons.length; i++){
                buttons[i].onclick = () => {
                    const title = `~~~ ${notes[i].title} ~~~\n\n`;
                    contentBox.innerHTML = title;
                    contentBox.innerHTML += notes[i].content;
                }
            }
        },
        error: function(error){
            console.log("error", error);
        }
    })
}


displayNotes();
setInterval(displayNotes, 5000);