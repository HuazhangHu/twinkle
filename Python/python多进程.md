### subprocess模块

### run()方法

```
process=subprocess.run(args,stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None) 
```

参数详情：args：表示要执行的命令。必须是一个字符串，字符串参数列表。  
stdout=subprocess.PIPE, #subprocess.PIPE 表示为子进程创建新的管道  
stderr=subprocess.STDOUT, #subprocess.STDOUT结果输出
shell=True# 将通过操作系统的shell执行指定的命令

```
result = process.stdout.read()#获取输出结果
```

### Popen()方法

##### Popen 是 subprocess的核心，子进程的创建和管理都靠它处理。  

```
p = subprocess.Popen('ls -l', shell=True)#参数和run()类似
```

### Popen 对象方法

- poll(): 检查进程是否终止，如果终止返回 returncode，否则返回 None。
- wait(timeout): 等待子进程终止。
- communicate(input,timeout): 和子进程交互，发送和读取数据。
- send_signal(singnal): 发送信号到子进程 。
- terminate(): 停止子进程,也就是发送SIGTERM信号到子进程。
- kill(): 杀死子进程。发送 SIGKILL 信号到子进程。

```
示例代码
process=subprocess.Popen('ls -l',stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)  
result = process.stdout.read()
```

