# NIDDE — AG-02 REPOSITORY STRUCTURE

Project: NIDDE
Manifest baseline: NIDDE_MASTER_FILE_MANIFEST.md
Revision: V2.0.4
Architecture Gate: AG-02 — Repository & System Architecture
Status: VERIFIED
Application implementation: LOCKED
Physical-file count: NOT YET CALCULATED
Verification evidence: NIDDE_AG-02_V2.0.4_VERIFICATION_REPORT.md

---

## 1. Gate Objective

AG-02 defines and locks the repository's top-level boundaries, module boundaries, naming conventions, configuration locations, test locations, documentation locations, GitHub-native repository boundaries, and infrastructure boundaries.

This document does not create application source files and does not authorize application implementation.

AG-01 is VERIFIED.

AG-02 is VERIFIED.

The next architecture gate is AG-03, subject to its dependency prerequisites and verification rules.

---

## 2. Repository Root

The canonical repository root is:

NIDDE/

No application code is placed outside the repository root.

---

## 3. Canonical Top-Level Structure

The approved top-level structure is defined at the architecture-boundary level.

Exact physical-file inventory remains deferred until the required architecture gates are resolved and the canonical Master File Manifest is locked.

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

### .github/ Boundary

.github/ is a controlled repository-platform boundary reserved only for GitHub-native repository configuration that GitHub requires at this canonical path, including .github/workflows/ and repository automation metadata.

It must not contain:

- application runtime source code
- business-domain implementation
- unauthorized deployment infrastructure
- duplicated application modules

The existence of .github/ does not approve any specific CI/CD design.

CI/CD architecture, workflow policy, validation order, security checks, artifact handling, and deployment gates remain governed by AG-11.

### Boundary Rule

Only the directories explicitly defined by this gate may become canonical top-level implementation boundaries.

New top-level directories require a formal Change Request and impact assessment before adoption.

---

## 4. Directory Responsibilities

### 4.1 backend/

Server-side application code, API interfaces, domain/application services, authentication enforcement, business rules, background jobs, and backend runtime concerns.

Backend code must not silently own database migration history that belongs in database/.

### 4.2 database/

Database schema artifacts, migrations, database-specific configuration that is not environment-secret material, seed strategy artifacts, and database verification support.

### 4.3 shared/

Only genuinely shared, contract-level or cross-client artifacts belong here.

Shared code must not become a dumping ground for backend-only or Android-only implementation.

### 4.4 android/

The Android application and its Android-specific modules, resources, configuration, permissions, navigation, networking integration, local storage, notifications, location, payment integration, and Android tests as defined by AG-09.

### 4.5 admin/

Administrative interface/application artifacts and admin-specific presentation/integration code.

Administrative authority and security rules remain governed by backend authorization.

### 4.6 tests/

Repository-level test assets that do not belong exclusively to one implementation module, including cross-domain, end-to-end, critical-path, security, and integration orchestration where applicable.

Module-local tests remain with their owning module where required by AG-10.

### 4.7 docs/

Architecture decisions, technical documentation, operational documentation, verification evidence, release evidence, final-audit evidence, and other project documentation intended to live with the repository.

### 4.8 infrastructure/

Deployment, production infrastructure, monitoring, backup/recovery, environment orchestration, and infrastructure validation artifacts.

CI/CD supporting configuration may live here only when it is not GitHub-native and does not duplicate or own files whose canonical path is under .github/.

Final CI/CD architecture and workflow ownership remain governed by AG-11.

---

## 5. Root File Responsibilities

| Path | Responsibility | Canonical? |
|---|---|---|
| README.md | Project entry documentation | YES |
| NIDDE_PROJECT_CONTROL.md | Central execution/status control | YES |
| NIDDE_MASTER_FILE_MANIFEST.md | Master physical-file planning/control | YES |
| .gitignore | Repository exclusion rules | YES |
| .env.example | Non-secret environment variable template | YES |

No production secret, private key, token, password, credential, or real environment file may be committed.

---

## 6. Module Boundary Rules

1. backend/ owns server-side runtime behavior.
2. database/ owns database evolution artifacts.
3. android/ owns Android platform implementation.
4. admin/ owns administrative UI/application implementation.
5. shared/ is restricted to artifacts genuinely shared across boundaries.
6. tests/ contains cross-boundary test assets; module-local tests remain with their owning module where AG-10 permits.
7. docs/ contains documentation and evidence, not runtime source code.
8. infrastructure/ contains deployment/operations infrastructure, not business-domain implementation.
9. .github/ contains GitHub-native repository automation/configuration only.
10. .github/ and infrastructure/ must not contain duplicate CI/CD ownership. GitHub-required workflow files belong under .github/; non-GitHub-native infrastructure/supporting configuration may belong under infrastructure/. AG-11 remains authoritative for final CI/CD architecture.

