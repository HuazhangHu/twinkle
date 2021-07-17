# Docker基本原理

**学习资源：**菜鸟教程

https://blog.csdn.net/deng624796905/article/details/86493330

### 容器与虚拟机的差别

容器与主机共享宿主主机的硬件资源和操作系统，与其他容器共享操作系统内核；

虚拟机占用了分配给他的全部资源

**Docker 属于 Linux 容器的一种封装**

Linux 容器是 Linux 发展出了另一种虚拟化技术，Linux 容器不是模拟一个完整的操作系统，而是对进程进行隔离，相当于是在正常进程的外面套了一个保护层。对于容器里面的进程来说，它接触到的各种资源都是虚拟的，从而实现与底层系统的隔离。docker属于进程间的隔离。

### Docker的组成

1）image镜像

Docker 镜像可以看作是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）,只可读不可写

2）container容器

容器 (container) 的定义和镜像 (image) 几乎一模一样，也是一堆层的统一视角，唯一区别在于容器的最上面那一层是可读可写的。

容器=镜像+读写层

docker容器是docker镜像的运行实例。

3)Repository仓库

Docker仓库(Repository)是集中存放镜像文件的场所（Docker Hub）。Registry(仓库注册服务器)负责镜像的分发，类似于GitHub这样的托管服务，而Repository类似于git。

![Docker原理](https://github.com/957001934/twinkle/blob/main/photostore/docker%E5%8E%9F%E7%90%86.png)

### Docker的使用

(1)docker客户端连接到Docker守护进程。

(2)docker守护进程从Docker仓库Docker Hub中pull 程序镜像。

(3)docker守护进程从docker镜像中创建一个新的容器。

(4)docker守护进程输出给客户端。

Docker daemon守护进程是运行在服务器后台的组件，他帮助服务器完成交互分发等一系列动作

### 常用命令

Docker run images 通过一个镜像创建一个全新的容器并启用

Docker create images 创建容器但不启用

Docker attach containers 连接到正在运行的容器中

Docker images 查看本地保存的镜像列表

Docker kill containers 删除本地的容器

Docker pull images_name 从镜像源拉取镜像

Docker build path 用于从dockerfile中获取镜像

Docker ps -a 查看本地所有容器

Docker start 容器编号 启动容器