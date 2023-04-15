let count = 0;

document.addEventListener('DOMContentLoaded', function(){
	var item = localStorage.getItem('emotional-condition');
	document.getElementById("main-bottom-change-second").innerHTML = item;

	const root = document.querySelector(':root');

	if (item === "Интроверт") {
		document.getElementById("dop-content").innerHTML = "Information about your emotional condition. (Introvert)";
		root.style.setProperty('--header-1', '#70C6F9');
		root.style.setProperty('--header-2', '#B4F0FF');
		root.style.setProperty('--text-glow', '#B4F0FF');
		root.style.setProperty('--B-static', '#5087CD');
		root.style.setProperty('--PI-info-block', '#F8F5FE');
		root.style.setProperty('--PI-text-changing', '#012034');
		root.style.setProperty('--CI-main-block-1', '#B1D3FF');
		root.style.setProperty('--CI-main-block-2', '#B1D3FF');
		root.style.setProperty('--CI-changing', '#044368');
		root.style.setProperty('--CI-button', '#8CC5FF');
		document.getElementById("select").value="Интроверт";
	} else if (item === "Амбиверт") {
		document.getElementById("dop-content").innerHTML = "Information about your emotional condition. (Ambivert)";
		root.style.setProperty('--header-1', '#0C2A22');
		root.style.setProperty('--header-2', '#BABB8F');
		root.style.setProperty('--text-glow', '#BABB8F');
		root.style.setProperty('--B-static', '#0C2A22');
		root.style.setProperty('--PI-info-block', '#dad9bb');
		root.style.setProperty('--PI-text-changing', '#0C2A22');
		root.style.setProperty('--CI-main-block-1', '#359935');
		root.style.setProperty('--CI-main-block-2', '#87E251');
		root.style.setProperty('--CI-changing', '#0C2A22');
		root.style.setProperty('--CI-button', '#ACA878');
		document.getElementById("select").value="Амбиверт";
	} else if (item === "Экстраверт") {
		document.getElementById("dop-content").innerHTML = "Information about your emotional condition. (Ekstravert)";
		root.style.setProperty('--header-1', '#3F0B0F');
		root.style.setProperty('--header-2', '#90817C');
		root.style.setProperty('--text-glow', '#90817C');
		root.style.setProperty('--B-static', '#3F0B0F');
		root.style.setProperty('--PI-info-block', '#FEFAEF');
		root.style.setProperty('--PI-text-changing', '#3F0B0F');
		root.style.setProperty('--CI-main-block-1', '#ff9edb');
		root.style.setProperty('--CI-main-block-2', '#FDDFA3');
		root.style.setProperty('--CI-changing', '#3F0B0F');
		root.style.setProperty('--CI-button', '#3F0B0F');
		document.getElementById("select").value="Экстраверт";
	}

	var item1 = localStorage.getItem('PI-name-input');
	document.getElementById("PI-name-and-edit").innerHTML = item1;
});

function submitForm(){
	var select = document.getElementById("emotional-condition");
	var value = select.options[select.selectedIndex].value;
	localStorage.setItem('emotional-condition', value);

	localStorage.setItem('PI-name-input', document.getElementById("PI-name-input").value);
	document.getElementById("fio").value=document.getElementById("PI-name-input").value;
}

function edit() {
	count += 1;

	if (count % 2 === 1) {
		document.querySelector(".PI-name-input").style.visibility = "visible";
		document.querySelector(".PI-name-and-edit").style.visibility = "hidden";

		$(".PI-photo-img-input").addClass("dop");
		$(".main-bottom-change-first").addClass("dop");
		$(".main-bottom-change-second").addClass("dop");
		$(".PI-save-button").addClass("dop");

		document.querySelector(".PI-edit-button-block").style.visibility = "hidden";
		document.querySelector('.PI-photo-img').setAttribute('src', '#');

	} else {
		count = 0;

		document.querySelector(".PI-name-input").style.visibility = "hidden";
		document.querySelector(".PI-name-and-edit").style.visibility = "visible";

		$(".PI-photo-img-input").removeClass("dop");
		$(".main-bottom-change-first").removeClass("dop");
		$(".main-bottom-change-second").removeClass("dop");
		$(".PI-save-button").removeClass("dop");

		var e = document.getElementById("emotional-condition");
		var value = e.options[e.selectedIndex].value;
	}
}