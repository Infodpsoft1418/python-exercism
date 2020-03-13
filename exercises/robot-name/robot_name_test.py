import random
import re

from robot_name import Robot


class TestRobotName:

    name_re = r"^[A-Z]{2}\d{3}$"

    def test_has_name(self):
        assert re.match(self.name_re, Robot().name)

    def test_name_sticks(self):
        robot = Robot()
        robot.name
        assert robot.name == robot.name

    def test_different_robots_have_different_names(self):
        assert Robot().name != Robot().name

    def test_reset_name(self):
        # Set a seed
        seed = "Totally random."

        # Initialize RNG using the seed
        random.seed(seed)

        # Call the generator
        robot = Robot()
        name = robot.name

        # Reinitialize RNG using seed
        random.seed(seed)

        # Call the generator again
        robot.reset()
        name2 = robot.name
        assert name != name2
        assert re.match(self.name_re, name2)
