# NIDDE — MASTER FILE MANIFEST V2.0.3

> **STATUS: PHASE 00 / ARCHITECTURE — FILE COUNT NOT YET LOCKED**
>
> This document is the planning authority for the NIDDE rebuild. It deliberately does **not** guess the final physical-file count. Exact file records are created only after the architecture gates below are approved.

## 1. Project Identity

| Field | Value |
|---|---|
| Project | NIDDE |
| Repository | NIDDE |
| Mode | STRICT |
| Current Phase | 00 — ARCHITECTURE |
| Canonical Manifest Path | `/NIDDE_MASTER_FILE_MANIFEST.md` |
| Manifest Version | V2.0.3 |
| GitHub Application Upload | LOCKED |
| Application Files Uploaded | 0 |
| Verified Files | 0 |
| Blocked Files | 0 |
| Patched Files | 0 |
| Total Planned Physical Files | NOT YET CALCULATED |
| Final Physical-File Count | NOT LOCKED |
| Last Verified File | AG-01 — TECHNOLOGY STACK |
| Next File | NOT YET CREATED |

## 2. Authority and Source-of-Truth Rules

1. During planning, this Manifest defines the approved file plan.
2. After an implementation file is verified and committed, GitHub is the authoritative source for that implementation file.
3. `NIDDE_PROJECT_CONTROL.md` is the authoritative project-status register.
4. The Manifest is the authoritative file/dependency register.
5. Conversation messages, old ZIPs, phone copies, and historical generated files are **not** sources of project state.
6. No application file may be uploaded merely because it exists locally or appears to work.
7. No file may be silently added, removed, renamed, or moved after the manifest is locked.
8. Any post-lock change requires a Change Request.

## 3. Canonical Naming Rule

The canonical repository file is:

`/NIDDE_MASTER_FILE_MANIFEST.md`

Versioned exported copies such as `NIDDE_MASTER_FILE_MANIFEST_V2.0.0.md` are historical/export artifacts and are **not** additional project files unless explicitly registered through a Change Request.

The Manifest ID assigned to the canonical manifest is reserved for the manifest itself once the exact physical-file inventory is locked.

## 4. Mandatory Physical-File Record

Every exact physical file in the locked manifest MUST have all fields below.

| Field | Requirement |
|---|---|
| ID | Immutable `NIDDE-XXX` identifier |
| Name | Exact physical filename |
| Path | Exact repository path |
| Type | Exact file format/language |
| Phase | Owning NIDDE phase |
| Domain | Owning system domain |
| Purpose | Single primary responsibility |
| Inputs | Direct inputs, contracts, environment/config references |
| Outputs | Direct outputs, artifacts, side effects |
| DEPENDS_ON | Direct prerequisite Manifest IDs only |
| USED_BY | Direct consumer Manifest IDs only |
| Test Method | Exact validation/acceptance method |
| Acceptance Criteria | Conditions required for VERIFIED |
| Verification Evidence | Test/report/command/evidence reference |
| Status | Controlled lifecycle state |
| Commit | Exact Git commit reference after verification |
| Patch History | Patch IDs and outcomes |
| Change Request | CR ID when created/changed by a CR |
| Notes | Constraints, architecture decisions, exceptions |

**No exact physical-file record is complete if any mandatory field is unknown.**

## 5. Controlled Status Lifecycle

Allowed statuses:

- `PLANNED`
- `BUILDING`
- `TESTING`
- `VERIFIED`
- `BLOCKED`
- `PATCHED`
- `DEPRECATED`

Rules:

- `PLANNED`: approved in the manifest but not yet implemented.
- `BUILDING`: implementation is in progress.
- `TESTING`: implementation exists and is undergoing required checks.
- `VERIFIED`: all applicable required checks passed and evidence is recorded.
- `BLOCKED`: at least one required gate failed; dependent work is stopped.
- `PATCHED`: an existing file was changed after verification and must pass the applicable re-verification gates before it can return to `VERIFIED`.
- `DEPRECATED`: removed from active architecture; active files may not depend on it.

A file cannot be `VERIFIED` when a required dependency is missing, `BLOCKED`, `DEPRECATED`, or otherwise unverified.

## 6. Mandatory Verification Pipeline

Every implementation file follows:

`PLAN → BUILD → STATIC CHECK → DEPENDENCY CHECK → INTEGRATION CHECK → TEST → VERIFY → COMMIT → GITHUB → REGISTER`

Not every file requires identical runtime checks, but every file must have an explicit applicable test/verification method.

If a required check fails:

`BLOCKED`

Recovery sequence:

