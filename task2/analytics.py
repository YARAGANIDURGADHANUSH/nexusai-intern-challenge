import asyncpg


async def lowest_resolution_intents(dsn: str):

    conn = await asyncpg.connect(dsn)

    query = """
    SELECT
        intent,
        COUNT(*) AS total_calls,
        AVG(csat_score) AS avg_csat,
        SUM(CASE WHEN outcome='resolved' THEN 1 ELSE 0 END)::float
            / COUNT(*) AS resolution_rate
    FROM call_records
    WHERE timestamp >= NOW() - INTERVAL '7 days'
    GROUP BY intent
    ORDER BY resolution_rate ASC
    LIMIT 5
    """

    rows = await conn.fetch(query)

    await conn.close()

    return [dict(r) for r in rows]