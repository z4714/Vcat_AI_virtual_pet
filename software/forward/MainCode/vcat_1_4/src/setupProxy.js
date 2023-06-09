const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app){


	app.use(
		'/api/chat',
		createProxyMiddleware({
			target:'http://59.110.7.219:1002',
			changeOrigin:true,
			pathRewrite: {'^/api/chat': ''}
		})
	);
};
