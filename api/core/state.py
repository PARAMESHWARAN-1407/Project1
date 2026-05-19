import aiosqlite
import uuid

DB_NAME = "prism.db"


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            run_id TEXT PRIMARY KEY,
            status TEXT,
            feature_spec_json TEXT,
            final_report_md TEXT
        )
        """)
        await db.commit()


async def create_run():
    run_id = str(uuid.uuid4())

    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO runs (run_id, status) VALUES (?, ?)",
            (run_id, "created")
        )
        await db.commit()

    return run_id


async def get_run(run_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT * FROM runs WHERE run_id=?",
            (run_id,)
        )
        row = await cursor.fetchone()

    return row


async def update_run(run_id, status, feature_spec=None):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            UPDATE runs
            SET status=?, feature_spec_json=?
            WHERE run_id=?
            """,
            (status, feature_spec, run_id)
        )
        await db.commit()