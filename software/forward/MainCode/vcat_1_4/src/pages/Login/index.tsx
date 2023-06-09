import React, { useState } from 'react';
import { PageContainer } from '@ant-design/pro-components';
import { useModel, history } from '@umijs/max';
import Guide from '@/components/Guide';
import { trim } from '@/utils/format';
import styles from './index.less';
import { login } from '@/api';
import { InitialStateType,UserInfo,LoginResponse, } from '@/app';



const Login: React.FC = () => {
  const { name } = useModel('global');
  const [errorMessage, setErrorMessage] = useState('');
  const { initialState, setInitialState } = useModel('@@initialState');

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const username = event.currentTarget.username.value;
    const password = event.currentTarget.password.value;

    try {
      const apiResponse = await login(username, password);
      console.log(apiResponse.code);
      console.log(apiResponse.type);
      const response =  apiResponse as LoginResponse;
      //const userInfo = JSON.parse(response.UserInfo);
      console.log(response.code); 
      console.log(response.message); 
      console.log(response.UserInfo); 
      //console.log(userInfo);
      // 设置 loggedIn 为 true
      setInitialState({ ...initialState, loggedIn: true,avatar:"/api"+response.UserInfo.photo,loginResponse:response  } as InitialStateType);

      // 跳转到用户资料页


      history.push(`/user`);
    } catch (error) {
      console.error(error);
      setErrorMessage('登录失败，请检查用户名和密码。');
    }
  };

  return (
    <PageContainer ghost>
      <div className={styles.container}>
        <Guide name={trim(name)} />
        <div className={styles['form-box']}>
          <h1>Login</h1>
          {errorMessage && <p className={styles.error}>{errorMessage}</p>}
          <form onSubmit={handleSubmit}>
            <input type="text" name="username" placeholder="Username" />
            <input type="password" name="password" placeholder="Password" />
            <input type="submit" value="登录" />
          </form>
          <p>新用户? <a href="#">注册账号</a></p>
        </div>
      </div>
    </PageContainer>
  );
};

export default Login;