`ROOT CAUSE → FIX/PATCH → STATIC CHECK → DEPENDENCY CHECK → INTEGRATION CHECK → TEST → VERIFY → COMMIT → REGISTER`

## 7. File Identity Rules

1. IDs are immutable once assigned.
2. IDs are never silently reused.
3. A physical path belongs to one active file ID only.
4. A file ID cannot silently change its physical path.
5. Renaming or moving a file requires a Change Request and dependency impact analysis.
6. Generated/build/cache artifacts are not counted as source files unless explicitly required by the architecture.
7. Directories are not files and do not count toward `TOTAL PLANNED`.
8. Wildcards (`*`) and placeholders (`...`) are forbidden inside the final locked physical-file table.

## 8. Architecture Gates — Phase 00

The final physical-file inventory MUST NOT be calculated by guessing.

The following gates must be explicitly resolved before the file count is locked:

### AG-01 — Technology Stack

Lock languages, runtimes, frameworks, package managers, database technology, Android stack, and required build/package tooling. Exact compatible dependency/tool versions are locked through the Compatibility/Implementation Gates before the physical-file inventory is locked.

### AG-02 — Repository Structure

Lock top-level directories, module boundaries, naming conventions, configuration locations, test locations, documentation locations, and infrastructure boundaries.

### AG-03 — System Architecture

Lock domain boundaries, application layers, service boundaries, data flow, ownership, interfaces, and runtime responsibilities.

### AG-04 — Data Model

Lock entities, fields, relations, constraints, indexes, lifecycle fields, audit fields, migration strategy, and seed strategy.

### AG-05 — API Contract

Lock endpoints/interfaces, authentication requirements, request/response contracts, errors, pagination, idempotency, versioning, and webhook contracts.

### AG-06 — Authentication / Authorization

Lock identity flows, sessions/tokens, roles, permissions, account recovery, verification requirements, guards, and privilege boundaries.

### AG-07 — Security Model

Lock secrets handling, validation, rate limiting, authorization enforcement, audit requirements, data protection, logging rules, and security testing.

### AG-08 — External Integrations

Lock maps/geocoding, payment providers, push notifications, email/SMS if required, storage, identity/KYC providers, and failure/retry behavior.

### AG-09 — Android Architecture

Lock Android language/framework, package structure, modules, navigation, state management, networking, storage, permissions, notifications, location, payment integration, and test structure.

### AG-10 — Testing Architecture

Lock unit, integration, API, database, authentication, payment, security, critical-path, Android, and end-to-end strategy.

### AG-11 — CI/CD Architecture

Lock workflow boundaries, validation order, build checks, security checks, artifact handling, branch/commit rules, and deployment gates.

### AG-12 — Production Architecture

Lock deployment topology, environments, database production setup, monitoring, logging, backup, recovery, migrations, rollback, and operational access.

### AG-13 — Release Architecture

Lock release checklist, versioning, final audit, acceptance criteria, rollback criteria, and production-readiness definition.

**Only after AG-01 through AG-13 pass may the exact physical-file inventory be generated and counted. AG-01 does not require every dependency version to be frozen; it requires the technology families and package/build tooling to be unambiguous. Exact versions are frozen by the relevant compatibility/implementation gates before physical-file lock.**

## 9. Required Domain Coverage

Architecture analysis must explicitly cover:

1. Backend
2. Database
3. Authentication
4. Client
5. Artisan
6. Company
7. Services / Marketplace
8. Requests
9. Offers
10. Service Lifecycle
11. Messaging
12. Location / Maps / Tracking
13. Payments
14. Cash
15. Reviews
16. KYC
17. Notifications
18. Admin
19. Analytics / Reporting
20. Security
21. Audit / Logs
22. Android
23. Testing
24. CI/CD
25. Production Infrastructure
26. Release / Final Audit

A domain is not considered complete because a directory exists. Its components, interfaces, dependencies, permissions, failure modes, and tests must be mapped.

## 10. Service Lifecycle Gate

The service lifecycle must explicitly model and test at least:

`REQUESTED → ACCEPTED → EN_ROUTE → ARRIVED → IN_PROGRESS → COMPLETED`

and valid cancellation/error transitions, including who may trigger them, what conditions apply, and what financial/notification/audit effects result.

No lifecycle implementation is considered complete without state-transition validation.

## 11. Critical Path Gate

Before Production Ready, these end-to-end flows must pass.

### Client

`Registration → Login → Search → Request → Receive Offers → Select → Service → Payment → Review`

### Artisan

`Registration → KYC → Approval → Online → Receive Request → Offer → Accept → Execute → Complete → Payout`

### Admin

