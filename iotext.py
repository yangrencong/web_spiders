"""
该程序利用了python3.6内部的asyncio实现协程
该程序实现了并发
"""
import time
import asyncio

now = lambda: time.time()


async def do_some_work(x):
    print("waiting", x)
    # await后面的就是调用耗时的操作
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(3)
    tasks = [
            asyncio.ensure_future(coroutine1),
            asyncio.ensure_future(coroutine2),
            asyncio.ensure_future(coroutine3)
            ]
    dones, pendings = await asyncio.wait(tasks)
    for task in tasks:
        print("Task ret:", task.result())


start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Time:", now()-start)
