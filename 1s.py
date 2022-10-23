#import enchant - потом момжет понадобится для исправления текста
import difflib

class MyClass():
    allTransport = ['троллейбус', 'трамвай', 'автобус'] 
    def Question(thisStr: str): #Запрос: *остановка*_*вид траспорта*_*номер*
        trKind = str(None)
        trNumb = str(None)
        place = str(None)
        strArr = thisStr.split(sep=' ')
        #Ищем вид транспорта
        kindCheck = False
        for i in strArr:
            if (kindCheck == True):
                break
            for j in MyClass.allTransport:
                if (difflib.SequenceMatcher(None, str(i.lower()), str(j)).ratio() > 0.75):
                    trKind = j
                    kindCheck = True
                    break
        #Ищем номер      
        if ((kindCheck == True) and (len(strArr) > 1)):
            index = strArr.index(trKind)
            if (index == 0):
                if(strArr[index + 1].isdigit() == True):
                    trNumb = str(strArr[index + 1])
            elif (index == len(strArr) - 1):
                 if(strArr[index - 1].isdigit() == True):
                    trNumb = str(strArr[index - 1])
            else:
                if(strArr[index + 1].isdigit() == True):
                    trNumb = str(strArr[index + 1])
                elif(strArr[index - 1].isdigit() == True):
                    trNumb = str(strArr[index - 1])
        #Ищем остановку
        if (not(trKind == None)):
            strArr.remove(trKind)
        if (not(trNumb == None)):
            strArr.remove(trNumb) 
        place = ' '.join(strArr) 
        #Вывод
        return "Ваш транспорт: {0}\nЕго номер: {1}\nОстановка: {2}".format(trKind, trNumb, place)

inStr = str(input())
outSTr = MyClass.Question(inStr)
print(outSTr)