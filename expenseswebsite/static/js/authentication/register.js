const usernameFIeld=document.querySelector('#usernameField');

usernameFIeld.addEventListener('keyup',()=> {console.log('777777',777777);



const usernameVal = e.target.value;
if(usernameVal.length >0){
fetch("/authentication/validate-username",{

body: JSON.stringify({username : usernameVal}),
method: "POST",

})
.then((res)=>res.json())
then((data) => {
    console.log("data",data)
});
}

});




