import router_mqtt
import display_engine
from router import Router
from wifi_connectivity import Wifi


display_engine.startup()
status=Wifi().connect()
router_mqtt.main()

