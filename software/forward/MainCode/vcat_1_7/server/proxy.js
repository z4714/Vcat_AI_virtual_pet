


const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 8002; // 代理服务器的端口

// 允许来自"http://localhost:8001"的跨域请求
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:8001');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Origin');
    res.setHeader('Access-Control-Allow-Credentials', 'true');
    if (req.method === 'OPTIONS') {
      res.sendStatus(200);
    } else {
      next();
    }
  });

app.all('/api/chat/*', async (req, res) => {
  try {
    const response = await axios({
      method: req.method,
      url: `http://59.110.7.219:1002${req.originalUrl}`, // 目标服务器的地址
      data: req.body,
      headers: {
        'Access-Control-Allow-Origin': 'http://localhost:8001', // 请将该地址替换为你的源的地址
        'Access-Control-Allow-Credentials': 'true',
      },
      withCredentials: true,
    });

    res.send(response.data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.listen(PORT, () => {
  console.log(`Proxy server is running on port ${PORT}`);
});