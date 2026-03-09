import asyncpg


async def lowest_resolution_intents(dsn: str):
    """
    Returns the intents with the lowest resolution rates.
    Resolution rate is approximated using CSAT scores.
    """

    conn = await asyncpg.connect(dsn)

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