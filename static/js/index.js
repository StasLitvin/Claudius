function myNewFunction(sel) {
    s = sel.options[sel.selectedIndex].text
    if (s == "Экстроверт") {
        document.getElementById("reset").href = "../static/css/reset_extr.css";
        document.getElementById("style").href = "../static/css/style_extr.css";
    }
    if (s == "Интроверт") {
        document.getElementById("reset").href = "../static/css/reset_intr.css";
        document.getElementById("style").href = "../static/css/style_intr.css";
    }
}

document.addEventListener('DOMContentLoaded', function () {
    let showPass = document.querySelector(".btns__show-password");
    let pass = document.querySelector(".password");
    let login = document.querySelector(".login");
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