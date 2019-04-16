var messageText = 'hii'

var container = $.find('.chat-online-users')[0]
var onlineUsers = $(container).children()
var messageInput = $('#msg_content')
var sendButton = $('#msg > div.col-xs-4.text-right.pdd-0-xs > a.btn.btn-chat-send.sendMsg')

onlineUsers.each(function (i, user) {
    user.click()
    messageInput.val(messageText)
    sendButton.click()
});