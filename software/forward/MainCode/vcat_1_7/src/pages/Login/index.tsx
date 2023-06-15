import React, { useState, useEffect } from 'react';
import { LoadingOutlined, PlusOutlined } from '@ant-design/icons';
import type { UploadChangeParam } from 'antd/es/upload';
import type { RcFile, UploadFile, UploadProps } from 'antd/es/upload/interface';

import { PageContainer } from '@ant-design/pro-components';
import { Select,DatePicker,message, Upload,Divider  } from 'antd';
import { useModel, history } from '@umijs/max';
import Guide from '@/components/Guide';
import { trim } from '@/utils/format';
import styles from './index.less';
import { login ,checkEmail, checkCAPTCHA, regist} from '@/api';
import { InitialStateType,UserInfo,LoginResponse, } from '@/app';
import { Outlet } from '@umijs/max';

const getBase64 = (img: RcFile, callback: (url: string) => void) => {
  const reader = new FileReader();
  reader.addEventListener('load', () => callback(reader.result as string));
  reader.readAsDataURL(img);
};


const beforeUpload = (file: RcFile) => {
  const isJpgOrPng = file.type === 'image/jpeg' || file.type === 'image/png';
  if (!isJpgOrPng) {
    message.error('You can only upload JPG/PNG file!');
  }
  const isLt2M = file.size / 1024 / 1024 < 2;
  if (!isLt2M) {
    message.error('Image must smaller than 2MB!');
  }
  return isJpgOrPng && isLt2M;
};


