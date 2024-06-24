#pragma once

#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace huawei_lte {
    
//TODO: Add Sensor Types

enum class HUAWEI_LTE_SENSOR_TYPE{
    UNSET
};

class HuaweiLTESensor: public sensor::Sensor, public PollingComponent {
 public:
  void setup() override;
  void dump_config() override;
  void set_type(HUAWEI_LTE_SENSOR_TYPE type){this->type_ = type;}
 protected:
    HUAWEI_LTE_SENSOR_TYPE type_;   
};

} 
} 