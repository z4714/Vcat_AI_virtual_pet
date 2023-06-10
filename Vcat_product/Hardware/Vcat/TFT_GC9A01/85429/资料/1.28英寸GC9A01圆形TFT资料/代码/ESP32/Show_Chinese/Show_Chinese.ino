/*******************************************************************************
  ESP32         1.28 LCD_GC9A01
  GND                GND
  3V3                VIN
  1                  SCL
  1                  SDA
  1                  RES
  1                  DC
  1                  CS
  1                  BLK

  代码使用U8g2和Arduino_GFX库
 ******************************************************************************/

#include <U8g2lib.h>
#include <Arduino_GFX_Library.h>

#define GFX_BL 22
Arduino_DataBus *bus = new Arduino_ESP32SPI(27 /* DC */, 5 /* CS */, 18 /* SCK */, 23 /* MOSI */, -1 /* MISO */, VSPI /* spi_num */);
Arduino_GFX *gfx = new Arduino_GC9A01(bus, 33 /* RST */, 0 /* rotation */, true /* IPS */);

void setup(void)
{
    gfx->begin();   //初始化LCD
    gfx->fillScreen(BLACK);   //背景色黑色
    gfx->setUTF8Print(true);   //使字体支持Unicode字形
    gfx->setFont(u8g2_font_unifont_t_chinese2);   //设置字体，如果不需要显示中文可以不用这段

/*背光设置*/
#ifdef GFX_BL
    pinMode(GFX_BL, OUTPUT);
    digitalWrite(GFX_BL, HIGH);
#endif

    gfx->setCursor(80, 150);   //设置显示坐标
    gfx->setTextColor(RED);   //显示内容颜色
    gfx->println("优信电子!");   //显示内容

    delay(5000); // 5 seconds
}

void loop()
{
    delay(1000); // 1 second
}
