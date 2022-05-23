"""HomeAssistant MQTT Auto Discover"""
import logging
from somfy_protect.api.model import Site, Device

LOGGER = logging.getLogger(__name__)

ALARM_STATUS = {
    "partial": "armed_night",
    "disarmed": "disarmed",
    "armed": "armed_away",
    "triggered": "triggered",
}

DEVICE_CAPABILITIES = {
    "temperature": {
        "type": "sensor",
        "config": {
            "device_class": "temperature",
            "unit_of_measurement": "°C",
        },
    },
    "battery_level": {
        "type": "sensor",
        "config": {
            "device_class": "battery",
            "unit_of_measurement": "%",
        },
    },
    "battery_low": {
        "type": "binary_sensor",
        "config": {
            "device_class": "battery",
        },
    },
    "rlink_quality": {
        "type": "sensor",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
        },
    },
    "rlink_quality_percent": {
        "type": "sensor",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "%",
        },
    },
    "sensitivity": {
        "type": "number",
        "config": {"min": 0, "max": 100},
    },
    "sensitivity_IntelliTag": {
        "type": "number",
        "config": {"min": 1, "max": 9},
    },
    "night_vision": {
        "type": "select",
        "config": {
            "options": ["automatic"],
        },
    },
    "sensitivity_level": {
        "type": "select",
        "config": {
            "options": ["low", "medium", "high"],
        },
    },
    "support_type": {
        "type": "select",
        "config": {
            "options": ["slidedoor", "window", "externdoor", "slidewindow", "garage"],
        },
    },
    "video_mode": {
        "type": "select",
        "config": {
            "options": ["FHD", "HD", "SD"],
        },
    },
    "power_mode": {
        "type": "sensor",
        "config": {},
    },
    "wifi_ssid": {
        "type": "sensor",
        "config": {},
    },
    "fsk_level": {
        "type": "sensor",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
        },
    },
    "ble_level": {
        "type": "sensor",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
        },
    },
    "wifi_level": {
        "type": "sensor",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
        },
    },
    "wifi_level_percent": {
        "type": "sensor",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "%",
        },
    },
    "lora_quality_percent": {
        "type": "sensor",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "%",
        },
    },
    "temperatureAt": {
        "type": "sensor",
        "config": {},
    },
    "last_online_at": {
        "type": "sensor",
        "config": {},
    },
    "last_offline_at": {
        "type": "sensor",
        "config": {},
    },
    "mounted_at": {
        "type": "sensor",
        "config": {},
    },
    "last_shutter_closed_at": {
        "type": "sensor",
        "config": {},
    },
    "last_shutter_opened_at": {
        "type": "sensor",
        "config": {},
    },
    "last_status_at": {
        "type": "sensor",
        "config": {},
    },
    "mfa_last_test_at": {
        "type": "sensor",
        "config": {},
    },
    "mfa_last_test_success_at": {
        "type": "sensor",
        "config": {},
    },
    "mfa_last_online_at": {
        "type": "sensor",
        "config": {},
    },
    "mfa_last_offline_at": {
        "type": "sensor",
        "config": {},
    },
    "mfa_last_connected_at": {
        "type": "sensor",
        "config": {},
    },
    "mfa_last_disconnected_at": {
        "type": "sensor",
        "config": {},
    },
    "lora_last_test_at": {
        "type": "sensor",
        "config": {},
    },
    "lora_last_test_success_at": {
        "type": "sensor",
        "config": {},
    },
    "lora_last_online_at": {
        "type": "sensor",
        "config": {},
    },
    "lora_test_on_going": {
        "type": "sensor",
        "config": {},
    },
    "lora_last_offline_at": {
        "type": "sensor",
        "config": {},
    },
    "lora_last_connected_at": {
        "type": "sensor",
        "config": {},
    },
    "lora_last_disconnected_at": {
        "type": "sensor",
        "config": {},
    },
    "last_check_in_state": {
        "type": "sensor",
        "config": {},
    },
    "last_check_out_state": {
        "type": "sensor",
        "config": {},
    },
    "keep_alive": {
        "type": "sensor",
        "config": {},
    },
    "rlink_state": {
        "type": "sensor",
        "config": {},
    },
    "battery_level_state": {
        "type": "sensor",
        "config": {},
    },
    "power_state": {
        "type": "sensor",
        "config": {},
    },
    "thresholdAcc": {
        "type": "sensor",
        "config": {},
    },
    "night_mode": {
        "type": "sensor",
        "config": {},
    },
    "mfa_quality_percent": {
        "type": "sensor",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "%",
        },
    },
    "recalibration_required": {
        "type": "binary_sensor",
        "config": {
            "device_class": "problem",
        },
    },
    "cover_present": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "device_lost": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "shutter_state": {
        "type": "switch",
        "config": {
            "pl_on": "opened",
            "pl_off": "closed",
        },
    },
    "detection_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "led_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "hdr_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "siren_on_camera_detection_disabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "sound_recording_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "sound_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "light_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "auto_protect_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "night_mode_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "prealarm_enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "enabled": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "sp_smoke_detector_alarm_muted": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "recalibrateable": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "sp_smoke_detector_error_chamber": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "sp_smoke_detector_no_disturb": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "sp_smoke_detector_role": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "end_device",
            "pl_off": "coordinator",
        },
    },
    "sp_smoke_detector_smoke_detection": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
    "snapshot": {
        "type": "switch",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
            "optimistic": "True",
        },
    },
    "presence": {
        "type": "device_tracker",
        "config": {
            " payload_home": "home",
            " payload_not_home": "not_home",
        },
    },
    "motion_sensor": {
        "type": "binary_sensor",
        "config": {
            "pl_on": "True",
            "pl_off": "False",
        },
    },
}


