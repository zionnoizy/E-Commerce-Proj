


var roomName = {{ room_name }};
var wsStart = 'ws://'

var chatSocket = new WebSocket(
    wsStart + window.location.host + '/ws/chat/' + roomName + '/');


chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];

    document.querySelector('#chat-log').value += (message + " " + data.username + '\n');
    console.log('message: '+ message)
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
    console.log('close')
};

chatSocket.onopen = function(e) {
  console.log("open", e)
  var msgText =
}

chatSocket.onerror = function(e) {
  console.log("error", e)
}
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};
document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    console.log('send:')
    messageInputDom.value = '';
};
