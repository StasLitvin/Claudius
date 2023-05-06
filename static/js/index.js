function myNewFunction(sel) {
    s = sel.options[sel.selectedIndex].text
    if (s == "Экстраверт") {
        document.getElementById("style_header_f").href = "../static/css/header_extr.css";
        document.getElementById("reset").href = "../static/css/reset_extr.css";
        document.getElementById("style").href = "../static/css/style_extr.css";

    }
    if (s == "Интроверт") {
        document.getElementById("style_header_f").href = "../static/css/header_intr.css";
        document.getElementById("reset").href = "../static/css/reset_intr.css";
        document.getElementById("style").href = "../static/css/style_intr.css";

    }
    if (s == "Амбиверт") {
        document.getElementById("style_header_f").href = "../static/css/header_ambr.css";
        document.getElementById("reset").href = "../static/css/reset_ambr.css";
        document.getElementById("style").href = "../static/css/style_ambr.css";

    }
}

/** 
* @description строка заглушка для поля пароля, когда поле пустое
*
*/
const defaultText = "Заполните поле!";

document.addEventListener('DOMContentLoaded', function () {
    let showPass = document.querySelector(".btns__show-password");
    let pass = document.querySelector(".password");
    let logins = document.querySelectorAll(".login");
    let form = document.querySelector('.form')
    let sogl = document.querySelector("input[name='sogl']");
    let submit = document.querySelector(".submit-btn");

    for (login of logins) {
        login.addEventListener("blur", (e) => {
            if (!e.target.value) {
                console.log(e.target.value);
                e.target.classList.add("login--invalid");
                e.target.value = defaultText
            }
        });
    }
    pass.addEventListener('blur', e => {
        if (!e.target.value) {
            e.target.classList.add('password--invalid')
            e.target.setAttribute('type', 'text')
            e.target.value = defaultText
        }
    })

        for (login of logins) {
            login.addEventListener("focus", (e) => {
                if (e.target.classList.contains("login--invalid")) {
                    e.target.value = "";
                    e.target.classList.remove("login--invalid");
                }
            });
        }
    pass.addEventListener('focus', e => {
        if (e.target.classList.contains('password--invalid')) {
            e.target.setAttribute('type', 'password')
            e.target.value = ''
            e.target.classList.remove('password--invalid')
        }
    })
        sogl.addEventListener("change", (e) => {
            console.log(e.target.checked);
            if (e.target.checked) {
                submit.disabled = false;
            } else {
                submit.disabled = true;
            }
        });

    form.addEventListener('submit', e => {
        e.preventDefault()

    })
    showPass.addEventListener('pointerup', (e) => {
        pass.setAttribute('type', 'password')
        e.target.classList.toggle('btns__show-password--open')
    })
    showPass.addEventListener('pointerdown', (e) => {
        pass.setAttribute('type', 'text')
        e.target.classList.toggle('btns__show-password--open')
    })
}, false);

/**
 * fix 
     * var говно, поменял на let
     * лучше сразу брать картинку как элемент, поместил картинку в eyeIcon
     * чтобы не было бага, меняю картинку когда когда поле непустое и значение не равно значению по default
     * разбил togglePassword на 2 функции
     * 
     */
/**
 * @description показывает пароль при событии onpointerdown
 */
const showPassword = () =>{
    let passwordField = document.getElementById("password");
    let eyeIcon = document.querySelector('.btns__img');
    if(passwordField.value && passwordField.value != defaultText){
        passwordField.type = "text";
        eyeIcon.src = "../static/img/eye-close.svg";
    }
    
 }
 /**
 * @description скрывает пароль при событии onpointerup
 *
 */
 const hidePassword = () =>{
    let passwordField = document.getElementById("password");
    let eyeIcon = document.querySelector('.btns__img');
    if(passwordField.value && passwordField.value != defaultText){
        passwordField.type = "password";
        eyeIcon.src = "../static/img/eye-open.svg";
    }
 }


function clearPlaceholder1(input) {
	input.placeholder = "";
 }

function addPlaceholder1(input, placeholder) {
	if (input.value === "") {
	  input.placeholder = placeholder;
	}
 }


const homeBtn= document.querySelector('#sidebar-btn');
const closeSidebar=document.querySelector('#closeSidebar')
const sidebar= document.querySelector('#sidebar');
homeBtn.addEventListener('click', () =>sidebar.hidden = false);
closeSidebar.addEventListener('click', () =>sidebar.hidden = true);
const progressBtn = document.querySelector('#progress-btn');
const progress = document.querySelectorAll('#progress');
progressBtn.addEventListener('click', ()=> progress.forEach(i => i.hidden = !i.hidden));
const tableBtn = document.querySelector('#table');
const table = document.querySelectorAll('#table1');
tableBtn.addEventListener('click', ()=> table.forEach(i => i.hidden = !i.hidden));
