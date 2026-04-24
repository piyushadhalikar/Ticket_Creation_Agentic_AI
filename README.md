# Ticket_Creation_Agentic_AI

An AI Agent for Ticket Creation Automation that:

Takes a user issue (plain English)
Understands intent (bug / access / infra / request)
Extracts key details
Creates a structured ticket (like Jira/ServiceNow style)
(Optional) Sends it to an API or stores it

🧠 Architecture

Agent Flow:

User Input → LLM Agent → Tool Selection → Ticket Generator → Output/API

Components:

LLM (OpenAI) → reasoning + extraction
Agent → decides what to do
Tools → create_ticket, classify_issue
Memory (optional) → conversation history

📁 Project Structure
ai-ticket-agent/
│── agent.py
│── tools.py
│── config.py
│── requirements.txt
│── README.md
