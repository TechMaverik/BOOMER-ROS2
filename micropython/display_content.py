import time
import display_engine


class DisplayContent:

    def display_content_with_topic(self, topic):
        if topic == "happy":
            display_engine.happy_face()
            time.sleep(1)

        if topic == "sad":
            display_engine.sad_face()
            time.sleep(1)

        if topic == "blink":
            display_engine.blink_eye()
            time.sleep(1)

        if topic == "open eyes":
            display_engine.open_eyes()

        if topic == "close eyes":
            display_engine.close_eyes()
