import csv
class MessageAnalyzer():   

    users_stages = dict()
    users_info = dict()
    route = dict()

    def __init__(self):  
        pass

    def AddUser(self, id: str):
        self.users_stages[id] = '0'
        self.users_info[id] = ['', '', '']
        pass

    def UserIsHere(self, id: str):
        if (self.users_stages.get(id) == None):
            return False
        else:
            return True

    # CreateRouteInfo() заполняет словарь route, в котором Ключ - это строка "номер_тип_направление" (например "29_bus_forward"),
    # а Значения в словаре представляют из себя двумерный массив, где первый индекс - это номер остановки по порядку, а второй определённые её характеристики
    def CreateRouteInfo(self):
        routeFile = open('Viber/route.csv', newline='')
        routeReader = csv.reader(routeFile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for route in routeReader:
            i = 1
            id = route[0]
            type1 = route[1]
            name = route[2]
            subRoutFile = open('Viber/subroute.csv', newline='')
            subReader = csv.reader(subRoutFile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            for subRoute in subReader:
                if (subRoute[0] == id):
                    direction = ""
                    if (i == 1): 
                        direction = "forward"
                        i += 1
                    else: 
                        direction = "backward"
                    self.route["{0}_{1}_{2}".format(name, type1, direction)] = []
                    ostanovki = subRoute[2].split(',')
                    for ost in ostanovki:
                        stopFile = open('Viber/stop.csv', newline='')
                        stopReader = csv.reader(stopFile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                        for stop in stopReader:
                            if(ost == stop[0]): self.route["{0}_{1}_{2}".format(name, type1, direction)].append([stop[0], stop[1], stop[2]]) 
                        stopFile.close()
            subRoutFile.close()        
        routeFile.close()
        pass

    def CreateMessage(self, id: str, userMes):
        if (not(userMes._message_type == "text")):
            return 'Введите текстовое сообщение!'

        if (self.users_stages[id] == '0'):
            botMes = (
            'Выберите действиее (Отправте цифру)\n' +
            '1) Узнать время прибытия автобуса к заданной остановке'
            )
            self.users_stages[id] = '1'
            return botMes

        elif (self.users_stages[id] == '1'):
            if (userMes.text == '1'):
                botMes = (
                'Выберите тип траспорта: \n' +
                '1) Автобус \n' +
                '2) Трамвай\n' +
                '3) Троллейбус'
                )
                self.users_stages[id] = '2'
                return botMes
            else:
                botMes = (
                'Введите соответствующую цифру'
                )
                return botMes

        elif (self.users_stages[id] == '2'):
            if (userMes.text == '1' or userMes.text == '2' or userMes.text == '3'):
                if (userMes.text == '1'): self.users_info[id][0] = 'Автобус'
                if (userMes.text == '2'): self.users_info[id][0] = 'Трамвай'
                if (userMes.text == '3'): self.users_info[id][0] = 'Троллейбус'
                botMes = (
                'Укажите номер маршрута (Без лишних символов)'
                )
                self.users_stages[id] = '3'
                return botMes    
            else:
                botMes = (
                'Введите соответствующую цифру'
                )
                return botMes

        elif (self.users_stages[id] == '3'):
                    if (True):
                        self.users_info[id][1] = userMes.text
                        botMes = (
                        'Укажите остановку'
                        )
                        self.users_stages[id] = '4'
                        return botMes    
                    else:
                        botMes = (
                        'Введите соответствующую цифру'
                        )
                        return botMes

        elif (self.users_stages[id] == '4'):
                    if (True):
                        self.users_info[id][2] = userMes.text
                        botMes = (
                        'Время прибытия \'{0},№{1}\' на остановку \'{2}\':\n'.format(self.users_info[id][0], self.users_info[id][1], self.users_info[id][2]) +
                        '...'
                        )
                        self.users_stages[id] = 'end'
                        return botMes    
                    else:
                        botMes = (
                        'Введите соответствующую цифру'
                        )
                        return botMes                
        pass
