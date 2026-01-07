-- 1. LEADS TABLE (The Input)
-- Stores potential clients found by the generic scraper or n8n.
CREATE TABLE IF NOT EXISTS leads (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    website_url VARCHAR(255),
    industry VARCHAR(100),
    status VARCHAR(50) DEFAULT 'new', -- options: new, qualified, disqualified, contacted
    summary TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 2. AI LOGS TABLE (The Brain's Diary)
-- Stores the thought process and actions taken by the AI Agents.
CREATE TABLE IF NOT EXISTS ai_logs (
    id SERIAL PRIMARY KEY,
    agent_name VARCHAR(50), -- e.g., 'Jules', 'Researcher'
    action_taken TEXT,
    result_summary TEXT,
    tokens_used INT,
    timestamp TIMESTAMP DEFAULT NOW()
);

-- 3. APPROVAL QUEUE (The Human Loop)
-- Stores tasks that require human permission before executing.
CREATE TABLE IF NOT EXISTS approval_queue (
    task_id SERIAL PRIMARY KEY,
    agent_name VARCHAR(50),
    task_type VARCHAR(50), -- e.g., 'send_email'
    payload JSONB,         -- The data (email draft, recipient, etc.)
    status VARCHAR(20) DEFAULT 'pending',
    human_feedback TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