const Login: React.FC = () => {
  const { name} = useModel('global');
  const [errorMessage, setErrorMessage] = useState('');
  const { initialState, setInitialState } = useModel('@@initialState');
  const [showEmailForm, setShowEmailForm] = useState(false);
  const [emailValue, setEmailValue] = useState('');
  const [showCAPTCHAForm, setShowCAPTCHAForm] = useState(false);
  const [showRegisterForm, setShowRegisterForm] = useState(false);
  const [genderValue, setGender] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const [imageUrl, setImageUrl] = useState<string>();
  const [registerSuccess, setRegisterSuccess] = useState(false);

  useEffect(() => {
    if (registerSuccess) {
      setTimeout(() => {
        setShowEmailForm(false);
        setShowCAPTCHAForm(false);
        setShowRegisterForm(false);
        setRegisterSuccess(false);
      }, 5000);
    }
  }, [registerSuccess]);


  const handleLogin = async (event: React.FormEvent<HTMLFormElement>) => {
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
      setInitialState({ ...initialState, loggedIn: true,avatar:response.UserInfo.avatar,loginResponse:response  } as InitialStateType);

      // 跳转到用户资料页


      history.push(`/user`);
    } catch (error) {
      console.error(error);
      setErrorMessage('登录失败，请检查用户名和密码。');
    }
  };





  const handleEmail= async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const email = event.currentTarget.email.value;
    
    try {
      const emailResponse = await checkEmail(email);
      console.log(emailResponse.code);
      console.log(emailResponse.message);
      if(emailResponse.code===200){
        setShowEmailForm(false);
        setShowCAPTCHAForm(true);
        setEmailValue(email);
        //event.currentTarget.email.value = '';弃用
       //event.currentTarget.reset(); // 重置表单元素的值
      }
      // 跳转到验证码输入
    } catch (error) {
      console.error(error);
      setErrorMessage('邮箱验证失败');
    }
  };





  const handleCAPTCHA= async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const user_captcha = event.currentTarget.captcha.value;
    try {
      const captchaResponse = await checkCAPTCHA(user_captcha);
      console.log(captchaResponse.code);
      console.log(captchaResponse.message);
      if(captchaResponse.code===200){
        setShowRegisterForm(true);
        setShowCAPTCHAForm(false);
        //event.currentTarget.reset(); // 重置表单元素的值
        //这个问题好像是网页cookie影响的，暂且保留
      }
      // 跳转到用户资料页
 
    } catch (error) {
      console.error(error);
      setErrorMessage('邮箱验证失败');
    }
  };


  const handleRegister= async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const nickname = event.currentTarget.nickname.value;
    const password = event.currentTarget.password.value;
    const birth = event.currentTarget.birth.value;
    const avatar = imageUrl;


    try {
      console.log(emailValue);
      const registerResponse = await regist(emailValue, password,
         nickname, genderValue, birth, avatar);
      
      //console.log(captchaResponse.code);
      console.log(registerResponse);
      if(registerResponse.code===200){
          // 跳转到登录页
          setRegisterSuccess(true);
          setErrorMessage('');
      }
        
    } catch (error) {
      console.error(error);
      setErrorMessage('用户注册失败');
    }
  };

  
  const handleAvatar: UploadProps['onChange'] = (info: UploadChangeParam<UploadFile>) => {
    if (info.file.status === 'uploading') {
      setLoading(true);
      return;
    }
    if (info.file.status === 'done') {
      // Get this url from response in real world.
      getBase64(info.file.originFileObj as RcFile, (url) => {
        setLoading(false);
        setImageUrl(url);
      });
    }
  };


  const uploadButton = (
      <div>
        {loading ? <LoadingOutlined /> : <PlusOutlined />}
        <div style={{ marginTop: 8 }}>Upload</div>
      </div>
  );
  

  return (
    <PageContainer ghost>
      <div className={styles.container}>
        <Guide name={trim(name)} />
        <div className={styles['form-box']}>
          {registerSuccess ? (
            <div className={styles['login-form-box']}>
            <h1>注册成功,5秒后跳转到登录页</h1>
            
          </div>            
          ) : showEmailForm ? (
            
              <div className={styles['register-form-box']}>
                <h1>Register-请输入邮箱</h1>
                {errorMessage && <p className={styles.error}>{errorMessage}</p>}
                {
                  <form onSubmit={handleEmail}>
                    <input type="text" name="email" placeholder="邮箱" />
                    <input type="submit" value="验证邮箱" onClick={() => setShowCAPTCHAForm(true)}/>
                  </form>

                }
              </div>
            
          ) : showCAPTCHAForm ? (
            <div className={styles['register-form-box']}>
              <h1>Register-请输入收到的验证码</h1>
              {errorMessage && <p className={styles.error}>{errorMessage}</p>}
              {
                <form onSubmit={handleCAPTCHA}>
                  <input type="text" name="captcha" placeholder="验证码" />
                  <input type="submit" value="验证" onClick={() => setShowRegisterForm(true)}/>
                </form>
              }
            </div>
          ) : showRegisterForm ? (
            <div className={styles['register-form-box']}>
              <h1>Register-输入用户资料</h1>
              {errorMessage && <p className={styles.error}>{errorMessage}</p>}
              {
                <form onSubmit={handleRegister}>
                  <input type="text" name="nickname" placeholder="用户名称" />
                  <input type="password" name="password" placeholder="密码" />
                  <Select 
                    
                    defaultValue={"武装直升机"}
                    options={[
                      {value:'男',label:'男'},
                      {value:'女',label:'女'},
                      {value:'武装直升机',label:'武装直升机'},
                    
                    ]}
                    onChange={(value)=>setGender(value)}
                  />
                  
                  <DatePicker name='birth' placeholder='生日'/>

                  
                  <Divider>上传头像：</Divider>
                  <Upload
                    name="avatar"
                    listType="picture-circle"
                    className="avatar-uploader"
                    showUploadList={false}
                    
                    beforeUpload={beforeUpload}
                    onChange={handleAvatar}
                    >
                      {imageUrl ? <img src={imageUrl} alt="avatar" style={{ width: '100%' }} /> : uploadButton}
                    </Upload>
                  
                  <input type="submit" value="验证" onClick={() => setShowRegisterForm(true)}/>
                </form>
              }
            </div>

          ) : (
            <div className={styles['login-form-box']}>
              <h1>Login</h1>
              {errorMessage && <p className={styles.error}>{errorMessage}</p>}
              <form onSubmit={handleLogin}>
                <input type="text" name="username" placeholder="Username" />
                <input type="password" name="password" placeholder="Password" />
                <input type="submit" value="登录" />
              </form>
              <p>
                新用户?{' '}
                <a href="#" onClick={() => setShowEmailForm(true)}>
                  注册账号
                </a>
              </p>
            </div>
          )}
        </div>
      </div>
    </PageContainer>
  );
};

export default Login;
