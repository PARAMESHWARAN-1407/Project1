from api.core.radar import RADAR
from api.core.judge import JUDGE


class PULSE:
    def __init__(self):
        self.radar = RADAR()
        self.judge = JUDGE()

    async def run(self, parsed_data):
        print("PULSE started")

        # RADAR (sync call)
        research = self.radar.research(parsed_data)
        print("RADAR completed")

        # JUDGE (sync or async safe)
        decision = self.judge.evaluate(parsed_data, research)
        print("JUDGE completed")

        return {
            "radar": research,
            "judge": decision
        }