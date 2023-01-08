# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Position:
from sc2.position import Point3, Point2

# > Bot AI:
from sc2.bot_ai import BotAI

# Dataclasses:
import dataclasses

# Numpy:
import numpy

# Bases:
from bot.bases import Manager

# Classes:
@dataclasses.dataclass
class DebuggingManager(Manager):
    """
    Uses debugging methods from BotAI to represent what the bot has access too.
    Inherits from Manager class.
    
    :param DRAW_VISIBILITY_PIXELMAP:
    :param DRAW_PLACEMENT_GRID:
    :param DRAW_PATHING_GRID:
    :param DRAW_EXPANSIONS:
    """
    
    DRAW_VISIBLITY_PIXELMAP: bool = False
    DRAW_PLACEMENT_GRID: bool = False
    DRAW_PATHING_GRID: bool = False
    DRAW_EXPANSIONS: bool = False
    
    # Properties:
    @property
    def VISIBILITY_PIXELMAP_UNSEEN_COLOR(self) -> Point3:
        return Point3((255, 0, 0))
    
    @property
    def VISIBILITY_PIXELMAP_SEEN_COLOR(self) -> Point3:
        return Point3((255, 255, 255))

    @property
    def PLACEMENT_GRID_COLOR(self) -> Point3:
        return Point3((255, 255, 255))
    
    @property
    def PATHING_GRID_COLOR(self) -> Point3: 
        return Point3((0, 255, 0))
    
    @property
    def EXPANSION_COLOR(self) -> Point3:
        return Point3((0, 0, 255))
    
    # Methods:
    def draw_visibility_pixelmap(self, AI: BotAI) -> None:
        """
        Draws the visibility pixelmap, a grid of what the bot can see, and what the bot can not see.
        
        :param AI:
        """
        
        for (y, x), value in numpy.ndenumerate(AI.state.visibility.data_numpy):
            position: Point2 = Point2((x, y))

            three_dimensional_coordinate: Point3 = Point3(
                (position.x, position.y, AI.get_terrain_z_height(position))
            )

            bound_0: Point3 = Point3(
                (
                    three_dimensional_coordinate.x - 0.25,
                    three_dimensional_coordinate.y - 0.25,
                    three_dimensional_coordinate.z + 0.25,
                )
            )

            bound_1: Point3 = Point3(
                (
                    three_dimensional_coordinate.x + 0.25,
                    three_dimensional_coordinate.y + 0.25,
                    three_dimensional_coordinate.z - 0.25,
                )
            )

            color: Point3 = self.VISIBILITY_PIXELMAP_UNSEEN_COLOR

            if value == 2:
                color: Point3 = self.VISIBILITY_PIXELMAP_SEEN_COLOR

            AI.client.debug_box_out(bound_0, bound_1, color=color)

    def draw_expansions(self, AI: BotAI) -> None:
        """
        Draws a square in the center of each expansion location.
        
        :param AI:
        """
        
        for expansion_position in AI.expansion_locations_list:
            AI.client.debug_box2_out(
                Point3(
                    (
                        *expansion_position,
                        AI.get_terrain_z_height(expansion_position),
                    )
                ),
                half_vertex_length=0.25,
                color=self.EXPANSION_COLOR,
            )

    def draw_grid(self, data_numpy, color: Point3, AI: BotAI) -> None:
        """
        Draws a grid provided the data numpy, the color preffered, and the AI object.
        
        :param data_numpy:
        :param color:
        :param AI:
        """
        
        map_area = AI.game_info.playable_area

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
                (position.x, position.y, AI.get_terrain_z_height(position))
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

            AI.client.debug_box_out(
                bound_0,
                bound_1,
                color=color,
            )
            
    async def update(self, AI: BotAI) -> None:
        # Calling Methods:
        if self.DRAW_VISIBLITY_PIXELMAP is True:
            self.draw_visibility_pixelmap(AI)

        if self.DRAW_PLACEMENT_GRID is True:
            self.draw_grid(
                AI.game_info.placement_grid.data_numpy, self.PLACEMENT_GRID_COLOR, AI
            )

        if self.DRAW_PATHING_GRID is True:
            self.draw_grid(
                AI.game_info.pathing_grid.data_numpy, self.PATHING_GRID_COLOR, AI
            )

        if self.DRAW_EXPANSIONS is True:
            self.draw_expansions(AI)
