#include "huawei_lte_sensor.h"
#include "esphome/core/log.h"
#include "esphome.h"

//Copied from esphome/components/http_request/http_request_arduino.h
#if defined(USE_ESP32) || defined(USE_RP2040)
#include <HTTPClient.h>
#endif
#ifdef USE_ESP8266
#include <ESP8266HTTPClient.h>
#ifdef USE_HTTP_REQUEST_ESP8266_HTTPS
#include <WiFiClientSecure.h>
#endif
#endif

namespace esphome {
namespace huawei_lte {

static const char *TAG = "huawei_lte.sensor";

std::string connection_str;
void HuaweiLTESensor::setup() {
    //connection_str = HuaweiLTE::connection_string();
}
void HuaweiLTESensor::loop(){
}
void HuaweiLTESensor::update(){
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin("http://google.com"); // Specify the URL
    int httpCode = http.GET();              // Make the request

    if (httpCode > 0) { // Check for the returning code
      String payload = http.getString();
    
      ESP_LOGI("custom_component", "HTTP request succeeded, payload: %s", payload.c_str());
    } else {
      ESP_LOGE("custom_component", "HTTP request failed, error: %s", http.errorToString(httpCode).c_str());
    }

    http.end(); // Free the resources
  } else {
    ESP_LOGE("custom_component", "WiFi not connected");
  }
}


void HuaweiLTESensor::dump_config() { ESP_LOGCONFIG(TAG, "Empty custom sensor"); }

}  
}  
