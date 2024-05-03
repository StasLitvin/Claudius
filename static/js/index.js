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
                e.target.value = "Заполните поле!";
            }
        });
    }
    pass.addEventListener('blur', e => {
        if (!e.target.value) {
            e.target.classList.add('password--invalid')
            e.target.setAttribute('type', 'text')
            e.target.value = 'Заполните поле!'
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

function togglePassword() {
	var passwordField = document.getElementById("password");
	var passwordToggle = document.getElementById("password-toggle");
	if (passwordField.type === "password") {
	  passwordField.type = "text";
	  passwordToggle.querySelector("img").src = "../static/img/eye-close.svg";
	} else {
	  passwordField.type = "password";
	  passwordToggle.querySelector("img").src = "../static/img/eye-open.svg";
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
progressBtn.addEventListener('click', ()=> {progressBtn.classList.toggle('active') ;progress.forEach(i => {i.classList.toggle('active')})});
const tableBtn = document.querySelector('#table');
const table = document.querySelectorAll('#table1');
tableBtn.addEventListener('click', ()=> table.forEach(i => i.hidden = !i.hidden));

function clik_arrow(id){
    if (document.getElementById(String(id)+"p").hidden===true) {
        document.getElementById(String(id)+"p").hidden=false
        document.getElementById(String(id)+"s").style="transform: rotate(0deg)"
    }
    else {
        document.getElementById(String(id)+"p").hidden=true
        document.getElementById(String(id)+"s").style="transform: rotate(180deg)"
    }

}
function closee(id){
    if (document.getElementById(String(id)+"s").style.display==="block") {
        document.getElementById(String(id)+"s").style.display="none"
        document.getElementById(String(id)+"c").style.display="block"
    }
    else {
        document.getElementById(String(id)+"s").style.display="block"
        document.getElementById(String(id)+"c").style.display="none"
    }

}
function submit_message(message) {
        $.post( "/send_message", {message: message}, handle_response);
        $.ajax({
        type: "POST", // Метод запроса
        url: "/send_message", // url запроса
        data: {                 // Параметры для запроса
            'id': messa,
        },
        success: function handle_response(response) {
          // append the bot repsonse to the div
          $('.chat-container').append(`
                <div class="chat-message col-md-5 offset-md-7 bot-message">
                    ${response.message}
                </div>
          `)
          // remove the loading indicator
          $( "#loading" ).remove();
        },
        error: function(response) { // Код который выполнится  при ошибке запроса
            console.log(response);
    }

});}
        function handle_response(data) {
          // append the bot repsonse to the div
          $('.chat-container').append(`
                <div class="chat-message col-md-5 offset-md-7 bot-message">
                    ${data.message}
                </div>
          `)
          // remove the loading indicator
          $( "#loading" ).remove();
    }   $('#target').on('submit', function(e){
        alert("asda")
        e.preventDefault();
        const input_message = $('#input_message').val()
        alert(input_message)
        // return if the user does not enter any text
        if (!input_message) {
          return
        }

        $('.chat-container').append(`
            <div class="chat-message col-md-5 human-message">
                ${input_message}
            </div>
        `)

        // loading
        $('.chat-container').append(`
            <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading">
                <b>...</b>
            </div>
        `)

        // clear the text input
        $('#input_message').val('')

        // send the message
        submit_message(input_message)
    });