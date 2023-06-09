import axios from 'axios';




const chatApi = axios.create({
  baseURL: '/api/chat',
  //axios 发送跨域请求时，自动携带cookie信息
  withCredentials: false,
});

const loginApi = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,

});


export const login = async (username: string, password: string) => {
  try {
    const response = await loginApi.post('/login/', { account: username, password: password });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const chat = async (question: string, history: []) => {
  try {
    const response = await chatApi.post('/', { question: question, history: history });
    return response.data;
  } catch (error) {
    throw error;
  }
};