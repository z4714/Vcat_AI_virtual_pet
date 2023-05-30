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
