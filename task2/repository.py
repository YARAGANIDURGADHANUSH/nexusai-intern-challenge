import asyncpg


class CallRecordRepository:

    def __init__(self, dsn: str):
        self.dsn = dsn

    async def save(self, call_data: dict):

        conn = await asyncpg.connect(self.dsn)

        query = """
        INSERT INTO call_records
        (customer_phone, channel, transcript, ai_response,
         outcome, confidence_score, csat_score, duration)
        VALUES ($1,$2,$3,$4,$5,$6,$7,$8)
        """

        await conn.execute(
            query,
            call_data["customer_phone"],
            call_data["channel"],
            call_data["transcript"],
            call_data["ai_response"],
            call_data["outcome"],
            call_data["confidence_score"],
            call_data.get("csat_score"),
            call_data["duration"]
        )

        await conn.close()

    async def get_recent(self, phone: str, limit: int = 5):

        conn = await asyncpg.connect(self.dsn)

        rows = await conn.fetch(
            """
            SELECT *
            FROM call_records
            WHERE customer_phone = $1
            ORDER BY timestamp DESC
            LIMIT $2
            """,
            phone,
            limit
        )

        await conn.close()

        return [dict(r) for r in rows]