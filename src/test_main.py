from main import parse_coordinates, parse_input, move, main


class TestParseCoordinates:
    def test_parse_surface_coordinates(self):
        assert parse_coordinates("3 5") == (3, 5)
        assert parse_coordinates("30 5") == (30, 5)

    def test_parse_robot_positions(self):
        assert parse_coordinates("3 5 E") == (3, 5, "E")
        assert parse_coordinates("30 5 W") == (30, 5, "W")


class TestParseInput:
    def test_sample_input_with_line_breaks(self):
        sample_input = (
            "5 3\n10 1 E\nRFRFRFRF\n\n3 2 N\nFRRFLLFFRRFLL\n\n0 3 W\nLLFFFLFLFL\n"
        )

        surface, robots = parse_input(sample_input)

        assert surface == (5, 3)
        assert robots == [
            ((10, 1, "E"), "RFRFRFRF"),
            ((3, 2, "N"), "FRRFLLFFRRFLL"),
            ((0, 3, "W"), "LLFFFLFLFL"),
        ]

    def test_sample_input_in_quotes_with_indents(self):
        sample_input = """
        5 3
        10 1 E
        RFRFRFRF

        3 2 N
        FRRFLLFFRRFLL

        0 3 W
        LLFFFLFLFL
        """
        surface, robots = parse_input(sample_input)

        assert surface == (5, 3)
        assert robots == [
            ((10, 1, "E"), "RFRFRFRF"),
            ((3, 2, "N"), "FRRFLLFFRRFLL"),
            ((0, 3, "W"), "LLFFFLFLFL"),
        ]


class TestMove:
    def test_sample_input(self):
        assert move((5, 3), (1, 1, "E"), "RFRFRFRF") == (False, 1, 1, "E")
        assert move((5, 3), (3, 2, "N"), "FRRFLLFFRRFLL") == (True, 3, 3, "N")
        assert move((5, 3), (0, 3, "W"), "LLFFFLFLFL") == (True, 3, 3, "N")
        assert move((5, 3), (0, 3, "W"), "LLFFFLFLFL", {(3, 3)}) == (
            False,
            2,
            3,
            "S",
        )


class TestMain:
    def test_sample_input(self):
        sample_input = """
        5 3
        1 1 E
        RFRFRFRF

        3 2 N
        FRRFLLFFRRFLL

        0 3 W
        LLFFFLFLFL
        """
        assert main(sample_input) == "1 1 E\n3 3 N LOST\n2 3 S\n"
