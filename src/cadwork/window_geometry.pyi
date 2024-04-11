class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class window_geometry:
    def __init__(self):
        self.bottom_left = self.point(0, 0)
        self.bottom_right = self.point(0, 0)
        self.top_left = self.point(0, 0)
        self.top_right = self.point(0, 0)
    
    @property
    def bottom_left(self) -> point: ...

    @property
    def bottom_right(self) -> point: ...

    @property
    def top_left(self) -> point: ...

    @property
    def top_right(self) -> point: ...