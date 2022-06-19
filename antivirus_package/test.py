# def foo(bar, baz):
#     print(f"hello {bar}")
#     return "foo" + baz
#
# from multiprocessing.pool import ThreadPool
# pool = ThreadPool()
# async_result = pool.apply_async(foo, ("world", "foo"))
#
# return_val = async_result.get()
# print(return_val)
#
# import sys
# import time
# import threading
#
# from PyQt5 import QtWidgets, QtCore
#
#
# def thread(my_func):
#     """
#     Запускает функцию в отдельном потоке
#     """
#
#     def wrapper(*args, **kwargs):
#         my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
#         my_thread.start()
#
#     return wrapper
#
#
# @thread
# def processing(signal):
#     """
#     Эмулирует обработку (скачивание) каких-то данных
#     """
#     res = [i for i in 'hello']
#     time.sleep(5)
#     signal.emit(res)  # Посылаем сигнал в котором передаём полученные данные
#
#
# class MyWidget(QtWidgets.QWidget):
#     my_signal = QtCore.pyqtSignal(list, name='my_signal')
#
#     def __init__(self, parent=None):
#         super(MyWidget, self).__init__(parent)
#         self.mainLayout = QtWidgets.QHBoxLayout()
#         self.setLayout(self.mainLayout)
#
#         self.button = QtWidgets.QPushButton("Emit your signal!", self)
#         self.mainLayout.addWidget(self.button)
#
#         # При нажатии на кнопку запускаем обработку данных
#         self.button.clicked.connect(lambda: processing(self.my_signal))
#
#         # Обработчик сигнала
#         self.my_signal.connect(self.mySignalHandler, QtCore.Qt.QueuedConnection)
#
#     def mySignalHandler(self, data):  # Вызывается для обработки сигнала
#         print(data)
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWidget()
#     window.show()
#     app.exec_()
import threading
import time
import queue

q = queue.Queue()


def thread_func(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=(args, kwargs), name="my thread")
        thread.start()
    return wrapper

@thread_func
def test():
    print(111)
    time.sleep(5)
    q.put("Hello")
    return "hello"

print(q.get())