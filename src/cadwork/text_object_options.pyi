from cadwork import text_element_type

class text_object_options:
    
    def set_font_name(self, font_name: str) -> None:
        """set font name

        Parameters:
            font_name: font_name

        Returns:
            None
        """

    def get_font_name(self) -> str:
        """get font name

        Returns:
            str
        """

    def set_text(self, text: str) -> None:
        """set text

        Parameters:
            text: text

        Returns:
            None
        """

    def get_text(self) -> str:
        """get text

        Returns:
            str
        """

    def set_bold(self, value: bool) -> None:
        """set bold

        Parameters:
            value: value

        Returns:
            None
        """

    def get_bold(self) -> bool:
        """get bold

        Returns:
            bool
        """

    def set_italic(self, value: bool) -> None:
        """set italic

        Parameters:
            value: value

        Returns:
            None
        """

    def get_italic(self) -> bool:
        """get italic

        Returns:
            bool
        """

    def set_height(self, height: float) -> None:
        """set height

        Parameters:
            height: height

        Returns:
            None
        """

    def get_height(self) -> float:
        """get height

        Returns:
            float
        """

    def set_element_type(self, element_type: text_element_type) -> None:
        """set element type

        Parameters:
            element_type: element_type

        Returns:
            None
        """

    def get_element_type(self) -> text_element_type:
        """get element type

        Returns:
            text_element_type
        """

    def set_thickness(self, thickness: float) -> None:
        """set thickness

        Parameters:
            thickness: thickness

        Returns:
            None
        """

    def get_thickness(self) -> float:
        """get thickness

        Returns:
            float
        """

    def set_color(self, color: int) -> None:
        """set color

        Parameters:
            color: color

        Returns:
            None
        """

    def get_color(self) -> int:
        """get color

        Returns:
            int
        """

    def set_height_relative(self, value: bool) -> None:
        """set height relative

        Parameters:
            value: value

        Returns:
            None
        """

    def get_height_relative(self) -> bool:
        """get height relative

        Returns:
            bool
        """

