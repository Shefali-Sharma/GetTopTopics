// src="https://code.jquery.com/jquery-3.3.1.min.js"
// integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
// crossorigin="anonymous">

// $(document).ready(function() {
//   $('form').on('submit', function(event) {
//
//     $.ajax({
//       data : {
//         input : $('inputURL').val()
//       },
//       type : 'POST',
//       url: '/callback'
//
//     });
//
//
//     });
//
//     event.preventDefault();
//   });
// });

// $('button').click(function() {
// $.ajax({
//   url: '/callback',
//   type: 'POST'
// });
// });

//

// $("#search").click(function() {
//   // $("html").load("www.google.com");
// });

$('form').on('submit', function() {
  $('#errorAlert').text('hi').show();
  // $("html").load("www.google.com");
});
