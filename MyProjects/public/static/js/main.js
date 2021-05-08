
function login(){
    var username = document.getElementById('LoginEmail').value
    var password = document.getElementById('LoginPassword').value
    var csrf = document.getElementById('csrf').value


    if(username == '' && password ==''){
        alert('You have to enter both the fields')
    }

    var data = {
        'username':username,
        'password':password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' : csrf,
        },

        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
    })
}


function register(){
    var RegisterEmail = document.getElementById('RegisterEmail').value
    var RegisterName = document.getElementById('RegisterName').value
    var RegisterPassword = document.getElementById('RegisterPassword').value
    var RegisterConfirmPassword = document.getElementById('RegisterConfirmPassword').value
    var csrf = document.getElementById('csrf').value


    if(RegisterEmail == '' && RegisterName =='' && RegisterPassword =='' && RegisterConfirmPassword ==''){
        alert('You have to all the fields')
    }

    var data = {
        'RegisterEmail': RegisterEmail,
        'RegisterName':RegisterName,
        'RegisterPassword':RegisterPassword,
        'RegisterConfirmPassword':RegisterConfirmPassword
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' : csrf,
        },

        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
    })
}