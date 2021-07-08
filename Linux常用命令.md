# Linux 常用命令小记
#### /代表根目录，~代表用户的家目录  
每个用户都有家目录，也就是用户的个人目录，比如root用户的”家“目录就是/root,普通用户a的家目录就是/home/a
#### 解压
filename.zip的解压 unzip filename.zip  
filename.tar.gz的解压 tar -zxvf filename.tar.gz 
###### 自动识别压缩格式 
tar -xvf filename.tar.gz  
tar -xvf filename.tar.bz2    
tar -xvf filename.tar.xz  
tar -xvf filename.tar.Z  
tar --help 
#### 打包压缩  
打包成tar.gz格式压缩包 tar -zcvf filename.tar.gz /filename   
打包成.zip格式 zip -q -r filename.zip /filename
#### 远程拷贝  
scp -r local_folder remote_username@remote_ip:remote_folder    
scp /home/space/music/1.mp3 root@www.runoob.com:/home/root/others/music  
-r： 递归复制整个目录  
#### ssh远程连接（前提是在同一个局域网下）  
ssh username@ip_address  
#### 修改文件权限  
sudo chmod 777  data/ project/  
文件或目录的用户，有3种不同类型：文件所有者、群组用户、其他用户，所以，chmod 777中，三个数字7分别对应上面三种用户，权限值都为7。二进制的三位分别代表只读、只写、可执行    
-R : 对目前目录下的所有文件与子目录进行相同的权限变更(即以递归的方式逐个变更) 
chmod +x init.sh 赋予shell脚本执行权限  
#### U盘挂载  
 查看U盘 fdisk -l    
 挂载U盘  mount /dev/sdc1 /mnt  
 复制文件cp –r 源地址 目的地址  
 -r 指操作文件夹下的多个文件  
 卸载U盘 umount /dev/sd1  
#### 数据库导入 
sudo mysql -uroot -p database_name < input_name.sql    
#### 数据库导出 
sudo mysqldump -u root -p database_name > output_name.sql 
root登录加了密码，多个参数 -p 
#### 建立软链接（快捷方式） 
软链接： ln -s 源文件 目标文件  
硬链接： ln 源文件 目的文件  
#### 查看文件内容  
vi 文件名 #编辑方式查看，可修改  
cat 文件名 #显示全部文件内容  
more 文件名 #分页显示文件内容  
less 文件名 #与 more 相似，更好的是可以往前翻页  
tail 文件名 #仅查看尾部，可以指定行数，一个常用的参数 -f ，常用于查阅正在改变的日志文件  
head 文件名 #仅查看头部,还可以指定行数  
#### 查看进程    
ps -aux 显示所有包含其他使用者的行程  （-au 显示较详细的资讯）    
ps -ef | grep 进程关键字 例如ps -ef|grep vim   
ps -A 显示所有进程信息  
ps -u root  显示root进程用户的信息  
 
使一个命令在后台运行：一般都是使用 & 在命令结尾来让程序自动运行。(命令后可以不追加空格)  
#### kill杀死进程  
kill SIGNAL_VALUE PID
列出所有信号名称 kill -l  
先用ps查找进程，然后用kill杀掉 kill 3268
彻底杀死进程 kill –9 3268  
value 1 挂起进程   
value 15 发出终止信号  
value 17，19，23 停止进程  
#### 搜索文件  
find <指定目录> <指定条件> <指定动作> find / -name "string*"  
whereis 加参数与文件名,只能查二进制文件、说明文档，源文件等  
locate 只加文件名  
which 只能查可执行文件  

#### 查看用过的命令列表 history
#### 查看磁盘使用空间   
df -a 显示所有文件系统，-h 用人们可读的方式进行显示 df -ah 命令来查看磁盘剩余空间  
#### 查看网络连通状况 netstat
#### service服务
查看服务状态 service [servicename] status  
启动/停止/重启服务 service [servicename] [start|stop|restart]  
查看一个目录的大小du -sh [目录]  例如 du -sh tmp  
#### 查看各个进程的资源占用情况 top  
#### man <命令> 查看命令的详细使用手册
#### 清理屏幕  
clear
#### 进入root权限 sudo -s 退出root exit
#### 显示系统版本号等信息 uname -a
#### 查看目录与文件的磁盘占用 du   
-a 显示所有 -h 按k.M.GB显示
#### 查看端口 
netstat -an

#### 查看ubuntu版本
lsb_release -a  

#### 查看系统是32还是64位
getconf LONG_BIT  

#### 查询套件
rpm -a -q | grep mysql

#### TCPDUMP抓包
sudo tcpdump -i enp1s0 -w 保存的CAP文件.cap 
