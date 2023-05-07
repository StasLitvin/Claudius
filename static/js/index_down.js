$('input[type=file]').on('change', function () {
            let file = this.files[0];
            alert(file)
            $(this).next().html(file.name);
        });
function Rename(id){
    document.getElementById(id+id).textContent=document.getElementById(id).value.split(/(\\|\/)/g).pop();
}
let k=1;
let b=1;
        function set(id) {
            k+=1
            str="name"+ String(k)
            var as = '<div><input type="text" class="question" placeholder="Название задачи"><br> <input type="text" class="answer" placeholder="Неправильный ответ "><br> <input type="text" class="answer" placeholder="Правильный ответ"><br> <input type="text" class="answer" placeholder="Неправильный ответ "><br> <div class="answer"> <label class="input-file"> <input type="file" name="file" id='+str+' onchange="Rename(this.id)"> <span id='+str+str+' >Выберите файл задачи</span> </label><br> </div> </div>';
            var subject = document.querySelector("#" + id);
            subject.insertAdjacentHTML("beforebegin", as);

        }
        function set_lec(id){
            b+=1
            var as='<input type="text" class="question" placeholder="Название лекции">\n' +
                '                <label class="input-file">\n' +
                '                    <input type="file" name="file">\n' +
                '                    <span>Выберите файл лекции</span>\n' +
                '                </label>\n' +
                '                <div class="answer">\n' +
                '                    <input type="text" class="question" placeholder="Название задачи"><br>\n' +
                '                    <input type="text" class="answer" placeholder="Неправильный ответ "><br>\n' +
                '                    <input type="text" class="answer" placeholder="Правильный ответ"><br>\n' +
                '                    <input type="text" class="answer" placeholder="Неправильный ответ "><br>\n' +
                '                    <div class="answer">\n' +
                '                        <label class="input-file">\n' +
                '                            <input type="file" name="file">\n' +
                '                            <span>Выберите файл задачи</span>\n' +
                '                        </label><br>\n' +
                '                 </div>\n' +
                '\n' +
                '                </div>\n' +
                '                    <div class="answer">\n' +
                '                        <div class="answer" id="but'+String(b)+'">\n' +
                '                        <button type="button" class="border-button"  value="but'+String(b)+'"\n' +
                '                                onclick="set(this.value)">+ Добавить задачу\n' +
                '                        </button>\n' +
                '                    </div>\n' +
                '                        </div>\n' +
                '\n' +
                '                <br>'
            var subject = document.querySelector("#" + id);
            subject.insertAdjacentHTML("beforebegin", as);
        }