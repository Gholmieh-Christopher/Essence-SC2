# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Position:
from sc2.position import Point3, Point2

# > Bot AI:
from sc2.bot_ai import BotAI

# Numpy:
import numpy

# Classes:
class DebuggerManager:
    # Configuration:
    DRAW_PLACEMENT_GRID: bool = True
    DRAW_PATHING_GRID: bool = True
    DRAW_EXPANSIONS: bool = True

    PLACEMENT_GRID_COLOR: Point3 = Point3((255, 255, 255))
    PATHING_GRID_COLOR: Point3 = Point3((0, 255, 0))
    EXPANSION_COLOR: Point3 = Point3((0, 0, 255))

    # Initialization:
    def __init__(self, AI: BotAI) -> None:
        # Miscellaneous:
        self.AI: BotAI = AI

    # Functions:
    def update(self, AI: BotAI) -> None:
        # Updating Variables:
        self.AI: BotAI = AI

        # Calling Methods:
        if self.DRAW_PLACEMENT_GRID is True:
            self.draw_grid(
                self.AI.game_info.placement_grid.data_numpy, self.PLACEMENT_GRID_COLOR
            )

        if self.DRAW_PATHING_GRID is True:
            self.draw_grid(
                self.AI.game_info.pathing_grid.data_numpy, self.PATHING_GRID_COLOR
            )

        if self.DRAW_EXPANSIONS is True:
            self.draw_expansions()

    # Methods:
    def draw_expansions(self) -> None:
        for expansion_position in self.AI.expansion_locations_list:
            self.AI.client.debug_box2_out(
                Point3(
                    (
                        *expansion_position,
                        self.AI.get_terrain_z_height(expansion_position),
                    )
                ),
                half_vertex_length=0.25,
                color=self.EXPANSION_COLOR,
            )

    def draw_grid(self, data_numpy, color: Point3) -> None:
        map_area = self.AI.game_info.playable_area

        for (b, a), value in numpy.ndenumerate(data_numpy):
            # Guardian Statements:
            if value == 0:
                continue

            if not map_area.x <= a < map_area.x + map_area.width:
                continue

            if not map_area.y <= b < map_area.y + map_area.height:
                continue

            # Drawing:
            position: Point2 = Point2((a, b))

            three_dimensional_coordinate: Point3 = Point3(
                (position.x, position.y, self.AI.get_terrain_z_height(position))
            )

            bound_0: Point3 = Point3(
                (
                    three_dimensional_coordinate.x - 0.25,
                    three_dimensional_coordinate.y - 0.25,
                    three_dimensional_coordinate.z + 0.25,
                )
            ) + Point2((0.5, 0.5))

            bound_1: Point3 = Point3(
                (
                    three_dimensional_coordinate.x + 0.25,
                    three_dimensional_coordinate.y + 0.25,
                    three_dimensional_coordinate.z - 0.25,
                )
            ) + Point2((0.5, 0.5))

            self.AI.client.debug_box_out(
                bound_0,
                bound_1,
                color=color,
            )