def ha_discovery_alarm(site: Site, mqtt_config: dict, homeassistant_config: dict):
    """Auto Discover Alarm"""
    if homeassistant_config:
        code = homeassistant_config.get("code")
        code_arm_required = homeassistant_config.get("code_arm_required")
        code_disarm_required = homeassistant_config.get("code_disarm_required")
    else:
        code = None
        code_arm_required = None
        code_disarm_required = None

    site_config = {}

    site_info = {
        "identifiers": [site.id],
        "manufacturer": "Somfy",
        "model": "Somfy Home Alarm",
        "name": site.label,
        "sw_version": "SomfyProtect2MQTT",
    }

    command_topic = (
        f"{mqtt_config.get('topic_prefix', 'somfyProtect2mqtt')}/{site.id}/command"
    )
    site_config[
        "topic"
    ] = f"{mqtt_config.get('ha_discover_prefix', 'homeassistant')}/alarm_control_panel/{site.id}/alarm/config"
    site_config["config"] = {
        "name": site.label,
        "unique_id": f"{site.id}_{site.label}",
        "state_topic": f"{mqtt_config.get('topic_prefix', 'somfyProtect2mqtt')}/{site.id}/state",
        "command_topic": command_topic,
        "payload_arm_away": "armed",
        "payload_arm_night": "partial",
        "payload_disarm": "disarmed",
        "value_template": "{{ value_json.security_level }}",
        "device": site_info,
    }
    if code and (isinstance(code, int)):
        site_config["config"]["code"] = code
    if not code_arm_required:
        site_config["config"]["code_arm_required"] = False
    if not code_disarm_required:
        site_config["config"]["code_disarm_required"] = False
    return site_config


