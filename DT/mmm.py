from multiprocessing import Process
import sys, os
import time


def timetask(times):
    time.sleep(times)
    print(time.localtime())


def works(func, arg, worknum):
    proc_record = []
    for i in range(worknum):
        p = Process(target=func, args=(arg,))
        p.start()
        proc_record.append(p)
    for p in proc_record:
        p.join()

    
if __name__ == '__main__':
    arg = 5
    procs = 4
    works(timetask, arg, procs)
