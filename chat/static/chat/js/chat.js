const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);
const receiver = JSON.parse(document.getElementById('json-username-receiver').textContent);
const avatar_receiver = JSON.parse(document.getElementById('json-avatar-receiver').textContent);
const avatar_sender = JSON.parse(document.getElementById('json-avatar-sender').textContent);

const chatSocket = new WebSocket(
    'ws://' + window.location.host +
    '/ws/chat/' + id + '/'
);

chatSocket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

chatSocket.onclose = function (e) {
    console.log("CONNECTION LOST");
}

chatSocket.onerror = function (e) {
    console.log("ERROR OCCURED");
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data);

    if (data.message) {
        let htmlUser = '<div class="chat-avatar">';

        if (data.username === message_username) {
            htmlUser += '<img src="' + avatar_sender + '" alt="Retail Admin">';
        } else {
            htmlUser += '<img src="' + avatar_receiver + '" alt="Retail Admin">';
        }

        htmlUser += '<div class="chat-name">' + data.username + '</div></div>';
        let htmlText = '<div class="chat-text">' + data.message + '</div>';
        let html = '';
        let liEl = document.createElement('li');

        if (data.username === message_username) {
            html = htmlText + htmlUser
            liEl.className = 'chat-right';
        } else {
            html = htmlUser + htmlText
            liEl.className = 'chat-left';
        }
        liEl.innerHTML += html

        document.querySelector('#chat-log').appendChild(liEl);
        scrollToBottom()
    } else {
        alert("The message was empty!")
    }
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': message_username,
    }));
    messageInputDom.value = '';
};

function scrollToBottom() {
    const objDiv = document.querySelector('#chat-log');
    objDiv.scrollTop = objDiv.scrollHeight;
}
scrollToBottom()