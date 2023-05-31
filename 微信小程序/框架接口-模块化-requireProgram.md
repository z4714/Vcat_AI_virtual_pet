# 框架接口

## 模块化

requireMiniProgram

### any requireMiniProgram()

插件引入当前使用者小程序。返回使用者小程序通过插件配置中 `export` 暴露的接口。参考 [使用插件 - 导出到插件](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/using.html#导出到插件)

**该接口仅在插件中存在。**

## 参数

> 该接口不需要参数

## 示例代码

```javascript
// in plugin
var mp = requireMiniProgram()
console.log(mp.whoami)  // 'Wechat MiniProgram'
```