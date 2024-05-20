document.getElementById('register-btn').addEventListener('click',function(event){
    event.preventDefault();

    const username = document.getElementById('uname-reg').value;
    const email = document.getElementById('email').value; 
    const password = document.getElementById('pwd-reg').value;

    const formData = {
        username: username,
        email: email,
        password: password
    };

    fetch('http://127.0.0.1:5000/users/register',{
        method: 'POST',
        headers:{
            'Content-Type' : 'application/json'
         },

         body: JSON.stringify(formData)
    })
    .then(res => res.json())
    .then(data =>{
        if(data.success){
            document.getElementById('text').innerHTML = 'Post Created';
        }else{
            document.getElementById('text').innerHTML = 'Error';
            console.log(data)
        }
    })
});