A file must have one clear owning boundary.

Cross-boundary reuse must be explicit through a dependency or contract relationship.

---

## 7. Naming Rules

### Files

- Use descriptive, stable names.
- Use the repository's established naming convention consistently within each technology.
- Do not use temporary names such as new, final2, latest, test2, or copy as canonical production filenames.
- Version numbers must not be used to create uncontrolled duplicate source files.
- Superseded canonical files must be explicitly identified through the approved Manifest/Project Control process.

### Directories

- Lowercase directory names are preferred for repository paths.
- Use stable semantic names.
- Avoid spaces in canonical paths.
- Avoid duplicate semantic directories such as backend2/, old_backend/, or backup_backend/.

### IDs

Physical file IDs are assigned later by the Master File Manifest after the architecture gates are resolved.

AG-02 does not guess the final physical-file count.

---

## 8. Configuration Boundaries

Configuration is separated into:

1. Committed templates — safe examples such as .env.example.
2. Non-secret repository configuration — version-controlled configuration required to build/test.
3. Environment secrets — supplied only through an approved secure environment/secret manager.
4. Production configuration — controlled by deployment/infrastructure processes.

No secret is embedded in:

- source code
- documentation
- test fixtures
- committed configuration
- Android source
- CI/CD output

---

## 9. Test Boundaries

Testing is layered according to the architecture established by AG-10.

At the repository-boundary level:

module-local tests
        ↓
component/integration tests
        ↓
API/database/auth/security tests
        ↓
critical-path tests
        ↓
Android/end-to-end tests
        ↓
production-safe verification

Exact test tooling, test semantics, and physical test-file inventory remain governed by AG-10 and the canonical Master File Manifest.

AG-02 does not redefine testing architecture.

---

## 10. Documentation Boundaries

docs/ may contain:

- Architecture decisions
- Domain documentation
- API documentation
- Operational procedures
- Security documentation
- Testing evidence
- Verification evidence
- Release evidence
- Final-audit evidence

The two central control documents remain at repository root:

NIDDE_PROJECT_CONTROL.md
NIDDE_MASTER_FILE_MANIFEST.md

---

## 11. Infrastructure Boundary

All deployment and operational infrastructure belongs under:

infrastructure/

This includes, when approved by later architecture gates:

- Non-GitHub-native CI/CD supporting configuration, where required by AG-11
- Deployment configuration
- Environment orchestration
- Monitoring configuration
- Logging infrastructure configuration
- Backup/recovery configuration
- Production validation tooling

Secrets remain outside Git and are injected through approved secure mechanisms.

AG-12 owns the production architecture.

AG-11 owns CI/CD architecture.

AG-02 does not replace either gate.

---

## 12. Forbidden Repository Patterns

The following are prohibited as canonical project structure:

- duplicate repositories nested inside the repository
- old/, backup/, copy/, final/, final2/, or similar uncontrolled source trees
- generated build output committed as source
- IDE caches and local machine artifacts
- production secrets
- arbitrary top-level directories
- arbitrary files or runtime source under .github/ outside approved GitHub-native automation/configuration
- duplicated implementations of the same module
- files with ambiguous ownership
- temporary experiments presented as production source
- unauthorized architecture copies presented as canonical
- silent replacement of canonical control documents

---

## 13. Dependency Direction

The repository structure must preserve clear dependency direction.

At a high level:

Android ────────┐
Admin ──────────┼──→ Backend contracts/API
Shared ─────────┘

Backend ─────────→ Database contracts/storage

Tests ───────────→ Approved system boundaries

Infrastructure ──→ Deployment/runtime boundaries

No UI layer may bypass backend authorization or directly own privileged database operations.

The exact dependency graph is governed by AG-03 and later architecture gates.

AG-02 does not redefine dependency ownership.

---

## 14. Change Control

A new top-level directory, boundary change, or canonical root-file change requires:

CHANGE REQUEST
→ impact assessment
→ dependency impact
→ security impact
→ test impact
→ approval
→ manifest/control update

No structural change is accepted merely because it is convenient during implementation.

