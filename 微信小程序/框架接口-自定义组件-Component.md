# 框架接口

## 自定义组件

### Component

#### Component(Object object)

创建自定义组件，接受一个 `Object` 类型的参数。



## 参数

#### Object object

| 定义段          | 类型         | 是否必填 | 描述                                                         | 最低版本                                                     |
| :-------------- | :----------- | :------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| properties      | Object Map   | 否       | 组件的对外属性，是属性名到属性设置的映射表                   |                                                              |
| data            | Object       | 否       | 组件的内部数据，和 `properties` 一同用于组件的模板渲染       |                                                              |
| observers       | Object       | 否       | 组件数据字段监听器，用于监听 properties 和 data 的变化，参见 [数据监听器](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/observer.html) | [2.6.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| methods         | Object       | 否       | 组件的方法，包括事件响应函数和任意的自定义方法，关于事件响应函数的使用，参见 [组件间通信与事件](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html) |                                                              |
| behaviors       | String Array | 否       | 类似于mixins和traits的组件间代码复用机制，参见 [behaviors](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/behaviors.html) |                                                              |
| created         | Function     | 否       | 组件生命周期函数-在组件实例刚刚被创建时执行，注意此时不能调用 `setData` ) |                                                              |
| attached        | Function     | 否       | 组件生命周期函数-在组件实例进入页面节点树时执行)             |                                                              |
| ready           | Function     | 否       | 组件生命周期函数-在组件布局完成后执行)                       |                                                              |
| moved           | Function     | 否       | 组件生命周期函数-在组件实例被移动到节点树另一个位置时执行)   |                                                              |
| detached        | Function     | 否       | 组件生命周期函数-在组件实例被从页面节点树移除时执行)         |                                                              |
| relations       | Object       | 否       | 组件间关系定义，参见 [组件间关系](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/relations.html) |                                                              |
| externalClasses | String Array | 否       | 组件接受的外部样式类，参见 [外部样式类](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html) |                                                              |
| options         | Object Map   | 否       | 一些选项（文档中介绍相关特性时会涉及具体的选项设置，这里暂不列举） |                                                              |
| lifetimes       | Object       | 否       | 组件生命周期声明对象，参见 [组件生命周期](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) | [2.2.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| pageLifetimes   | Object       | 否       | 组件所在页面的生命周期声明对象，参见 [组件生命周期](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) | [2.2.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

生成的组件实例可以在组件的方法、生命周期函数和属性 `observer` 中通过 `this` 访问。组件包含一些通用属性和方法。

| 属性名     | 类型   | 描述                                                         |
| :--------- | :----- | :----------------------------------------------------------- |
| is         | String | 组件的文件路径                                               |
| id         | String | 节点id                                                       |
| dataset    | String | 节点dataset                                                  |
| data       | Object | 组件数据，**包括内部数据和属性值**                           |
| properties | Object | 组件数据，**包括内部数据和属性值**（与 `data` 一致）         |
| router     | Object | 相对于当前自定义组件的 [Router](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Router.html) 对象 |
| pageRouter | Object | 相对于当前自定义组件所在页面的 [Router](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Router.html) 对象 |
| renderer   | string | 渲染当前组件的渲染后端                                       |

| 方法名                       | 参数                                                         | 描述                                                         | 最低版本                                                     |
| :--------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| setData                      | Object `newData`                                             | 设置data并执行视图层渲染                                     |                                                              |
| hasBehavior                  | Object `behavior`                                            | 检查组件是否具有 `behavior` （检查时会递归检查被直接或间接引入的所有behavior） |                                                              |
| triggerEvent                 | String `name`, Object `detail`, Object `options`             | 触发事件，参见 [组件间通信与事件](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html) |                                                              |
| createSelectorQuery          |                                                              | 创建一个 [SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html) 对象，选择器选取范围为这个组件实例内 |                                                              |
| createIntersectionObserver   |                                                              | 创建一个 [IntersectionObserver](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.html) 对象，选择器选取范围为这个组件实例内 |                                                              |
| createMediaQueryObserver     |                                                              | 创建一个 [MediaQueryObserver](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/MediaQueryObserver.html) 对象 | [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| selectComponent              | String `selector`                                            | 使用选择器选择组件实例节点，返回匹配到的第一个组件实例对象（会被 `wx://component-export` 影响） |                                                              |
| selectAllComponents          | String `selector`                                            | 使用选择器选择组件实例节点，返回匹配到的全部组件实例对象组成的数组（会被 `wx://component-export` 影响） |                                                              |
| selectOwnerComponent         |                                                              | 选取当前组件节点所在的组件实例（即组件的引用者），返回它的组件实例对象（会被 `wx://component-export` 影响） | [2.8.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| getRelationNodes             | String `relationKey`                                         | 获取这个关系所对应的所有关联节点，参见 [组件间关系](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/relations.html) |                                                              |
| groupSetData                 | Function `callback`                                          | 立刻执行 `callback` ，其中的多个 `setData` 之间不会触发界面绘制（只有某些特殊场景中需要，如用于在不同组件同时 setData 时进行界面绘制同步） | [2.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| getTabBar                    |                                                              | 返回当前页面的 custom-tab-bar 的组件实例，详见[自定义 tabBar](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/custom-tabbar.html) | [2.6.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| getPageId                    |                                                              | 返回页面标识符（一个字符串），可以用来判断几个自定义组件实例是不是在同一个页面内 | [2.7.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| animate                      | String `selector`, Array `keyframes`, Number `duration`, Function `callback` | 执行关键帧动画，详见[动画](https://developers.weixin.qq.com/miniprogram/dev/framework/view/animation.html) | [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| clearAnimation               | String `selector`, Object `options`, Function `callback`     | 清除关键帧动画，详见[动画](https://developers.weixin.qq.com/miniprogram/dev/framework/view/animation.html) | [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| applyAnimatedStyle           | String `selector`, Function `updater`, Object `config`, Function `callback` | 绑定由 worklet 驱动的样式到相应的节点，详见[worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html) | [2.29.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|                              |                                                              |                                                              |                                                              |
| clearAnimatedStyle           | String `selector`, Array `styleIds`, Function `callback`     | 清除节点上 worklet 驱动样式的绑定关系                        | [2.30.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|                              |                                                              |                                                              |                                                              |
| setUpdatePerformanceListener | Object `options`, Function `listener`                        | 设置更新性能统计信息接收函数，详见[获取更新性能统计信息](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/update-perf-stat.html) | [2.12.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

### applyAnimatedStyle 参数定义

| 定义段     | 类型     | 是否必填 | 描述                 | 最低版本                                                     |
| :--------- | :------- | :------- | :------------------- | :----------------------------------------------------------- |
| selector   | String   | 是       | 节点选择器           | [2.29.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| updater    | Function | 是       | worklet 样式更新函数 | [2.29.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| userConfig | Object   | 否       | 配置项               | [2.30.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| callback   | Function | 否       | 完成样式绑定的回调   | [2.30.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

#### 配置项定义

| 属性      | 类型    | 默认值 | 描述                          |
| :-------- | :------ | :----- | :---------------------------- |
| immediate | boolean | true   | 是否立即执行一次 updater 函数 |
| flush     | string  | async  | 刷新时机，枚举值 async / sync |

`selector` 语法同 [SelectorQuery.select](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.select.html)。

默认情况下，`updater` 函数将被执行一次，其结果作为初值被应用到节点上，设置 `immediate: false` 则跳过首次执行。

`updater` 函数返回的 `StyleObject` 支持的样式集，参考 [skyline wxss 样式](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html)。`StyleObject` 的 key 为 css 属性的驼峰写法。

当依赖的 `sharedValue` 值更新时，`updater` 函数将被重新执行，并将新的 `style` 应用到选中节点上。默认情况下，新的样式会在下一个渲染时间片上生效（性能更好），设置 `flush: sync` 可使得在当前渲染时间片上生效。

`callback` 回调返回的 `styleId`，可用于清除样式绑定。

```js
const offset = shared(0)
const styleIds = []
this.applyAnimatedStyle('.box', () => {
  'worklet'
  return {
    transform: `translateX(${offset.value}px) rotate(30deg)`
  }
}, {
  immediate: true,
  flush: false
}, (res) => {
  console.log('animatedStyle 已绑定到节点 ', res.styleId)
  styleIds.push(res.styleId)
})

this.clearAnimatedStyle('.box', styleIds, () => {
  console.log('animatedStyle 已清除绑定')
})
```

### clearAnimatedStyle 参数定义

| 定义段   | 类型            | 是否必填 | 描述                    | 最低版本                                                     |
| :------- | :-------------- | :------- | :---------------------- | :----------------------------------------------------------- |
| selector | String          | 是       | 节点选择器              | [2.30.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| styleIds | `Array<Number>` | 是       | 需要清除的 styleId 集合 | [2.30.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| callback | Function        | 否       | 清除样式绑定的回调      | [2.30.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

`styleIds` 数组为空，则清除选中节点上所有绑定的 `animatedStyle`，需要注意的是样式并不会重置，只是解除了依赖关系。`styleId` 可由 `applyAnimatedStyle` 回调参数中获取。

节点移除时，相关的 `animatedStyle` 会自动释放，`clearAnimatedStyle` 可用于需要提前解绑的情况。

### 示例代码

```js
Component({

  behaviors: [],

  // 属性定义（详情参见下文）
  properties: {
    myProperty: { // 属性名
      type: String,
      value: ''
    },
    myProperty2: String // 简化的定义方式
  },

  data: {}, // 私有数据，可用于模板渲染

  lifetimes: {
    // 生命周期函数，可以为函数，或一个在methods段中定义的方法名
    attached: function () { },
    moved: function () { },
    detached: function () { },
  },

  // 生命周期函数，可以为函数，或一个在methods段中定义的方法名
  attached: function () { }, // 此处attached的声明会被lifetimes字段中的声明覆盖
  ready: function() { },

  pageLifetimes: {
    // 组件所在页面的生命周期函数
    show: function () { },
    hide: function () { },
    resize: function () { },
  },

  methods: {
    onMyButtonTap: function(){
      this.setData({
        // 更新属性和数据的方法与更新页面数据的方法类似
      })
    },
    // 内部方法建议以下划线开头
    _myPrivateMethod: function(){
      // 这里将 data.A[0].B 设为 'myPrivateData'
      this.setData({
        'A[0].B': 'myPrivateData'
      })
    },
    _propertyChange: function(newVal, oldVal) {

    }
  }

})
```

注意：在 `properties` 定义段中，属性名采用驼峰写法（`propertyName`）；在 `wxml` 中，指定属性值时则对应使用连字符写法（`component-tag-name property-name="attr value"`），应用于数据绑定时采用驼峰写法（`attr=""`）。

### properties 定义

| 定义段        | 类型     | 是否必填 | 描述                       | 最低版本                                                     |
| :------------ | :------- | :------- | :------------------------- | :----------------------------------------------------------- |
| type          |          | 是       | 属性的类型                 |                                                              |
| optionalTypes | Array    | 否       | 属性的类型（可以指定多个） | [2.6.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| value         |          | 否       | 属性的初始值               |                                                              |
| observer      | Function | 否       | 属性值变化时的回调函数     |                                                              |

属性值的改变情况可以使用 observer 来监听。目前，在新版本基础库中不推荐使用这个字段，而是使用 Component 构造器的 `observers` 字段代替，它更加强大且性能更好。

**请注意：** 定义段中的 `type` 字段为 **必填** 项，虽然 [2.17.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 及以上的基础库增加了对未填写的兼容（未填写时兼容为填写 `null`），但更低版本的基础库无法处理未填写的情况，最坏可能会使页面无法正常渲染，请注意兼容。

#### 示例代码

```text
Component({
  properties: {
    min: {
      type: Number,
      value: 0
    },
    max: {
      type: Number,
      value: 0,
      observer: function(newVal, oldVal) {
        // 属性值变化时执行
      }
    },
    lastLeaf: {
      // 这个属性可以是 Number 、 String 、 Boolean 三种类型中的一种
      type: Number,
      optionalTypes: [String, Object],
      value: 0
    }
  }
})
```

属性的类型可以为 `String` `Number` `Boolean` `Object` `Array` 其一，也可以为 `null` 表示不限制类型。

多数情况下，属性最好指定一个确切的类型。这样，在 WXML 中以字面量指定属性值时，值可以获得一个确切的类型，如：

```html
<custom-comp min="1" max="5" />
```

此时，由于自定义组件的对应属性被规定为 `Number` 类型， `min` 和 `max` 会被赋值为 `1` 和 `5` ，而非 `"1"` 和 `"5"` ，即：

```js
this.data.min === 1 // true
this.data.max === 5 // true
```

## Bug & Tip

- 使用 `this.data` 可以获取内部数据和属性值；但直接修改它不会将变更应用到界面上，应使用 `setData` 修改。
- 生命周期函数无法在组件方法中通过 `this` 访问到。
- 属性名应避免以 data 开头，即不要命名成 `dataXyz` 这样的形式，因为在 WXML 中， `data-xyz=""` 会被作为节点 dataset 来处理，而不是组件属性。
- 在一个组件的定义和使用时，组件的属性名和 data 字段相互间都不能冲突（尽管它们位于不同的定义段中）。
- 从基础库 [2.0.9](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，对象类型的属性和 data 字段中可以包含函数类型的子字段，即可以通过对象类型的属性字段来传递函数。低于这一版本的基础库不支持这一特性。
- `bug` : 位于 slot 中的自定义组件没有触发 `pageLifetimes` 中声明的页面生命周期，此问题在 [2.5.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 中修复。
- `bug` : 对于 type 为 Object 或 Array 的属性，如果通过该组件自身的 this.setData 来改变属性值的一个子字段，则依旧会触发属性 observer ，且 observer 接收到的 `newVal` 是变化的那个子字段的值， `oldVal` 为空， `changedPath` 包含子字段的字段名相关信息；目前推荐使用 `observers` 