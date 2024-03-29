# 爬虫

网络爬虫（又称为**网页蜘蛛**，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。

## 爬虫分类

### 通用网络爬虫(Scalable Web Crawler)

通用网络爬虫的结构大致可以分为**页面爬行**模块、**页面分析**模块、**链接过滤**模块、页面数据库、URL 队列、初始 URL 集合

- 深度优先策略:按照深度又低到高的顺序，依次访问下一级网页链接，这种策略比较适合垂直搜索或站内搜索。
- 广度优先策略:按照网页内容目录层次深浅来爬行页面，处于较浅目录层次的页面首先被爬行。这种策略能够有效控制页面的爬行深度。

### 聚焦网络爬虫(Focused Crawler)

选择性爬行那些与预**先定义好的主题相关页面**的网络爬虫

- 基于内容评价的爬行策略：将用户输入查询词作为主题，包含查询词的页面被视为与主题相关，起局限性在于无法评价页面与主题相关度的高低。
- 基于链接结构评价的爬行策略：通过计算每个已访问页面的Authority权重和Hub权重，并依次决定链接的访问顺序。
- 基于增强学习的爬行策略：Rennie 和 McCallum 将增强学习引入聚焦爬虫，利用贝叶斯分类器，根据整个网页文本和链接文本对超链接进行分类，为每个链接计算出重要性，从而决定链接的访问顺序。
- 基于语境图的爬行策略：通过建立语境图学习网页之间的相似度，训练一个机器学习系统，通过该系统可计算当前页面到相关Web页面的距离，距离越近的页面中的链接优先访问。

### 增量式网络爬虫(Incremental Web Carawler)

指对已下载网页采取增量式更新和只爬行新产生的或者已经发生变化网页的爬虫，它能够在一定程度上保证所爬行的页面尽可能新的页面。

常用的方法有：

- 统一更新发
- 个体更新发
- 基于分类的更新法

### Deep Web爬虫(Surface Web)

Deep Web 是那些大部分内容不能通过**静态链接获取**的、**隐藏在搜索表单后的**，只有用户提交一些关键词才能获得的 Web 页面。

Deep Web 爬虫体系结构包含六个基本功能模块 （**爬行控制器、解析器、表单分析器、表单处理器、响应分析器、LVS 控制器**）和两个爬虫内部数据结构（URL 列表、LVS 表）。 其中 LVS（Label Value Set）表示标签/数值集合，用来表示填充表单的数据源。

#### Deep Web爬虫爬行过程中表单填写类型：

- 基于领域知识的表单填写
- 基于网页结构分析的表单填写

## 爬虫核心

- 爬取网页数据
- 解析数据
- 爬虫和反爬之间的博弈

## 爬虫用途

![](imgs/spider-10.jpeg)

 - 数据分析/数据源
 - 社交软件冷启动
 - 竞争对手监控
 - 舆情监控
