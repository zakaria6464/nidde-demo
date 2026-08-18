# Contributing to NIDDE

## Strict Workflow

All NIDDE changes follow:

PLAN → BUILD → STATIC CHECK → DEPENDENCY CHECK → INTEGRATION CHECK → TEST → VERIFY → COMMIT → GITHUB → REGISTER

## Rules

- Do not create random files.
- Do not commit unverified changes.
- Do not introduce application implementation before the required architecture gates are approved.
- Do not expose secrets or credentials.
- Changes must preserve compatibility with the approved architecture.
- Failed verification blocks dependent work.

## Changes

Every change must have a clear reason, verification result, and traceable commit.

Patches should identify the affected component and the verification performed.

## Pull Requests

A change should not be merged until the required checks have passed.
