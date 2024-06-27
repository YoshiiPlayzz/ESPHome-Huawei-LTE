#include "huawei_lte_sensor.h"
#include "esphome/core/log.h"
#include "esphome.h"

namespace esphome {
namespace huawei_lte {

static const char *TAG = "huawei_lte.sensor";

std::string connection_str;
void HuaweiLTESensor::setup() {
    connection_str = HuaweiLTE::connection_string();
}
void HuaweiLTESensor::loop(){
}
void HuaweiLTESensor::update(){
    auto *request = new esphome::http_request::HttpRequestComponent();


}


void HuaweiLTESensor::dump_config() { ESP_LOGCONFIG(TAG, "Empty custom sensor"); }

}  
}  