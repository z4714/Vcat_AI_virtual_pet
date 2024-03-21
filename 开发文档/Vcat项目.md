# Vcat项目






Reality——Game interface: An intellgent  generating and interactable vitural pet 

+ 基于游戏用户互动的数据挖掘系统

+ 基于图像融合的游戏生物自动生成模型

+ 自动环境绘图

+ 生成自然的npc对话

+ 词性评价（非须）

+ 元宇宙——计算机视觉自动建模——数字孪生

  启发：

  元宇宙与现实世界互动的成本高，数字孪生成本高

  游戏内容发展局限于预设内容，自由度有限——新型精灵游戏与图像融合技术

  宠物饲养困难
  
  贾维斯——AI助手
  
  https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111/blob/main/README_CN.md

# 1.硬件

### (1) 元件、打板

#### 核心

#### 传感

#### 显示

arduino触摸屏 or 全息

#### 接口

### (2) 焊接

# 2.软件

## (1) Arduino烧录

## (2) 算法

#### CV

#### NLP

#### 强化学习

#### 数据处理算法

## (3) 前端

### 1）开发方法

#### (a) 概览

使用“React技术栈”，即React JS库及其相关框架

本项目采用==React+TypeScript+umi+dva+antd-mobile==的框架开发方式进行搭建。

#### (b) 理由

1.  React：指用于构建用户界面的JavaScript库，具有组件化、声明式等特点，具有优秀的DOM性能优化。

2. React技术栈：其整个技术栈是一个渐进式的框架——主张最少，可以只用其中一部分。例如，开始时只需React， 有新需求后可以引入其他类库如路由库、状态管理库等。

3. TypeScript：TypeScript是JavaScript的超集，最终会被编译为JS代码。它添加了可选的静态类型系统与很多尚未正式发布的ECMAScript新特性，如装饰器。

