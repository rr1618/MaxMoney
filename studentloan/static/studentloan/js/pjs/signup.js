

$(document).ready(function(){
	$('#basicForm').submit(function(e){
			console.log("called");
			e.preventDefault();
			e.stopPropagation();
			$form = $(this)
			var formData = new FormData(this);
			$.ajax({
				url: '/studentloan/dashboard/basicForm',
				type: 'POST',
				data: formData,
				success: function (response) {
					$('.error').remove();
					console.log(response)
					if(response.error){
						$.each(response.errors, function(name, error){
							error = '<small class="text-muted error">' + error + '</small>'
							$form.find('[name=' + name + ']').after(error);
						})
					}
					else{
						// alert(response.message)
						$("#form1").animate({left: '300px', opacity: '0.1'},500,function(){
													$(this).hide()
													$(".thin").css('width','40%')
													$(".thick").css('width','50%')
													$("#selfieForm").fadeIn(800)
								});
					}
				},
				cache: false,
				contentType: false,
				processData: false
			});
		});
		// end
});

function open_webcam() {
	document.getElementById("results").style.display = "none";
	document.getElementById("open_camera").style.display = "none"; // hide camera button
	document.getElementById("capture").style.display = "block";   //show capture button
	document.getElementById("my_camera").style.display = "block";  //show camera box


	Webcam.set({
		width: 320,
		height: 240,
		image_format: 'jpeg',
		jpeg_quality: 90
	});
	Webcam.attach('#my_camera');
}
function take_snapshot() {
	document.getElementById("my_camera").style.display = "none";  //hide camera box
	document.getElementById("results").style.display = "block";
	// take snapshot and get image data
	//									document.getElementById("results").style.display="none";
	Webcam.snap(function (data_uri) {
		// display results in page
		document.getElementById('results').innerHTML =
			'<img  id="imageprev" src="' + data_uri + '" style="width:320px;height:240px;"/>';

	document.getElementById("capture").style.display = "none";
	document.getElementById("open_camera").style.display = "block";
	Webcam.reset();

});
}
function saveSnap(){
	// Get base64 value from <img id='imageprev'> source
	var base64image = $('#imageprev').attr('src')
	console.log("savesnap");
	$.ajax({
		data:{
			selfie : base64image,
		},
		type: "POST",
		url : '/studentloan/dashboard/submitSelfie/'
	})
	.done(function(data)
	{
		if(data.error){
			$(".thin").css('width','60%')
			$(".thick").css('width','75%')
			console.log("Something went wrong");
		}
		else {
			{
        window.location.href = '/studentloan/dashboard'
				console.log("Uploaded Successfully");
			}
		}
	});
}
