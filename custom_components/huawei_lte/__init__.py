import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

CODEOWNERS = ["@YoshiiPlayzz"]

CONF_HUAWEI_LTE_SENSOR_ID = 'huawei_lte_sensor_id'
CONF_HOST = 'host'
CONF_USERNAME = 'username'
CONF_PASSWORD = 'password'

huawei_lte_ns = cg.esphome_ns.namespace('huawei_lte')
HuaweiLTEComponent = huawei_lte_ns.class_('HuaweiLTE', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(HuaweiLTEComponent),
    cv.Required(CONF_HOST): cv.string,
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

