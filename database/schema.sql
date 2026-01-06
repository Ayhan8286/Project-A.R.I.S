-- Schema for GTM Engine

-- Table: leads
CREATE TABLE IF NOT EXISTS leads (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: ai_logs
CREATE TABLE IF NOT EXISTS ai_logs (
    id SERIAL PRIMARY KEY,
    agent_name VARCHAR(100),
    prompt TEXT,
    response TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: approval_queue
CREATE TABLE IF NOT EXISTS approval_queue (
    id SERIAL PRIMARY KEY,
    task_id VARCHAR(100),
    action VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
