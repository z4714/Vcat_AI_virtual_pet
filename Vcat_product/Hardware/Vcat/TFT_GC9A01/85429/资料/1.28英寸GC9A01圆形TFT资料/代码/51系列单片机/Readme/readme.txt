接线说明

	LCD端口定义在 lcd_init.h 文件中   用户若需要修改端口修改 引脚定义部分即可

	默认接线如下
	stc89c516		GC9A01
	
	5V				VIN
	GND				GND
	SCL				P1.0
	SDA				P1.1
	RES				P1.2
	DC				P1.3
	CS				P1.4
	BLK				P1.5
	
	
	
代码说明

	LCD显示部分代码移植中景园代码, lcd.h 文件中包含 颜色填充 画点/线/矩形/圆形  显示汉字(需要自行取模)  图片等函数,用户可根据自己需要自行调用
	
	显示汉字部分数组在 lcdfont.h 文件中  图片在 image.h 中  用户可自行研究移植  
	
	用户移植代码后,代码因空间大小编译不过可以在魔术棒中找到选项 memory model 修改为 XDATA ,值得注意的是用户显示图片非常容易出现空间不够的情况,并且本代码使用 STC89C51/52等空间较小的单片机因空间过小无法显示图片需用户自行修改







