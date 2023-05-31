# 框架接口

## 页面

### page

#### 组件事件处理函数

`Page` 中还可以定义组件事件处理函数。在渲染层的组件中加入[事件绑定](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html)，当事件被触发时，就会执行 Page 中定义的事件处理函数。

**示例代码：**

```html
<view bindtap="viewTap"> click me </view>
Page({
  viewTap: function() {
    console.log('view tap')
  }
})
```

##### Page.route

###### 到当前页面的路径，类型为`String`。

```javascript
Page({
  onShow: function() {
    console.log(this.route)
  }
})
```

##### Page.prototype.setData(Object data, Function callback)

`setData` 函数用于将数据从逻辑层发送到视图层（异步），同时改变对应的 `this.data` 的值（同步）。

#### 参数说明

| 字段     | 类型     | 必填 | 描述                                      | 最低版本                                                     |
| :------- | :------- | :--- | :---------------------------------------- | :----------------------------------------------------------- |
| data     | Object   | 是   | 这次要改变的数据                          |                                                              |
| callback | Function | 否   | setData引起的界面更新渲染完毕后的回调函数 | [1.5.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

`Object` 以 `key: value` 的形式表示，将 `this.data` 中的 `key` 对应的值改变成 `value`。

**其中 `key` 可以以数据路径的形式给出，支持改变数组中的某一项或对象的某个属性，如 `array[2].message`，`a.b.c.d`，并且不需要在 this.data 中预先定义。**

**注意：**

1. **直接修改 this.data 而不调用 this.setData 是无法改变页面的状态的，还会造成数据不一致**。
2. 仅支持设置可 JSON 化的数据。
3. 单次设置的数据不能超过1024kB，请尽量避免一次设置过多的数据。
4. 请不要把 data 中任何一项的 value 设为 `undefined` ，否则这一项将不被设置并可能遗留一些潜在问题。

**示例代码：**

```html
<!--index.wxml-->
<view>{{text}}</view>
<button bindtap="changeText"> Change normal data </button>
<view>{{num}}</view>
<button bindtap="changeNum"> Change normal num </button>
<view>{{array[0].text}}</view>
<button bindtap="changeItemInArray"> Change Array data </button>
<view>{{object.text}}</view>
<button bindtap="changeItemInObject"> Change Object data </button>
<view>{{newField.text}}</view>
<button bindtap="addNewField"> Add new data </button>
// index.js
Page({
  data: {
    text: 'init data',
    num: 0,
    array: [{text: 'init data'}],
    object: {
      text: 'init data'
    }
  },
  changeText: function() {
    // this.data.text = 'changed data' // 不要直接修改 this.data
    // 应该使用 setData
    this.setData({
      text: 'changed data'
    })
  },
  changeNum: function() {
    // 或者，可以修改 this.data 之后马上用 setData 设置一下修改了的字段
    this.data.num = 1
    this.setData({
      num: this.data.num
    })
  },
  changeItemInArray: function() {
    // 对于对象或数组字段，可以直接修改一个其下的子字段，这样做通常比修改整个对象或数组更好
    this.setData({
      'array[0].text':'changed data'
    })
  },
  changeItemInObject: function(){
    this.setData({
      'object.text': 'changed data'
    });
  },
  addNewField: function() {
    this.setData({
      'newField.text': 'new data'
    })
  }
})
```