`Login → User Management → Orders → KYC → Payments → Complaints/Moderation → Logs → Analytics`

Any critical-path failure means:

`PRODUCTION READY = FALSE`

## 12. Dependency Rules

`DEPENDS_ON` contains **direct prerequisites only**.

`USED_BY` contains **direct consumers only**.

Rules:

1. Every referenced ID must exist in the manifest.
2. No dependency may reference an unknown ID.
3. No active file may depend on `BLOCKED`.
4. No active file may depend on `DEPRECATED`.
5. A file must not be marked `VERIFIED` if any required dependency is unverified.
6. Dependency changes require impact analysis.
7. Dependency cycles are forbidden unless explicitly justified by an architecture decision and verified as safe.
8. The dependency graph must be internally consistent: every `DEPENDS_ON` relationship must have the corresponding direct `USED_BY` relationship.

## 13. Phase Dependency Rule

A file may depend on a file from an earlier phase, the same phase, or an explicitly approved later-phase interface only when the architecture requires it.

Implementation order is determined by the dependency graph, not by ID number alone.

`NIDDE-XXX` numbering is an identity system, **not a guarantee of build order**.

The next executable item is the first unverified item whose required dependencies are all satisfied.

## 14. Phase Integration Gate

Every NIDDE phase must have an integration acceptance check before the phase is marked `VERIFIED`.

A phase is:

- `VERIFIED` only when its required files pass and its phase integration test passes.
- `BLOCKED` when any required file or phase integration test fails.

Phase verification must be recorded in `NIDDE_PROJECT_CONTROL.md` and linked to evidence.

## 15. Security and Secrets Gate

Never commit:

- passwords
- API keys
- tokens
- private keys
- production credentials
- sensitive production configuration

Use templates such as:

`/.env.example`

Real secrets must remain in an approved secure environment.

Every GitHub registration must include a secret/sensitive-data scan.

## 16. Commit Rules

Verified implementation commit:

`NIDDE-[ID] | [NAME] | VERIFIED`

Patch commit:

`NIDDE-[ID]-P## | [PATCH NAME] | VERIFIED`

The exact commit reference/hash MUST be recorded after successful verification.

A GitHub commit does not itself prove that verification succeeded.

## 17. GitHub Registration Gate

After verification and commit, the following must be checked:

1. File exists.
2. Exact path is correct.
3. Exact filename is correct.
4. Expected content is present.
5. Commit is present.
6. Required dependencies are present and valid.
7. No forbidden secrets are present.
8. Manifest record is updated.
9. `NIDDE_PROJECT_CONTROL.md` is updated.

Only then is the file considered registered.

## 18. Patch Rules

Every patch must record:

- Patch ID
- File ID
- Problem
- Root Cause
- Fix
- Tests run
- Test results
- Verification result
- Commit
- Date/reference

A patched file is never assumed to remain verified. Applicable verification must be rerun.

## 19. Change Request Rules

Any requirement discovered after manifest lock follows:

`CHANGE REQUEST → IMPACT ANALYSIS → APPROVAL → MANIFEST UPDATE → BUILD → VERIFY`

A Change Request must identify:

- CR ID
- Reason
- Affected files
- Affected dependencies
- Affected phases
- Security impact
- Testing impact
- Production impact
- Count impact
- Approval/status

No random file creation.
No silent dependency changes.
No silent architecture changes.

## 20. Definition of Done — File

A file is DONE only when:

- exact path/name/type are correct;
- syntax/static checks pass where applicable;
- all dependencies resolve;
- security checks pass;
- integration checks pass where applicable;
- tests pass;
- runtime checks pass where applicable;
- regression checks pass where applicable;
- evidence is recorded;
- commit is recorded;
- GitHub registration is verified;
- Manifest and Control are updated.

## 21. Definition of Done — Phase

A phase is DONE only when:

- all required files are verified;
- all dependency relationships are valid;
- phase integration tests pass;
- no required file is blocked;
- regression checks pass;
- phase evidence is recorded;
- `NIDDE_PROJECT_CONTROL.md` is updated.

## 22. Definition of Production Ready

NIDDE is not Production Ready merely because an application opens.

Production Ready requires, at minimum:

- Backend operational
- Database operational
- Authentication operational
- Client operational
- Artisan operational
- Company operational
- Admin operational
- Requests operational
- Offers operational
- Service lifecycle operational
- Messaging operational
- Location operational
- Tracking operational
- Electronic payments operational where approved
- Cash flow operational
- Reviews operational
- KYC operational
- Notifications operational
- Analytics operational
- Security controls operational
- Audit/logging operational
- Android integrated with backend
- Critical tests passing
- Production infrastructure ready
- Backup/recovery verified
- Final audit passed
- Release gates passed

