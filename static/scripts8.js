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
    alert("abc");

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
               alert(data); // show response from the php script.
               console.log("Changing src to" + data);
               document.getElementById("result-image").src = data;
               console.log("Changed src to" + data);
           }
         });

    

    e.preventDefault(); // avoid to execute the actual submit of the form.
});
}); 