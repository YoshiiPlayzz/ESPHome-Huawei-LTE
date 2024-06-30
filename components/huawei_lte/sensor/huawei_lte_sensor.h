#pragma once

#include "esphome/components/huawei_lte/huawei_lte.h"
#include "esphome/core/log.h"
#include "esphome/components/sensor/sensor.h"
#include <unordered_map>
#include <string>
#include <sstream>
namespace esphome {
namespace huawei_lte {
    
//TODO: Add Sensor Types

enum class HUAWEI_LTE_SENSOR_TYPE{
    DEVICE_INFORMATION, 
    MONITORING_MONTH, 
    UNSET
};

enum class HUAWEI_LTE_SENSOR_SUBTYPE{
    DATA_UP, 
    DATA_DOWN,
    UNSET
};
static const std::unordered_map<HUAWEI_LTE_SENSOR_TYPE, std::string> HUAWEI_LTE_SENSOR_TYPE_MAP = {
    {HUAWEI_LTE_SENSOR_TYPE::DEVICE_INFORMATION, "device/information"},
    {HUAWEI_LTE_SENSOR_TYPE::MONITORING_MONTH, "monitoring/month_statistics_wlan"}
};
static const std::unordered_map<HUAWEI_LTE_SENSOR_SUBTYPE, std::string> HUAWEI_LTE_SENSOR_SUBTYPE_MAP = {
    //MONITORING_MONTH
    {HUAWEI_LTE_SENSOR_SUBTYPE::DATA_UP, HUAWEI_LTE_SENSOR_TYPE_MAP.at(HUAWEI_LTE_SENSOR_TYPE::MONITORING_MONTH) + ":CurrentMonthDownload"},
    {HUAWEI_LTE_SENSOR_SUBTYPE::DATA_DOWN, HUAWEI_LTE_SENSOR_TYPE_MAP.at(HUAWEI_LTE_SENSOR_TYPE::MONITORING_MONTH) + ":CurrentMonthUpload"},
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
  void loop() override;
  void update() override;
  void dump_config() override;
  void set_type(HUAWEI_LTE_SENSOR_TYPE type){this->type_ = type;};
  HUAWEI_LTE_SENSOR_TYPE get_type(){return this->type_; };
  HUAWEI_LTE_SENSOR_SUBTYPE get_subtype(){return this->subtype_; };
  void set_subtype(HUAWEI_LTE_SENSOR_SUBTYPE subtype){this->subtype_ = subtype;};
 private:
    std::vector<std::string> parse(std::string& to_parse, std::vector<std::string> paths);
    std::vector<std::string> split(const std::string& str, char delimiter);
 protected:
    HUAWEI_LTE_SENSOR_TYPE type_ = HUAWEI_LTE_SENSOR_TYPE::UNSET;   
    HUAWEI_LTE_SENSOR_SUBTYPE subtype_ = HUAWEI_LTE_SENSOR_SUBTYPE::UNSET;
};

} 
} 