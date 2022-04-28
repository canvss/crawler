# HTTP

## HTTP简介：

HTTP（HyperText Transfer Protocol）即超文本传输协议，是一种详细规定了浏览器和万维网服务器之间互相通信的规则，它是万维网交换信息的基础，它允许将HTML（超文本标记语言）文档从Web服务器传送到Web浏览器。

HTTP协议目前最新版的版本是1.1，HTTP是一种无状态的协议，无状态是指Web浏览器与Web服务器之间不需要建立持久的连接，这意味着当一个客户端向服务器端发出请求，然后Web服务器返回响应（Response），连接就被关闭了，在服务器端不保留连接的有关信息。也就是说，HTTP请求只能由客户端发起，而服务器不能主动向客户端发送数据。

HTTP是一个基于TCP/IP通信协议来传递数据（HTML 文件, 图片文件, 查询结果等）。

## HTTP工作原理：

- HTTP协议工作于客户端-服务端架构上。浏览器作为HTTP客户端通过URL向HTTP服务端即WEB服务器发送所有请求。
- Web服务器有：Apache服务器，IIS服务器等
- Web服务器根据接收到的请求后，向客户端发送响应信息
- HTTP默认端口号80

## HTTP请求头信息（request）

**HTTP请求报文由3部门组成(请求行+请求头+请求体)**

![](/static/imgs/crawler/http01.png)

### HTTP请求报文

**请求URL地址（统一资源定位符）**

**协议名称版本号**

**报文头（服务端获取客户端信息key：value）**

**报文体（a=1&b=2的键值对编码成一个格式字符串传递数值）**

#### 请求方法（Request method）

- GET
- POST
- HEAD
- PUT

#### HTTP请求报文属性

- Accpet：高数服务器客户端接受什么类型的响应
- Referer：表示这个请求是从那个url进来的
- Cache-Control：对缓存进行控制
- Accept-Encoding：接收编码格式
- Host：指定要请求资源所在主机和端口
- User-Agent：浏览器版本信息

### HTTP响应报文

**响应报文由三个部分组成（相应行，响应头，响应体）**

![](/static/imgs/crawler/http04.png)

- 报文协议及版本；

- 状态码及状态描述；

- 响应报文头，也是由多个属性组成；

- 响应报文体，即我们要的数据。

### HTTP相应状态码

![](/static/imgs/crawler/status_code.png)

- 200 OK 表示成功
- 303 重定向,把你重定向到其他页面
- 304 资源并未修改,可以直接使用本地的缓存
- 404 找不到页面(页面被删除或其他)
- 500 服务端错误

#### HTTP响应报文属性

- Cache-Control：响应输出到客户端后，服务器通过该属性告诉客户端该怎么控制响应内容的缓存
- ETag：表示你请求资源的版本，如果该资源发生变化，那么属性也会跟着变化
- Location：在重定向中或者创建新资源时使用
- Set-Cookie：服务端可以设置客户端cookie



### 一次完整的http请求过程

**域名解析 --> 建立连接 --> 接受请求 --> 处理请求 --> 访问资源 --> 构建相应报文 --> 发送响应报文 --> 记录日志**

![](/static/imgs/crawler/http03.png)

#### 域名解析：

当用户在浏览器地址栏输入http://www.baidu.com 发起一个请求，首先会把该域名解析为ip地址。

DNS 的详细解析过程：http://vinsent.blog.51cto.com/13116656/1967876

#### 建立连接：

浏览器会开启一个随机端口向服务器的80端口发起tcp连接请求，经过3次握手后建立tcp连接，然后向服务器发起httpd请求。   

- TCP三次握手
- TCP四次挥手

