#pragma once

#include "esphome/core/component.h"
#include "esphome/core/defines.h"


namespace esphome {
namespace huawei_lte { 
    class HuaweiLTE: public Component{
     public:
        void setup() override;
        void loop() override;
        void dump_config() override;
        void set_host(std::string host){
            this->host_ = host;
        };
        void set_username(std::string username){
            this->username_ = username;
        };
        void set_password(std::string password){
            this->password_ = password;
        };
        std::string connection_string(){
            return this->host_.substr(1, 7) + this->username_ + ":" + this->password_ + "@"+this->host_.substr(7);
        }
     protected:
        std::string host_;
        std::string username_;
        std::string password_;

        
    };

}
}