4. umi：React开发框架。理解为一个专注性能的类next.js前端框架，通过约定、自动生成和解析代码等方式辅助开发。

   - 内置大量性能优化
   - 多端，无缝支持容器和浏览器访问，
   - 类webpack的插件机制
   - 对antd和dva有友好支持

   “文件即路由”——page文件夹下新建文件，umi自动生成与文件路径对应的路由。

   ​	解决如下问题：

   - ​	项目既可以跑在如支付宝/淘宝/微信容器里（多页），又可以跑在普通浏览器里（单页）。
   - 开发调试的启动和热更新时间随项目变大越来越长。
   - 基于路由做按需加载。
   - 支持PWA
   - preact
   - 部署问题

   [umi参考文档](https://www.cnblogs.com/AllenPan/p/16440013.html)

#### （c) 服务器项目打包方式

zip....但很慢

### 2）umi + nginx部署前端网站

打开Nginx的配置文件（通常在/etc/nginx/nginx.conf），在http块内添加以下内容：

```bash
server {
    listen 81;   # 注意端口号设置
    server_name xxx.xx.x.xx;   # 注意替换为的服务器公网IP
    location / {
        proxy_pass http://localhost:8000;   # 注意替换为Dumi项目的端口号
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}


```

为Nginx监听了81端口，并将请求代理到本地的8000端口上，这是umi项目启动时默认的端口号。如果你的Dumi项目使用了其他端口号，需要相应地修改。

此时在对应umi项目文件夹下进行npm start即可访问网站。

npm start报错

```
  opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ],
  library: 'digital envelope routines',
  reason: 'unsupported',
  code: 'ERR_OSSL_EVP_UNSUPPORTED'
```

原因：nodejs版本过高

解决：

```bash
export NODE_OPTIONS=--openssl-legacy-provider 
```

  pnpm 创建项目

```bash
pnpm dlx create-umi@latest
```

 https://umijs.org/docs/tutorials/getting-started



pnpm build 打包项目成dist文件夹

配置服务器项目路径：

/etc/nginx/nginx.conf:

```
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       8001;
        server_name  xxx.xx.x.xx;

        charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            #proxy_pass http://localhost:8000;
            #proxy_http_version 1.1;
            #proxy_set_header Upgrade $http_upgrade;
            #proxy_set_header Connection 'upgrade';
            #proxy_set_header Host $host;
            #proxy_cache_bypass $http_upgrade;
            root /home/comp3070/COMP3070/Vcat_1_5/dist/;
            index index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}
```

```
sudo service nginx reload
sudo service nginx restart
```

部署后内容不更新可以等待一下，是由于浏览器缓存等因素导致的

### 3）底层模板页与登录页面（弃用）

`@umi/max` 内置了**全局初始状态管理**[插件](https://github.com/umijs/umi/blob/master/packages/plugins/src/initial-state.ts)，允许您快速构建并在组件内获取 Umi 项目全局的初始状态。

全局初始状态是一种特殊的 Model。

全局初始状态在整个 Umi 项目的最开始创建。编写 `src/app.ts` 的导出方法 `getInitialState()`，其返回值将成为全局初始状态。

### 3) 底层模板页与登录页面（弃用）

#### (a) 模板页面：

1. 带顶部导航条的基础模板（BasicLayout）
2. 权限模板（SecurityLayout）
3. 后续具体增加

#### (b) 基础模板

基础模板作为所有页面的底层模板，会==首先请求用户基本信息==，判断是否登录，如果是进入需要登录的页面并且未登录，则跳转登录页，否则留在当前页面。基础模板需要判断是否需要显示导航条。同时，每个页面刷新都需要判断是否登录，获取用户基础信息也都放在基础模板页，同时记录到user state中。

```react
import {ConnectState,ConnectProps, UserModelState} from '@/models/connect';
interface BasicLayoutProps extends ConnectProps{
    user: UserModelState;
}
```

检测客户端设备对应IP登录状态

（React—>Django(axios->JWT->user)

##### 基本开发

CSS+JS+HTML

[vitejs](https://cn.vitejs.dev/guide/)

[react](https://react.docschina.org/)



##### 响应式网页

ASouthernCat

#### 图像展示

##### 动画制作

blender+verge3D

gooblend

##### AI 动画

Stable diffusion

##### 数据监测展示

Flask 、Dashboard

#### 基本网页框架

##### 基本开发

CSS+JS+HTML

react

[vitejs](https://cn.vitejs.dev/guide/)

[react](https://react.docschina.org/)

##### 响应式网页

ASouthernCat

#### API

##### 微信小程序接口





### 4) webpack代码打包工具部署

新建目录，在新建目录下执行

```bash
npm init -y
```

初始化项目(生成package.json)



安装webpack-cli(使用webpack的命令行工具）：

```bash
npm install webpack webpack-cli -D
```



运行webpack：

```bash
npx webpack
```

 (要先有src目录和index.html才能成功)



使webpack全局环境下可用：

```bash
npm install webpack -global
```

但全局可能会导致一些版本问题（如项目中webpack被锁定到指定版本）

最新版：

```bash
npm install webpack@beta
```

#### （a) 初始化项目结构

项目结构：

```c
webpack-demo
    |-node_modules
    |-package.json
    |-package-lock.json
   +|-index.html
   +|-/src
   +	|-index.js
   +	|-show.js
```

#### (b) 代码开发

根据个人体验，推荐先使用在线IDE [StackBlitz](https://stackblitz.com/)进行实时渲染开发，然后将代码移植到服务器项目目录中。

git下对应工作目录：[vcat前端](..\软件开发\前端\vcat)

![image-20230517134327929](COMP3070大项目.assets/image-20230517134327929.png)

![image-20230517134411828](COMP3070大项目.assets/image-20230517134411828.png)

index.js文件被打包到了dist文件夹下，默认使用production mode（生产环境）。打开dist/main.js可以看到被压缩的代码，说明是生产环境打包。

执行构建后的项目结构：

```bash
webpack-demo
   +|-dist
   +	|-main.js
    |-node_modules
    |-package.json
    |-package-lock.json
    |-index.html
    |-/src
    	|-index.js
    	|-show.js
```

总的来说，执行npx webpack会将脚本src/index.js作为入口起点，也会生成dist/main.js作为输出。目录下多出dist目录，里面的main.js文件是一个可执行的JS文件，包含webpackBootstrap启动函数。

然后将index.html的js文件引用替换为dist/main.js

### 5)nginx配置

查看 Nginx 配置文件的位置：

```bash
nginx -t
```



### 6）TDesign

https://tdesign.tencent.com/starter/docs/react/get-started

使用腾讯的框架实现快速页面部署

```

```

### 7）AntDesign

最后选择AntDesign进行前端开发

https://landing.ant.design/docs/use/dumi



### 8）axios接口封装 - dist

npm build

将打包好的dist放到服务器nginx对应路径下



### 9) base64 图像编码

https://blog.csdn.net/sunyctf/article/details/125527656

### 10）useMemo

`useMemo` 是 React 的一个 Hook，它用于在函数组件中进行记忆化计算。它的作用是根据依赖项的变化来缓存计算结果，以避免不必要的重复计算。

`useMemo` 接受两个参数：计算函数和依赖项数组。计算函数是一个在每次渲染时都会执行的函数，它返回要缓存的值。依赖项数组是一个用于检测变化的依赖项列表，当依赖项发生变化时，`useMemo` 会重新计算值。

使用 `useMemo` 可以有效地优化性能，避免在每次渲染时都重新计算相同的值。当计算开销较大或依赖项变化时，使用 `useMemo` 可以避免不必要的计算，提升组件的性能。

#### 11)语法笔记

`let` 是 JavaScript 中的一个关键字，用于声明一个块级作用域的变量。使用 `let` 声明的变量具有块级作用域，只在声明的块内部有效，而在块外部无法访问。

相比之下，`var` 关键字声明的变量是具有函数作用域或全局作用域的，它们在整个函数或全局范围内都是可见的。

使用 `let` 可以避免变量提升和命名冲突等问题，更好地控制变量的作用范围。它是 ES6 引入的新特性，推荐在 JavaScript 开发中使用 `let` 来声明变量。

##### 钩子函数useEffect

`useEffect` 是 React 中的一个钩子函数，用于处理副作用操作。副作用操作指的是在组件渲染期间，需要进行一些与界面交互、网络请求、订阅事件等无法纯粹通过组件声明式渲染实现的操作。

`useEffect` 接受两个参数：一个函数和一个依赖数组（可选）。函数参数是副作用操作的逻辑，它会在组件渲染完成后执行。依赖数组用于指定哪些状态或属性的变化会触发副作用操作。

当组件渲染时，`useEffect` 会在组件第一次渲染完成后执行副作用操作。如果指定了依赖数组，那么当数组中的依赖项发生变化时，`useEffect` 会重新执行副作用操作。如果没有指定依赖数组，`useEffect` 每次组件重新渲染时都会执行副作用操作。

副作用操作可以包括以下内容：

- 发送网络请求
- 订阅和取消订阅事件
- 操作 DOM 元素
- 调用第三方库
- 更新状态

需要注意的是，在副作用操作中，可能需要进行清理操作以避免内存泄漏或无效的操作。例如，清除定时器、取消订阅等。可以在函数返回一个清理函数，该清理函数会在组件卸载或依赖项变化时执行。

`useEffect` 在函数组件内部使用，并且按照特定的执行顺序运行。它提供了一种简洁而强大的方式来管理副作用操作，使得组件的逻辑更加清晰和可维护。

### (DEBUG)

app.ts会不支持html语句，改成tsx




在React中，状态更新是异步的。在更新状态时，React可能会将多个状态更新合并为一个批量更新，以提高性能。因此，在调用`setInitialState`后立即访问`initialState`时，可能会看到旧的状态值。

如果想在状态更新后立即访问更新后的`initialState`，可以使用`useEffect`钩子函数来监听`initialState`的变化。

#### ==一个非常致命的前端跨域问题==

在windows本地开发的react前端不管用什么方法都无法解决跨域问题连接一个公网api

解决方案是直接打包dist部署到阿里云nginx，连反向代理都不用就可以正常接口通信。

为了方便开发测试，在本地使用postman的mock server模仿后端行为进行测试。

https://blog.csdn.net/qq_44614026/article/details/124334808

要先启用才会有：

2023/06/15 在一次测试中，意外的就解决了跨域问题，仅仅是设了一下是否携带cookie信息：


根据提供的代码，可能导致提交添加宠物表单后收到的响应是空白且没有成功添加宠物信息到数据库的原因如下：

1. 前端部分：
   - 在提交表单时，点击提交按钮后立即将`addSuccess`状态设置为`true`，这会导致在调用`addPet` API之前就将表单设置为成功状态，而不是等待实际的添加宠物请求完成后再设置成功状态。应该将`setAddSuccess(true)`移动到`if (addPetResponse.code === 200)`条件语句中。
   - 在上传宠物图像时，点击提交按钮后立即将`addSuccess`状态设置为`true`，而不是在实际的添加宠物请求完成后设置成功状态。同样，应将`setAddSuccess(true)`移动到`if (addPetResponse.code === 200)`条件语句中。
2. 后端部分：
   - 在`CabinView`视图的`post`方法中，获取请求参数时使用了`request.POSt`，应该改为`request.POST`。这可能导致无法正确获取请求的参数，进而影响后续的操作。
   - 在`AddPetView`视图的`post`方法中，创建`PetsInfo`对象时，使用了`params.get('p_avatar')`作为`p_avatar`字段的值，但`params.get('p_avatar')`获取的是一个`File`对象，而不是文件路径或文件内容。因此，应将文件保存到服务器上的某个路径，并将该路径作为`p_avatar`字段的值。
   - 在`increment_pet_id`信号接收器中，使用了`instance.uname`作为返回值，但`uname`字段在`PetsInfo`模型中并不存在，可能导致异常。应该返回一个有效的字符串，例如返回`self.pet_name`。

这些问题可能导致表单数据无法正确提交到后端，并且可能导致后端无法正确处理数据并将其保存到数据库中。修复这些问题应该能够解决提交添加宠物表单后收到空白响应且无法成功添加宠物信息到数据库的问题。

## (4) 后端

### (整体目录)

```
VirtualCat_Web
    |-login
    |-media
    |-pets
    |-user
    |-userinfo
    |-VirtualCat_Web
    |-virtualenv
    	|-env-3.9.7
    		|-Lib
    		|-Scripts
    		|-pyvenv.cfg
 	|-db.sqlite3
 	|-manage.py
```



### 1）框架

使用Django框架，系统采用前后端分离设计，后端Django采用Django RestFramework，为前端界面提供数据及其他资源。页面端为微信小程序的开发提供API预置接口。

#### (a) Django Rest framework —— JWT实现登录

JWT （Json Web Token) 主要用于用户登录鉴权，一种认证机制，让后台知道该请求是来自于受信的客户端。


1. 用户使用账号、密码登录应用，登录的请求发送到 Authentication Server。
2. Authentication Server 进行用户验证，然后创建 JWT 字符串返回给客户端。
3. 客户端请求接口时，在请求头带上 JWT。
4. Application Server 验证 JWT 合法性，如果合法则继续调用应用接口返回结果。

```reStructuredText
xxxxx.yyyyy.zzzzz
```


##### Header

JWT 第一部分是头部分，它是一个描述 JWT 元数据的 Json 对象，通常如下所示。

```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

alg 属性表示签名使用的算法，默认为 HMAC SHA256（写为HS256），typ 属性表示令牌的类型，JWT 令牌统一写为JWT。

最后，使用 Base64 URL 算法将上述 JSON 对象转换为字符串保存。

##### Payload

JWT 第二部分是 Payload，也是一个 Json 对象，除了包含需要传递的数据，还有七个默认的字段供选择。

- iss (issuer)：签发人/发行人
- sub (subject)：主题
- aud (audience)：用户
- exp (expiration time)：过期时间
- nbf (Not Before)：生效时间，在此之前是无效的
- iat (Issued At)：签发时间
- jti (JWT ID)：用于标识该 JWT

```json
{
    //默认字段
    "sub":"主题123",
    //自定义字段
    "name":"java技术爱好者",
    "isAdmin":"true",
    "loginTime":"2021-12-05 12:00:03"
}
```

需要注意的是，默认情况下 JWT 是未加密的，任何人都可以解读其内容，因此一些敏感信息不要存放于此，以防信息泄露。

JSON 对象也使用 Base64 URL 算法转换为字符串后保存，是可以反向反编码回原样的，这也是为什么不要在 JWT 中放敏感数据的原因。



##### Signature

```text
header (base64URL 加密后的)

payload (base64URL 加密后的)

secret
```

JWT 第三部分是签名。是这样生成的，首先需要指定一个 secret，该 secret  仅仅保存在服务器中，保证不能让其他用户知道。这个部分需要 base64URL 加密后的 header 和 base64URL 加密后的  payload 使用 . 连接组成的字符串，然后通过header 中声明的加密算法 进行加盐secret组合加密，然后就得出一个签名哈希，也就是Signature，且无法反向解密。

那么 Application Server 如何进行验证呢？可以利用 JWT 前两段，用同一套哈希算法和同一个 secret 计算一个签名值，然后把计算出来的签名值和收到的 JWT 第三段比较，如果相同则认证通过。

```react
loginHandler(){
	this.$axios.post(`${this.$settings.HOST}/user/login/`, {
	  username: this.username,
	  password: this.password
	}).then(response=>{
	  if(this.remember){
	    //记住登录状态
	    sessionStorage.removeItem("user_token")
	    localStorage.user_token = response.token
	  }else{
	    //不记住登录状态
	    localStorage.removeItem("user_token")
	    sessionStorage.user_token = response.token
	  }
	}).catch(error=>{
	  this.$message.error("登录失败")
	  console.log(error.response)
	})
}

```

[JWT参考文档1(定义、与Django的user)](https://blog.csdn.net/weixin_45410366/article/details/125031959)

#### (b) axios 实现前后端通信

##### pre: ajax

**AJAX（ Asynchronous JavaScript and XML）**指异步和JavaScript和XML结合的一种技术。ajax可以实现网页的异步更新，意味着可以不重新加载整个页面的情况下，对网页的某个部分进行更新。组成：

1. 异步的js事件
2. 其他的js（用来处理解析数数据）
3. XMLHttpRequest对象
4. 数据（txt、json、xml、html）

请求原理

1. 创建XMLHttpRequest实例对象；
2. 设置回调函数；
3. 通过XMLHttpRequest.open发出Http网络请求,和服务器端进行连接；
4. 服务器端收到请求，发出请求的数据；
5. 检查网络请求对象的状态，如果响应成功，浏览器接收返回的数据，并且更新页面。

##### Axios

axios是通过Promise对ajax的封装，是一个基于Promise 的Http库，可以在浏览器和Node.js中使用。

简单理解为：axios是一个封装好的，基于Promise的发送请求的方法，不用设置回调，直接调用then方法。

1. 在浏览器中创建XMLHttpRequest对象；
2. 在node.js中创建Http请求
3. 支持拦截请求和响应
4. 自动转换将响应为JSON格式
5. 提供一些并发请求

##### Why axios

1. axios是通过Promise实现ajax技术的一种封装，就像jquery对ajax的封装一样；
2. axios返回的数据是一个promise，ajax返回的数据是回调；
3. axios比ajax更加好用，更加安全；

[axios参考文档（定义、基本使用）](https://blog.csdn.net/Senora/article/details/122220983)

[axios实现登录操作react与Django前后端交互](https://backend.devrank.cn/traffic-information/7081681144735107109)



### 2)协议


#### 数据库

mysql + json + ....

#### 服务器与网络

##### 服务器

服务器：阿里云[ecs-workbench](https://ecs-workbench.aliyun.com/?from=EcsConsole&instanceType=ecs&regionId=cn-shenzhen&instanceId=i-wz9d1gubaizfxmkfak9t&resourceGroupId=&language=zh)

先登录个人阿里云用户再用Linux用户登录服务器：

如果workbench无法登录则下载xshell登录



域名：

apache2 + .....

###### zsh

实例名：




#### 核心开发语言

C/py/java

#### 

### 3) Django

4.1.2

#### (1)virtualenv


```
activate
```



[参考书目《Django+Vue.js实战派》]()

#### (2)路由

urls.py中urlpatterns从上到下进行匹配，不成功返回404




#### (3) 配置中间件行为CORS

后端Django服务器在运行，并且仍然没有接收到数据，可能有以下几个原因：

1. 跨域请求：在开发过程中，如果前端应用运行在不同的域名或端口下，可能会遇到跨域请求的问题。在这种情况下，你需要在Django后端配置跨域访问的允许规则，以便接收来自前端应用的请求。你可以使用Django的CORS插件来处理跨域请求。
2. CSRF保护：Django默认启用了CSRF保护，要求在进行POST请求时，需要包含CSRF令牌。如果你的前端应用发送POST请求时没有正确地包含CSRF令牌，Django会拒绝请求。你可以在前端代码中添加CSRF令牌来解决此问题。你可以通过Django的`csrftoken`cookie来获取CSRF令牌，并将其包含在POST请求的头部中。

https://github-com.translate.goog/adamchainz/django-cors-headers?_x_tr_sl=auto&_x_tr_tl=zh-CN&_x_tr_hl=zh-CN

pip install django-cors-headers

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",# 权限管理模块
    "django.contrib.contenttypes",# 内容管理模块
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders", #跨域
    'rest_framework',
    'rest_framework_simplejwt',
    'login',
    'pets',
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    #前后端分离
    #"django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#CORS
#凡是出现在白名单中的域名，都可以访问后端接口
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8001',
    'http://127.0.0.1:8001',
    'http://xxx.xxx.x.xxx:8001',
)

#运行所有用户访问,和上面的二选一
#CORS_ORIGIN_ALLOW_ALL = True

#指明在跨域访问中，后端是否支持对cookie的操作
CORS_ALLOW_CREDENTIALS = True;
```

```
const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  devServer:{
    host:'localhost',
    port:'8080',
    proxy:{
      '/api':{
          target: 'http://127.0.0.1:8180/attendance',//代理地址，这里设置的地址会代替axios中设置的baseURL
          changeOrigin: true,// 如果接口跨域，需要进行这个参数配置
          //ws: true, // proxy websockets,
          onProxyReq: function (proxyReq) {
            proxyReq.removeHeader('origin')
          },
          //pathRewrite方法重写url
          pathRewrite: {
              '^/api': '/' 
              //pathRewrite: {'^/api': '/'} 重写之后url为 http://xxx.xxx.x.xx:8085/xxxx
              //pathRewrite: {'^/api': '/api'} 重写之后url为 http://xxx.xxx.x.xx:8085/api/xxxx
         }
    }}
  }
})

```



#### (4)migrations 迁移文件 —— 数据库和模型对应

生成迁移文件：根据模型类生成创建表的迁移文件

```
python manage.py makemigrations
```

执行迁移：根据生成的迁移文件在数据库中建表

```python
python manage.py migrate
```



#### (5)后台系统admin


```
python manage.py createsuperuser
```


修改语言及时区

可以直接对数据进行增删改查

##### 自定义管理页面

继承admin.ModelAdmin



#### (6)视图函数

视图函数必须定义一个参数（通过命名为request）

request参数: 用来接受客户端的请求信息

视图函数返回值必须是一个HttpResponse的对象或子类

可以通过django.shortcuts调用

- `django.shortcuts`提供了更高级的函数，可以简化常见的开发任务。例如，`render`函数可以渲染模板并返回一个`HttpResponse`对象，而不需要显式创建`HttpResponse`对象。
- `django.http`提供了更底层的HTTP相关的类和函数，允许你更精细地控制HTTP请求和响应的各个方面。`HttpResponse`类允许你手动设置HTTP状态码、响应头和响应内容等。

使用`django.shortcuts`模块中的函数可以帮助你更快地完成常见任务，而使用`django.http`模块中的类和函数可以提供更大的灵活性和控制力。



MVT思想中view更像MVC的controller




##### 配置URL

方便管理，在应用目录下复制项目的url文件



配置路由规则



访问路径login -> 调用视图函数login

如果访问路径是login开头的则进入login.urls文件进行匹配



视图使用流程：

​	在应用的views定义视图函数

​	配置路由

​		在项目目录的urls.py中关联应用下的urls.py

​		在应用的目录下定义一个urls.py文件（可以直接复制项目目录下的）

​		配置具体的访问规则



#### (7)ORM

Object Relation Mapping


host可以填云数据库的公网ip

 pip install mysqlclient




创建model和表的映射


从后台进行管理


##### 模型类的查询方法

​	get方法：查询一条数据

​			NewsType.object.get(id=3)

​	没找到数据会直接报错（DoesNotExist)

filter根据条件过滤查询

​	返回查询集querySet对象



惰性查询，支持索引和切片



#### 8)接口实现（Postman测试）

##### 登录接口

###### 定义视图

###### 配置url


JSON传递参数


request.POST:获取表单参数

request.body:获取JSON参数

```python
import json
param = request.POST if len(request.POST) else json.loads(request.body.decode())

```

```python
class LoginView(View):
    def login(self, request):
        #获取账号密码
        params = request.POST if len(request.POST) else json.loads(request.body.decode())
        
        print("进入页面")
        account  = params.get('account')
        password = params.POST.get('password')
        #验证用户存在
        username = account
        corr_email = Email.objects.filter(accout=email).first()
        corr_username = Account.objects.filter(accout=uname).first()
        corr_id = Account.objects.filter(accout=uid).first()
        if account == corr_id.uid:
            username = corr_id.uname
            corr_pwd = UserInfo.objects.filter(username=uname).first()
            if password==corr_pwd.pwd:
                return JsonResponse({'code':200,'message':"登录成功"})

        elif account == corr_email.email:
            username = corr_email.uid
            username = Account.objects.filter(username=uid).first()
            username = username.uname
            corr_pwd = UserInfo.objects.filter(username=uname).first()
            if password==corr_pwd.pwd:
                return JsonResponse({'code':200,'message':"登录成功"})

        elif account == corr_username.uname:
            corr_pwd = UserInfo.objects.filter(username=uname).first()
            if password==corr_pwd.pwd:
                return JsonResponse({'code':200,'message':"登录成功"})
        else:
            return JsonResponse({'code':400,'message':"登录失败"},status=400)#登录接口定义视图
class LoginView(View):
    def post(self, request):
        # 处理POST请求
        params = request.POST if len(request.POST) else json.loads(request.body.decode())
        account = params.get('account')
        password = params.get('password')

        if account.isnumeric():
            # 账号是一个数字，按uid匹配
            corr_id = Account.objects.filter(uid=int(account)).first()
            if corr_id:
                # 找到匹配的账号
                # 进一步处理密码验证逻辑
                if password == corr_id.password:
                    return JsonResponse({'code': 200, 'message': "登录成功"})
                else:
                    return JsonResponse({'code': 400, 'message': "密码错误"})
            else:
                return JsonResponse({'code': 400, 'message': "账号不存在"})
        else:
            # 账号不是一个数字，按email或uname匹配
            corr_email = Email.objects.filter(email=account).first()
            corr_username = Account.objects.filter(uname=account).first()

            if corr_email:
                # 账号匹配到了email字段
                username = corr_email.uid
                username = Account.objects.filter(uid=username).first()
                username = username.uname
                corr_pwd = UserInfo.objects.filter(uname=username).first()
                if password == corr_pwd.pwd:
                    return JsonResponse({'code': 200, 'message': "登录成功"})
            elif corr_username:
                # 账号匹配到了uname字段
                corr_pwd = UserInfo.objects.filter(uname=account).first()
                if password == corr_pwd.pwd:
                    return JsonResponse({'code': 200, 'message': "登录成功"})

            return JsonResponse({'code': 400, 'message': "登录失败"}, status=400)
```


##### 接口权限管理

使用Django的会话（session）机制来跟踪用户的认证状态。会话是一种存储在服务器上的数据，用于在用户请求之间存储和共享信息。在Django中，您可以通过使用`request.session`对象来访问和操作会话数据。

```python
 request.session['user_id'] = corr_username.uid
```

```python
class PetView(View):
    #宠物仓接口
    def get(self,request):
        #权限管理
        if 'user_id' not in request.session:
            # 用户未登录，返回未授权的错误信息
            return JsonResponse({'code': 401, 'message': "未授权"}, status=401)
        '''获取宠物列表'''
        petsInfo = PetsInfo.objects.all()
        petcabin = []
        for p in petsInfo:
            dict = {"id":p.pet_id,"name":p.pet_name,"level":p.level}
            petcabin.append(dict)
        return JsonResponse({'code': 1000, 'message': "获取成功","petcabin":petcabin})

    def post(self,request):
        '''添加及其他操作'''
    def delete(self,request):
        '''删除宠物'''
```

另外可以定义一个装饰器函数，用于检查用户是否已登录。如果用户已登录，则继续执行视图函数；否则，返回相应的错误响应。

postman测试时要利用cookie新建环境



##### 一个巨下头的bug

postman的localhoat和127不是默认相同的，然后就会导致明明登录了却还是没权限

改正后如下：



##### Mock

如果你想使用Postman来模拟一个假后端并将响应返回给前端，你可以使用Postman的Mock服务功能。这个功能允许你创建一个模拟的API端点，并定义它的请求和响应。

下面是使用Postman的Mock服务创建假后端的步骤：

1. 打开Postman应用程序并登录到你的帐户。
2. 在顶部导航栏中选择"Mock"选项卡。
3. 点击"Create a Mock"按钮。
4. 在"Create a new mock"页面中，选择一个合适的环境和名称。
5. 在"Choose a collection to mock"下拉菜单中选择你的API请求集合或创建一个新的集合。
6. 定义模拟的请求和响应。
   - 点击"Add a new example"按钮，然后输入请求的URL、请求方法、请求头和请求体。
   - 在"Response"部分中，定义模拟的响应，包括状态码、响应头和响应体。
7. 保存并创建模拟。
8. 一旦模拟创建成功，你将获得一个模拟的URL，类似于`https://mocks.postman.com/<your-mock-id>`.
9. 将模拟的URL配置到你的前端应用程序中，使其发送请求到模拟的URL。
10. 当你的前端应用程序发送请求到模拟的URL时，Postman会返回预定义的响应作为假后端的结果。

通过这些步骤，你可以使用Postman的Mock服务模拟一个假后端，并将预定义的响应返回给前端应用程序。请注意，Mock服务在免费版Postman中有一些限制，如果需要更高级的功能，可能需要升级到付费版。

#### (9) transaction

Django的transaction模块提供了一种在数据库事务中执行操作的方式。事务是数据库操作的一种机制，可以将一组相关的操作作为一个单元进行执行，要么全部成功提交，要么全部回滚到事务开始之前的状态。

transaction模块的主要功能包括：

1. 事务装饰器：transaction模块提供了`@transaction.atomic`装饰器，它可以应用于函数或方法，将其包装在一个数据库事务中。如果在被装饰的函数或方法执行过程中发生异常，事务将会回滚，否则，如果执行成功，事务将会提交。
2. 事务管理器：transaction模块提供了`transaction.atomic()`上下文管理器，可以手动控制事务的开始、提交和回滚。你可以在这个上下文管理器中执行一组数据库操作，并根据需要手动提交或回滚事务。
3. 嵌套事务支持：Django的transaction模块还提供了对嵌套事务的支持。你可以在一个事务中嵌套另一个事务，内层事务的结果将与外层事务保持独立。当外层事务提交时，内层事务的结果也会提交，如果发生回滚，则内层事务也将回滚。

使用transaction模块可以确保在执行数据库操作时保持数据的一致性和完整性。它可以帮助你处理复杂的数据库操作，保证多个操作之间的原子性，以及在出现错误时进行回滚，避免数据不一致的情况。

下面是一个使用transaction模块的示例：

```
python
from django.db import transaction

@transaction.atomic
def my_view(request):
    # 在这个函数中执行数据库操作
    # 如果发生异常，事务将会回滚，否则会提交
    pass
```

在上面的示例中，`my_view`函数被`@transaction.atomic`装饰器修饰，表示将这个函数的执行放在一个数据库事务中。如果函数执行期间出现异常，事务将会回滚，否则，如果执行成功，事务将会提交。

请注意，transaction模块默认会自动管理每个HTTP请求的事务，因此在视图函数中通常不需要显式使用transaction模块。但在一些特殊情况下，例如在一个视图函数中需要执行多个数据库操作，并且希望它们在同一个事务中，你可以使用transaction模块来手动管理事务的边界。

#### (10) 用uWSGI+nginx进行部署

网关，在协议直接进行转换

uwsgi - 线路协议

uWSGI - Web服务器

https://blog.csdn.net/qq_41341757/article/details/113825603



首先在windows对项目进行处理：

```
pip freeze > requirements.txt
```

在服务器解压压缩包后

要将Django项目部署到Ubuntu服务器上，需要执行以下步骤：

步骤1：将项目文件上传到服务器
将项目文件从Windows系统上传到Ubuntu服务器上。你可以使用文件传输工具（如WinSCP）将整个项目文件夹复制到Ubuntu服务器的目标位置。

步骤2：安装Python和虚拟环境
在Ubuntu服务器上安装Python 3.9.7。打开终端，并执行以下命令：

```
sudo apt update
sudo apt install python3.9
```

接下来，安装虚拟环境工具`venv`：

```
sudo apt install python3.9-venv
```

步骤3：创建和激活虚拟环境
在项目文件夹中创建虚拟环境。在终端中导航到项目文件夹的根目录，并执行以下命令：

```
python3.9 -m venv virtualenv/env-3.9.7
```

然后，激活虚拟环境：

```
source virtualenv/env-3.9.7/bin/activate
```

步骤4：安装依赖项
在虚拟环境中，使用`pip`安装项目的依赖项。在终端中执行以下命令，确保当前路径是项目文件夹的根目录：

```
pip install -r requirements.txt
```

这将安装项目所需的所有Python包。

步骤5：配置数据库
如果你的Django项目使用了SQLite数据库（`db.sqlite3`），则无需进行额外配置。但如果你计划使用其他数据库（如MySQL或PostgreSQL），请根据需求进行相应的数据库配置。

步骤6：运行数据库迁移
在终端中执行以下命令，应用数据库迁移：

```
python manage.py migrate
```

这将创建或更新数据库结构。

步骤7：收集静态文件
在终端中执行以下命令，收集项目的静态文件：

```
python manage.py collectstatic
```

这将将静态文件复制到适当的位置，以便Web服务器能够提供它们。

步骤8：运行Django项目
执行以下命令启动Django开发服务器：

```
python manage.py runserver 0.0.0.0:8000
```

这将在服务器的8000端口上启动Django项目。你可以根据需要更改端口号。

现在，你的Django项目应该已经成功部署到Ubuntu服务器上了。你可以使用服务器的IP地址和端口号来访问它。例如，如果服务器的IP地址是192.168.0.100，你可以在浏览器中访问`http://192.168.0.100:8000`来查看你的应用程序。

使用uwsgi部署：



```
sudo netstat -tuln | grep 8000
```

```
pgrep uwsgi
```


通过下面这样配置使得通过公网ip也可以访问服务器私网ip显示的内容：


#### (Debug)





下载sqlite3

https://www.cnblogs.com/xiaoqianbook/articles/14580553.html

https://blog.csdn.net/qq_42685893/article/details/116519140

##### ImageField报错找不到Pillow

https://blog.csdn.net/rusi__/article/details/102958987?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-102958987-blog-98448219.235%5Ev38%5Epc_relevant_default_base3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-102958987-blog-98448219.235%5Ev38%5Epc_relevant_default_base3&utm_relevant_index=1


##### 由于在模型类的字段定义中，无法直接引用其他字段作为默认值。



要实现将`nickname`字段的默认值设置为`username`字段的值，可以通过重写`save()`方法来实现。

在`UserInfo`模型类中添加以下代码：



##### migrate提示被删除的表存在

数字开头文件全删



### 4）阿里云RDS MySQL

https://help.aliyun.com/document_detail/607694.html?spm=5176.28008736.J_6443120770.d941683_1.330b3e4dx0H2ga&pipCode=mysql&goodsId=941683&scm=20140722.M_941683._.V_1

使用workbench连接

ctrl+enter步进



自此数据库上云


### (5) 游戏本体

#### 引擎

Unity

#### 算法

PettingZoo

#### 图形设计

#### 策划

# 3.书面

### (1) 文献

#### 数据库

#### 论文

#### 其他参考资料

[莱洛三角开发](https://gitee.com/coll45/foc/tree/master)

星露谷开发参考

[稚晖君ElectronBot](https://github.com/peng-zhihui/ElectronBot)

### (2) 策划

#### SRS

#### UML

#### PPT

#### 产品说明书

### (3) 财务计算

## (4)架构

### 三层B/S

https://baike.baidu.com/item/B%2FS%E7%BB%93%E6%9E%84/4868588?fr=aladdin

三层架构(3-tier application) 通常意义上的三层架构就是将整个业务应用划分为：表现层（UI）、业务逻辑层（BLL）、数据访问层（DAL）。区分层次的目的即为了“高内聚，低耦合”的思想。
 　　１、表现层（UI）：通俗讲就是展现给用户的界面，即用户在使用一个系统的时候他的所见所得。
 　　２、业务逻辑层（BLL）：针对具体问题的操作，也可以说是对数据层的操作，对数据业务逻辑处理。
 　　３、数据访问层（DAL）：该层所做事务直接操作数据库，针对数据的增添、删除、修改、更新、查找等。
 在软件体系架构设计中，分层式结构是最常见，也是最重要的一种结构。微软推荐的分层式结构一般分为三层，从下至上分别为：数据访问层、业务逻辑层（又或成为领域层）、表示层。
 　　三层结构原理：
 　　3个层次中，系统主要功能和业务逻辑都在业务逻辑层进行处理。
 　　所谓三层体系结构，是在客户端与数据库之间加入了一个“中间层”，也叫组件层。这里所说的三层体系，不是指物理上的三层，不是简单地放置三台机器就是三层体系结构，也不仅仅有B/S应用才是三层体系结构，三层是指逻辑上的三层，即使这三个层放置到一台机器上。
 　　三层体系的应用程序将业务规则、数据访问、合法性校验等工作放到了中间层进行处理。通常情况下，客户端不直接与数据库进行交互，而是通过COM/DCOM通讯与中间层建立连接，再经由中间层与数据库进行交互。
 　　表示层
 　位于最外层（最上层），离用户最近。用于显示数据和接收用户输入的数据，为用户提供一种交互式操作的界面。
 　　
 　　业务逻辑层
 　业务逻辑层（Business Logic  Layer）无疑是系统架构中体现核心价值的部分。它的关注点主要集中在业务规则的制定、业务流程的实现等与业务需求有关的系统设计，也即是说它是与系统所应对的领域（Domain）逻辑有关，很多时候，也将业务逻辑层称为领域层。例如Martin Fowler在《Patterns of Enterprise Application  Architecture》一书中，将整个架构分为三个主要的层：表示层、领域层和数据源层。作为领域驱动设计的先驱Eric  Evans，对业务逻辑层作了更细致地划分，细分为应用层与领域层，通过分层进一步将领域逻辑与领域逻辑的解决方案分离。
 　　
  　业务逻辑层在体系架构中的位置很关键，它处于数据访问层与表示层中间，起到了数据交换中承上启下的作用。由于层是一种弱耦合结构，层与层之间的依赖是向下的，底层对于上层而言是“无知”的，改变上层的设计对于其调用的底层而言没有任何影响。如果在分层设计时，遵循了面向接口设计的思想，那么这种向下的依赖也应该是一种弱依赖关系。因而在不改变接口定义的前提下，理想的分层式架构，应该是一个支持可抽取、可替换的“抽屉”式架构。正因为如此，业务逻辑层的设计对于一个支持可扩展的架构尤为关键，因为它扮演了两个不同的角色。对于数据访问层而言，它是调用者；对于表示层而言，它却是被调用者。依赖与被依赖的关系都纠结在业务逻辑层上，如何实现依赖关系的解耦，则是除了实现业务逻辑之外留给设计师的任务。
 　　数据层
 　数据访问层：有时候也称为是持久层，其功能主要是负责数据库的访问，可以访问数据库系统、二进制文件、文本文档或是XML文档。
 　　
 　　简单的说法就是实现对数据表的Select，Insert，Update，Delete的操作。如果要加入ORM的元素，那么就会包括对象和数据表之间的mapping，以及对象实体的持久化。
 Django -> MVT



# RESTful模式

https://www.jianshu.com/p/210946ab5c1f

RESTFul的架构中，URL满足"动作+URI"的格式，

```
GET：读取（Read），具有幂等性
POST：新建（Create），不具有幂等性
PUT：更新（Update），具有幂等性
PATCH：更新（Update），通常是部分更新
DELETE：删除（Delete），幂等性
```

```
1xx：服务器收到请求，需要请求者继续执行操作
2xx：执行成功
3xx：重定向
4xx：客户端请求错误
5xx：服务器错误

```

