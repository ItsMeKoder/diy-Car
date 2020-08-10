#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WiFiMulti.h> 
#include <ESP8266mDNS.h>
#include <ESP8266WebServer.h>   // Include the WebServer library

ESP8266WiFiMulti wifiMulti;

ESP8266WebServer server(80);    // Create a webserver object that listens for HTTP request on port 80
const char* ssid = "Devars";  // Enter SSID here
const char* password = "1vaghela";  //Enter Password here

void handleRoot();              // function prototypes for HTTP handlers
void handleNotFound();


int lf=16;
int lb=5;
int rf=4;
int rb=0;


bool lfstatus = LOW;
bool lbstatus = LOW;
bool rfstatus = LOW;
bool rbstatus = LOW;



void handle_OnConnect() {
//  digitalWrite(lf, LOW);
//  digitalWrite(rf, LOW);
//  digitalWrite(lb, LOW);
//  digitalWrite(rb, LOW);
  server.send(200, "text/html", SendHTML()); 
}

void handle_forward() {

  digitalWrite(lf,HIGH);
  digitalWrite(lb,HIGH);
  digitalWrite(rf,HIGH);
  digitalWrite(rb,HIGH);
//  delay(2000);
  digitalWrite(lf,LOW);
  digitalWrite(rf,LOW);
  delay(100);
  digitalWrite(lf,HIGH);
  digitalWrite(lb,HIGH);
  digitalWrite(rf,HIGH);
  digitalWrite(rb,HIGH);
  Serial.println("MOVING FORWARD");
  server.send(200, "text/html", SendHTML()); 
}

void handle_backward() {
  digitalWrite(lf,HIGH);
  digitalWrite(lb,HIGH);
  digitalWrite(rf,HIGH);
  digitalWrite(rb,HIGH);
//  delay(2000);
  digitalWrite(lb,LOW);
  digitalWrite(rb,LOW);
  delay(100);
  digitalWrite(lf,HIGH);
  digitalWrite(lb,HIGH);
  digitalWrite(rf,HIGH);
  digitalWrite(rb,HIGH);
  Serial.println("MOVING BACKWARD");
  server.send(200, "text/html", SendHTML()); 
}

void handle_right() {
  digitalWrite(lf,HIGH);
  digitalWrite(lb,HIGH);
  digitalWrite(rf,HIGH);
  digitalWrite(rb,HIGH);
//  delay(500);
  digitalWrite(lf,LOW);
  digitalWrite(rb,LOW);

  delay(100);
  digitalWrite(lf,HIGH);
  digitalWrite(lb,HIGH);
  digitalWrite(rf,HIGH);
  digitalWrite(rb,HIGH);
  Serial.println("TURNING RIGHT");
  server.send(200, "text/html", SendHTML()); 
}

void handle_left() {
  digitalWrite(lf,HIGH);
  digitalWrite(lb,HIGH);
  digitalWrite(rf,HIGH);
  digitalWrite(rb,HIGH);
//  delay(500);
  digitalWrite(rf,LOW);
  digitalWrite(lb,LOW) ;
  delay(100);
  digitalWrite(lf,HIGH);
  digitalWrite(lb,HIGH);
  digitalWrite(rf,HIGH);
  digitalWrite(rb,HIGH);
  Serial.println("TURNING LEFT");
  server.send(200, "text/html", SendHTML()); 
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}





String SendHTML(){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>Car Control</title>\n";
  ptr +="<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
  ptr +="body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;} h3 {color: #444444;margin-bottom: 50px;}\n";
  ptr +=".button {display: block;width: 80px;background-color: #1abc9c;border: none;color: white;padding: 13px 30px;text-decoration: none;font-size: 25px;margin: 0px auto 35px;cursor: pointer;border-radius: 4px;}\n";
  ptr +=".button-on {background-color: #1abc9c;}\n";
  ptr +=".button-on:active {background-color: #16a085;}\n";
  ptr +=".button-off {background-color: #34495e;}\n";
  ptr +=".button-off:active {background-color: #2c3e50;}\n";
  ptr +="p {font-size: 14px;color: #888;margin-bottom: 10px;}\n";
  ptr +="</style>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<h1>Car Controling</h1>\n";
//  ptr +="<button type=button>forward</button>";
//  ptr +="<button type=button>backward</button>";
//  ptr +="<button type=button>left</button>";
//  ptr +="<a href=\"/right\"></a>";
//  ptr +="<button type=button >Turn right</button>";
    ptr +="<a class=\"button button-on\" href=\"/forward\">Move Forward</a>\n";
    ptr +="<a class=\"button button-on\" href=\"/backward\">Move Backward</a>\n";
    ptr +="<a class=\"button button-on\" href=\"/left\">Turn Right</a>\n";
    ptr +="<a class=\"button button-on\" href=\"/right\">Turn Left</a>\n";
//  
//  if(lfstatus)
//  {ptr +="<p>LED1 Status: ON</p><a class=\"button button-off\" href=\"/led1off\">OFF</a>\n";}
//  else
//  {ptr +="<p>LED1 Status: OFF</p><a class=\"button button-on\" href=\"/led1on\">ON</a>\n";}
//
//  if(led2stat)
//  {ptr +="<p>LED2 Status: ON</p><a class=\"button button-off\" href=\"/led2off\">OFF</a>\n";}
//  else
//  {ptr +="<p>LED2 Status: OFF</p><a class=\"button button-on\" href=\"/led2on\">ON</a>\n";}

  ptr +="</body>\n";
  ptr +="</html>\n";
  return ptr;
}




void handleRoot() {
  server.send(200, "text/html", SendHTML());   // Send HTTP status 200 (Ok) and send some text to the browser/client
}

void handleNotFound(){
  server.send(404, "text/plain", "404: Not found"); // Send HTTP status 404 (Not Found) when there's no handler for the URI in the request
}

void setup() {
  
  pinMode(lf, OUTPUT);     
  pinMode(lb, OUTPUT);     
  pinMode(rf, OUTPUT);     
  pinMode(rb, OUTPUT);  
  
  Serial.begin(115200);         
  delay(10);
  Serial.println('\n');

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
     delay(500);
     Serial.print("*");
  }
  
  Serial.println("");
  Serial.println("WiFi connection Successful");
  Serial.println("The IP Address of ESP8266 Module is: ");
  Serial.print(WiFi.localIP());
  server.on("/", handleRoot);               // Call the 'handleRoot' function when a client requests URI "/"
  server.onNotFound(handleNotFound);        // When a client requests an unknown URI (i.e. something other than "/"), call function "handleNotFound"

  server.begin();                           // Actually start the server
  Serial.println("HTTP server started");

  
  server.on("/", handle_OnConnect);
  server.on("/forward", handle_forward);
  server.on("/backward", handle_backward);
  server.on("/right", handle_right);
  server.on("/left", handle_left);
  server.onNotFound(handle_NotFound);
  
  server.begin();
  Serial.println("HTTP server started");
}


  
// the loop function runs over and over again forever
void loop() {
  server.handleClient();                    // Listen for HTTP requests from clients
}
