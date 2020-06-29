function proceed() {
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/');
    form.style.display = 'hidden';
    document.body.appendChild(form)
    form.submit();
}

function GetImage()
{

        var x = document.getElementById("x").value; 
        var y = document.getElementById("y").value; 
        var z = document.getElementById("z").value; 
        var data={'x':x, 'y':y,"z":z};
        var xhr = new XMLHttpRequest();
        console.log("sending: ");
        console.log(data);
        xhr.open("post", "/", true);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

    // send the collected data as JSON
        xhr.send(JSON.stringify(data));

        xhr.onloadend = function () {
 
		
           
            var response=JSON.parse(xhr.response);
	if (response==null)
	{
		document.getElementById("search_result_label").innerText="Could not find any matching songs, please try again";
		console.log(response);
		document.getElementById("search_results_dropdown").innerHTML="";
		return;
	}
	 document.getElementById("search_result_label").innerText="Select a song from below";
		document.getElementById("search_results_dropdown").innerHTML="";
            response["result"].forEach(record => {
                var content='<option value="'+record+'">'+record+"</option>";
                document.getElementById("search_results_dropdown").innerHTML+=content;
            })
        }

    
}