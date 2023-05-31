# 组件-视图容器

# cover-image

目前[原生组件](https://developers.weixin.qq.com/miniprogram/dev/component/native-component.html)均已支持同层渲染，建议使用 [image](https://developers.weixin.qq.com/miniprogram/dev/component/image.html) 替代



## 功能描述

覆盖在原生组件之上的图片视图。

可覆盖的原生组件同[cover-view](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html)，支持嵌套在[cover-view](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html)里。

## 属性说明

|      | 属性            | 类型        | 默认值      | 必填 | 说明                                                         | 最低版本                                                     |
| :--- | :-------------- | :---------- | :---------- | :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
|      | src             | string      |             | 否   | 图标路径，支持临时路径、网络地址（1.6.0起支持）、云文件ID（2.2.3起支持）。 | [1.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | referrer-policy | string      | no-referrer | 否   | 格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      |                 |             |             |      |                                                              |                                                              |
|      | bindload        | eventhandle |             | 否   | 图片加载成功时触发                                           | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | binderror       | eventhandle |             | 否   | 图片加载失败时触发                                           | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

#### 支持的格式

| 格式   | iOS  | Android   |
| :----- | :--- | :-------- |
| JPG    | √    | √         |
| PNG    | √    | √         |
| SVG    | x    | x         |
| WEBP   | √    | √         |
| GIF    | √    | √         |
| BASE64 | x    | x相关回答 |



