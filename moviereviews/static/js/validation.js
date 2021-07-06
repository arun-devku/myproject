function validate() {
  
  var name= document.getElementById("name").value;
  var director= document.getElementById("director").value;
  var cast= document.getElementById("cast").value;
  var description=document.getElementById("description").value;
  var release=document.getElementById("release").value;
  var n = /^[+-]?((\.\d+)|(\d+(\.\d+)?))$/;
  var rating=document.getElementById("rating").value;
  
  var images= document.getElementById("images").value;
  if(name.trim()==""){
    document.getElementById("name").style.border="3px solid red";
    // name.style.border="3px solid red";
    status=0
  }
  else{
    document.getElementById("name").style.visibility="hidden";
    status=1
  }

  if(director.trim()==""){
    document.getElementById("director").style.border="3px solid red";
    status=0
  }
  else{
    document.getElementById("director").style.visibility="hidden";
    status=1
  }
  if(cast.trim()==""){
    document.getElementById("cast").style.border="3px solid red";
    // name.style.border="3px solid red";
    status=0
  }
  else{
    document.getElementById("cast").style.visibility="hidden";
    status=1
  }
  if(description.trim()==""){
    document.getElementById("description").style.border="3px solid red";
    status=0
  }
  else{
    document.getElementById("description").style.visibility="hidden";
    status=1
  }
  if(release.trim()==""){
    document.getElementById("release").style.border="3px solid red";
    status=0
  }
  else{
    document.getElementById("release").style.visibility="hidden";
    status=1
  }
  if(rating.trim()==""){
    document.getElementById("rating").style.border="3px solid red";
    status=0
  }
  else if(rating.match(!isNaN)) {
    document.getElementById("rating").style.border="3px solid red";
    status=0
  }
 
  else{
    document.getElementById("rating").style.visibility="hidden";
    status=1
  }
  
  if(images.trim()==""){
    document.getElementById("images").style.border="3px solid red";
    status=0
  }
  else{
    document.getElementById("images").style.visibility="hidden";
    status=1
  }
  if(status==1){
    return true;
}
else{
    return false;
}
}