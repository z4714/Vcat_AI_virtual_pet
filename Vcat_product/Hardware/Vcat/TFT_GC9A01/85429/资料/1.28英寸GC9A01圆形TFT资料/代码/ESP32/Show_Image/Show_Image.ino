/*******************************************************************************
  ESP32         1.28 LCD_GC9A01
  GND                GND
  3V3                VIN
  18                 SCL
  23                 SDA
  33                 RES
  27                 DC
  5                  CS
  22                 BLK

  代码使用Arduino_GFX库
 ******************************************************************************/

#include <Arduino_GFX_Library.h>
#include "image.h"

#define GFX_BL 22
Arduino_DataBus *bus = new Arduino_ESP32SPI(27 /* DC */, 5 /* CS */, 18 /* SCK */, 23 /* MOSI */, -1 /* MISO */, VSPI /* spi_num */);
Arduino_GFX *gfx = new Arduino_GC9A01(bus, 33 /* RST */, 0 /* rotation */, true /* IPS */);

void setup(void)
{
    gfx->begin();   //初始化LCD
    gfx->fillScreen(BLACK);   //背景色黑色

/*背光设置*/
#ifdef GFX_BL
    pinMode(GFX_BL, OUTPUT);
    digitalWrite(GFX_BL, HIGH);
#endif

    gfx->draw16bitRGBBitmap(0,0,(const uint16_t*)Image_240x240,240,240);

    delay(5000); // 5 seconds
}

void loop()
{
    delay(1000); // 1 second
}
