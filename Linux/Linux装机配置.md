#### 换源   
换源的话一定要注意ubuntu的版本和源的版本是否对的上
换源，为了方便把sources.list的内容放在公网服务器了      
cd /etc/apt  
sudo mv sources.list sources.list.bak  
sudo wget http://47.107.150.167:81/sources.list  
sudo apt update  

#### 安装python3.7并改为默认python 
sudo apt install python3.7 python3.7-dev python3.7-distutils    
sudo rm /usr/bin/python  
sudo ln -s /usr/bin/python3.7 /usr/bin/python    
 
#### 设置时区 
sudo timedatectl set-timezone Asia/Shanghai  
 
#### 安装pip  
mkdir -p tool/pip  
cd tool/pip    
wget https://bootstrap.pypa.io/get-pip.py   
sudo python get-pip.py    
  
#### 查看是否安装成功，正确会显示为python3.7    
pip --version  

#### pip更换国内源    
sudo su  
mkdir ~/.pip  
cat > ~/.pip/pip.conf << EOF  
[global]  
trusted-host=mirrors.aliyun.com  
index-url=https://mirrors.aliyun.com/pypi/simple/  
EOF

sudo pip3.7 config set global.index-url https://mirrors.aliyun.com/pypi/simple/  
##### 查看pip源  
pip config list  
#### 解决虚拟机突然上不了网
sudo service network-manager stop  

sudo rm /var/lib/NetworkManager/NetworkManager.state  

sudo service network-manager start  

##### Conda  
[conda安装](https://blog.csdn.net/qq_44173974/article/details/125336916)
conda env list  
source activate  
conda activate [env_name]  
conda deactivate  
conda install  
