#include "huawei_lte_sensor.h"
#include "esphome/core/log.h"
#include "esphome.h"
#include <ArduinoJson.h>
// Copied from esphome/components/http_request/http_request_arduino.h

#if defined(USE_ESP32) || defined(USE_RP2040)
#include <HTTPClient.h>
#endif
#ifdef USE_ESP8266
#include <ESP8266HTTPClient.h>
#ifdef USE_HTTP_REQUEST_ESP8266_HTTPS
#include <WiFiClientSecure.h>
#endif
#endif

namespace esphome
{
  namespace huawei_lte
  {

    static const char *TAG = "huawei_lte.sensor";

    std::string connection_type;
    bool hasSubtype = false;

    void HuaweiLTESensor::setup()
    {
      if (this->type_ != HUAWEI_LTE_SENSOR_TYPE::UNSET)
      {
        connection_type = HUAWEI_LTE_SENSOR_TYPE_MAP.at(this->type_);
        ESP_LOGI(TAG, "Setup of sensor of type '%s' successfull", connection_type.c_str());
        if (this->subtype_ != HUAWEI_LTE_SENSOR_SUBTYPE::UNSET)
        {
          hasSubtype = true;
          ESP_LOGI(TAG, "Subtype used on '%s'", connection_type.c_str());
        }
      }
      else
      {
        ESP_LOGE(TAG, "Please set type of sensor!");
      }
      
      std::string input = "{'CurrentDayDuration': '82912', 'CurrentDayUsed': '8312517125', 'CurrentMonthDownload': '123230947348', 'CurrentMonthUpload': '9950250844', 'MonthDuration': '2403653','MonthLastClearTime': '2024-05-30'}";

      DynamicJsonDocument doc(1024);
      DeserializationError error = deserializeJson(doc, input);
      if (error)
      {
        ESP_LOGE(TAG, "Failed to parse payload");
      }
      else
      {
        ESP_LOGI(TAG, doc["CurrentMonthDownload"]);
      }
    }
    void HuaweiLTESensor::loop()
    {
    }

    void HuaweiLTESensor::update()
    {

      if (WiFi.status() == WL_CONNECTED)
      {
        HTTPClient http;
        ESP_LOGI(TAG, "Connection String: %s", this->parent_->connection_string().c_str());
        // TODO: Change
        http.begin(this->parent_->connection_string().c_str() ); // Specify the URL
        int httpCode = http.GET();       // Make the request

        if (httpCode > 0)
        { // Check for the returning code
          String payload = http.getString();
          ESP_LOGI(TAG, "HTTP request succeeded, payload: %s", payload.c_str());
        }
        else
        {
          ESP_LOGE(TAG, "HTTP request failed, error: %s", http.errorToString(httpCode).c_str());
        }

        http.end(); // Free the resources
      }
      else
      {
        ESP_LOGE(TAG, "WiFi not connected");
      }
    }

    void HuaweiLTESensor::dump_config() { ESP_LOGCONFIG(TAG, "Empty custom sensor"); }

  }
}
