const allMessagesWrapper = document.getElementById("support__messages")
const sendBtn = document.getElementById('support__send-button');
const sendInput = document.getElementById('support__user-input')

sendBtn.addEventListener('click', function() {
  addNewMessages(sendInput.value);
});
async function addNewMessages() {
    inputValue=sendInput.value
    // Определяем функцию которая принимает в качестве параметров url и данные которые необходимо обработать:
const postData = async (url = '', data = {}) => {
  // Формируем запрос
  const response = await fetch(url, {
    // Метод, если не указывать, будет использоваться GET
    method: 'POST',
   // Заголовок запроса
    headers: {
      'Content-Type': 'application/json'
    },
    // Данные
    body: JSON.stringify(data)
  });
  return response.json();
}
postData('/send_message', { message: sendInput.value })
  .then((data) => {
    let supportMessageData = data["message"];
    createNewMyMessage(inputValue);
    createNewSupportMessage(supportMessageData);
  });
}

function createNewMyMessage(inputValue) {
    let myMessage = document.createElement('div');
    myMessage.className = "support__my-message";
    myMessage.innerHTML = `${inputValue}`;
    allMessagesWrapper.appendChild(myMessage);
}

function createNewSupportMessage(supportMessageData) {
    let div = document.createElement('div');
    div.className = "support__support-message";
    div.innerHTML = `${supportMessageData}`;
    allMessagesWrapper.appendChild(div);
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