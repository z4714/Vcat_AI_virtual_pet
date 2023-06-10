#include "reg51.h"
#include "lcd_init.h"
#include "lcd.h"
#include "image.h"


int main(void)
{
	LCD_Init();//LCD≥ı ºªØ
	LCD_Fill(0,0,LCD_W,LCD_H,WHITE);
	while(1)
	{
		LCD_ShowPicture(62,62,115,115,YXDZ_logo);
	}
}



