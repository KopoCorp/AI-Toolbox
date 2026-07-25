---
name: kopo-smart-ai
description: Index and routing map for every skill in this AI-Toolbox repository. Use this when it's unclear which locally installed skill applies to the current request — before writing or reviewing code, before building a Kopo website or page, before drafting or editing text, before automating a browser, or when starting any nontrivial task — so the right skill gets invoked by its exact name instead of being guessed, skipped, or silently reinvented.
---

# Kopo Smart IA — skill router

This repository bundles several independent skills. Each one already triggers on its own description, but when several could plausibly apply, or it's unclear whether any of them do, use this file as the map: invoke the skill by the **exact name** in the table below — that's the `name:` field in its own SKILL.md. Claude Code resolves skills by that name, not by folder path, repo name, or a paraphrase.

## Available skills

| Situation | Skill to invoke | What it does |
|---|---|---|
| Building or editing anything for Kopo: a website, landing page, dashboard, doc page, legal page | `kopo-website-skill` | Full Kopo V1.4 brand system — assets, CSS/JS, four templates, animated Kobot, design-excellence and UX references |
| Starting any nontrivial coding task (new feature, refactor, bug fix) | `superpowers:brainstorming`, then the relevant `superpowers:*` skill (`test-driven-development`, `systematic-debugging`, `writing-plans`, `executing-plans`, `requesting-code-review`, `using-git-worktrees`, ...) | 14-skill development methodology suite — brainstorm before planning, plan before coding, verify before declaring done |
| Writing, reviewing, or refactoring any code | `karpathy-guidelines` | Behavioral guardrails against common LLM coding mistakes: no overcomplication, surgical changes, surface assumptions, verifiable success criteria |
| The brief is vague or ambiguous, or the user wants their plan stress-tested | `grill-me` | Relentless one-question-at-a-time interview to reach a shared understanding before acting |
| The user wants a capability this toolbox doesn't have | `find-skills` | Searches the public agent-skills ecosystem and proposes an install command |
| The task requires interacting with a real website (navigate, fill forms, click, screenshot, scrape, test a web app) | `agent-browser` | Browser automation CLI (requires `npm i -g agent-browser`) |
| Any user-facing text needs to read less like AI-generated writing | `humanizer` | Removes AI writing tics — inflated symbolism, promotional tone, filler phrases, em-dash overuse, etc. |

## How to use this map

1. Match the request to a row above.
2. Invoke the corresponding skill by its exact name (`superpowers:<sub-skill>` for the methodology suite, the bare name for everything else).
3. If more than one row applies, invoke them in the order they'd naturally occur — e.g. `grill-me` to clarify a vague brief, then `superpowers:brainstorming`, then `kopo-website-skill` to build the actual page.
4. If nothing here applies but the task still feels like it needs a specialized skill, use `find-skills` rather than improvising an ad hoc approach.

## Why exact names matter

Claude Code resolves and invokes skills by their declared `name:`, not by folder name or a description of what they roughly do. Always use the names in the table above verbatim — a close-but-wrong name (e.g. "dev-methodology" or "llm-coding-guidelines", both retired) will fail to resolve even though the underlying skill is installed.
