import React, { useState } from 'react';
import default_head from './svgs/cat1.svg';
import { Modal, Dropdown, Menu, message, Avatar } from 'antd';
import { LogoutOutlined, LoginOutlined } from '@ant-design/icons';
import { useModel,history } from '@umijs/max'; // 导入 Redirect 组件
import './app.less';

export interface InitialStateType {
  name: string;
  avatar: string;
  loggedIn: boolean;
  cat_name: string;
  loginResponse: LoginResponse;
}



export interface UserInfo {
  uid: number;
  username: string;
  email: string;
  nickname: string;
  gender: string | null;
  birth: string;
  date: string;
  avatar: string;
}

export interface LoginResponse {
  code: number;
  message: string;
  UserInfo: UserInfo;
}



export function getInitialState(): InitialStateType {
  return {
    name: '游客',
    avatar: default_head,
    loggedIn: false,
    cat_name: "None",
    loginResponse: {
      code: 0,
      message: "未登录",
      UserInfo: {
        uid: -1,
        username: "未登录",
        email: "",
        nickname: "",
        gender: null,
        birth: "",
        date: "",
        avatar: "",
      },
    }

  };
}




export const layout = () => {
  const [logoutVisible, setLogoutVisible] = useState(false);
  const { initialState, setInitialState } = useModel('@@initialState' as const); // 使用 '@@initialState' 作为命名空间

  const handleLogout = () => {
    alert('退出登录');
    setInitialState({ ...initialState, loggedIn: false } as InitialStateType);
    window.location.href = '/home';
  };

  const handleLogin = () => {
    //alert('登录');
    window.location.href = '/login';
  };

  const menu = (
    <Menu>
      {initialState?.loggedIn ? (
        <Menu.Item key="logout" icon={<LogoutOutlined />} onClick={handleLogout}>
          退出登录
        </Menu.Item>
      ) : (
        <Menu.Item key="login" icon={<LoginOutlined />} onClick={handleLogin}>
          登录
        </Menu.Item>
      )}
    </Menu>
  );

  return {
    title: 'Vcat',
    logo: 'https://raw.githubusercontent.com/z4714/Vcat_AI_virtual_pet/c05ed077aee1bf0a54281bc18a6645ecf2f0c822/product_document/svgs/cat64.svg',
    menu: {
      locale: false,
    },

    rightContentRender: () => (
      <Dropdown
        overlay={menu}
        trigger={['click']}
        visible={logoutVisible}
        onVisibleChange={visible => setLogoutVisible(visible)}
      >
        <span className="avatar-trigger">
          <Avatar src={initialState?.avatar} alt="User Avatar"/>
          {/*<img className="avatar" src={initialState?.avatar} alt="User Avatar" />*/}
        </span>
      </Dropdown>
    ),
  };
};
