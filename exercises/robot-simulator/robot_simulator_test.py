from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST


class TestRobotSimulator:

    # Test create robot
    def test_at_origin_facing_north(self):
        robot = Robot(NORTH, 0, 0)
        assert robot.coordinates == (0, 0)
        assert robot.direction == NORTH

    def test_at_negative_position_facing_south(self):
        robot = Robot(SOUTH, -1, -1)
        assert robot.coordinates == (-1, -1)
        assert robot.direction == SOUTH

    # Test rotating clockwise
    def test_changes_north_to_east(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("R")

        assert robot.coordinates == (0, 0)
        assert robot.direction == EAST

    def test_changes_east_to_south(self):
        robot = Robot(EAST, 0, 0)
        robot.move("R")

        assert robot.coordinates == (0, 0)
        assert robot.direction == SOUTH

    def test_changes_south_to_west(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("R")

        assert robot.coordinates == (0, 0)
        assert robot.direction == WEST

    def test_changes_west_to_north(self):
        robot = Robot(WEST, 0, 0)
        robot.move("R")

        assert robot.coordinates == (0, 0)
        assert robot.direction == NORTH

    # Test rotating counter-clockwise
    def test_changes_north_to_west(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("L")

        assert robot.coordinates == (0, 0)
        assert robot.direction == WEST

    def test_changes_west_to_south(self):
        robot = Robot(WEST, 0, 0)
        robot.move("L")

        assert robot.coordinates == (0, 0)
        assert robot.direction == SOUTH

    def test_changes_south_to_east(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("L")

        assert robot.coordinates == (0, 0)
        assert robot.direction == EAST

    def test_changes_east_to_north(self):
        robot = Robot(EAST, 0, 0)
        robot.move("L")

        assert robot.coordinates == (0, 0)
        assert robot.direction == NORTH

    # Test moving forward one
    def test_facing_north_increments_y(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("A")

        assert robot.coordinates == (0, 1)
        assert robot.direction == NORTH

    def test_facing_south_decrements_y(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("A")

        assert robot.coordinates == (0, -1)
        assert robot.direction == SOUTH

    def test_facing_east_increments_x(self):
        robot = Robot(EAST, 0, 0)
        robot.move("A")

        assert robot.coordinates == (1, 0)
        assert robot.direction == EAST

    def test_facing_west_decrements_x(self):
        robot = Robot(WEST, 0, 0)
        robot.move("A")

        assert robot.coordinates == (-1, 0)
        assert robot.direction == WEST

    # Test follow series of instructions
    def test_moving_east_and_north_from_readme(self):
        robot = Robot(NORTH, 7, 3)
        robot.move("RAALAL")

        assert robot.coordinates == (9, 4)
        assert robot.direction == WEST

    def test_moving_west_and_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("LAAARALA")

        assert robot.coordinates == (-4, 1)
        assert robot.direction == WEST

    def test_moving_west_and_south(self):
        robot = Robot(EAST, 2, -7)
        robot.move("RRAAAAALA")

        assert robot.coordinates == (-3, -8)
        assert robot.direction == SOUTH

    def test_moving_east_and_north(self):
        robot = Robot(SOUTH, 8, 4)
        robot.move("LAAARRRALLLL")

        assert robot.coordinates == (11, 5)
        assert robot.direction == NORTH
