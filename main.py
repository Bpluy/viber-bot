from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming():
	logger.debug("received request. post data: {0}".format(request.get_data()))
	# handle the request here
	return Response(status=200)

context = ('server.crt', 'server.key')
app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
bot_configuration = BotConfiguration(
	name='ITransBotTEST',
	avatar='',
	auth_token='4fe241c73de7dc0b-b7ec515681c531d7-65a29900ef6b1756'
)
viber = Api(bot_configuration)