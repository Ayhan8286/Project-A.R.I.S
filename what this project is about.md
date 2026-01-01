# Project-A.R.I.S
autonomous revenue intelligance system


### 1. What the project does

This project is an **"Autonomous Revenue Engine."**

It is not just a "stack" of tools; it is a **single, intelligent, autonomous AI agent** designed to perform the entire job of a Sales Development Rep (SDR) and GTM Engineer for $0.00.

Its core functions are to:
* **Find & Research:** Autonomously scan the web (`n8n`) to find ideal target companies.
* **Enrich & Analyze:** Use AI agents (`CrewAI`) and a vector "memory" (`Qdrant`) to perform deep, human-level research on those companies.
* **Contact & Qualify:** Autonomously write and send hyper-personalized emails, read the replies, and handle the back-and-forth to **book a meeting on a human's calendar.**
* **Analyze & Quote:** Listen to the sales call (`Fireflies`), analyze it for insights, and **autonomously generate a quote (AI-CPQ)** based on the conversation.
* **Integrate & Handoff:** Autonomously connect the entire business by creating tickets for Engineering (in `Jira`) and creating invoices for Finance (in an `ERP` like ERPNext).

### 2. Why the project is useful

The million-dollar problem this solves is that modern Go-to-Market (GTM) stacks are **fragmented, expensive, and dumb.**

Companies spend $100,000+ per year on separate, disconnected tools for lead gen (`Apollo`), call analysis (`Gong`), sales (`HubSpot`), and product (`Jira`). This forces them to hire expensive teams of humans to manually copy-paste data and perform repetitive, low-value work.

This project is useful because it is not a *cheaper* alternative; it is a *smarter* one.

It unifies the entire customer lifecycle—from the first cold email to the final paid invoice—into a single, intelligent system. It saves companies money on software, but more importantly, it **automates the high-cost, high-friction, repetitive *work* of an entire sales team**, allowing humans to focus on one thing: closing deals.

### 3. How users can get started with the project

This is a 100% open-source, self-hosted platform. To get started, a user would:

1.  **Provision the Server:** Run the provided **`Terraform`** scripts to automatically build the "Always Free" (24GB RAM) server infrastructure on **Oracle Cloud (OCI)**.
2.  **Launch the Stack:** Use a single **`docker-compose up`** command to launch the entire core stack (`PostgreSQL`, `n8n`, `Airflow`, `Qdrant`, `Grafana`, etc.) in containers.
3.  **Configure the "Brain":** Connect their API keys for the free LLMs (`Groq`, `Google AI Studio`) and their front-end tools (`HubSpot`, `Jira`, `Google Calendar`).
4.  **Activate:** Run the first `n8n` workflow to begin finding leads. The autonomous agents will take over from there.

### 4. Where users can get help with your project

As an open-source project, support is community-driven. Users can:

* **Report Bugs:** By opening an "Issue" on the project's **GitHub** repository.
* **Get Help:** By asking questions in the community **Discord** server.
* **Read Documentation:** By consulting the official **Wiki** on GitHub, which will contain all the setup guides and API references.

### 5. Who maintains and contributes to the project

As the capstone project for portfolio, **@Ayhan8286 is the founder, core maintainer, and lead contributor.**

You designed the v6.0 architecture and wrote the initial code. The project is maintained by you, with the goal of attracting a community of like-minded open-source contributors who are also passionate about building a truly autonomous, free alternative to the expensive, fragmented GTM stack.
