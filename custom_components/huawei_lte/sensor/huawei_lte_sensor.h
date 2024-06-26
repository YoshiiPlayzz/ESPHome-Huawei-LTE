#pragma once

#include "esphome/components/sensor/sensor.h"
#include "esphome/components/huawei_lte/huawei_lte.h"
#include "esphome/core/log.h"

namespace esphome {
namespace huawei_lte {
    
//TODO: Add Sensor Types

enum class HUAWEI_LTE_SENSOR_TYPE: std::string{
    DEVICE_INFORMATION = "device/information",
    UNSET = "",
};
static const char *enum_to_c_str(const HUAWEI_LTE_SENSOR_TYPE val) {
switch(val){
    case HUAWEI_LTE_SENSOR_TYPE::DEVICE_INFORMATION:
        return "DEVICE_INFORMATION";
    case  HUAWEI_LTE_SENSOR_TYPE::UNSET:
        return "UNSET";
    default:
        return "";
}
}

class HuaweiLTESensor: public sensor::Sensor, public PollingComponent, public Parented<HuaweiLTE> {
 public:
  void setup() override;
  void dump_config() override;
  void set_type(HUAWEI_LTE_SENSOR_TYPE type){this->type_ = type;}
  
 protected:
    HUAWEI_LTE_SENSOR_TYPE type_;   
};

} 
} 