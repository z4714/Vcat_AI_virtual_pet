接线说明

	LCD端口定义在 lcd_init.h 文件中   用户若需要修改端口，除了需要修改 lcd_init.h 文件中的宏定义外还需修改 lcd_init.c 中函数 void LCD_GPIO_Init(void); 对 GPIO 引脚以及时钟初始化部分

	默认接线如下
	stm32F10x			GC9A01
	
	3V3				VIN
	GND				GND
	SCL				PA5
	SDA				PA4
	RES				PA6
	DC				PA7
	CS				PB6
	BLK				PB7
	
	
	
代码说明

	LCD显示部分代码移植中景园代码, lcd.h 文件中包含 颜色填充 画点/线/矩形/圆形  显示汉字(需要自行取模)  图片等函数,用户可根据自己需要自行调用
	
	显示汉字部分数组在 lcdfont.h 文件中  图片在 image.h 中  用户可自行研究移植







