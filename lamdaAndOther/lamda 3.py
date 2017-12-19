"""Описание лямда функции в нашей основной функции"""
def knights():
    title = "Sir"
    action = (lambda x: title + " " + x)
    return action

fun = knights()
print(fun("hero"))
