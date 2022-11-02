from cgitb import text
from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import json
import module

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='ITransBotTEST',
    avatar='',
    auth_token='4fe241c73de7dc0b-b7ec515681c531d7-65a29900ef6b1756'
))

ma = module.MessageAnalyzer()

@app.route('/', methods=['POST'])
def incoming():
    #logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        global ma
        if (ma.UserIsHere(str(viber_request.sender.id)) == False):
            ma.AddUser(str(viber_request.sender.id))
        # lets echo back
        viber.send_messages(viber_request.sender.id, [TextMessage(text=ma.CreateMessage(str(viber_request.sender.id), message))])
        if (ma.users_stages[str(viber_request.sender.id)] == 'end'):
            ma.users_stages[str(viber_request.sender.id)] = '0'
            viber.send_messages(viber_request.sender.id, [TextMessage(text=ma.CreateMessage(str(viber_request.sender.id), message))])

    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])

    return Response(status=200)

if __name__ == "__main__":
    context = ('server.crt', 'server.key')
    app.run(port=8080)

# ngrok.exe http --host-header=rewrite localhost:8080
    


