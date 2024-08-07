import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ACCURACY_DECIMALS,
    CONF_DEVICE_CLASS,
    CONF_ICON,
    CONF_ID,
    CONF_STATE_CLASS,
    CONF_TYPE,
    CONF_UNIT_OF_MEASUREMENT,
    DEVICE_CLASS_APPARENT_POWER,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_DATA_SIZE,
    ICON_BATTERY,
    ICON_POWER,
    ICON_THERMOMETER,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_BYTES,
    UNIT_KILOWATT_HOURS,
    UNIT_MINUTE,
    UNIT_PERCENT,
    UNIT_VOLT,
    UNIT_VOLT_AMPS,
    UNIT_WATT,
)

from .. import CONF_HUAWEI_LTE_ID, HuaweiLTEComponent, huawei_lte_ns


DEPENDENCIES = ["huawei_lte"]
CODEOWNERS = ["@YoshiiPlayzz"]
CONF_SUBTYPE = "subtype"

HuaweiLTESensor = huawei_lte_ns.class_("HuaweiLTESensor",  sensor.Sensor,  cg.PollingComponent)
HUAWEI_LTE_SENSOR_TYPE = huawei_lte_ns.namespace("HUAWEI_LTE_SENSOR_TYPE")
HUAWEI_LTE_SENSOR_SUBTYPE = huawei_lte_ns.namespace("HUAWEI_LTE_SENSOR_SUBTYPE")

CONF_SUPPORTED_TYPE = {
    "DEVICE_INFORMATION": {
        CONF_TYPE: HUAWEI_LTE_SENSOR_TYPE.DEVICE_INFORMATION,
        CONF_UNIT_OF_MEASUREMENT: UNIT_EMPTY,
        CONF_ACCURACY_DECIMALS: 1,
        CONF_DEVICE_CLASS: DEVICE_CLASS_EMPTY
    },
    "MONITORING_MONTH": {
        CONF_TYPE: HUAWEI_LTE_SENSOR_TYPE.MONITORING_MONTH,
        CONF_UNIT_OF_MEASUREMENT: UNIT_BYTES,
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_DATA_SIZE
    }
}
CONF_SUPPORTED_SUBTYPE = {
    "DATA_UP": {
        CONF_TYPE: HUAWEI_LTE_SENSOR_TYPE.MONITORING_MONTH,
        CONF_UNIT_OF_MEASUREMENT: UNIT_BYTES,
        CONF_SUBTYPE: HUAWEI_LTE_SENSOR_SUBTYPE.DATA_UP,
        CONF_ICON: "mdi:wifi-arrow-up",
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_DATA_SIZE
    },
      "DATA_DOWN": {
        CONF_TYPE: HUAWEI_LTE_SENSOR_TYPE.MONITORING_MONTH,
        CONF_SUBTYPE: HUAWEI_LTE_SENSOR_SUBTYPE.DATA_DOWN,
        CONF_UNIT_OF_MEASUREMENT: UNIT_BYTES,
        CONF_ICON: "mdi:wifi-arrow-down",
        CONF_ACCURACY_DECIMALS: 0,
        CONF_DEVICE_CLASS: DEVICE_CLASS_DATA_SIZE
    }
}

def set_default_based_on_type():
    def set_defaults_(config):
        type = config[CONF_TYPE]
        type_dict = CONF_SUPPORTED_TYPE
        if CONF_SUBTYPE in config:
            type_dict = CONF_SUPPORTED_SUBTYPE
            type = config[CONF_SUBTYPE]
            print("Using subtype dict.")
      

        # set defaults based on sensor type:
        if CONF_STATE_CLASS not in config:
            if CONF_STATE_CLASS in type_dict[type]:
                config[CONF_STATE_CLASS] = sensor.validate_state_class(
                    type_dict[type][CONF_STATE_CLASS]
                )
            else:
                config[CONF_STATE_CLASS] = sensor.validate_state_class(
                    STATE_CLASS_MEASUREMENT
                )

        if (
            CONF_UNIT_OF_MEASUREMENT not in config
            and CONF_UNIT_OF_MEASUREMENT in type_dict[type]
        ):
            config[CONF_UNIT_OF_MEASUREMENT] = type_dict[type][
                CONF_UNIT_OF_MEASUREMENT
            ]

        if CONF_ICON not in config and CONF_ICON in type_dict[type]:
            config[CONF_ICON] = type_dict[type][CONF_ICON]

        if (
            CONF_ACCURACY_DECIMALS not in config
            and CONF_ACCURACY_DECIMALS in type_dict[type]
        ):
            config[CONF_ACCURACY_DECIMALS] = type_dict[type][
                CONF_ACCURACY_DECIMALS
            ]

        if (
            CONF_DEVICE_CLASS not in config
            and CONF_DEVICE_CLASS in type_dict[type]
        ):
            config[CONF_DEVICE_CLASS] = type_dict[type][CONF_DEVICE_CLASS]

        return config

    return set_defaults_

CONFIG_SCHEMA = sensor.sensor_schema(HuaweiLTESensor, unit_of_measurement=UNIT_EMPTY, icon=ICON_BATTERY, accuracy_decimals=1).extend(
    {
        cv.GenerateID(): cv.declare_id(HuaweiLTESensor),
        cv.GenerateID(CONF_HUAWEI_LTE_ID): cv.use_id(HuaweiLTEComponent),
        cv.Required(CONF_TYPE): cv.enum(CONF_SUPPORTED_TYPE, upper=True),
        cv.Optional(CONF_SUBTYPE): cv.enum(CONF_SUPPORTED_SUBTYPE, upper=True),
    }).extend(cv.COMPONENT_SCHEMA).extend(cv.polling_component_schema("20s"))
    
FINAL_VALIDATE_SCHEMA = set_default_based_on_type()

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await sensor.register_sensor(var, config)
    await cg.register_component(var, config)
    await cg.register_parented(var, config[CONF_HUAWEI_LTE_ID])
    cg.add(var.set_type(CONF_SUPPORTED_TYPE[config[CONF_TYPE]][CONF_TYPE]))
    if CONF_SUBTYPE in config:
        cg.add(var.set_subtype(CONF_SUPPORTED_SUBTYPE[config[CONF_SUBTYPE]][CONF_SUBTYPE]))