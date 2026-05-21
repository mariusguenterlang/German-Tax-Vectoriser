-- postgres/init.sql

CREATE TABLE IF NOT EXISTS legal_documents (
    id UUID PRIMARY KEY,
    law_name TEXT NOT NULL,
    section TEXT,
    content TEXT NOT NULL,
    source_url TEXT,
    effective_from DATE,
    effective_to DATE,
    created_at TIMESTAMPTZ DEFAULT NOW()
)