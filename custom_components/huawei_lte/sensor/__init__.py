import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (UNIT_EMPTY, ICON_EMPTY, 
                            CONF_TYPE, CONF_ID,
                            CONF_STATE_CLASS, CONF_UNIT_OF_MEASUREMENT,
                            CONF_ICON, CONF_ACCURACY_DECIMALS,
                            CONF_DEVICE_CLASS, DEVICE_CLASS_EMPTY,
                            STATE_CLASS_MEASUREMENT)
from .. import HuaweiLTEComponent, CONF_HUAWEI_LTE_ID, huawei_lte_ns

DEPENDENCIES = ["huawei_lte"]
CODEOWNERS = ["@YoshiiPlayzz"]


HuaweiLTESensor = huawei_lte_ns.class_("HuaweiLTESensor",  sensor.Sensor,  cg.PollingComponent, HuaweiLTEComponent)
HUAWEI_LTE_SENSOR_TYPE = huawei_lte_ns.namespace("HUAWEI_LTE_SENSOR_TYPE")

CONF_SUPPORTED_TYPE = {
    "DEVICE_INFORMATION": {
        CONF_TYPE: HUAWEI_LTE_SENSOR_TYPE.DEVICE_INFORMATION,
        CONF_UNIT_OF_MEASUREMENT: UNIT_EMPTY,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_EMPTY
    },

}
def set_default_based_on_type():
    def set_defaults_(config):
        type = config[CONF_TYPE]
        # set defaults based on sensor type:
        if CONF_STATE_CLASS not in config:
            if CONF_STATE_CLASS in CONF_SUPPORTED_TYPE[type]:
                config[CONF_STATE_CLASS] = sensor.validate_state_class(
                    CONF_SUPPORTED_TYPE[type][CONF_STATE_CLASS]
                )
            else:
                config[CONF_STATE_CLASS] = sensor.validate_state_class(
                    STATE_CLASS_MEASUREMENT
                )

        if (
            CONF_UNIT_OF_MEASUREMENT not in config
            and CONF_UNIT_OF_MEASUREMENT in CONF_SUPPORTED_TYPE[type]
        ):
            config[CONF_UNIT_OF_MEASUREMENT] = CONF_SUPPORTED_TYPE[type][
                CONF_UNIT_OF_MEASUREMENT
            ]

        if CONF_ICON not in config and CONF_ICON in CONF_SUPPORTED_TYPE[type]:
            config[CONF_ICON] = CONF_SUPPORTED_TYPE[type][CONF_ICON]

        if (
            CONF_ACCURACY_DECIMALS not in config
            and CONF_ACCURACY_DECIMALS in CONF_SUPPORTED_TYPE[type]
        ):
            config[CONF_ACCURACY_DECIMALS] = CONF_SUPPORTED_TYPE[type][
                CONF_ACCURACY_DECIMALS
            ]

        if (
            CONF_DEVICE_CLASS not in config
            and CONF_DEVICE_CLASS in CONF_SUPPORTED_TYPE[type]
        ):
            config[CONF_DEVICE_CLASS] = CONF_SUPPORTED_TYPE[type][CONF_DEVICE_CLASS]

        return config

    return set_defaults_

CONFIG_SCHEMA = (
    sensor.sensor_schema()
    .extend({
        cv.GenerateID(): cv.declare_id(HuaweiLTESensor),
        cv.GenerateID(CONF_HUAWEI_LTE_ID): cv.declare_id(HuaweiLTEComponent),
        cv.Required(CONF_TYPE): cv.enum(CONF_SUPPORTED_TYPE, upper=True)
    })
    .extend(cv.COMPONENT_SCHEMA)
    )
FINAL_VALIDATE_SCHEMA = set_default_based_on_type()

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    await cg.register_parented(var, config[CONF_HUAWEI_LTE_ID])
    cg.add(var.set_type(CONF_SUPPORTED_TYPE[config[CONF_TYPE]][CONF_TYPE]))