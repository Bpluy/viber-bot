from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

app = Flask(__name__)
# сюда нужно вставить инфу со своего бота
viber = Api(BotConfiguration(
    name='ITransBotTEST',
    avatar='http://site.com/avatar.jpg',
    auth_token='4fe241c73de7dc0b-b7ec515681c531d7-65a29900ef6b1756'
))
viber.set_webhook('https://bot-testj.herokuapp.com:443/')
