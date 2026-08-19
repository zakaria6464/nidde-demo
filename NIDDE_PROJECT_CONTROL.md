# NIDDE — PROJECT CONTROL

**Project:** NIDDE  
**Control Revision:** V2.0.4  
**Phase:** 00 — ARCHITECTURE  
**Last Updated:** 2026-08-19

---

## 1. Purpose

This document is the central execution and status-control record for NIDDE. It records the current architecture phase, verified gates, repository registration state, implementation lock, and the next authorized action.

The canonical Master File Manifest remains the authority for physical-file planning and dependency identity.

---

## 2. Current Project State

| Control | Status |
|---|---|
| Current Phase | PHASE 00 — ARCHITECTURE |
| AG-01 — Technology Stack | VERIFIED |
| AG-02 — Repository Structure | VERIFIED |
| Application Implementation | LOCKED |
| Physical-File Inventory | NOT YET LOCKED |
| Physical-File Count | NOT YET CALCULATED |
| Production Secrets in Git | FORBIDDEN |
| Application Runtime Upload | LOCKED |

No application runtime implementation is authorized merely because repository structure documents exist.

---

## 3. Verified Architecture Gates

### AG-01 — Technology Stack

**Status:** VERIFIED

AG-01 established the technology families and architecture baseline. Its verification record confirms that the technology stack is aligned and that implementation remains locked until the remaining architecture gates are completed.

### AG-02 — Repository Structure

**Status:** VERIFIED

AG-02 establishes the canonical repository boundaries:

```text
NIDDE/
├── README.md
├── NIDDE_PROJECT_CONTROL.md
├── NIDDE_MASTER_FILE_MANIFEST.md
├── .gitignore
├── .env.example
├── .github/
│   └── workflows/
├── backend/
├── database/
├── shared/
├── android/
├── admin/
├── tests/
├── docs/
└── infrastructure/
```

`.github/` is reserved for GitHub-native repository configuration and workflows. `infrastructure/` owns non-GitHub-native deployment and operations infrastructure. These boundaries must not duplicate CI/CD ownership.

---

## 4. Repository Registration State

The following control/document files are expected at repository root:

- `README.md`
- `NIDDE_PROJECT_CONTROL.md`
- `NIDDE_MASTER_FILE_MANIFEST.md`
- `.gitignore`
- `.env.example`

Architecture evidence may also be stored under the repository root or `docs/` according to the approved repository structure.

The current GitHub repository has the following architecture evidence registered during this work:

- `NIDDE_AG-02_REPOSITORY_STRUCTURE_V2.0.4_VERIFIED.md`
- `NIDDE_MASTER_FILE_MANIFEST_V2.0.3_FIXED-2.md`

The canonical root control filename is:

```text
NIDDE_PROJECT_CONTROL.md
```

---

## 5. Security Control

Never commit:

- passwords
- API keys
- JWT secrets
- private keys
- production credentials
- real production environment files
- sensitive production configuration

`.env.example` may contain safe placeholders only. Real secrets must be supplied through an approved secure environment.

Every repository registration must include a sensitive-data review.

---

## 6. Architecture Lock

The project remains in architecture-first mode.

The exact physical-file inventory is **not yet locked**. The Master File Manifest requires the architecture gates to be completed before the final physical-file count and dependency graph are frozen.

Therefore:

```text
APPLICATION IMPLEMENTATION = LOCKED
PHYSICAL FILE COUNT = NOT YET CALCULATED
```

No arbitrary application source files are to be created at the repository root or outside the approved boundaries.

---

## 7. Gate Sequence

The remaining architecture work proceeds through the defined gates before Phase 01 implementation begins.

```text
AG-01 — Technology Stack              VERIFIED
AG-02 — Repository Structure          VERIFIED
AG-03 — System / Dependency Architecture   NEXT
AG-04 — Data / Database Architecture
AG-05 — Authentication / Authorization
AG-06 — Domain / Service Architecture
AG-07 — Client / Android Architecture
AG-08 — Admin Architecture
AG-09 — Payments / Financial Architecture
AG-10 — Testing Architecture
AG-11 — CI/CD Architecture
AG-12 — Security / Operations Architecture
AG-13 — Release / Production Architecture
```

Exact gate naming and scope remain governed by the canonical architecture documents and Master File Manifest.

---

## 8. Next Authorized Action

```text
PHASE 00
→ COMPLETE AG-03 AND REMAINING ARCHITECTURE GATES
→ ENUMERATE EXACT PHYSICAL FILES
→ BUILD DEPENDENCY GRAPH
→ DEFINE TESTS
→ LOCK TOTAL PLANNED FILE COUNT
→ BEGIN PHASE 01
```

The next executable architecture action is **AG-03**.

No application implementation is authorized until the required architecture and physical-file controls are completed.

---

## 9. Recovery Rule

After any interruption:

1. Read this Project Control document.
2. Read the canonical Master File Manifest.
3. Inspect the GitHub repository.
4. Determine the last verified gate and registered evidence.
5. Determine the first unverified architecture action whose prerequisites are satisfied.
6. Continue from that point.

Progress must never be inferred from conversation memory alone.

---

## 10. Source-of-Truth Order

When documents disagree, use this order:

1. Canonical Master File Manifest
2. `NIDDE_PROJECT_CONTROL.md`
3. Verified architecture-gate documents
4. Repository state
5. Unverified drafts or local copies

A GitHub commit alone does not prove verification. Verification status must be supported by the corresponding evidence and control records.
