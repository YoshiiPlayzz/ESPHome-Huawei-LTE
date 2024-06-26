import esphome.codegen as cg
import re
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome.core import  CORE
from esphome.components import esp32

CODEOWNERS = ["@YoshiiPlayzz"]
DEPENDENCIES = ["network"]

CONF_HUAWEI_LTE_ID = "huawei_lte_id" 
CONF_HOST = 'host'
CONF_USERNAME = 'username'
CONF_PASSWORD = 'password'


def check_host(val):
    if "http://" in val:
        if re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", val[7:]) != []:
            return val
        else:
            return ""
    else:
        return ""

huawei_lte_ns = cg.esphome_ns.namespace('huawei_lte')
HuaweiLTEComponent = huawei_lte_ns.class_('HuaweiLTE', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(HuaweiLTEComponent),
    cv.Required(CONF_HOST): check_host,
    cv.Required(CONF_USERNAME): cv.string,
    cv.Required(CONF_PASSWORD): cv.string,
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    if CONF_HOST in config:
        cg.add(var.set_host(config[CONF_HOST]))
    if CONF_USERNAME in config:
        cg.add(var.set_username(config[CONF_USERNAME]))
    if CONF_PASSWORD in config:
        cg.add(var.set_password(config[CONF_PASSWORD]))
    
    if CORE.is_esp32:
        if not CORE.using_esp_idf:
            cg.add_library("WiFiClientSecure", None)
            cg.add_library("HTTPClient", None)
    if CORE.is_esp8266:
        cg.add_library("ESP8266HTTPClient", None)
    if CORE.is_rp2040 and CORE.using_arduino:
        cg.add_library("HTTPClient", None)

