#pragma once

#include "esphome/core/component.h"

namespace esphome {
namespace huawei_lte { 
    class HuaweiLTE: public  Component{
        void setup() override;
        void loop() override;
        void dump_config() override;
    };

}
}
