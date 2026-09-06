import aiosqlite
import uuid

DB_NAME = "prism.db"


# -------------------------
# Initialize Database
# -------------------------
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


# -------------------------
# Create Run
# -------------------------
async def create_run(parsed):
    run_id = str(uuid.uuid4())

    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            INSERT INTO runs (run_id, status, feature_spec_json)
            VALUES (?, ?, ?)
            """,
            (run_id, "created", str(parsed))
        )
        await db.commit()

    return run_id


# -------------------------
# Get Run
# -------------------------
async def get_run(run_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT run_id, status, feature_spec_json, final_report_md FROM runs WHERE run_id=?",
            (run_id,)
        )
        row = await cursor.fetchone()

    if row is None:
        return {"error": "run not found"}

    return {
        "run_id": row[0],
        "status": row[1],
        "feature_spec_json": row[2],
        "final_report_md": row[3]
    }


# -------------------------
# Update Run
# -------------------------
async def update_run(run_id, status, feature_spec=None, final_report=None):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            UPDATE runs
            SET status=?,
                feature_spec_json=COALESCE(?, feature_spec_json),
                final_report_md=COALESCE(?, final_report_md)
            WHERE run_id=?
            """,
            (status, feature_spec, final_report, run_id)
        )
        await db.commit()