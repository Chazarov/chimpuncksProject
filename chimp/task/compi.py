import threading
import time

finished = False

class alive(threading.Thread):
    def run(self):
        timer=0
        while(True):
            timer+=1
            time.sleep(1)
            if (timer>4):
                print("Время ожидания истекло")
                exit(-1)
            if (finished==True):
                break


def checkTask(code, SIGN ,values, res):
    alive().start()

    code = code+"\n\nresult = "+SIGN + "(" + values + ")"
    global finished
    try:
        data = {}
        exec(code, data)

        if str(data['result']) == str(res):
            
            finished = True
            return "Задача выполнена"
        else:
            finished = True
            return "Задача не выполнена"

        
    except Exception as e:
        finished = True
        return "Ошибка при выполнении кода:"


