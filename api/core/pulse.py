from api.core.state import update_run
from api.core.parse import parse_document


class PULSE:
    async def run(self, run_id, text):
        await update_run(run_id, "parsing")

        result = parse_document(text)

        await update_run(
            run_id,
            "completed",
            str(result)
        )

        return result