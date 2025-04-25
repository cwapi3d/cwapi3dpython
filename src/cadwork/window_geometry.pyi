from cadwork import point


class window_geometry:
    def __init__(self, bottom_left: point, bottom_right: point, top_left: point, top_right: point):
        """
        Initialize window geometry with points defining the window corners.

        Args:
            bottom_left (point): The bottom left corner of the window.
            bottom_right (point): The bottom right corner of the window.
            top_left (point): The top left corner of the window.
            top_right (point): The top right corner of the window.
        """
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.top_left = top_left
        self.top_right = top_right