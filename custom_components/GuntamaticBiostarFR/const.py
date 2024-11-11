"""The GuntamaticBiostar component for controlling the Guntamatic Biostar heating via home assistant / API"""
from __future__ import annotations

from dataclasses import dataclass
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.binary_sensor import (
    # BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)

from homeassistant.components.select import SelectEntityDescription

from homeassistant.const import (
    PERCENTAGE,
    Platform,
    UnitOfTemperature,
    UnitOfTime,
    UnitOfVolume,
)
from homeassistant.helpers.entity import EntityCategory

PLATFORMS = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.SELECT,
]

# Global values
DOMAIN = "GuntamaticBiostarFR"
MANUFACTURER = "Guntamatic"
MODEL = "Biostar"
DATA_SCHEMA_HOST = "host"
DATA_SCHEMA_API_KEY = "api_key"

# Data schema required by configuration flow
DATA_SCHEMA = vol.Schema(
    {
        vol.Required(DATA_SCHEMA_HOST): cv.string,
        vol.Required(DATA_SCHEMA_API_KEY): cv.string,
    }
)


@dataclass
class guntamaticSelectEntityDescription(SelectEntityDescription):
    """Enhance the select entity description for Guntamatic"""

    optionsMapping: dict | None = None
    modes: list | None = None


SENSOR_DESC = [
    SensorEntityDescription(
        key="temp.exterieure",
        name="temp.exterieure",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:sun-thermometer-outline",
    ),
    SensorEntityDescription(
        key="Temp.chaudière",
        name="Temp.chaudière",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="puissance",
        name="puissance",
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:gauge",
    ),
    SensorEntityDescription(
        key="CO2 teneur",
        name="CO2 teneur",
        device_class=SensorDeviceClass.CO2,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="accu haut",
        name="accu haut",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer-chevron-up",
    ),
    SensorEntityDescription(
        key="accu bas",
        name="accu bas",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer-chevron-down",
    ),
    SensorEntityDescription(
        key="ECS 0",
        name="ECS 0",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="temp.amb. CH 1",
        name="temp.amb. CH 1",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="aller effect. 1",
        name="aller effect. 1",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="aller effect. 2",
        name="aller effect. 2",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="temps fonct",
        name="temps fonct",
        # device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.HOURS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:counter",
    ),
    SensorEntityDescription(
        key="dern.révision",
        name="dern.révision",
        # device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.DAYS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:account-wrench",
    ),
    SensorEntityDescription(
        key="Vider cendr.ds",
        name="Vider cendr.ds",
        # device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.HOURS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:delete-empty",
    ),
    SensorEntityDescription(
        key="aller effect. 0",
        name="aller effect. 0",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="Brennstoffzähler",
        name="Brennstoffzähler",
        device_class=None,
        native_unit_of_measurement=UnitOfVolume.CUBIC_METERS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:counter",
    ),
    SensorEntityDescription(
        key="charge accu",
        name="charge accu",
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="Betriebscode",
        name="Betriebscode",
        device_class=None,
        native_unit_of_measurement=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="program.",
        name="program.",
        device_class=None,
        native_unit_of_measurement=None,
        state_class=None,
        # entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:cog",
    ),
    SensorEntityDescription(
        key="Programme CH0",
        name="Programme CH0",
        device_class=None,
        native_unit_of_measurement=None,
        state_class=None,
        # entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:cog",
    ),
    SensorEntityDescription(
        key="Programme CH1",
        name="Programme CH1",
        device_class=None,
        native_unit_of_measurement=None,
        state_class=None,
        # entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:cog",
    ),
    SensorEntityDescription(
        key="Programme CH2",
        name="Programme CH2",
        device_class=None,
        native_unit_of_measurement=None,
        state_class=None,
        # entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:cog",
    ),
    # Daten vom alten API
    SensorEntityDescription(
        key="Mot. vis d'extraction",
        name="Mot. vis d'extraction",
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:gauge",
    ),
    SensorEntityDescription(
        key="CO2 Soll",
        name="CO2 Soll",
        device_class=SensorDeviceClass.CO2,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="Kesselsolltemp",
        name="Kesselsolltemperatur",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer-lines",
    ),
    SensorEntityDescription(
        key="Rauchgasauslastung",
        name="Rauchgasauslastung",
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:gauge",
    ),
    SensorEntityDescription(
        key="grill",
        name="grill",
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:gauge",
    ),
    SensorEntityDescription(
        key="Rücklauftemp. Soll",
        name="Rücklauftemperatur Soll",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer-lines",
    ),
    SensorEntityDescription(
        key="Rücklauftemp.",
        name="Rücklauftemperatur",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="vent. aspiration",
        name="vent. aspiration",
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:gauge",
    ),
    SensorEntityDescription(
        key="Vorlauf Soll 1",
        name="Vorlauf Soll 1",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer-lines",
    ),
    SensorEntityDescription(
        key="Vorlauf Soll 2",
        name="Vorlauf Soll 2",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer-lines",
    ),
    SensorEntityDescription(
        key="Wirkungsgrad",
        name="Wirkungsgrad",
        device_class=SensorDeviceClass.POWER_FACTOR,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:gauge",
    ),
    SensorEntityDescription(
        key="Defaut 0",
        name="Defaut 0",
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:alert-circle",
    ),
    SensorEntityDescription(
        key="Defaut 1",
        name="Defaut 1",
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:alert-circle",
    ),
    SensorEntityDescription(
        key="Kesselzustand-Nr.",
        name="Kesselzustand-Nr.",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="Version",
        name="Version",
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_visible_default=False,
    ),
    SensorEntityDescription(
        key="Série",
        name="Série",
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_visible_default=False,
    ),
    SensorEntityDescription(
        key="Fonction",
        name="Fonction",
        state_class=None,
        entity_registry_visible_default=True,
        entity_category=EntityCategory.DIAGNOSTIC,
        icon="mdi:cog",
    ),
]

BINARY_SENSOR_DESC = [
    BinarySensorEntityDescription(
        key="Pompe HP0",
        name="Pompe HP0",
    ),
    BinarySensorEntityDescription(
        key="P ECS 0",
        name="P ECS 0",
    ),
    BinarySensorEntityDescription(
        key="circ.chauf. 0",
        name="circ.chauf. 0",
    ),
    BinarySensorEntityDescription(
        key="Heizkreis 1",
        name="Heizkreis 1",
    ),
    BinarySensorEntityDescription(
        key="circ.chauf. 2",
        name="circ.chauf. 2",
    ),
    BinarySensorEntityDescription(
        key="Kesselfreigabe",
        name="Kesselfreigabe",
    ),
    # Daten vom alten API
    BinarySensorEntityDescription(
        key="Austragungsgebläse",
        name="Austragungsgebläse",
    ),
    BinarySensorEntityDescription(
        key="Füllstand",
        name="Füllstand",
    ),
    BinarySensorEntityDescription(
        key="Mischer 1",
        name="Mischer 1",
    ),
    BinarySensorEntityDescription(
        key="Mischer 2",
        name="Mischer 2",
    ),
]
SELECT_DESC = [
    guntamaticSelectEntityDescription(
        key="Program",
        name="Program",
        icon="mdi:cog",
        modes=[
            "ETEINT",
            "NORMAL",
            "EAU CHAUDE",
            "WW RECHARGER",
        ],
        optionsMapping={"ETEINT": 0, "NORMAL": 1, "EAU CHAUDE": 2, "WW RECHARGER": 6},
    ),
]
