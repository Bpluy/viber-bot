# viber-bot
Viber-бот, для выдачи по запросам сведений об остановочных пунктах (включая поиск), о типах транспортных средств и их маршрутах, о движении транспортных средств на карте или схеме маршрута.

Файл main.py отвечает за работу бота и должен быть размещён на удалённом сервере. 
При размещении и запуске бот не работает, поскольку необходимо подвязать webhook.
За установку webhook-а отвечает POST-запрос на сайт вайбера с привязкой данных из viber.json.

Информация о непосредственно боте:

  Account Name:   ITransBotTEST  
  Token:          4fe241c73de7dc0b-b7ec515681c531d7-65a29900ef6b1756

Команды для запуска:
  
  ngrok.exe http --host-header=rewrite localhost:ПОРТ
  
  curl -# -i -g -H "X-Viber-Auth-Token:4fe241c73de7dc0b-b7ec515681c531d7-65a29900ef6b1756" -d @viber.json -X POST https://chatapi.viber.com/pa/set_webhook -v
