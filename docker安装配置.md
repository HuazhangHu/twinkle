### 卸载旧版本  
sudo apt-get remove docker docker-engine docker.io containerd runc  
### 添加Docker官方GPG key  
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
### 验证指纹  
sudo apt-key fingerprint 0EBFCD88  
### 添加稳定版repository 
sudo add-apt-repository \  
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
   $(lsb_release -cs) \  
   stable"   
### 安装最新版docker
sudo apt-get install docker-ce docker-ce-cli containerd.io  

### 查看docker版本  
docker --version  
  
