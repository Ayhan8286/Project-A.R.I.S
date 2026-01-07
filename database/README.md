# Database Schema

This directory contains the database schema definitions for the GTM Engine.

## Compatibility

*   **Database:** PostgreSQL 15
*   **Usage:** These tables are primarily used by **n8n workflows** to store leads, log AI actions, and manage the human approval queue.

## Tables

1.  **leads:** Stores potential clients and their status.
2.  **ai_logs:** Records the activities and decisions made by AI agents.
3.  **approval_queue:** Manages tasks that require human intervention before execution.
