function validate()
{
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;
    if (username=="admin" && password=="123")
    {
        alert("login successful");

        window.open("http://127.0.0.1:5500/client_home-page.html");
      
        return false;
    }
    else 
    {
        alert("Invalid username or Password");
    }

}
