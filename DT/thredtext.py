import _thread
import time
from time import sleep,ctime
#为该线程定义一个函数
def print_time(threadName ,delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName ,time.ctime())

_thread.start_new_thread(print_time ,("Thread_1" ,1))
_thread.start_new_thread(print_time ,("Thread_2" ,2))
print("Main Finish")
sleep(10)
