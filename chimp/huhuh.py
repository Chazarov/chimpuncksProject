import subprocess
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

    try:
        data = {}
        exec(code, data)

        if str(data['result']) == str(res):
            print("Задача выполнена")
        else:
            print("Задача не выполнена")

        global finished
        finished = True
    except Exception as e:
        print("Ошибка при выполнении кода:", e)


code = """
def check(a,b):
    return(a+b)
"""
checkTask(code, "check","7,8","15")