def ha_discovery_alarm_actions(site: Site, mqtt_config: dict):
    """Auto Discover Actions"""
    site_config = {}

    site_info = {
        "identifiers": [site.id],
        "manufacturer": "Somfy",
        "model": "Somfy Home Alarm",
        "name": site.label,
        "sw_version": "SomfyProtect2MQTT",
    }

    command_topic = f"{mqtt_config.get('topic_prefix', 'somfyProtect2mqtt')}/{site.id}/siren/command"
    site_config[
        "topic"
    ] = f"{mqtt_config.get('ha_discover_prefix', 'homeassistant')}/switch/{site.id}/siren/config"
    site_config["config"] = {
        "name": f"{site.label} Siren",
        "unique_id": f"{site.id}_{site.label}",
        "command_topic": command_topic,
        "device": site_info,
        "pl_on": "panic",
        "pl_off": "stop",
    }

    return site_config


def ha_discovery_devices(
    site_id: str,
    device: Device,
    mqtt_config: dict,
    sensor_name: str,
):
    """Auto Discover Devices"""
    device_config = {}
    device_type = DEVICE_CAPABILITIES.get(sensor_name).get("type")

    device_info = {
        "identifiers": [device.id],
        "manufacturer": "Somfy",
        "model": device.device_definition.get("label"),
        "name": device.label,
        "sw_version": device.version,
    }

    command_topic = f"{mqtt_config.get('topic_prefix', 'somfyProtect2mqtt')}/{site_id}/{device.id}/{sensor_name}/command"
    device_config[
        "topic"
    ] = f"{mqtt_config.get('ha_discover_prefix', 'homeassistant')}/{device_type}/{site_id}_{device.id}/{sensor_name}/config"
    device_config["config"] = {
        "name": f"{device.label} {sensor_name}",
        "unique_id": f"{device.id}_{sensor_name}",
        "state_topic": f"{mqtt_config.get('topic_prefix', 'somfyProtect2mqtt')}/{site_id}/{device.id}/state",
        "value_template": "{{ value_json." + sensor_name + " }}",
        "device": device_info,
    }

    for config_entry in DEVICE_CAPABILITIES.get(sensor_name).get("config"):
        device_config["config"][config_entry] = (
            DEVICE_CAPABILITIES.get(sensor_name).get("config").get(config_entry)
        )
        # Specifiy for Intellitag Sensivity
        if (
            device.device_definition.get("label") == "IntelliTag"
            and sensor_name == "sensitivity"
        ):
            device_config["config"][config_entry] = (
                DEVICE_CAPABILITIES.get(
                    f"{sensor_name}_{device.device_definition.get('label')}"
                )
                .get("config")
                .get(config_entry)
            )
    if device_type in ("switch", "number", "select"):
        device_config["config"]["command_topic"] = command_topic
    if sensor_name == "snapshot":
        device_config["config"].pop("value_template")
    if sensor_name == "presence":
        device_config["config"][
            "state_topic"
        ] = f"{mqtt_config.get('topic_prefix', 'somfyProtect2mqtt')}/{site_id}/{device.id}/presence"
    if sensor_name == "motion_sensor":
        device_config["config"][
            "state_topic"
        ] = f"{mqtt_config.get('topic_prefix', 'somfyProtect2mqtt')}/{site_id}/{device.id}/pir"

    return device_config


def ha_discovery_cameras(
    site_id: str,
    device: Device,
    mqtt_config: dict,
):
    """Auto Discover Cameras"""
    camera_config = {}

    device_info = {
        "identifiers": [device.id],
        "manufacturer": "Somfy",
        "model": device.device_definition.get("label"),
        "name": device.label,
        "sw_version": device.version,
    }

    camera_config[
        "topic"
    ] = f"{mqtt_config.get('ha_discover_prefix', 'homeassistant')}/camera/{site_id}_{device.id}/snapshot/config"
    camera_config["config"] = {
        "name": f"{device.label} snapshot",
        "unique_id": f"{device.id}_snapshot",
        "topic": f"{mqtt_config.get('topic_prefix', 'somfyProtect2mqtt')}/{site_id}/{device.id}/snapshot",
        "device": device_info,
    }

    return camera_config
