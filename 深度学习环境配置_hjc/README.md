# 1.Pytorch和CUDA配置

## 1.cuda

**统一计算设备架构**(Compute Unified Device Architecture,CUDA)，由 NVIDIA 推出的并行计算平台和编程模型。 

GPU版本的CUDA

![image-20230322215118326](F:\大项目\git\Vcat_AI_virtual_pet\深度学习环境配置_hjc\README.assets\image-20230322215118326.png)

1. 首先先确定CUDA版本不能超过自身显卡版本，4080是12.1
2. 确定电脑python版本
   1. ![image-20230322215239182](F:\大项目\git\Vcat_AI_virtual_pet\深度学习环境配置_hjc\README.assets\image-20230322215239182.png)
3. 确定pytorch和cuda的对应关系：
   1. [Start Locally | PyTorch](https://pytorch.org/get-started/locally/)
   2. 使用conda安装:一定要有vpn
      1. ![image-20230322215809619](F:\大项目\git\Vcat_AI_virtual_pet\深度学习环境配置_hjc\README.assets\image-20230322215809619.png)