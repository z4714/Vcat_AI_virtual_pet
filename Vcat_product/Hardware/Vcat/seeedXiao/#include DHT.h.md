```c
#include <WiFi.h>
#include "DHT.h"
#include "PubSubClient.h"
#define DHTPIN D1
#define DHTTYPE DHT11  
DHT dht(DHTPIN, DHTTYPE);

/* 设备的三元组信息*/
#define PRODUCT_KEY       "ifpbejqG726"     
#define DEVICE_NAME       "XIAO_ESP32C3"       //设备名
#define DEVICE_SECRET     "ef710ff2b76682f28df0e6e98679bb22"
#define REGION_ID         "cn-shanghai"   //看你选择在哪个地方

/* 线上环境域名和端口号，不需要改 */
#define MQTT_SERVER    PRODUCT_KEY".iot-as-mqtt."REGION_ID".aliyuncs.com"
#define MQTT_PORT         1883
#define MQTT_USRNAME      "XIAO_ESP32C3&ifpbejqG726"

#define CLIENT_ID         "ifpbejqG726.XIAO_ESP32C3|securemode=2,signmethod=hmacsha256,timestamp=1685328909683|"
#define MQTT_PASSWD       "eb863cfd2776b4c57afe3e7e89dd4da86c10f53b715293672d1332ce2e78243f"

#define ALINK_BODY_FORMAT         "{\"id\":\"XIAO_ESP32C3\",\"version\":\"1.0\",\"method\":\"thing.event.property.post\",\"params\":%s}\r"    //dht11是设备名，换成你的就可以
#define ALINK_TOPIC_PROP_POST     "/sys/" PRODUCT_KEY "/" DEVICE_NAME "/thing/event/property/post"


const char* ssid     = "ahaNoFace";
const char* password = "deemoender47140222";   

const int buttonPin = 6;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

int buttonState = 0;

WiFiServer server(80);
WiFiClient client1;
const char html_page[] PROGMEM = {
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "Connection: close\r\n"  // the connection will be closed after completion of the response
    //"Refresh: 1\r\n"         // refresh the page automatically every n sec
    "\r\n"
    "<!DOCTYPE HTML>\r\n"
    "<html>\r\n"
    "<head>\r\n"
      "<meta charset=\"UTF-8\">\r\n"
      "<title>Vcat: Cloud pointer to GPT</title>\r\n"
      "<link rel=\"icon\" href=\"img/logo.jpg\" type=\"image/x-icon\">\r\n"
    "</head>\r\n"
    "<body>\r\n"
    "<img alt=\"V\" src=\"./img/V.png\" height=\"100\" width=\"410\">\r\n"
    "<p style=\"text-align:center;\">\r\n"
    "<img alt=\"Cat\" src=\"./img/Cat.png\" height=\"200\" width=\"200\">\r\n"
    "<h1 align=\"center\">Cloud Printer</h1>\r\n" 
    "<h1 align=\"center\">OpenAI ChatGPT</h1>\r\n" 
    "<div style=\"text-align:center;vertical-align:middle;\">"
    "<form action=\"/\" method=\"post\">"
    "<input type=\"text\" placeholder=\"Please enter your question\" size=\"35\" name=\"chatgpttext\" required=\"required\"/>\r\n"
    "<input type=\"submit\" value=\"Submit\" style=\"height:30px; width:80px;\"/>"
    "</form>"
    "</div>"
    "</p>\r\n"
    "</body>\r\n"
    "<html>\r\n"
};


unsigned long lastMs = 0;
WiFiClient espClient;
PubSubClient  client(espClient);

float soil_data ;  
float tep;  
float humidity;
float temp;
String json_String;
String dataStr;
size_t dataStart;
String chatgpt_Q;

//mqtt连接
void mqttCheckConnect()
{
    client.setBufferSize(1024);
    client.setKeepAlive(65);
    while (!client.connected())
    {
        Serial.println("Connecting to MQTT Server ...");
        if(client.connect(CLIENT_ID, MQTT_USRNAME, MQTT_PASSWD))
        {
          Serial.println("MQTT Connected!");
        }
        else{
           Serial.print("MQTT Connect err:");
            Serial.println(client.state());
            delay(5000);

          }
        
    }
}

