NORTH, EAST, SOUTH, WEST = range(4)


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    def _advance(self):
        if self.direction == NORTH:
            self.y += 1
        elif self.direction == SOUTH:
            self.y -= 1
        elif self.direction == EAST:
            self.x += 1
        elif self.direction == WEST:
            self.x -= 1

    def _move_left(self):
        self.direction = (self.direction - 1) % 4

    def _move_right(self):
        self.direction = (self.direction + 1) % 4

    def move(self, commands):
        for cmd in commands:
            if cmd == "R":
                self._move_right()
            elif cmd == "L":
                self._move_left()
            elif cmd == "A":
                self._advance()
