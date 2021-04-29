# 安装python3.7并改为默认python  
sudo apt install python3.7 python3.7-dev python3.7-distutils  
sudo rm /usr/bin/python  
sudo ln -s /usr/bin/python3.7 /usr/bin/python  

# 安装pip3.7    
cd && mkdir -p tool/pip && \  
cd tool/pip && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
sudo python get-pip.py  
  
# 查看是否安装成功，正确会显示为python3.7    
pip --version  

# pip更换国内源    
sudo su  
mkdir ~/.pip  
cat > ~/.pip/pip.conf << EOF  
[global]  
trusted-host=mirrors.aliyun.com  
index-url=https://mirrors.aliyun.com/pypi/simple/  
EOF

sudo pip3.7 config set global.index-url https://mirrors.aliyun.com/pypi/simple/  
# 查看pip源  
pip config list  
