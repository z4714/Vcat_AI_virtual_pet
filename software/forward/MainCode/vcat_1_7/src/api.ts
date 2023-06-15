import axios from 'axios';




const glmApi = axios.create({
  baseURL: 'http://59.110.7.219:1002',
  //axios 发送跨域请求时，自动携带cookie信息
  withCredentials: true,
});

const serverApi = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,

});





export const login = async (username: string, password: string) => {
  try {
    const response = await serverApi.post('/login/', { account: username, password: password });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const chat = async (question: string, history: []) => {
  try {
    const response = await glmApi.post('/api/chat', { question: question, history: history });
    return response.data;
  } catch (error) {
    throw error;
  }
};


export const regist = async (account:string, password:string, nickname:string, gender:string, birth:Date, avatar:string|undefined) => {
  try {
    console.log(account);
    const response = await serverApi.post('/register/userInfo', {account:account, password:password, nickname:nickname, gender:gender, birth:birth, avatar:avatar});
    //uname实际上指的是account,nickname是用户在填写用户资料时填入的用户名称
 
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const checkEmail = async (email: string) => {
  try {
    const response = await serverApi.post('/register/', { email:email });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const checkCAPTCHA = async (captcha: string) => {
  try {
    const response = await serverApi.post('/register/', { captcha:captcha });
    return response.data;
  } catch (error) {
    throw error;
  }
};