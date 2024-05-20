document.getElementById('submit').addEventListener("click",function (event){
    event.preventDefault()
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;   
    const tags = document.getElementById('tags').value; 

    const formData = new FormData();

    const fileInput = document.getElementById('code').files;   
    for (let i = 0; i < fileInput.length; i++) {
      formData.append('files[]', fileInput[i]);
    }

    formData.append('title',title);
    formData.append('content',content);
    formData.append('tags',tags)
 

	for(item of formData){
		console.log(item[0],item[1]);
	}

    fetch('http://127.0.0.1:5000/posts/new',{
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
        },
        body: formData

    })
    .then(response => response.json())
    .then(data => {
        if(data.success){
            document.getElementById('text').innerHTML = 'Post Created';
        }else{
            document.getElementById('text').innerHTML = 'Error';
            console.log(data)
        }
    }).catch(error => {
        console.error(error)
        console.log("error logging in.")
    })

});

