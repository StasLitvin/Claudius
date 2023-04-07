let rotation = 0;

function rotateImg() {
	rotation += 90;

	if (rotation % 180 === 0) {
		rotation = 0;

		document.querySelector("#imgScrollBar").style.transform = `rotate(0deg)`;
		$('#imgScrollBar').click(function () {
			$('.CI-content-box').animate({ scrollTop: 0}, 10);
		});
		$(".CI-content-box").removeClass("noScroll");
		document.querySelector(".scroller").style.visibility = "hidden";
		document.querySelector(".scrollbar").style.visibility = "hidden";
		document.querySelector(".scroller").style.top = "0";
	} else {
		document.querySelector("#imgScrollBar").style.transform = `rotate(90deg)`;
		$(".CI-content-box").addClass("noScroll");
		document.querySelector(".scroller").style.visibility = "visible";
		document.querySelector(".scrollbar").style.visibility = "visible";
	}
}