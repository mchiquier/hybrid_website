
function updateTextInput(val) {
    document.getElementById('textInput').value=val;
    console.log("SET")
    console.log(document.getElementById('textInput').value) 
  }


function updateTextInput2(val) {
    document.getElementById('textInput2').value=val; 
  }

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#highpass')
                .attr('src', e.target.result)
                .width(200)
                .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function setCookie(cname='', exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    var highpassimg = document.getElementById("highpass").src;
    highpassimg = highpassimg.split("images/")[1]
    var lowpassimg = document.getElementById("lowpass").src;
    lowpassimg = lowpassimg.split("images/")[1] 
    var highthresh = document.getElementById("textInput").value;
    var lowthresh = document.getElementById("textInput2").value;
    console.log(highpassimg);
    console.log("low");
    document.cookie = cname + highpassimg + lowpassimg + "=" + highthresh + "+" + lowthresh + ";" + expires + ";path=/";
    console.log(document.cookie);
}

function deleteAllCookies() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
}

function toJson() {
    var cookies = document.cookie;
    var output = {};
cookie.split(/\s*;\s*/).forEach(function(pair) {
pair = pair.split(/\s*=\s*/);
output[pair[0]] = pair.splice(1).join('=');
});
document.getElementById('output').innerHTML = JSON.stringify(output,null,4);
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}


function checkCookie() {
    var username = getCookie("username");
    if (username != "") {
        alert("Welcome again " + username);
        document.cookie = username;
        console.log(document.cookie);
        console.log("what");
    } else {
        username = prompt("Please enter your name:", "");
        curr_username = username;
        if (username != "" && username != null) {
            document.cookie = username;
            console.log(document.cookie);
        }
    }
   
}

function readURL2(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#lowpass')
                .attr('src', e.target.result)
                .width(200)
                .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$( document ).ready(function(){
checkCookie();

$("form#data").submit(function(e) {

    var formData = new FormData($(this)[0]);   
    var form = $(this);
    var url = form.attr('action');

    $.ajax({
           type: "POST",
           url: "process",
           data: formData,
           contentType: false,
           processData : false,
           success: function(data)
           {
               console.log("Changing src to" + data);
               document.getElementById("result-image").src = data;
               document.getElementById("result-image2").src = data;
               console.log("Changed src to" + data);        
               $("size").css({'width':'120px' , 'height':'120px'});               
           }
         });
    e.preventDefault(); // avoid to execute the actual submit of the form.
    setCookie('',250);
});

$("#final").click(function(e) {
    console.log("a=" + document.cookie);
    console.log("this is in finalize above");
    $.ajax({
           type: "GET",
           url: "final_submission",
           data: "a=" + document.cookie,
           contentType: false,
           processData : false,
           success: function(data)
           {             
           }
         });
    // because its not a submit item we dont need to do e.preventDefault();
    //deleteCookie();
});

}); 
