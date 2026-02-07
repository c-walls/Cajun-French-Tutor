# Cajun French Learning Platform

AI-powered web app for learning and preserving Louisiana French dialects through practice, correction capture, and community knowledge.

## Stack
- **Frontend:** Server-rendered HTML + HTMX + minimal vanilla JS
- **Backend:** FastAPI with explicit route and service layers
- **Data:** SQLite in development, PostgreSQL in production
- **Model:** Thin AI adapter for chat + translation

**Architecture:** hypermedia-first (server-rendered UI, no client SPA, no public JSON API in v0).

## Product Modes
- **Chat (v0):** Conversational practice with correction capture
- **Translate (v0):** Single-turn translation with edits + dialect notes
- **Lessons (v1):** Guided exercises
- **Contribute (v1):** Variant and regional contribution workflow
- **Visualize (v1+):** Dialect distribution and variant frequency views

## Core Data Entities
- **Users:** Anonymous session IDs in v0 → accounts in v1
- **Interactions:** Every model call (mode, input, output, timestamp, user/session)
- **Feedback:** Approve/reject/edit + dialect annotations linked to interactions
- **Lexicon (v1):** Entries, regional variants, frequencies, contributor metadata
- **Contributions (v1):** Community submissions with provenance + geography

> Preserve all feedback; never overwrite prior human judgments.

## Request Flow (HTMX)
1. User action triggers an HTMX request.
2. FastAPI route validates input and calls domain service.
3. Service executes model call and persistence.
4. Server returns HTML (page or partial).
5. HTMX swaps target DOM region.
6. Optional async feedback writes to audit log.

## Proposed Repository Layout
```text
backend/
├── app.py             # FastAPI server
├── routes.py          # HTTP endpoints
├── chat_flow.py       # Chat orchestration
├── translate_flow.py  # Translation orchestration
├── model.py           # AI wrapper
├── db.py              # Database layer
├── schema.sql         # Source-of-truth schema
└── data/
    └── app.db

frontend/
├── templates/         # Pages + HTMX partials
└── static/
    ├── htmx.min.js
    └── app.js
```

## Engineering Principles
- **Capture first, interpret later:** disagreement is linguistic signal.
- **Hypermedia over API sprawl:** server owns state transitions.
- **Schema reproducibility:** database rebuildable from tracked schema + migrations.
- **Provenance by default:** who/what/where retained for every contribution.
- **Keep it simple:** boring backend, minimal JS, observable flows.

## Roadmap
- **v0:** Chat + translate + feedback persistence
- **v1:** Lessons + lexicon + contribution workflows + contributor metadata
- **v2:** Mapping + variant analytics + export tooling
- **v3:** Family/community language network preservation
