# 机器学习学习笔记

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


## 进度记录

### 2024-06-22 星期六
学习卷积神经网络：观看李宏毅课程, 同时阅读了李沐的动手学习深度学习书籍卷积神经网络章节部分。
记录几个重要收获:
1. 卷积神经网络通过局部分析+共享参数， 结合图像的一些基本特性， 降低了模型的弹性，但提升了模型在图像任务上的表示能力
2. 卷积神经网络同时应用于当年赫赫有名的AlphaGo， 但它没有使用池化层， 因为在围棋比赛中比较重视细节，通过池化层汇聚往往使其无法很好地表现。(对为什么图像处理可以用池化层的原因解释)
3. 通过多个卷积层后， 卷积核可以看到更大的区域
4. 卷积神经网络最早期发明是应用于数字识别， 称为LeNet，2012年的AlexNet在此基础上又加入了几个卷积层， 同时选用ReLU激活函数代替原来的Sigmod
