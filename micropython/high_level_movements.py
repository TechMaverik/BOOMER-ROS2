from movements import Movements


class HighLevelMovements:

    def high_level_movements(self, message):
        if message == "default":
            Movements().set_to_default_positions()

        if message == "stand":
            Movements().set_to_standing_position()

        if message == "sit":
            Movements().set_to_sit_down_position()

        if message == "forward":
            Movements().set_to_move_forward()

        if message == "x":
            Movements().set_to_x_position()
