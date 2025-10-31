$(document).ready(function() {
  $(".messages").animate({ scrollTop: $(document).height() }, "fast");

  $("#profile-img").click(function () {
    $("#status-options").toggleClass("active");
  });

  $(".expand-button").click(function () {
    $("#profile").toggleClass("expanded");
    $("#contacts").toggleClass("expanded");
  });

  $("#status-options ul li").click(function () {
    $("#profile-img").removeClass();
    $("#status-online").removeClass("active");
    $("#status-away").removeClass("active");
    $("#status-busy").removeClass("active");
    $("#status-offline").removeClass("active");
    $(this).addClass("active");

    if ($("#status-online").hasClass("active")) {
      $("#profile-img").addClass("online");
    } else if ($("#status-away").hasClass("active")) {
      $("#profile-img").addClass("away");
    } else if ($("#status-busy").hasClass("active")) {
      $("#profile-img").addClass("busy");
    } else if ($("#status-offline").hasClass("active")) {
      $("#profile-img").addClass("offline");
    } else {
      $("#profile-img").removeClass();
    };

    $("#status-options").removeClass("active");
  });

  function newMessage() {
    message = $(".message-input input").val();
    if ($.trim(message) == '') {
      return false;
    }

    $('<li class="sent"><img src="https://avatars3.githubusercontent.com/u/30492527?s=460&v=4" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
    $.get("/get", { msg: message }).done(function (data) {
      $('<li class="replies"><img src="https://miro.medium.com/max/327/1*paQ7E6f2VyTKXHpR-aViFg.png" alt="" /><p>' + data + '</p></li>').appendTo($('.messages ul'));
    });
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
    $(".messages").animate({ scrollTop: $(document).height() }, "fast");
  };

  function getBotResponse() {
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
    $.get("/get", { msg: rawText }).done(function (data) {
      var botHtml = '<p class="replies"><span>' + data + "</span></p>";
      $("#chatbox").append(botHtml);
      document
        .getElementById("userInput")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    });
  }

  $('.submit').click(function () {
    newMessage();
  });

  $(window).on('keydown', function (e) {
    if (e.which == 13) {
      newMessage();
      return false;
    }
  });
});
