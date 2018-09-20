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
// $("form#data").submit(function(e) {
//     e.preventDefault();
//     var formData = new FormData(this);    

//     $.post('/process', formData, function(data) {
//         alert(data); // show response from the php script.
//         console.log("Changing src to" + data);
//         document.getElementById("result-image").src = data;
//         console.log("Changed src to" + data);
//     });
// });


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
               $("result-image2").css({'width':'120px' , 'height':'120px'});               
           }
         });

    

    e.preventDefault(); // avoid to execute the actual submit of the form.
});
}); 