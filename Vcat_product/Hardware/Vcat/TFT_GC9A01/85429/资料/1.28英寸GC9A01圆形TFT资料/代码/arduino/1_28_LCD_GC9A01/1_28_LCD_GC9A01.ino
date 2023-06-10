/*
  arduino UNO     1.28 LCD_GC9A01
    GND               GND
    5V                VIN
    D13               SCL
    D11               SDA
    D8                RES
    D7                DC
    D10               CS
    D9                BLK

    程序来源于微雪电子代码修改，以下代码使用arduino UNO在1.28寸LCD gc9a01圆形屏幕上显示一张图片
    其分辨率为115x115,由于arduino UNO空间有限导致显示图片大小受限，用户可自行优化代码
    图片数组存储于image.cpp和.h文件中，需要更换显示内容可自行修改
*/



#include <SPI.h>
#include "LCD_Driver.h"
#include "GUI_Paint.h"
#include "image.h"

void setup()
{
  Config_Init();
  LCD_Init();
  LCD_SetBacklight(1000);
  Paint_NewImage(LCD_WIDTH, LCD_HEIGHT, 0, BLACK);
  Paint_Clear(WHITE);

  Paint_DrawImage(gImage_115x115, 62, 62, 115, 115);

}
void loop()
{
  
}



/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
