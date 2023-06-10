#include "pbdata.h"
#include "lcd_init.h"
#include "lcd.h"

#include "image.h"

int main(void)
{
	LCD_Init();
	LCD_Fill(0,0,LCD_W,LCD_H,WHITE);   //填充为白色背景色
	while(1)
	{
		LCD_ShowPicture(0,0,LCD_W,LCD_H,YXDZ_logo);   //显示一张图片
	}
}

