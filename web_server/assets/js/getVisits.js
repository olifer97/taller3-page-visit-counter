$(document).ready(function(){ 
    var script = document.getElementById("getVisits");
    var url = script.getAttribute('counter-url');
    var key = script.getAttribute('key');
    $.getJSON( url + `?key=${key}`, function( data ) {
        $("#page-visits").text(data['visits']);
      });
 })