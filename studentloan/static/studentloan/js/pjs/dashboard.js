$(document).ready(function(){
	$("ul>li>a").click(function(){
		$("form").hide();
		$("table").hide();
		id = "#"+this.name
		console.log(id);
		$('.primnav').animate({width:"58px"});
		$('input.hamburger').prop('checked', false);
		$(id).show();
			
	});
	$("#id_borrow_amt,#id_borrow_month").blur(function () {
		var btime = $("#id_borrow_month").val();
		var pay=0;
		var bmoney = parseInt($("#id_borrow_amt").val());
		
		if(btime==1)
		{
			console.log("1");
			
			pay = bmoney + Math.round(bmoney*0.12);
		}

		else if(btime==2)
		{
			pay = bmoney + Math.round(bmoney*0.17);
		}
		else {
			pay = bmoney + Math.round(bmoney*0.25);
		}
		$("#pay").text(pay);
});

});