//发送数据
void mqttIntervalPost()
{
    char param[32];
    char jsonBuf[128];
    
    
    sprintf(param, "{\"humidity\":%f}", humidity);  //换成对应的标识符
    sprintf(jsonBuf, ALINK_BODY_FORMAT, param);
      
    Serial.println(jsonBuf);
    boolean b = client.publish(ALINK_TOPIC_PROP_POST, jsonBuf);
    if(b){
      Serial.println("publish Humidity success"); 
    }else{
      Serial.println("publish Humidity fail"); 
    }
    
    sprintf(param, "{\"temp\":%f}",temp); //换成对应的标识符
    sprintf(jsonBuf, ALINK_BODY_FORMAT, param);
    Serial.println(jsonBuf);
    boolean c = client.publish(ALINK_TOPIC_PROP_POST, jsonBuf);
    
    if(c){
      Serial.println("publish Temperature success"); 
    }else{
      Serial.println("publish Temperature fail"); 
    }
    
}

void WiFiConnect(void){
    WiFi.begin(ssid, password);
    Serial.print("Connecting to ");
    Serial.println(ssid);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected!");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}
void setup()
{   
    
    Serial.begin(115200);
    dht.begin();

    // We start by connecting to a WiFi network
    
    WiFi.mode(WIFI_STA);
    
    WiFi.disconnect();
    while(!Serial);

    Serial.println("WiFi Setup done!");
    WiFiConnect();
    
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    Serial.println();
    Serial.println();

    Serial.println(F("DHTxx test!"));

  


    client.setServer(MQTT_SERVER, MQTT_PORT);
    server.begin();

 
}
void loop()
{
  delay(2000);
  if(millis() - lastMs >= 5000){
    lastMs = millis();
    mqttCheckConnect();
    mqttIntervalPost();
  }
  client.loop();
  delay(200);
  humidity = dht.readHumidity();
  // Read temperature as Celsius (the default)
  temp = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(temp) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, humidity);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(temp, humidity, false);
  
  Serial.print(F("Humidity: "));
  Serial.print(humidity);
  Serial.print(F("%  Temperature: "));
  Serial.print(temp);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));

  client1 = server.available();
if (client1){
    Serial.println("New Client.");           // print a message out the serial port
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;    
    while (client1.connected()){
        if (client1.available()){  // Check if the client is connected
            char c = client1.read();
            json_String += c;
            if (c == '\n' && currentLineIsBlank) {                                 
                dataStr = json_String.substring(0, 4);
                Serial.println(dataStr);
                if(dataStr == "GET "){
                    client1.print(html_page);  //Send the response body to the client
                }         
                else if(dataStr == "POST"){
                    json_String = "";
                    while(client1.available()){
                        json_String += (char)client1.read();
                    }
                    Serial.println(json_String); 
                    dataStart = json_String.indexOf("chatgpttext=") + strlen("chatgpttext=");
                    chatgpt_Q = json_String.substring(dataStart, json_String.length());                    
                    client1.print(html_page);        
                    // close the connection:
                    delay(10);
                    client1.stop();       
                }
                json_String = "";
                break;
            }
            if (c == '\n') {
                // you're starting a new line
                currentLineIsBlank = true;
            }
            else if (c != '\r') {
                // you've gotten a character on the current line
                currentLineIsBlank = false;
            }
        }
    }
}
  
  }

```

#include "DHT.h"
#define DHTPIN 1
#define DHTTYPE DHT11  


DHT dht(DHTPIN, DHTTYPE);

const int buttonPin = 6;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);

  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));

  dht.begin();
}

void loop() {
  // read the state of the pushbutton value:
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));




  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, LOW);
  } else {
    // turn LED off:
    digitalWrite(ledPin, HIGH);
  }
}



```
#include <WiFi.h>
#include "DHT.h"
#define DHTPIN 1
#define DHTTYPE DHT11  


#define WIFI_SSID "ahaNoFace"
#define WIFI_PSW "deemoender47140222"
//MQTT连接物联网平台信息