## 23. Recovery After Interruption

When work resumes after a conversation interruption:

1. Read `NIDDE_PROJECT_CONTROL.md`.
2. Read this Manifest.
3. Inspect GitHub.
4. Determine the last verified file from recorded evidence.
5. Determine the first unverified file whose dependencies are satisfied.
6. Confirm no dependency or Change Request invalidates the next item.
7. Continue from that point.

Never infer progress from conversation memory alone.

## 24. Locked Physical-File Table

**INTENTIONALLY EMPTY UNTIL THE ARCHITECTURE LOCK IS COMPLETE.**

The exact physical-file table is generated only after Architecture Gates AG-01 through AG-13 pass.

Wildcards, directory placeholders, and guessed file lists are not allowed here.

| ID | Name | Path | Type | Phase | Domain | Purpose | Inputs | Outputs | DEPENDS_ON | USED_BY | Test Method | Acceptance Criteria | Verification Evidence | Status | Commit | Patch History | Change Request | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 25. Count Lock Rule

`TOTAL PLANNED` means the number of **exact physical-file records** in Section 24 after the architecture is locked.

The following do NOT count as physical files:

- directories;
- wildcard groups;
- `*` placeholders;
- `...` placeholders;
- conceptual modules;
- runtime-generated temporary files;
- build caches;
- unregistered artifacts.

Therefore, in V2.0.3:

- `TOTAL PLANNED = NOT YET CALCULATED`
- `FINAL PHYSICAL FILE COUNT = NOT LOCKED`
- `VERIFIED IMPLEMENTATION FILES = 0`
- `VERIFIED ARCHITECTURE GATES = 1`
- `BLOCKED = 0`
- `GITHUB APPLICATION UPLOAD = LOCKED`

## 26. Cross-Document Consistency Rules

The following three control documents must agree at all times:
- this Manifest;
- `NIDDE_PROJECT_CONTROL.md`;
- the active Architecture Gate document.

At the current point in Phase 00 they MUST state:
- `CURRENT_PHASE = 00 — ARCHITECTURE`;
- `CURRENT_GATE = AG-01 — TECHNOLOGY STACK`;
- `AG-01 STATUS = VERIFIED`;
- `LAST VERIFIED FILE = AG-01 — TECHNOLOGY STACK`;
- `TOTAL PLANNED PHYSICAL FILES = NOT YET CALCULATED`;
- `GITHUB APPLICATION UPLOAD = LOCKED`.

`NEXT ACTION` is a control action, not a File ID, while the physical-file `NEXT FILE` remains `NOT YET CREATED` until the exact inventory is locked.

## 27. Manifest Self-Audit Checklist

Before this Manifest can become the locked physical-file manifest, verify:

- [ ] Canonical filename/path is unique.
- [ ] Technology stack is locked.
- [ ] Repository structure is locked.
- [ ] All required domains are covered.
- [ ] Exact physical files are enumerated.
- [ ] Every file has a unique ID.
- [ ] Every path is unique for active files.
- [ ] Every file has all mandatory fields.
- [ ] No wildcard remains in the locked file table.
- [ ] No `...` placeholder remains in the locked file table.
- [ ] Every `DEPENDS_ON` ID exists.
- [ ] Every `USED_BY` ID exists.
- [ ] Dependency graph is internally consistent.
- [ ] No unapproved dependency cycle exists.
- [ ] Every file has an applicable test method.
- [ ] Every VERIFIED file has evidence and a commit reference.
- [ ] Security/secret checks are defined.
- [ ] Phase integration checks are defined.
- [ ] Critical paths are mapped to implementation and tests.
- [ ] Change Request mechanism is operational.
- [ ] Physical-file count is calculated from exact records only.
- [ ] `NIDDE_PROJECT_CONTROL.md` agrees with this Manifest.
- [ ] GitHub state agrees with the recorded verified files.

## 28. Current Next Action

`PHASE 00 → COMPLETE ARCHITECTURE GATES → ENUMERATE EXACT PHYSICAL FILES → BUILD DEPENDENCY GRAPH → DEFINE TESTS → LOCK TOTAL PLANNED → BEGIN PHASE 01`

**No application code is authorized for upload while the architecture/file-count lock is incomplete.**


## 29. Phase 00 Gate Verification Record

| Gate | Result | Evidence | Implementation unlocked? |
|---|---|---|---|
| AG-01 — Technology Stack | VERIFIED | Official documentation cross-check dated 2026-08-18 | NO |

AG-01 verification does not authorize application implementation. AG-02 is the next architecture gate.
