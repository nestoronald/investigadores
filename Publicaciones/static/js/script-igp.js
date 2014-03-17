$(function(){
  $(".nav-sidebar a").click(function(e){
    $(".nav-sidebar li").removeClass("active");
    var iddiv= $(this).attr("href");
    var top_div = $(iddiv).offset().top;
    $('body,html').animate({scrollTop: top_div}, 500);

    $(this).parent("li").addClass("active");
    conte = $(this).attr("href")
    $(".reser").hide();
    $(conte).show();
  })

  // if (window.location.hash) {
  //     idconte = $('div '+window.location.hash);
  //     // href = $("a[href="+window.location.hash+"]")
  //     $("a[href="+window.location.hash+"]").click();
  //     idconte.show();
  // }
  // else{
  //     $(".reser a:first").click();
  // }

  // $( '.calendar' ).datepicker({
  //     showOn: 'button',
  //     buttonImage: './img/calendar.gif',
  //     buttonImageOnly: true,
  //     changeMonth: true,
  //     changeYear: true,
  //     dateFormat:'yy-mm-dd',
  //     //minDate: '-15Y', maxDate: '+1M +10D',
  //     yearRange: '-70:+0'
  // }).mask('9999-99-99');

  // var f = new Date();
  // dia =f.getDate();
  // mes =f.getMonth() +1;
  // if (dia <=9) {dia="0"+dia};
  // if (mes <=9) {mes="0"+mes};
  // console.log(f.getDate());
  // fx_today=f.getFullYear() + "-" + mes + "-" + dia;
  // $(".fx_today").val(fx_today);
  $(".login-home input").addClass("span12");
});

