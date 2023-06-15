import React, { useEffect, useState } from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Avatar } from 'antd';
import { useParams,useModel,useLocation } from '@umijs/max'; // 导入 Redirect 组件
import { InitialStateType,UserInfo,LoginResponse,getInitialState } from '@/app';


const User: React.FC = () => {

  //const location = useLocation();
  //const response = location.state as LoginResponse;

  const { initialState, setInitialState } = useModel('@@initialState');
  const [updatedInitialState, setUpdatedInitialState] = useState(initialState);
  useEffect(() => {
    setUpdatedInitialState(initialState);
  }, [initialState]);
  const init = updatedInitialState as InitialStateType;
  const response = init.loginResponse;
  console.log(response)
  const userInfo = response.UserInfo;
  //const userInfo = JSON.parse(response);
 

  console.log(response.code);
  //if (response.code === 200) {


        // 更新应用状态中的用户信息和头像
        //setInitialState({ ...initialState, loggedIn: true,avatar:userInfo.photo,loginResponse:response } as InitialStateType);
    //  } else {
        // 处理获取用户信息失败的情况
     // }
  


  if (!userInfo) {
    return null; 
  }



  return (
    <PageContainer>
      <Card>
        <Card.Meta
          avatar={<Avatar src={userInfo.avatar} />}
          title={userInfo.username}
          description={userInfo.email}
        />
        <p>Nickname: {userInfo.nickname}</p>
        <p>Gender: {userInfo.gender}</p>
        <p>Birth: {userInfo.birth}</p>
        <p>Registration Date: {userInfo.date}</p>
      </Card>
    </PageContainer>
  );
};

export default User;
