

(function($) {

	"use strict";


  // Form
	var contactForm = function() {
		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					name: "required",
					subject: "required",
					email: {
						required: true,
						email: true
					},
					message: {
						required: true,
						minlength: 5
					}
				},
				messages: {
					name: "Lütfen adınızı giriniz",
					subject: "Lütfen konuyu giriniz",
					email: "Lütfen mail adresinizi giriniz",
					message: "Lütfen mesajınızı giriniz"
				},
				

			});
		}
	};
	contactForm();

})(jQuery);
