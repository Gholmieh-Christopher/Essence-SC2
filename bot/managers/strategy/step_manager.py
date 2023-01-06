# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# Random:
import random

# Enumerations:
from bot.enumerations import StepReturns

# Managers:
from bot.managers.game_sense import GameInfoManager

# Build Orders:
from .build_orders import DoubleGatePVP

# Classes:
class StepManager:
    ASSOCIATIONS: dict = {
        # Protoss:
        Race.Protoss: [DoubleGatePVP()]
    }

    # Initialization:
    def __init__(self, game_info_manager: GameInfoManager, AI: BotAI) -> None:
        # Miscellaneous:
        self.GameInfoManager: GameInfoManager = game_info_manager
        self.sequence = random.choice(
            self.ASSOCIATIONS[self.GameInfoManager.enemy_race]
        ).sequence
        self.AI: BotAI = AI

        # Dictionaries:
        self.goals: dict = {}

        # Lists:
        self.verifying: list = []
        self.verified: list = []

    # Methods:
    async def update(self, AI: BotAI) -> None:
        # Updating Variables:
        self.AI: BotAI = AI

        # Executing Steps:
        for step in self.sequence:
            for i in self.verifying:
                if i.action_id == step.action_id:
                    continue

            result = await step.execute(AI)

            if result == StepReturns.SUCCESSFUL_RETURN:
                self.verifying.append(step)

                self.goals[step.action_id] = (
                    self.goals.get(step.action_id, 0) + step.quantity
                )

        for step in self.verifying:
            if step in self.sequence:
                del self.sequence[self.sequence.index(step)]

            if (
                AI.structures.of_type(step.action_id).amount
                + AI.already_pending(step.action_id)
                < self.goals[step.action_id]
            ):
                await step.execute(AI)
            else:
                self.verified.append(step)

        for step in self.verified:
            del self.verifying[self.verifying.index(step)]

        self.verified: list = []
