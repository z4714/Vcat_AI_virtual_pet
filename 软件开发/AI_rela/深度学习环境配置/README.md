# 1.Pytorch和CUDA配置

## 1.cuda

**统一计算设备架构**(Compute Unified Device Architecture,CUDA)，由 NVIDIA 推出的并行计算平台和编程模型。 

GPU版本的CUDA

![image-20230322215118326](README.assets\image-20230322215118326.png)

1. 首先先确定CUDA版本不能超过自身显卡版本，4080是12.1
2. 确定电脑python版本
   1. ![image-20230322215239182](README.assets\image-20230322215239182.png)
3. 确定pytorch和cuda的对应关系：
   1. [Start Locally | PyTorch](https://pytorch.org/get-started/locally/)
   2. 使用conda安装:一定要有vpn
      1. ![image-20230322215809619](README.assets\image-20230322215809619.png)
      1. 这里选择CUDA 11.8

4. 安装CUDA和cuDNN

   1. CUDA看作是一个工作台，上面配有很多工具，如锤子、螺丝刀等。cuDNN是基于CUDA的深度学习GPU加速库，有了它才能在GPU上完成深度学习的计算。它就相当于工作的工具，比如它就是个扳手。但是CUDA这个工作台买来的时候，并没有送扳手。想要在CUDA上运行深度神经网络，就要安装cuDNN，就像你想要拧个螺帽就要把扳手买回来。这样才能使GPU进行深度神经网络的工作，工作速度相较CPU快很多。

   2. ![image-20230322235313262](README.assets\image-20230322235313262.png)

   3. 安装完成后，会提示Nsight Visual studio的整合情况，这里提示安装了vs2022版的，正是我们前面安装的VS版本，这样就能在vs2019里面做GPU方面的开发了

      1. ![image-20230323000956192](README.assets\image-20230323000956192.png)

      2. 安装成功

         ![image-20230323001209961](README.assets\image-20230323001209961.png)
   
      3. 下载cudnn
   
   4. 配置完成后在vs中创建cuda项目
   
   5. ![image-20230323004353444](README.assets\image-20230323004353444.png)
   
   6. 创建一个默认的数组相加的demo尝试运行![image-20230323004420637](README.assets\image-20230323004420637.png)
   
   7. ![image-20230323004502874](README.assets\image-20230323004502874.png)
   
   8. 配置成功

