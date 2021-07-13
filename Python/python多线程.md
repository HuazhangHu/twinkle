

# Python多线程  

Python中使用线程有两种方式：函数或者用类来包装线程对象。  

### 函数式  

调用 _thread 模块中的start_new_thread(func,func_args[])函数来产生新线程。python现在只支持_thread模块  

```
import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass
```

### 线程模块 

Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。  
_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。  
threading模块  
我们可以通过直接从 threading的Thread类继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：  

```
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        #线程初始化
        threading.Thread.__init__(self)
        self.threadID = threadID#thread类的属性
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程"
```

join()方法用于等待至所有线程中止再继续往下执行。他有个参数timout，用于设定等待时间。  

### 线程同步

线程的同步需要用到锁，需要用到threading模块的Lock()方法创建一个锁对象  

```
import threading
#创建一个锁对象
threadLock = threading.Lock()
#用acquire()方法获得锁
threadLock.acquire()
#用release()方法释放锁
threadLock.release()
```

### Python多线程的实质

Python代码的执行由Python虚拟机（解释器）来控制。Python在设计之初就考虑要在主循环中，同时只有一个线程在执行，就像单CPU的系统中运行多个进程那样，内存中可以存放多个程序，但任意时刻，只有一个程序在CPU中运行。同样地，虽然Python解释器可以运行多个线程，只有一个线程在解释器中运行。  

我们都知道，比方我有一个4核的CPU，那么这样一来，在单位时间内每个核只能跑一个线程，然后时间片轮转切换。但是Python不一样，它不管你有几个核，单位时间多个核只能跑一个线程，然后时间片轮转。看起来很不可思议？但是这就是GIL搞的鬼。任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以从根本上来说用python实现多线程实际上只占用了一个核的资源，无法实现多核利用。速度效率低下

[知乎：为什么python多线程是假的](https://www.zhihu.com/question/23474039)

解决方法：1、利用多进程  
[廖雪峰python多进程](https://www.liaoxuefeng.com/wiki/897692888725344/923056295693632)

