// JavaScript Document

//ready
var socket = null;
var isopen = false;
var my_address = null;

$(document).ready(function(){

    $('.search-book button').bind('click', function(e){

        e.preventDefault();

        socket = new WebSocket("ws://127.0.0.1:9000");
        socket.binaryType = "arraybuffer";

        socket.onopen = function(){
            console.log('Connected!');
            isopen = true;
        }

        socket.onmessage = function(e){
//            if (typeof e.data == "string") {
//                if (e.data.indexOf('tcp')+1){
//                    console.log("Text message received: " + e.data);
//                    my_address = e.data;
//                } else {
//                    console.log("Text message received: " + e.data);
//                    $.ajax({
//                        url: "/"+e.data+"/",
//                        type: "GET",
//                        data: ({}),
//                        dataType: "html",
//                        success: function(data){
//                            $('div.result-images').html(data);
//                            console.log('Close!');
//                            socket.close();
//                        }
//                    });
//                }
//            }
        }

        socket.onclose = function(e){
            console.log("Connection closed.");
            socket = null;
            isopen = false;
        }

        var text = $('.search-book #id_text').val(),
            mail = $('.search-book #id_email').val();




    });

});