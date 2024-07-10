class Point:
    def __init__(self, x: float, y: float):
        """
        Initialize a point with x and y coordinates.

        Args:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
        """
        self.x = x
        self.y = y

class WindowGeometry:
    def __init__(self, bottom_left: Point, bottom_right: Point, top_left: Point, top_right: Point):
        """
        Initialize window geometry with points defining the window corners.

        Args:
            bottom_left (Point): The bottom left corner of the window.
            bottom_right (Point): The bottom right corner of the window.
            top_left (Point): The top left corner of the window.
            top_right (Point): The top right corner of the window.
        """
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.top_left = top_left
        self.top_right = top_right