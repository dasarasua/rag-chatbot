# Roadmap

## Short term (next 2–4 weeks)
• Curate FAQs, policies, and event snippets  
• Close knowledge gaps (Job Board, FinTech events, CV)  
• Add UI feedback (👍/👎 + free text) to improve retrieval and prompts  
• **Add RAG evaluation** with RAGAS (or similar) to quantify:
  - Faithfulness (groundedness to sources)
  - Answer relevancy
  - Context precision & context recall
  - Semantic similarity vs. reference answers
• Track a simple KPI: ≥75% “good answers” on a 30–50 question eval set

## Mid term
• Lightweight CMS for non-engineers (edit content, trigger re-index)  
• Content categories + metadata tagging  
• Auto re-index on content changes (batch or near-real-time)  
• Periodic evals (weekly CI job) with trend chart in README

## Long term
• Integrations: coaching scheduler, events calendar, job board  
• Smart actions (e.g., “Book a session” opens scheduler prefilled)  
• Multi-surface: web widget + email assist with logging/analytics  
• Personalization guardrails (only use context the user has access to)
