# 深度学习 学习笔记



## 目录

- [简介](#简介)

- [安装指南](#安装指南)

- [笔记结构](#笔记结构)

- [学习资源](#学习资源)

- [进度记录](#进度记录)

  

## 简介

​	欢迎来到我的机器学习学习笔记仓库！本仓库主要记录我在学习机器学习过程中所整理的笔记、代码和相关资源。希望这些内容对你也有所帮助。



## 安装指南

​	如果想运行本仓库中的代码，请按照以下步骤进行设置：

1. **克隆仓库**：
   
   ```bash
   git clone https://github.com/ROOKIE-AI/DL.git
   ```



## 笔记结构



## 学习资源

​	学习过程中使用的一些资源

### 课程

* **[Andrew Ng:Deep Learning Specialization](https://www.bilibili.com/video/BV1FT4y1E74V?vd_source=b6653eb93cde9931ca6d7c2760d15b2d)**
* **[李宏毅:机器学习与深度学习](https://www.bilibili.com/video/BV1J94y1f7u5?vd_source=b6653eb93cde9931ca6d7c2760d15b2d)**

* **[fast.ai:面向程序员的实用深度学习](https://course.fast.ai/)**
* **[李沐动手学习深度学习](https://zh.d2l.ai/)**
* **[google:深度学习Tensorflow简介](https://learn.udacity.com/courses/ud187)**


### 书籍

### 其他
* [可视化卷积神经网络](https://ai-demos.cocorobo.hk/cnn-explainer/public/)
* [深度学习调整手册](https://developers.google.com/machine-learning/guides/deep-learning-tuning-playbook?hl=zh-cn)

## 进度记录



### 第一周

#### 2024-06-22 星期六
* 学习卷积神经网络：观看李宏毅课程, 同时阅读了李沐的动手学习深度学习书籍卷积神经网络章节部分。
* 几个重要收获:
  1. 卷积神经网络通过局部分析+共享参数， 结合图像的一些基本特性， 降低了模型的弹性，但提升了模型在图像任务上的表示能力
  1. 卷积神经网络同时应用于当年赫赫有名的AlphaGo， 但它没有使用池化层， 因为在围棋比赛中比较重视细节，通过池化层汇聚往往使其无法很好地表现。(对为什么图像处理可以用池化层的原因解释)
  1. 通过多个卷积层后， 卷积核可以看到更大的区域
  1. 卷积神经网络最早期发明是应用于数字识别， 称为LeNet，2012年的AlexNet在此基础上又加入了几个卷积层， 同时选用ReLU激活函数代替原来的Sigmod

#### 2024-06-23 星期日

* 学习内容:  Kaggle 计算机视觉 课程，构建图像分类器和了解卷积的特征提取过程
* 重要收获：
  * 关于迁移学习: 冻结原有模型的参数， 并在其原输出上加入几个全连接层， 就可以实现二分类判别卡车和小汽车
  * 关于过拟合：模型在训练集上的损失函数随epoch持续下降， 但在验证集上却发生了上升， 是过拟合的表现
  * 关于激活函数:  对于二分类概率预测， 最后输出通常使用sigmoid 函数
  * 关于损失函数:  在二分类任务上， 常使用二元交叉熵损失函数
  * 卷积分类器用于特征提取的前两个操作：使用 **卷积** **过滤** 图像并使用 **ReLU** **检测**特征



### 第二周

#### 2024-06-24 星期一

* 学习内容: Kaggle 计算机视觉课程，学习池化、滑动窗口(填充和步幅)、自定义卷积神经网络和数据增强
* 重要收获:
  * 关于最大池化: 使网络具备了平移不变性， 同样的能力在卷积的共享参数中也有
  * 关于步幅：步幅过大， 会使信息损失较多，通常在较大卷积核上使用较大的步幅
  * 数据增强: 数据增强可以增加数据量， 一定程度上防止过拟合

#### 2024-06-25 星期二

* 学习内容: 李沐动手学习机器学习

  * 11 模型选择 + 过拟合和欠拟合
    * 模型容量和数据量与欠拟合过拟合之间的关系
    * 关于训练集、验证集和测试集的划分
    * 手写实现欠拟合、过拟合的多项式拟合线性回归
  * 12 权重衰退
    * 通过加入正则项，由权重衰退来限制模型的容量， 使其拟合过程中更加平滑， 防止其过拟合

* 重要收获：

  * 验证集的作用：主要用于超参数的调整， 在数据量比较小的情况下， 可以采用K折交叉验证。 

    * K折交叉验证的划分选取， 通常K 取 5 或者 10， 最终的模型选取方案有很多， 比如
      1. 从K 个模型中选取损失最小的
      2. 直接将K个模型用作推理， 最终取K个模型推理的均值(回归)或投票结果(分类) （集成学习)
      3. 将超参数在整个训练集和验证集上再重新训练一遍
    * 对于样本不均衡情况(比如正例样本远少于反例样本)，测试集尽量选取均衡

  * 为什么会过拟合?

    * 模型容量太大， 或者说弹性太大， 拟合能力太强， 在训练集上学习到了过多的特征， 从而在测试集及验证集上表现反而随着训练迭代次数的增加而变差

  * 如何有效防止过拟合？

    * 增加样本量: 例如图像中可以通过简单的反转等操作增加样本集数量
    * 进行正则化: 例如在损失函数上加入惩罚项，限制模型容量，防止模型学到比较大的参数， 使拟合函数更加平滑一些

  * 如何判断模型发生过拟合了?

    * 随着迭代次数的增加， 模型在训练集上的loss 在不断下降， 但是在验证集上反而开始上升
    * .... -> 这个问题还需要进一步深入探讨  ★★★

  * 关于为什么CNN在图像识别上如此有效

    * 从函数拟合能力的角度上来看， 单个隐藏层的MLP足以拟合任何形态的函数， 但通常单隐藏层的MLP却学不到一些复杂的东西。 事实上， 无论是CNN还是RNN， 它们展开其实本质上都是MLP, 但因为其考虑了很多数据的一些特性， 所以使其在具体任务上有更好的表现能力。 
    * CNN 通过 局部分析 和共享参数机制， 有效增强了模型对特征的表现能力

  * 为什么叫权重衰退?

    ​	可以对w进行求导， 写出梯度下降表达式， 可以写做: $\mathbf{w} \leftarrow \mathbf{w} - \eta \lambda \mathbf{w}$

* 遇到问题：

  * 手写实现多项式拟合，来分析过拟合， 但代码出现了问题， 多元线性拟合过程中， 梯度下降异常， 不确定是在哪个环节出现的问题， 待明天排查

#### 2024-06-26 星期三

* 学习内容:
  * 过拟合问题的正则化方案: 丢弃法(dropout)
  * PyTorch神经网络基础:  模型构建、模型自定义、自定义层、参数管理等
* 重要收获:
  * 丢弃法的辛顿解释
    * 可以认为丢弃法实质上是在训练阶段使用一个子神经网络做训练， 最终再由多个子神经网络集成来进行推理， 因此能够有效提升模型的准确性
  * 通常dropout 主要在全连接层上使用
  * PyTorch模型构建
    * 一般的神经网络可以直接通过nn来按顺序连接， 对于一些特殊的需要自定义的场景， 也可以通过继承nn.Module 父类来实现一个自定义的神经网络模型或者是layer或块
    * 神经网络中， 对于共用的一些层， 他们通常共享参数
  * dropout 随机丢弃， 如何保证其可重复性？
    * 可以通过固定随机数种子来实现， 但通常没有必要
  * cuda计算的浮点运算相加顺序会影响结果，通常cpu运算就不会出现这种情况
* 遇到问题:
  * 昨天的手写实现多项式拟合， 还未排查问题， 待明天
* 明日计划:
  1. 新课程安排: 李沐CNN课程部分19 - 22
  2. 动手实现环节: 多项式的线性拟合、正则化(丢弃法和权重衰退)

#### 2024-06-27 星期四

* 学习内容
  * 李沐动手学习深度学习： 卷积神经网络 结构、填充和步幅、多通道、池化
  * 多项式的线性拟合
* 重要收获
  * 卷积神经网络实质是一个特殊的MLP， 主要有两大特性， 分别是局部性和平移不变性， 局部性通过卷积核作用来实现， 平移不变性通过共用参数来实现
  * 卷积神经网络 为什么经常用 3 x 3 的， 而不是 更大的卷积核?
    * 李沐的说法是小的卷积核通常运算效率更高些， 但是3x3 的视野域经过3层卷积后才可以达到5x5卷积核一层的视野域， 但是3x3的推理3层后效率比5x5一层要低， 关于效率的考虑存疑
  * 池化Pooling 对 卷积神经网络的位置敏感性做了一定的钝化， 是实现平移不变性的一个重要特性
* 遇到问题：
  * 排查动手实现多项式线性拟合， 排查至最后环节， 发现甚至连基本的一元线性拟合都无法训练出来。 具体问题仍需明天排查
* 明日计划:
  * 动手实现环节:多项式的线性拟合问题排查， 验证实现正则化和丢弃法
  * 李沐动手学习深度学习课程： 经典卷积神经网络 LeNet、AlexNet 、VGG (23-25)

#### 2024-06-27 星期五

* 学习内容
  * 李沐动手学习深度学习: 卷积神经网络 LeNet 、AlexNet、VGG、NiN(23-26), 以及深度学习硬件(31)
  * 动手环节: 排查多项式线性拟合、运行实现LeNet(CPU， 并尝试调参优化， 准确性接近90%)和 AlexNet(GPU colab， 准确性达到90%)
* 重要收获
  * AlexNet 相比 LeNet 的改进主要在哪里？
    * 增加了卷积层， 同时使用了更多通道和更大的全连接层
    * 使用Relu作为激活函数
  * VGG 相比LeNet 的主要改进在哪里?
    * 使用可块的概念， 构造了VGG 块(多个重复卷积层 + 池化层)， 简化了神经网络的结构， 同时创建了更深的网络模块
    * 倾向使用更小的卷积核， 让模型做得更深， 相同计算开销情况下通常比做得更胖效果要好
  * NiN 相比 VGG 的主要改进是什么?
    * 通过 1x1卷积 + 池化 来代替原来的全连接， 并在整个模型的各个环节穿插使用， 最终再用一个全局卷积核将参数控制到通道数等于输出的节点数规模
    * 1x1 的卷积实现了同一像素不同通道之间的互相关运算， 可以认为是对不同像素点分别做了全连接， 它有效降低了之前使用全连接层时参数量
  * GPU 和 CPU 在计算任务上的主要区别在哪里?
    * 用非常多的相对较弱的计算单元来计算， 会比使用不多的cpu 更快
    * GPU 更适合大规模矩阵运算， 但是控制单元等相对会比较弱
  * 使用CPU做高性能计算的主要语言是什么?
    * 早期主要是Fortran， 因为它的编译器在高性能计算方面更好。但现在C++的编译器其实也很好了，所以目前C++在基于CPU的高性能计算方面更有优势
  * CPU提升计算任务效率的几个主要方面是什么?
    * 在内存优化方面主要有两个考虑方向
      1. 时间方面：数据重复调用， 会更大概率被cache
      2. 空间方面: 计算任务中尽量进行顺序计算。 例如, 对于大规模矩阵计算， 按行访问比按列更快
    * 进行多CPU并行计算，或者HPC集群计算
  * 多项式线性拟合 代码中出现的问题
    * 模拟数据的labels的shape 忘记设置为 (-1， 1)了， 导致最终计算的损失loss有问题。多敲代码， 注意检查!!!、
* 遇到问题:
  * 使用多项式拟合 进行过拟合分析时， 效果并不明显， 感觉可能和高幂项计算的数值比较小， 导致loss被椭化有关系(值得后续分析的问题， 最近暂时不作深究) ★★★
* 明日计划:
  * 动手学习深度学习课程：GoogleNet、批量归一化、残差网络 (27 - 29)
  * 动手环节: 能训练哪个就动哪个，取决于GPU

#### 2024-06-28 星期六

* 学习内容:
  * 动手学习深度学习课程: GoogleNet 、批量归一化 和 残差网络， 额外学习了 序列模型(50)
  * 动手环节: 训练VGG， 重新设计实现VGG网络模块
* 重要收获：
  * GoogleNet 相比于之前的NiN、VGG 等架构的主要创新是什么?
    * 加入了并行的不同卷积结构通道， 最后进行汇总
  * 批量归一化的主要目的是什么?
    * 能够有效加速梯度下降， 但是对于精度提升基本帮助不大
  * 残差网络的主要创新是什么?
    * 加入了残差块， 使得模型能够更好地保留低层学到的特征
  * 序列模型预测
    * 基于条件概率的马尔可夫假设， 实现对文本的预测。这个可以用MLP来实现， 但是在多步转移过程中误差很大， 一个比较好的方式就是采用潜变量， 来表示历史的信息。
* 明日计划:
  * 休息一天

#### 第二周总结

* 主要学习内容

  > 主要围绕计算机视觉CV进行学习，除此之外掌握了一些常用的防止过拟合技术以及数据集划分方式，对PyTorch 实践， 还有硬件相关的一些知识

  * 理论环节
    * 关于深度学习框架: 学习掌握设计自定义及使用默认模块的神经网络、参数管理、模型存储等PyTorch基础
    * 关于训练集的划分: 了解学习 K折交叉验证等常用划分手段， 并理解其主要划分标准原因
    * 关于模型过拟合问题: 学习两种主要的正则化技术: 权重衰退和丢弃法， 同时通过数据增强来控制模型过拟合等
    * 关于卷积神经网络的基础概念: 卷积网络基本结构、卷积互相关计算、填充、步幅、池化(汇聚)、多通道输入和输出等
    * 关于经典的卷积神经网络模型: LeNet、AlexNet、VGG、NiN、GoogleNet、ResNet
    * 关于硬件知识: CPU 和 GPU 的硬件结构介绍和主要的优缺点对比等
  * 实践环节
    * 从零动手实现多项式拟合线性网络的线性回归模型训练， 用于分析过拟合问题
    * 动手实践PyTorch神经网络设计
    * 动手实践卷积神经网络特征学习(水平边缘提取卷积核学习)
    * 动手实现LeNet 经典神经网络， 并在CPU上进行训练和调参优化
    * 动手实验AlexNet网络训练， 并在CoLab使用T4 GPU 进行训练和调参
    * 动手实验VGG模型训练(GPU), 并重新动手实现其网络的代码设计， 并进行调参分析
    * 动手实践在LeNet神经网络采用批量归一化
    * 动手实践在LeNet 神经网络上采用丢弃法， 有效降低了过拟合， 准确率直接达到91%附近
    * 动手实践Kaggle 计算机视觉课程, 掌握了解微调技术以及数据增强等技术， 同时尝试在Kaggle上进行训练和直观分析

* 下周主要计划:

  * 暂缓关于计算机视觉相关的模块学习， 开始自然语言处理NLP的入门， 关键任务是:
    * 掌握RNN系列的经典模型并进行从零实现， 主要掌握包括 RNN、LSTM、GRU等
    * 入门了解Transorform神经网络结构设计
    * 入门BERT， 简单了解其主要原理
  * 采用课程:
    * 仍以李沐的动手学习深度学习课程为主， 辅以李宏毅老师的课程部分
  * 侧重部分:
    * 重点了解掌握其理论部分， 暂时适当弱化动手环节， 待之后通过不断实践来进行强化

### 第三周

#### 2024-07-03 星期三

* 主要学习内容
  * 课程: 自然语言处理基础, 序列模型、文本预处理及语言模型数据集等
  * 动手实践:  分词、序列模型预测、制作语言模型数据集等
* 重要收获
  * 语言序列模型处理， 传统方式基于n阶马尔可夫进行简化假设
  * 通常有两种预测时间序列的方式， 一种叫做自回归模型， 还有一种是潜变量模型
* 存在问题
  * 很多， 李沐的课程和 书本读完后， 有比较多的疑问， 涉及了很多NLP模型的理论基础介绍，并做了部分介绍， 但是感觉有点乱
* 明日计划
  * 大致简单了解NLP的一些基本概念， 并快速入门RNN循环神经网络
  * 动手实现循环神经网络

#### 2024-07-04 星期四

* 主要学习内容
  * 课程: 系统了解RNN的神经网络结构等细节
  * 书籍: 系统学习了解RNN神经网络结构及常见变种， 加深理解。 了解其优化方法等
  * 动手实践： 逐行阅读李沐的RNN从零实现代码， 并运行
* 重要收获
  * RNN 的 工作流程及优化方法和训练过程
  * NLP 自然语言处理的分词等相关的基础知识
* 存在问题
  * 对RNN的从零实现训练环节代码解读未完成， 同时对于顺序批量化的加载数据训练出现异常， 待分析解决
  * 对RNN的损失函数选取(交叉熵损失函数)需要进一步了解
  * 对NLP传统处理手段的原理理解还不完整， 待后续加深
* 明日计划
  * 动手环节： 完整解读RNN从零实现代码， 掌握其PyTorch 的简洁实现版本
  * 课程环节： 学习 LSTM、GRU和深度循环神经网络以及双向循环神经网络

#### 2024-07-05 星期五

* 主要学习内容
  * 课程： 李沐动手学深度学习的 LSTM、GRU、深度循环神经网络和双向循环神经网络课程
  * 动手环节: 重新解读RNN实现代码， 并预测周杰伦歌词
* 重要收获
  * 了解和掌握了GRU、LSTM、深度循环神经网络及双向循环神经网络的基本原理
  * 进一步熟悉文字分词的过程， 加深印象
* 存在问题
  * 周杰伦歌词预测效果不佳， 曲线也一直在抖动， 待后续进一步调参分析
* 明日计划
  * 动手环节： 尽量实现一下LSTM等RNN循环神经网络， 主要以PyTorch 的形式
  * 课程: 基于李宏毅的课程学习自注意力机制的原理

#### 2024-07-06 星期六

* 主要学习内容
  * 课程: 李宏毅的自注意力机制课程等
* 重要收获
  * 对自注意力机制有了一定的了解
*  存在问题
  * 理解的不够深入
* 明日计划
  * 休息

#### 第三周总结

* 主要学习内容
  * 理论环节
    * 循环神经网络： RNN、LSTM、GRU、双向循环神经网络和深度循环神经网络
    * 自然语言基础：分词、one_hat编码、词嵌入等
    * 自注意力机制: 了解子注意力机制的实现过程和直觉性解释
  * 实践环节
    * 循环神经网络RNN的歌词预测从零实现
* 下周主要计划
  * 核心任务
    * 掌握Transformer神经网络架构
    * 入门和微调BERT、GPT 模型
  * 次要任务
    * RNN实践环节， 翻译、seq2seq等
    * PyTorch刘二大人课程完整学习， 系统掌握该框架

### 第四周

#### 2024-07-08 星期一

* 主要学习内容

  * 理论环节
    * 李沐动手学深度学习:  机器翻译、编码器和解码器、seq2seq和束搜索、注意力机制
  * 实践环节
    * 机器翻译的数据集处理、编码器和解码器、seq2seq实现机器翻译的代码及解读
  * 拓展
    * AI 年报的李沐解读， 了解研究现状、应用情况、就业等情况
    * 李沐 AlexNet 论文解读: 粗读
    * 自动调参的技术原理了解

* 主要收获

  * RNN机器翻译的实现？
    * 数据集生成: 需要生成固定长度的序列， 超出的部分需要裁剪， 不足的部分进行填充
    * 网络结构: 分为编码器和解码器两部分， 编码器负责对翻译的文本信息进行编码， 解码器则将编码器的最后一个时间步输出作为其初始隐状态， 再进行解码翻译
  * 束搜索?
    * 每步通过选择k个预测， 来计算其后续预测的结果的联合概率， 选择联合概率最大的作为下一步的输入
  * 解码器和编码器？
    * 编码器主要进行特征提取
  * 注意力机制？
    * 注意力机制思想可以追溯到上世纪60年代， 非参注意力池化层， 通过类似K近邻的思想方式来计算权重信息，注意力机制则是将这个过程变成了可学习的参数的形式。

* 存在问题

  * seq2seq机器翻译的训练损失函数选取及训练流程还需要消化理解
  * 注意力机制还需要进一步理解其原理思想(目前半知不解)， 需要结合代码进行巩固消化

* 明日计划

  * 刘二大人的PyTorch 课程(2-3h)
  * RNN网络的实现和训练过程以及机器翻译实践过程的深入解读分析， 熟悉其代码实现的每个详细环节

  

#### 2024-07-09 星期二

* 学习内容
  * 理论环节
    *  seq2seq(李沐)
    * PyTorch(循环神经网络-刘二大人)
    * ChatGPT技术详解(李宏毅 2023春机器学习)
  * 实践环节
    * seq2seq 的 代码实现细节理解消化
* 主要收获
  * seq2seq中又发现了哪些细节?
    * EnCoder 的最后一个时间步的最后一个隐藏层和DeCoder的嵌入层输出拼接， 作为DeCoder的输出
    * 训练过程中， 对于填充部分， 不计入损失
    * seq2seq的推理阶段和训练阶段的过程是不一样的
  * PyTorch?
    * 基本流程： 数据处理， 制作DataSet、DataLoader、nn Model、 Train funcation、module 保存等
  * 循环神经网络？
    * 个人理解: 循环神经网络通过将中间隐藏层的状态传递到下个时间步， 通过不断往网络中加入新的输入， 使序列文本的原始输入的信息更多地保留在了隐藏层中。 它结合了时间序列信息的特点而设计， 相比MLP, RNN的每个时间步输入层往往离输出层更近， 同时 不同时间步的W_hh 和 W_xr 都是共享的， 因此减少了需要学习的参数数量，使模型更易于训练， 同时能够捕捉序列中的时间依赖关系和长期依赖关系。
  * ChatGPT？
    * 它是由两个阶段完成的， 第一阶段是直接从文本中学习的预训练模型， 第二阶段是通过语言微调训练后的
* 存在问题
  * seq2seq的机器翻译代码训练阶段部分仍无法完全消化， 代码部分太难懂
* 明日计划
  * 理论:自注意力机制和自注意力分数(李沐)、Transformer(李宏毅）
  *  实践:自注意力机制的非参数注意力代码部分以及注意力机制部分理解 

#### 2024-07-10 星期三

* 学习内容

  * 理论环节
    * 李宏毅 自注意力机制的过程及公式详解+Transformer编码器和解码器架构
    * 李沐: 注意力分数和注意力机制课程回顾
  * 实践环节
    * 非参注意力代码理解

* 主要收获

  * 对 Q、K、V 的理解：

    * Q: query, 类似于招聘者， 将原始输入信息 I 比喻为招聘者的聘用岗位具体业务信息，则 Wq 能够将原始信息中抽取出来该岗位所需要的一些技能要求Q:  Q = Wq X
    * K: key, 类似于招聘简历， 将原始输入信息 X 比喻为某人曾经的工作经历， Wk能够从工作经历中抽取出与求职相关的一些技能要求K， K = Wk X
    * V: 抽取与目标评价(比如说岗位契合度) 相关的信息

    > 总之， Q能基于自身总结出与自己需求相关的一部分信息进行表示； K能基于自身总结出主要特点的部分信息。 可以把这两者比作招聘要求和面试简历， 如果它们是相似的， 则说明匹配的较高。 V可以代表该招聘者主要的考核指标信息， 通过将市场中所有面试者的信息进行分析并总结(O = A'V)， 就可以获得该岗位招聘在市场中的真正定位

  * 自注意力机制中的共享参数？

    * Wh、Wq、Wv 在每个输入序列上都是共享的， 这样保证了不同位置的相同信息能够获得完全同样的KQV， 当然， 在这个表述中还需要考虑信息的位置因素， 所以实际上输入的x_i的位置信息， 因此不同位置x_i的 KQV会在考虑位置信息的情况下进行对应的表示。 
    * 所通过更贴近序列信息特点的表现结构， 共享参数的自注意力限制了模型容量，使得模型能够有效防止过拟合， 并增强其表示能力

  * 自注意力机制和气象中的相似法？

    * 筛选因子的表示和相似度计算等过程和注意力机制的思想很契合， 可以抽时间尝试输出一篇分享文章

  * Transformer中的残差连接?

    * Transformer 中同样使用了残差结构

* 明日计划

  * 理论环节
    * Transformer ： 李宏毅和李沐
    * BERT: 李沐
  * 实践环节
    * 继续理解李沐 attention分数 部分的代码



#### 2024-07-11 星期四

* 学习内容
  * 理论环节
    * 李沐: Transformer、BERT(大致了解)
    * 李宏毅: Transformer
  * 实践环节
    * attention 注意力分数代码逐行理解、运行及分析(加性注意力 & 点积注意力， 遮蔽softmax)
* 主要收获
  * Transformer？
    * 多头注意力, 可以类比为CNN中的多通道
    * norm是层归一化
  * BERT？
    * BERT是一个预训练模型结构， 采用了Transformer 的解码器架构
  * Attention scores？
    * **点积注意力** 更适合高维向量，计算效率更高，广泛应用于现代深度学习模型
    * **加性注意力** 更灵活，可以捕捉复杂的非线性关系，但计算开销较大，适用于低维向量或需要更复杂关系的场景
    * **mask-softmax** 屏蔽了无效字段的分数
* 存在问题
  * Transformer 的层归一化没太仔细理解
  * BERT只是大概了解了一些设计过程， 但印象不深刻， 待完全熟悉Transformer 后再仔细解读
* 明日计划
  * 实践环节: self-attention 、Transformer 代码逐行阅读理解及注解修改等 

#### 2024-07-12 星期五

* 主要内容

  * 课程环节： 李沐-实用机器学习

    课程介绍、数据获取、网页数据抓取、数据标注、探索性数据分析、数据清洗、数据变换、特征工程

  * 实践环节：李沐-加入attention 的seq2seq

* 主要收获

  * 机器学习任务的数据环节主要工作流程
    * 获取(爬虫或采集) -> 质控 -> 特征工程 -> 格式转换等
  * 数据标注的常用方法
    * 众包
    * 自训练(self-training)
    * 启发式生成
  * 加入attention 的 seq2seq
    * 一些关于PyTorch 的语法知识: 如转置(permute、transpose、t()、T)、矩阵乘法(bmm、mm、matmul、@)、unsqueeze
    * `nn.LazyLinear`: 不需要预先知道输入数据的维度，更加灵活，适合在动态计算图中使用

* 明日计划

  * 课程环节
    * 李沐:实用机器学习第3章课程
  * 实践环节
    * 文本数据处理

#### 2024-07-13 星期六

* 主要内容
  * 课程环节： 李沐实用机器学习第三章
  * 实践环节：阅读《Python深度学习》、《Python机器学习基础教程》
* 主要收获
  * 了解梯度提升树模型等
* 明日计划
  * 休息

#### 第四周总结

* 主要学习内容 
  *   循环神经网络、seq2seq、注意力机制、Transformer、BERT 
  *   NLP文本数据处理、seq2seq代码 
* 下周计划  
  *  实战图像处理Kaggle算法  
  *  阅读西瓜书， 掌握线性模型、树模型章节内容(公式推导) + 代码从零实现

### 第五周

#### 2024-07-15 星期一

* 学习内容

  * 理论环节
    * 西瓜书第二章 模型评估与选择
    * 数据结构与算法
      * 两数之和(哈希查找)
      * 数组类算法：做好初始定义
  * 实践环节
    * Kaggle 实战: 房价预测

* 主要收获

  * 过拟合的原因?

    * 个人理解
      *  模型的假设空间（容量或弹性）超过 数据的规模， 导致其学到了一些训练样本中特有的特征
      * 训练数据较少， 无法很好地平衡这些特征， 存在认知局限， 难以总结出共性
      * 可能性原因: 训练集和验证集在划分的时候， 不遵循同分布

  * 评估方法？

    * 留出法： 直接将训练数据中划分为两个互斥的集合， 作为训练集S和验证集T。 采样过程尽可能保持数据分布的一致性， 比如可以采用分层采样等， 避免由于数据划分过程引入的偏差而对最终结果产生影响

    * 交叉验证法： 将数据集划分为k个大小相似的互斥子集， 每次用k-1个子集作为训练集， 剩余1个作为测试集， 然后进行k轮训练。最终将k个模型的测试结果均值作为最终测试结果。

      留一法： 特殊的交叉验证法，假设有m个样本， 令k = m。 缺点是面对大规模训练集时训练成本太大

    * 自助法

  * 方差和偏差？

    * 均方误差主要由3部分构成， 方差、偏差和噪声

  * Kaggle 竞赛： 房价预测？

    * 尝试调参， 先采用MLP， 并以ReLU作为激活层

* 存在问题

  * 西瓜书第二章 比较检验、偏差和方差部分的公式尚未理解， 需要抽时间复习概统
  * Kaggle 竞赛 房价预测 模型优化效果不佳， 输入维度太大， 准备尝试做些特征的处理

* 明日i计划

  * Kaggle 竞赛： 房价预测
  * LeetCode 算法题练习：数组类 运用基础算法思想

#### 2024-07-16 星期二

* 学习内容
  * 理论环节
    * 统计学习 第一章: 统计学习与监督学习概论(粗读)
    * 线性代数: 概念回顾
  * 实战环节
    * Kaggle竞赛: 房价预测调参
  * 算法题
    * 数组类算法: 颜色分类、数组中的第K个最大元素(O(n)未实现) 、两数之和II
* 主要收获
  * Kaggle 竞赛： 房价预测？
    * 增加k折交叉验证中的划分子集数量k, 可以明显提升效果
    * 集成学习算法的表现效果通常比单一模型要更好
    * 使用AutoML进行调参， 其本质上也是基于集成学习实现
  * 颜色分类?
    * 解法一:  基数排序法， 用数组记录下0， 1， 2 的数字个数， 后重排， 实际遍历了两遍
    * 解法二:  快速排序法， 双指针， 只发生一遍循环遍历。在开始实现过程中， 一直在考虑nums[i]  置换得到 2的情况如何处理， 实际上从左往右看过的数字， 其前面不会出现2的
  * 两数之和II？
    * 已经完成排序的情况下， 只需要使用对撞指针两侧收缩遍历即可

* 存在问题
  * 数组中的第K个最大元素 算法 最优解未实现
* 明日计划
  * Kaggle 竞赛： 图片分类
  * LeetCode 算法题练习：数组类 双索引技巧
  * 统计学习 第一章 正则化与交叉验证、模型评估与模型选择

#### 2024-07-17 星期三

* 学习内容
  * 理论环节
    * 统计学习 第一章: 统计学习与监督学习概论精读
      * 笔记： 统计学习、统计学习分类、统计学习方法三要素
      * 精读： 模型评估与模型选择、正则化与交叉验证、泛化能力
  * 实践环节
    * Kaggle 竞赛： 图片分类
    * LeetCode 算法题刷题
      * 验证回文串
      * 反转字符串中的元音字符
      * 盛最多水的容器
      * 长度最小的子数组
* 主要收获
  * 在线学习和批量学习？
    * 在线学习一次只接受一个样本来进行学习优化
    * 批量学习每次接受批量数据进行学习
  * 验证回文串？
    * 首尾指针遍历收缩， 发现不匹配则直接返回Flase, 直到指针相遇后， 则返回True(碰撞指针)
  * 反转字符串中的元音字符？
    * 首尾双指针开始遍历(碰撞指针)
    * 遇到大写转为小写
    * 如果非字母，直接跳过(移动指针) 后进入下一轮判别
    * 如果其中一个指针指向了元音字符， 则不再前进， 等待另一个指针发现元音字符后再交换， 再同时移动指针
    * 如果两指针相遇或交错， 则终止循环
  * 盛最多水的容器？
    * 首尾双指针开始遍历(碰撞指针)
    * 记录开始时的盛水面积
    * 开始移动两个指针， 每次移动较小的那个指针1步后计算面积， 如果大于之前的记录面积， 则更新为当前
    * 如果两指针相遇， 终止循环
    * 返回最终记录的最大面积
  * 长度最小的子数组
    * （滑动窗口）
    * 要求是连续子数组，所以我们必须定义 i，j两个指针，i 向前遍历，j 向后遍历，相当与一个滑块，这样所有的子数组都会在 [i...j] 中出现，如果 nums[i..j] 的和小于目标值 s，那么j向后移一位，再次比较，直到大于目标值 s 之后，i 向前移动一位，缩小数组的长度。遍历到i到数组的最末端，就算结束了，如果不存在符合条件的就返回 0。
* 明日计划
  * 算法刷题：初级算法 数组
  * Kaggle实战： 图片分类
  * 统计学习：第一章剩余内容精读与笔记

#### 2024-07-18 星期四

* 学习内容

  * 理论环节
    * 统计学习 第一掌剩余部分(精读)
  * 实践环节
    * Kaggle: 图片分类
    * Leet Code 刷题: 
      * 初级算法:  数组大部分和字符串小部分

* 主要收获

  * 图像增广？

    * 使用torchvision 对应方法对图片进行局部放大、水平翻转等操作

  * colab下载Kaggle数据集?

    * 获取Kaggle API Key 文件 kaggle.json

    * 上传至colab, 配置相关环境变量后， 就可以通过命令下载， 示例如下：

      ```python
      os.environ['KAGGLE_CONFIG_DIR'] = './'
      !kaggle competitions download -c cifar-10
      ```

  * 生成模型？

    * 通过学习联合分布P(Y, X) 来进行预测

  * 召回率、精准率、F1?

    * 召回率 R 是指真实为正类的部分被正确预测的比例
    * 精准率 P 是指预测为正类当中实际也为正的比例
    * F1 : F1 = 2PR/(R + P)

  * 模型、策略、算法?

    * 李航的统计学习中的定义为
      * 模型： 存在于假设空间的 函数映射
      * 策略: 学习的目标， 首先定义损失函数loss function ，评估目标是损失期望
      * 算法: 优化方法， 即学习的方法 
    * 损失函数的期望
      * 通常叫做风险函数 或 期望损失
      * 理论定义为 L(Y, f(X)) 与联合分布P(X, Y) 的乘积 在 feature space x output space 上的 全积分
      * 实际上不可求
      * 可使用样本数据的平均loss来近似， 当样本数量N趋于无穷时， 损失期望 等于理论值
      * 我们用样本数据平均损失近似的 结果 叫做 经验风险 或经验损失
    * 经验风险最小化 和  结构风险最小化
      * 经验风险最小化
        * 最优解为 经验风险函数 在参数空间上的最小值
      * 结构风险最小化
        * 最优解为 结构风险函数 在参数空间上的最小值
        *  这里的结构风险函数通常是在经验风险函数的基础上加入了一个正则项 λ **J**(f)
      * 正则化
        * weight deacy: L1 、L2
        * dropout(待了解其正则化的数学形式)
    * 删除排序数组中的重复项
      * 有序数组: 双指针遍历， 如果值相同，右指针前进； 如果不同， 左指针的下一个值为当前右指针值， 然后同时前进两个指针。直到右指针到数组尾部为止
      * 无须数组： 维护一个Set 来实现
    * 卖股票的最佳时机II
      * 遍历数组， 凡是下一个值大于上一个值的， 将其差值加入到累计数组sum， 直到遍历完整个数组， 返回sum
    * 旋转数组
      * 方法1:
        1. 将最后k个元素单独放入一个创建好的数组A中
        2. 将前len-k个元素逐个从后往前移动k位
        3. 将数组A中的k个元素赋值到目标数组对应下标
      * 方法2：
        * 向前移动1步：取出最后一个元素赋值给变量t， 然后将前len-1个依次后移1位， 最后再把t赋给数组首个元素
        * 重复上述步骤k次(包含上个步骤在内)
      * 方法3: 
        * 先整体反转
        * 再反转前k位
        * 最后反转从k位开始到最后的部分
    * 存在重复元素
      * 维护1个set, 遍历过程中如果当前元素存在于set, 则返回true, 否则将当前元素加入set. 如果完整遍历完整个数组， 则返回false
    * 只出现一次的数字
      * 采用位运算：异或
    * 加一
      * 逢10进1, 最后如果还有进的一位， 则在数组最前面加入一位， 值为1
    * 移动零
      * 双指针(细节略)
    * 两数之和
      * 哈希(细节略)
    * 反转字符串
      * 对撞指针(细节略)
    * 整数反转
      * 辗转相除、取余， 注意数值溢出判断
    * 位1的个数
      * 基于10进制转2进制的公式

* 明日计划

  * 算法刷题：初级算法 字符串
  * Kaggle实战： 图片分类
  * 统计学习：第二章