//MQTT连接物联网平台信息
#define ProductKey    "ifpbejqG726"
#define DeviceName    "Vcat"
#define DeviceSecret  "ef710ff2b76682f28df0e6e98679bb22"


#define clientIDstr   "ifpbejqG726.XIAO_ESP32C3"
#define timestamp     "1685019176440"
#define password      "7C8407EC173E0C587320D31D364255B78863F596"  



//AT 连接WIFI命令
#define AT  "AT\r"
#define AT_OK "OK"
#define AT_REBOOT "AT+REBOOT\r"
#define AT_ECHO_OFF "AT+UARTE=OFF\r"
#define AT_MSG_ON "AT+WEVENT=ON\r"
#define AT_WIFI_START "AT+WJAP=%s,%s\r"
#define AT_WIFI_START_SUCC  "+WEVENT:STATION_UP"
#define AT_WIFI_CLOSE "AT+WJAPQ\r"
#define AT_WIFI_CLOSE_SUCC  "+WEVENT:STATION_DOWN"





//AT MQTT连接物联网平台命令
#define AT_MQTT_AUTH          "AT+MQTTAUTH=%s&%s,%s\r"
#define AT_MQTT_CID           "AT+MQTTCID=%s|securemode=3\\,signmethod=hmacsha1\\,timestamp=%s|\r"
#define AT_MQTT_SOCK          "AT+MQTTSOCK=%s.iot-as-mqtt.cn-shanghai.aliyuncs.com,1883\r"
#define AT_MQTT_CV_OFF        "AT+MQTTCAVERIFY=OFF,OFF\r"
#define AT_MQTT_SSL_OFF       "AT+MQTTSSL=OFF\r"
#define AT_MQTT_RECONN_ON     "AT+MQTTRECONN=ON\r"
#define AT_MQTT_AUTOSTART_OFF "AT+MQTTAUTOSTART=OFF\r"
#define AT_MQTT_ALIVE         "AT+MQTTKEEPALIVE=500\r"
#define AT_MQTT_START         "AT+MQTTSTART\r"
#define AT_MQTT_START_SUCC    "+MQTTEVENT:CONNECT,SUCCESS"
#define AT_MQTT_CLOSE         "AT+MQTTCLOSE\r"
#define AT_MQTT_CLOSE_SUCC    "+MQTTEVENT:CLOSE,SUCCESS"

#define AT_MQTT_PUB_SET       "AT+MQTTPUB=/sys/%s/%s/thing/event/property/post,1\r"
#define AT_MQTT_PUB_DATA      "AT+MQTTSEND=%d\r"
#define JSON_DATA_PACK        "{\"id\":\"100\",\"version\":\"1.0\",\"method\":\"thing.event.property.post\",\"params\":{\"humidity\":%f}}\r"//修改
#define AT_MQTT_PUB_DATA_SUCC "+MQTTEVENT:PUBLISH,SUCCESS"

#define AT_MQTT_SUB_SET       "AT+MQTTSUB=0,/sys/%s/%s/thing/service/alarmFree,1\r"
#define AT_MQTT_SUB_STATUS    "AT+MQTTSTATUS=subscribe,0"
#define ALARM_FREE            "alarmFree"
//缓冲区大小
#define BUFFER_LENGTH 100
#define CMD_LENGTH  100
#define DATA_LENGTH  100
char AT_buffer[BUFFER_LENGTH];
char AT_cmd[CMD_LENGTH];
char AT_data[DATA_LENGTH];

//默认溢出时间
#define DEFAULT_TIMEOUT 10

//采样次数
#define SIMPLE 10

const char* ssid     = "ahaNoFace";
const char* pwd = "deemoender47140222";   


DHT dht(DHTPIN, DHTTYPE);

const int buttonPin = 6;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin
int buttonState = 0;         // variable for reading the pushbutton status

int sensorPin = D1;
int sensorValue = 0;


void setup()
{   
    //pinMode(ledPin, OUTPUT);
    //pinMode(buttonPin, INPUT);
    Serial.begin(115200);
    Serial.println(F("DHTxx test!"));
    dht.begin();
    delay(10);

    // We start by connecting to a WiFi network

    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, pwd);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
     while (1)
  {
   if (!WIFI_Init())
    {
      Serial.println("init");
      continue;
    }
    if(!Ali_connect())
    {
      Serial.println("connect");
      continue;
    }
    break;
  }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}  
