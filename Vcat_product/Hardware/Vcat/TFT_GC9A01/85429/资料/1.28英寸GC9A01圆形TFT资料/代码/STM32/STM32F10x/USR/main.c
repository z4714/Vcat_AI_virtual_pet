#include "pbdata.h"
#include "lcd_init.h"
#include "lcd.h"

#include "image.h"

int main(void)
{
	LCD_Init();
	LCD_Fill(0,0,LCD_W,LCD_H,WHITE);   //���Ϊ��ɫ����ɫ
	while(1)
	{
		LCD_ShowPicture(0,0,LCD_W,LCD_H,YXDZ_logo);   //��ʾһ��ͼƬ
	}
}

