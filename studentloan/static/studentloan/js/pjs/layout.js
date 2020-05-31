$(document).ready(function(){

    // ========== Username Availability ===================
    $("#id_username").blur(function () {
		$("#check").attr("class","float-left spinner-border text-primary")
		var username = $(this).val();
			console.log( $(this).val() );
	$.ajax({
		url: 'check_username/',
		data : {
			'username' : username,
		},
		dataType: 'json',
		success: function (data) {
          if (data.is_taken) {
						$("#pills-home-tab").attr("class","nav-link")
						$("#pills-profile-tab").attr("class","nav-link active")
						$("#check").attr("class","float-left fa fa-times-circle")
          }
					else{
						$("#check").attr("class"," float-left fa fa-check")
					}
        }
			});
		});
        // ========== Username Availability ===================

        // ========== SideNavigation animation ===================
    $('#hamburger').change(function(){
        var check = $('#hamburger').is(":checked");
        var widw = $(window).width();
        console.log("widw",widw);
        console.log("check",check);
        
         
        // console.log(wid);
        
        if(check){
            
            $('.navbar label').attr('class','fas fa-times fa-2x');
            if(widw <500)
            {
                console.log("less than 500");
                
                $('.sidenav').animate({width:"100vw"});
            }
            else{
                $('.sidenav').animate({width:"275px"});
            }	
            
        }
        else{
            $('.navbar label').attr('class','fas fa-bars fa-2x');
            
            console.log("else");
            
            $('.sidenav').animate({width:"58px"});
            
        }
        
    });
    // ========== SideNavigation animation ===================
});
