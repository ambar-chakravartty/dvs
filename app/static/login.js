document.getElementById('login-btn').addEventListener('click', function (event){
    event.preventDefault()
    const username = document.getElementById('uname-login').value;
    const password = document.getElementById('pwd-login').value;

    const loginData = {
        username: username,
        password: password
    }

    fetch('http://127.0.0.1:5000/users/login',{
        method: 'POST',

        headers:{
            'Content-Type' : 'application/json'
        },

        body: JSON.stringify(loginData)
    })
    .then(res => res.json())
    .then(data => {
        localStorage.setItem('jwt',data.access_token)
    })
    .catch(error => {
        console.log(error);
    })

    
    

});


function logout() {
    localStorage.removeItem('jwt');
}
  
