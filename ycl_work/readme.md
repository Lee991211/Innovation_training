# 做了什么
### 2020-06-05
- 前台html模板简陋完成
- 后台程序简要完成
- 需要训练后的数据给出相应的可视化图表
- 训练前的数据也看了，这玩意怎么可视化啊，脑阔痛

*************
### 2020-06-07
- 有了爬虫同学爬下来的数据
- jieba对数据处理
- wordcloud生成词云
具体见代码注释及可视化文件夹下readme

*************
### 2020-06-08
- 添加读取方法，自动对某目录下的文件进行读取
- 添加多种读取方式：csv、txt、excel等等

*************
### 2020-06-10
- 增加search.py
- 增加了新的搜索路由和前台界面简陋如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200610220628148.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NkeWlucnVpY2hhbw==,size_16,color_FFFFFF,t_70)
- 使用搜索功能后可以根据关键字生成词云，这期间需要进行爬取、数据处理，其中和爬虫的对接还没有搞
- 生成的词云为返回的代码，现在已经可以获取到产生的代码并插入到html