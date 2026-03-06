CREATE TABLE call_records (

    id SERIAL PRIMARY KEY,

    customer_phone VARCHAR(20) NOT NULL,

    channel VARCHAR(20),

    transcript TEXT,

    ai_response TEXT,

    outcome VARCHAR(20),

    confidence_score FLOAT
    CHECK (confidence_score >= 0 AND confidence_score <= 1),

    csat_score INT
    CHECK (csat_score BETWEEN 1 AND 5),

    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    duration INT
);

CREATE INDEX idx_phone
ON call_records(customer_phone);
-- Speeds up customer history lookup

CREATE INDEX idx_timestamp
ON call_records(timestamp DESC);
-- Faster recent call queries

CREATE INDEX idx_outcome
ON call_records(outcome);
-- Used for analytics queries
