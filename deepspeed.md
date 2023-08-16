### DDP 
分布式训练过程： 
1. 一次训练开始时，PyTorch 通过分布式backend，将 rank 0 的模型参数广播到其他 rank，保证所有 rank 都有同样的初始状态
2. 模型训练时backward产生梯度，由于分布式训练数据并行时不同的训练 process 使用不同的数据（数据拆分）进行训练，这样每张卡上产生的梯度也是不同的。PyTorch 的分布式backend会借助集合通信库在所有训练 process 中进行梯度同步。
3. 更新梯度到本地的模型上，开始下一次forward-backward产生梯度-梯度同步-模型更新的迭代

### Deepspeed 
一种替代dp的训练推理方法，适用于大规模模型训练。DeepSpeed的核心在于，** gpu现存不够时，cpu内存来凑 **。  
具体来说，就是将当前时刻用不到的参数缓存到cpu内存中，等需要用到时再从cpu到gpu。这里的参数不仅指模型参数还包括优化器、梯度等。  
DeepSpeed的一个核心要点，就在于写一个config文件，即zero。  
ZeRO的实现方法，就是把参数占用，逻辑上分成三种类型。将这些类型的参数划分：  
* optimizer states：即优化器的参数状态。
* gradients：梯度缓存。
* parameters：模型参数。