[![alt text](/static/imgs/crawler/tcp.png "TCP三次握手，四次挥手”你真的懂吗？")](https://zhuanlan.zhihu.com/p/53374516)

#### 接收请求：

接受请求所要完成的工作就是接收来自网络的请求报文中对某一资源的请求过程

- 单进程I/O模型
- 多进程I/O模型
- 复用I/O结构
- 复用多线程I/O模型

- 处理请求：以Apache的prefork工作模式为例，管理进程在接受到请求报文后会选择一个工作进程来对该请求进行处理，得到其请求方法和资源URL等相关信息
- 访问资源：对请求处理时一般需要访问后端资源，执行代码得到请求结果，把结果返回给服务器
- 构建响应报文：在得到返回的请求结果后，开始构建响应报文
  - 永久重定向
  - 零时重定向
- 发送响应报文：响应报文构建完成后，发送响应报文
- 记录日志：最后，当事务结束时，web服务器会在日志文件中添加一个条目，来描述已执行的事务


### Cookie

**Cookie，有时也用其复数形式 Cookies。类型为“小型文本文件”，是某些网站为了辨别用户身份，进行Session跟踪而储存在用户本地终端上的数据（通常经过加密），由用户客户端计算机暂时或永久保存的信息**

![](/static/imgs/crawler/cookie.png)

- 1、Cookie是一种在客户端保持HTTP状态信息的技术

- 2、Cookie是在浏览器访问WEB服务器的某个资源时，由WEB服务器在HTTP响应消息头中附带发送给浏览器的数据

- 3、一旦WEB浏览器保存了某个Cookie，那么它在以后每次访问该WEB服务器时，都应在HTTP请求头中将这个Cookie发送给WEB服务器

#### Cookie功能特点：

- 存储于浏览器头部/传输于HTTP头部
- 写时带属性，读时无属性
- HTTP头中Cookie：user=admin;pwd=123;
- 属性name/value/expire/domain/path/.....
- 由三元组[name,doman,path]确定唯一cookie

#### Cookie的安全属性：

- secure属性：当设置为true时，表示创建的Cookie会被以安全的形式向服务器传输，也就是只能在HTTPS连接中被浏览器传递到服务器段进行会话验证，如果时HTTP连接则不会传递该信息，所以不能窃取到Cookie的具体内容。
- HttpOnly属性：如果在Cookie中设置了”HttpOnly“属性，那么通过程序（JS脚本等）将无法读取到Cookie信息，这样能有效防止XSS攻击。

 secure属性是防止信息在传递的过程中被监听捕获后信息泄露，HttpOnly属性的目的是防止程序获取cookie后进行攻击

### Session

**Session 是 用于保持状态的基于Web服务器的方法。Session允许通过将对象存储在Web服务器的内存中在整个用户会话过程中保持任何对象**

![](/static/imgs/crawler/session2.png)

- 使用Cookie和附加URL参数都可以将上次请求的状态信息传递到下次请求中，但是如果传递的状态信息较多，将极大降低网络传输效率和增大服务器端程序处理的难度。

- Session是一种将会话状态保存在服务器端的技术。

- 客户端需要接收、记忆和发送Session的会话标识号，Session可以且通常是借助于Cookie来传递会话标识号。

### 利用Cookie实现Session跟踪

- 如果web服务器处理某个访问请求时创建了新的HttpSession对象，它将会把会话标识号作为一个Cookie项加入到响应消息中，通常情况下，浏览器在随后发出的访问请求中又将会话标识号以Cookie的形式回传给web服务器。
- web服务器端程序依据回传的会话标识号就知道以前已经为该客户端创建了HttpSession对象，不必再为客户端创建新的HttpSession对象。而是直接使用与该会话标识号匹配的HttpSession对象，通过这种方式就实现了对同一个客户端的会话状态的跟踪。

### Cookie和Session

![](/static/imgs/crawler/session&cookie.png)

**session和cookie同样都是针对单独用户对象，不同的用户在访问网站时，都会拥有各种的session或者cookie，不同用户之间互不干扰。**

- 存储位置
- 生命周期

### cookie和session区别

- cookie数据存放在客户的浏览器，session数据存放在服务器。
- cookie不是很安全，可以分析存放在本地COOKIE并进行COOKIE欺骗考虑安全应当使用session。
- session会在一定时间内保存在服务器。当访问增多，会占用服务器性能。考虑减轻服务器性能方面，应当使用COOKIE。
- 单个cookie在客户端的限制时3k。
