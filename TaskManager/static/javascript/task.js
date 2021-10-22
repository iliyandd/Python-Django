function task_delete(id, url)
{
    $.ajax({type: 'POST', 
    // Here, we define the used method to send data to the Django
    // views. Other values are possible as POST, GET, and other HTTP request methods.
        url: url,
    // This line is used to specify the URL that will process the request.
        data: {task: id},
    // The data property is used to define the data that will be sent with the AJAX request.
        dataType: 'json',
        success: task_delete_confirm,
        error: function () {alert('AJAX error.');}
    });
}

function task_delete_confirm(response)
{
    task_id = JSON.parse(response);
    // This line is in the function that receives the AJAX response when
    // the request was successful. This line allows deserializing the JSON
    // response returned by Django views.

    if(task.id > 0)
    {
        $('#task_' + task_id).remove();
        // This line will delete the <tr> tag containing the task we have just removed
    }
    else
    {
        alert('Error');
    }
}