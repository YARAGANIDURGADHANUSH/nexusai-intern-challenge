import asyncpg


class CallRepository:

    def __init__(self, dsn: str):
        self.dsn = dsn

    async def get_connection(self):
        return await asyncpg.connect(self.dsn)

    async def lowest_resolution_intents(self):

        conn = await self.get_connection()

        query = """
        SELECT
            intent,
            COUNT(*) AS total_calls,
            AVG(csat_score) AS avg_csat
        FROM call_records
        GROUP BY intent
        ORDER BY avg_csat ASC
        LIMIT 3;
        """

        rows = await conn.fetch(query)

        await conn.close()

        return rows