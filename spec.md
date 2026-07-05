# Capstone Project: Personal Content Engine & Workflow Concierge
**Track:** Concierge Agents

## Overview
An autonomous personal assistant designed to streamline everyday creative workflows. It takes unstructured raw ideas or topics from the user, processes them using a multi-step execution loop, and formats them into viral short-form interactive scripts while saving the assets locally.

## Core Capabilities & Tools
1. **Script Generation Engine:** Creates interactive storytelling hooks and pacing metrics using Gemini.
2. **Local File Writer Tool:** Automatically writes the final polished scripts into a structured JSON file on the local machine for production use.

## Guardrails
- Validates that the output strictly adheres to a structured JSON schema.
- Filters out any corrupted strings before writing to disk.