let backButton;
let nextButton;
let finishButton;


let testContainer = document.querySelector(".another-question");
testContainer.addEventListener("click", (event) => {
  const target = event.target.closest("form[data-role]");
  
  
  if (!target) return; // Не обрабатываем, если не нашли нужный элемент
        
  const role = target.getAttribute("data-role");

  console.log(event.target)
  if (role === "back") {
    backButton = document.querySelector("#back_but");
    if (backButton) {
      rememberSelectedAnswer(getCheckedRadioButtonValue());
    }
  } else if (role === "next") {
    nextButton = document.querySelector("#next_but");
    if (nextButton) {
      rememberSelectedAnswer(getCheckedRadioButtonValue());
    }
  } else if (role === "send") {
    finishButton = document.querySelector("#finish_but");
    if (finishButton) {
      console.log(selectedAnswers);
      rememberSelectedAnswer(getCheckedRadioButtonValue());
      sendAnswersToServerandGetanswer()
    }
  }
});


//  Нужно определиться откуда нужно брать вопросы
 async function fetchTestData() {
   try {
     const response = await fetch("/get_test_data");
     const testData = await response.json();
     return testData;
   } catch (error) {
     console.error("Ошибка при получении данных теста:", error);
     return null;
   }
 }

function getCheckedRadioButtonValue() {
  if(!document.querySelector('input[name="radio"]:checked')) {
    console.error("Нужно выбрать один из ответов(По умолчанию выбирается НЕТ)")
    return "Нет"
  }
  let x = document.querySelector('input[name="radio"]:checked').value
  console.log(x);
  return x
}

let selectedAnswers = [];

// Функция загрузки сохраненных ответов из localStorage
function loadSelectedAnswers() {
  const savedAnswers = localStorage.getItem("selectedAnswers");
  if (savedAnswers) {
    selectedAnswers = JSON.parse(savedAnswers);
    console.log("Загруженные ответы:", selectedAnswers);
  }
}

// Функция сохранения ответов в localStorage
function saveSelectedAnswers() {
  localStorage.setItem("selectedAnswers", JSON.stringify(selectedAnswers));
  console.log("Ответы сохранены:", selectedAnswers);
}

// Функция удаления сохраненных ответов из localStorage
function clearSelectedAnswers() {
  localStorage.removeItem("selectedAnswers");
  console.log("Сохраненные ответы удалены");
}

// При выборе ответа сохраняем его и сохраняем в localStorage
function rememberSelectedAnswer(answer) {
  let result = document.querySelector(".questions-left").textContent.split("/")[0]; // будет сохранен в виде НОМЕР - ОТВЕТ
  
  let answerKey = result + " - " + answer;
  // проверям есть ли ответ на вопрос если есть заменяем в лучшем случае при получении вопроса сразу нужно автоматически это нужно сделать
  let existingIndex = selectedAnswers.findIndex(item => item.startsWith(result)); // ищем индекс существующего ответа

  if (existingIndex !== -1) {
    // Если ответ уже существует в массиве, заменяем его
    selectedAnswers[existingIndex] = answerKey;
  } else {
    // Если ответа нет в массиве, добавляем его
    selectedAnswers.push(answerKey);
  }

  console.log("Выбранные ответы:", selectedAnswers);
  saveSelectedAnswers();
}

// вот здесь нужно писать критерии оценивания
function checkAnswers(result) {
  selectedAnswers.sort()
  // for(let i = 0; < selectedAnswers.length; i++ ) {

  // }
}




// При завершении теста отправляем ответы на сервер и очищаем localStorage
function sendAnswersToServerandGetanswer() {


  // асинхронна не сработала так как другой js файл перехвативает раньше чем получим данные
  try {
    const response =  fetch("/submit_answers");
    const result = response.json();
    console.log("Ответ от сервера:", result);

    // Получили массив теперь сравниваем его

    checkAnswers(result);



    clearSelectedAnswers(); //очищаем localStorage
  } catch (error) {
    console.error("Ошибка при отправке ответов на сервер:", error);
  }
}

document.addEventListener("DOMContentLoaded", async function () {
loadSelectedAnswers(); // Загружаем сохраненные ответы при загрузке страницы
});
