"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[739],{49363:function(P,o,r){r.d(o,{W:function(){return g},x:function(){return _}});var i=r(25359),a=r.n(i),p=r(49811),v=r.n(p),m=r(73669),l=m.Z.create({baseURL:"http://59.110.7.219:1002",withCredentials:!1}),h=m.Z.create({baseURL:"http://localhost:8000",withCredentials:!0}),_=function(){var c=v()(a()().mark(function n(s,d){var u;return a()().wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,h.post("/login/",{account:s,password:d});case 3:return u=e.sent,e.abrupt("return",u.data);case 7:throw e.prev=7,e.t0=e.catch(0),e.t0;case 10:case"end":return e.stop()}},n,null,[[0,7]])}));return function(s,d){return c.apply(this,arguments)}}(),g=function(){var c=v()(a()().mark(function n(s,d){var u;return a()().wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,l.post("/api/chat",{question:s,history:d});case 3:return u=e.sent,e.abrupt("return",u.data);case 7:throw e.prev=7,e.t0=e.catch(0),e.t0;case 10:case"end":return e.stop()}},n,null,[[0,7]])}));return function(s,d){return c.apply(this,arguments)}}()},94191:function(P,o,r){r.d(o,{Z:function(){return g}});var i=r(80696),a=r(24699),p=r(52385),v=r(93236),m={title:"title___xIGPY"},l=r(62086),h=function(n){var s=n.name;return(0,l.jsx)(i.Z,{children:(0,l.jsx)(a.Z,{children:(0,l.jsxs)(p.Z.Title,{level:3,className:m.title,children:["\u6B22\u8FCE\u4F7F\u7528 ",(0,l.jsx)("strong",{children:s})," \uFF01"]})})})},_=h,g=_},18847:function(P,o,r){r.r(o),r.d(o,{default:function(){return O}});var i=r(25359),a=r.n(i),p=r(57213),v=r.n(p),m=r(49811),l=r.n(m),h=r(54306),_=r.n(h),g=r(93236),c=r(83),n=r(95403),s=r(94191),d=r(25450),u={"form-box":"form-box___qZCiP"},M=r(49363),e=r(62086),b=function(){var R=(0,n.useModel)("global"),S=R.name,I=(0,g.useState)(""),y=_()(I,2),C=y[0],U=y[1],E=(0,n.useModel)("@@initialState"),A=E.initialState,x=E.setInitialState,B=function(){var Z=l()(a()().mark(function T(j){var G,L,D,f;return a()().wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return j.preventDefault(),G=j.currentTarget.username.value,L=j.currentTarget.password.value,t.prev=3,t.next=6,(0,M.x)(G,L);case 6:D=t.sent,console.log(D.code),console.log(D.type),f=D,console.log(f.code),console.log(f.message),console.log(f.UserInfo),x(v()(v()({},A),{},{loggedIn:!0,avatar:"/api"+f.UserInfo.photo,loginResponse:f})),n.history.push("/user"),t.next=21;break;case 17:t.prev=17,t.t0=t.catch(3),console.error(t.t0),U("\u767B\u5F55\u5931\u8D25\uFF0C\u8BF7\u68C0\u67E5\u7528\u6237\u540D\u548C\u5BC6\u7801\u3002");case 21:case"end":return t.stop()}},T,null,[[3,17]])}));return function(j){return Z.apply(this,arguments)}}();return(0,e.jsx)(c._z,{ghost:!0,children:(0,e.jsxs)("div",{className:u.container,children:[(0,e.jsx)(s.Z,{name:(0,d.f)(S)}),(0,e.jsxs)("div",{className:u["form-box"],children:[(0,e.jsx)("h1",{children:"Login"}),C&&(0,e.jsx)("p",{className:u.error,children:C}),(0,e.jsxs)("form",{onSubmit:B,children:[(0,e.jsx)("input",{type:"text",name:"username",placeholder:"Username"}),(0,e.jsx)("input",{type:"password",name:"password",placeholder:"Password"}),(0,e.jsx)("input",{type:"submit",value:"\u767B\u5F55"})]}),(0,e.jsxs)("p",{children:["\u65B0\u7528\u6237? ",(0,e.jsx)("a",{href:"#",children:"\u6CE8\u518C\u8D26\u53F7"})]})]})]})})},O=b},25450:function(P,o,r){r.d(o,{f:function(){return i}});function i(a){return a.trim()}}}]);
