from movements import Movements


class HighLevelMovements:

    def high_level_movements(self, message):
        if message == "default":
            Movements().set_to_default_positions()

        elif message == "stand":
            Movements().set_to_standing_position()

        elif message == "sit":
            Movements().set_to_sit_down_position()

        elif message == "forward":
            Movements().set_to_move_forward()

        elif message == "x":
            Movements().set_to_x_position()


class HighLevelMovementSDK:
    # for external control system

    def movements_sdk(self, payload_data):
        Movements().movements_sdk(payload_data)