void loop() {
  delay(100);
  // put your main code here, to run repeatedly:
  float humidity = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);
 // Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, humidity);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, humidity, false);

  Serial.print(F("Humidity: "));
  Serial.print(humidity);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));

  


  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, LOW);
  } else {
    // turn LED off:
    digitalWrite(ledPin, HIGH);
  }
  
  Wifi_sensor_upload(humidity);


}








bool Wifi_sensor_upload(int humidity)
{
  bool flag;
  int len;
 
  cleanBuffer(AT_data,DATA_LENGTH);

  len = snprintf(AT_data,DATA_LENGTH,JSON_DATA_PACK,humidity);
  printf("%s\n",len); 
  cleanBuffer(AT_cmd,CMD_LENGTH);
  printf("%s\n",snprintf(AT_cmd,CMD_LENGTH,AT_MQTT_PUB_DATA,len+1));
  flag = check_send_cmd(AT_cmd,">",DEFAULT_TIMEOUT);
  if(flag) flag = check_send_cmd(AT_data,AT_MQTT_PUB_DATA_SUCC,20);
  return flag;
}




bool WIFI_Init()
{
  bool flag;

  flag = check_send_cmd(AT,AT_OK,DEFAULT_TIMEOUT);
 
  if(!flag)return false;

  flag = check_send_cmd(AT_REBOOT,AT_OK,20);
  if(!flag)return false;
  delay(500);

  flag = check_send_cmd(AT_ECHO_OFF,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  flag = check_send_cmd(AT_MSG_ON,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;
  
  cleanBuffer(AT_cmd,CMD_LENGTH);
  snprintf(AT_cmd,CMD_LENGTH,AT_WIFI_START,WIFI_SSID,WIFI_PSW);
  flag = check_send_cmd(AT_cmd,AT_WIFI_START_SUCC,100);
  return flag;
}

//连接阿里云物联网平台
bool Ali_connect()
{
  bool flag;

  cleanBuffer(AT_cmd,CMD_LENGTH);
  snprintf(AT_cmd,CMD_LENGTH,AT_MQTT_AUTH,DeviceName,ProductKey,password);
  flag = check_send_cmd(AT_cmd,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  cleanBuffer(AT_cmd,CMD_LENGTH);
  snprintf(AT_cmd,CMD_LENGTH,AT_MQTT_CID,clientIDstr,timestamp);
  flag = check_send_cmd(AT_cmd,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  cleanBuffer(AT_cmd,CMD_LENGTH);
  snprintf(AT_cmd,CMD_LENGTH,AT_MQTT_SOCK,ProductKey);
  flag = check_send_cmd(AT_cmd,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  flag = check_send_cmd(AT_MQTT_CV_OFF,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  flag = check_send_cmd(AT_MQTT_SSL_OFF,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  flag = check_send_cmd(AT_MQTT_RECONN_ON,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  flag = check_send_cmd(AT_MQTT_AUTOSTART_OFF,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  flag = check_send_cmd(AT_MQTT_ALIVE,AT_OK,DEFAULT_TIMEOUT);
  if(!flag)return false;

  flag = check_send_cmd(AT_MQTT_START,AT_MQTT_START_SUCC,20);
  if(!flag)return false;
   //topic设置
  cleanBuffer(AT_cmd,CMD_LENGTH);
  snprintf(AT_cmd,CMD_LENGTH,AT_MQTT_PUB_SET,ProductKey,DeviceName);
  flag = check_send_cmd(AT_cmd,AT_OK,DEFAULT_TIMEOUT);

  cleanBuffer(AT_cmd,CMD_LENGTH);
  snprintf(AT_cmd,CMD_LENGTH,AT_MQTT_SUB_SET,ProductKey,DeviceName);
  flag = check_send_cmd(AT_cmd,AT_OK,DEFAULT_TIMEOUT);
  return flag;
}


//查看回复消息。
bool check_send_cmd(const char *cmd, const char *response, unsigned int timeout)
{
   int i = 0;
  unsigned long timeStart;
  timeStart = millis();
  cleanBuffer(AT_buffer,BUFFER_LENGTH);
  Serial.println(cmd);
  while(1)
  {
    while(Serial.available())
    {
      AT_buffer[i++] = Serial.read();
      
      if(i >= BUFFER_LENGTH)return false;
    }
    if(NULL != strstr(AT_buffer,response))break;
    if((unsigned long)(millis() - timeStart > timeout * 1000)) break;
  }
  Serial.flush(); 
  if(NULL != strstr(AT_buffer,response))return true;
  return false;
}

//清空缓存。
void cleanBuffer(char buffer[], int length)
{
  for (int i=0; i<length; i++)
  {
    buffer[i] = 0;
  }
}
//断掉连接
void disconnect_all()
{
  while(!check_send_cmd(AT_MQTT_CLOSE,AT_MQTT_CLOSE_SUCC,DEFAULT_TIMEOUT));
  while(!check_send_cmd(AT_WIFI_CLOSE,AT_WIFI_CLOSE_SUCC,DEFAULT_TIMEOUT));
}

```

```
#include <WiFi.h>
#include "DHT.h"
#define DHTPIN 1
#define DHTTYPE DHT11  




const char* ssid     = "ahaNoFace";
const char* password = "deemoender47140222";   
DHT dht(DHTPIN, DHTTYPE);
const int buttonPin = 6;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

int buttonState = 0;

void setup()
{
    Serial.begin(115200);
    delay(1000);

    // We start by connecting to a WiFi network

    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);
    Serial.println(F("DHTxx test!"));

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}  
void loop()
{
  delay(2000);
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));
  }
```

#include <WiFi.h>
#include "DHT.h"
#define DHTPIN D1
#define DHTTYPE DHT11  




const char* ssid     = "ahaNoFace";
const char* password = "deemoender47140222";   
DHT dht(DHTPIN, DHTTYPE);
const int buttonPin = 6;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

int buttonState = 0;

void setup()
{
    Serial.begin(115200);
    delay(1000);

    // We start by connecting to a WiFi network
    
    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);
    Serial.println(F("DHTxx test!"));
    
    WiFi.begin(ssid, password);
    
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}  
void loop()
{
  delay(2000);
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));
  }

```
#include <WiFi.h>
#include "DHT.h"
#include "PubSubClient.h"




#define DHTPIN D1
#define DHTTYPE DHT11  
DHT dht(DHTPIN, DHTTYPE);

/* 设备的三元组信息*/
#define PRODUCT_KEY       "ifpbejqG726"     
#define DEVICE_NAME       "XIAO_ESP32C3"       //设备名
#define DEVICE_SECRET     "ef710ff2b76682f28df0e6e98679bb22"
#define REGION_ID         "cn-shanghai"   //看你选择在哪个地方

/* 线上环境域名和端口号，不需要改 */
#define MQTT_SERVER    PRODUCT_KEY".iot-as-mqtt."REGION_ID".aliyuncs.com"
#define MQTT_PORT         1883
#define MQTT_USRNAME      "XIAO_ESP32C3&ifpbejqG726"

#define CLIENT_ID         "ifpbejqG726.XIAO_ESP32C3|securemode=2,signmethod=hmacsha256,timestamp=1685328909683|"
#define MQTT_PASSWD       "eb863cfd2776b4c57afe3e7e89dd4da86c10f53b715293672d1332ce2e78243f"

#define ALINK_BODY_FORMAT         "{\"id\":\"XIAO_ESP32C3\",\"version\":\"1.0\",\"method\":\"thing.event.property.post\",\"params\":%s}\r"    //dht11是设备名，换成你的就可以
#define ALINK_TOPIC_PROP_POST     "/sys/" PRODUCT_KEY "/" DEVICE_NAME "/thing/event/property/post"



const char* ssid     = "ahaNoFace";
const char* password = "deemoender47140222";   

const int buttonPin = 6;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

int buttonState = 0;

WiFiServer server(80);
WiFiClient client1;
const char html_page[] PROGMEM = {
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "Connection: close\r\n"  // the connection will be closed after completion of the response
    //"Refresh: 1\r\n"         // refresh the page automatically every n sec
    "\r\n"
    "<!DOCTYPE HTML>\r\n"
    "<html>\r\n"
    "<head>\r\n"
      "<meta charset=\"UTF-8\">\r\n"
      "<title>Cloud Printer: ChatGPT</title>\r\n"
      "<link rel=\"icon\" href=\"https://files.seeedstudio.com/wiki/xiaoesp32c3-chatgpt/chatgpt-logo.png\" type=\"image/x-icon\">\r\n"
    "</head>\r\n"
    "<body>\r\n"
    "<img alt=\"SEEED\" src=\"https://files.seeedstudio.com/wiki/xiaoesp32c3-chatgpt/logo.png\" height=\"100\" width=\"410\">\r\n"
    "<p style=\"text-align:center;\">\r\n"
    "<img alt=\"ChatGPT\" src=\"https://files.seeedstudio.com/wiki/xiaoesp32c3-chatgpt/chatgpt-logo.png\" height=\"200\" width=\"200\">\r\n"
    "<h1 align=\"center\">Cloud Printer</h1>\r\n" 
    "<h1 align=\"center\">OpenAI ChatGPT</h1>\r\n" 
    "<div style=\"text-align:center;vertical-align:middle;\">"
    "<form action=\"/\" method=\"post\">"
    "<input type=\"text\" placeholder=\"Please enter your question\" size=\"35\" name=\"chatgpttext\" required=\"required\"/>\r\n"
    "<input type=\"submit\" value=\"Submit\" style=\"height:30px; width:80px;\"/>"
    "</form>"
    "</div>"
    "</p>\r\n"
    "</body>\r\n"
    "<html>\r\n"
};


unsigned long lastMs = 0;
WiFiClient espClient;
PubSubClient  client(espClient);

float soil_data ;  
float tep;  
float humidity;
float temp;


//mqtt连接
void mqttCheckConnect()
{
    client.setBufferSize(1024);
    client.setKeepAlive(65);
    while (!client.connected())
    {
        Serial.println("Connecting to MQTT Server ...");
        if(client.connect(CLIENT_ID, MQTT_USRNAME, MQTT_PASSWD))
        {
          Serial.println("MQTT Connected!");
        }
        else{
           Serial.print("MQTT Connect err:");
            Serial.println(client.state());
            delay(5000);

          }
        
    }
}

//发送数据
void mqttIntervalPost()
{
    char param[32];
    char jsonBuf[128];
    
    
    sprintf(param, "{\"humidity\":%f}", humidity);  //换成对应的标识符
    sprintf(jsonBuf, ALINK_BODY_FORMAT, param);
      
    Serial.println(jsonBuf);
    boolean b = client.publish(ALINK_TOPIC_PROP_POST, jsonBuf);
    if(b){
      Serial.println("publish Humidity success"); 
    }else{
      Serial.println("publish Humidity fail"); 
    }
    
    sprintf(param, "{\"temp\":%f}",temp); //换成对应的标识符
    sprintf(jsonBuf, ALINK_BODY_FORMAT, param);
    Serial.println(jsonBuf);
    boolean c = client.publish(ALINK_TOPIC_PROP_POST, jsonBuf);
    
    if(c){
      Serial.println("publish Temperature success"); 
    }else{
      Serial.println("publish Temperature fail"); 
    }
    
}


void setup()
{   
    
    Serial.begin(115200);
    dht.begin();

    // We start by connecting to a WiFi network

    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);
    Serial.println(F("DHTxx test!"));

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    client.setServer(MQTT_SERVER, MQTT_PORT);
    server.begin();
}  
void loop()
{
  delay(2000);
  if(millis() - lastMs >= 5000){
    lastMs = millis();
    mqttCheckConnect();
    mqttIntervalPost();
  }
  client.loop();
  delay(200);
  humidity = dht.readHumidity();
  // Read temperature as Celsius (the default)
  temp = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(temp) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, humidity);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(temp, humidity, false);
  
  Serial.print(F("Humidity: "));
  Serial.print(humidity);
  Serial.print(F("%  Temperature: "));
  Serial.print(temp);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));

  
  
  }
```