No silent architecture change is permitted.

No silent dependency change is permitted.

No random file creation is permitted.

---

## 15. AG-02 Verification Checklist

| Check | Status |
|---|---|
| Top-level directories explicitly defined | VERIFIED |
| Module boundaries defined | VERIFIED |
| Naming rules defined | VERIFIED |
| Root configuration locations defined | VERIFIED |
| Test boundary defined | VERIFIED |
| Documentation boundary defined | VERIFIED |
| Infrastructure boundary defined | VERIFIED |
| GitHub-native .github/ boundary defined | VERIFIED |
| Forbidden duplicate/temporary structures defined | VERIFIED |
| Secret boundary defined | VERIFIED |
| Physical-file count calculated | NOT YET — intentionally deferred |
| Application implementation unlocked | NO |
| Verification evidence recorded | YES |

---

## 16. Verification Record

AG-02 V2.0.4 was formally reviewed against the required verification criteria.

Verification evidence is recorded in:

NIDDE_AG-02_V2.0.4_VERIFICATION_REPORT.md

The verification report records:

- Static/document consistency: PASS
- AG-01 compatibility: PASS
- Boundary/dependency review: PASS
- Security/configuration review: PASS
- Repository registration check: PASS
- Physical-file inventory: DEFERRED by design

Therefore:

AG-02 = VERIFIED

The physical-file count remains:

NOT YET CALCULATED

Application implementation remains:

LOCKED

---

## 17. Gate Decision

AG-02 STATUS: VERIFIED

The repository and system boundary defined by AG-02 is accepted.

The next authorized architecture gate is:

AG-03 — SYSTEM & DEPENDENCY ARCHITECTURE

This does not authorize application implementation.

Implementation remains locked until the complete canonical architecture sequence and final readiness conditions are satisfied.

---

## 18. Source-of-Truth and Control Rules

This document is governed by the canonical:

NIDDE_MASTER_FILE_MANIFEST.md
NIDDE_PROJECT_CONTROL.md

The verification evidence for this gate is:

NIDDE_AG-02_V2.0.4_VERIFICATION_REPORT.md

No unverified local copy may override the verified canonical state.

The canonical status of this gate is determined by the approved verification evidence and the canonical Project Control/Manifest state.

If a future change affects AG-02, the applicable Change Request and verification process must be completed.

A future patch must not be assumed verified merely because the file was edited.

---

## 19. Implementation Lock

AG-02 does not authorize implementation.

Implementation remains:

LOCKED

until:

- AG-01 through AG-13 satisfy their required verification conditions
- the canonical architecture sequence is complete
- the physical-file baseline is generated and locked
- dependency and control conditions are satisfied
- final readiness requirements are satisfied
- required verification evidence is recorded

No application implementation should be created solely because AG-02 is VERIFIED.

---

## 20. Cross-Gate Boundary

AG-02 must remain consistent with:

AG-01 — Technology Stack
AG-03 — System / Dependency Architecture
AG-04 — Data Model
AG-05 — API Contract
AG-06 — Authentication / Authorization
AG-07 — Security Model
AG-08 — External Integrations
AG-09 — Android Architecture
AG-10 — Testing Architecture
AG-11 — CI/CD Architecture
AG-12 — Production Architecture
AG-13 — Release Architecture

AG-02 owns repository/system boundaries only.

It must not redefine:

- technology decisions owned by AG-01
- dependency architecture owned by AG-03
- data ownership owned by AG-04
- API contract owned by AG-05
- authentication/authorization owned by AG-06
- security model owned by AG-07
- external integrations owned by AG-08
- Android architecture owned by AG-09
- testing architecture owned by AG-10
- CI/CD architecture owned by AG-11
- production architecture owned by AG-12
- release authority owned by AG-13

Any conflict must be resolved through the canonical architecture/change-control process.

---

## 21. Final Control Statement

AG-02 establishes the repository and system boundary required by NIDDE.

It does not authorize implementation.

It does not create the final physical-file inventory.

It does not replace any later architecture gate.

The authoritative state is:

PROJECT: NIDDE
PHASE: 00 — ARCHITECTURE
GATE: AG-02
REVISION: V2.0.4
STATUS: VERIFIED
APPLICATION IMPLEMENTATION: LOCKED
PHYSICAL-FILE COUNT: NOT YET CALCULATED
NEXT ARCHITECTURE GATE: AG-03

AG-02 STATUS: VERIFIED

IMPLEMENTATION: LOCKED
