# NIDDE — AG-02 REPOSITORY STRUCTURE

**Project:** NIDDE
**Manifest baseline:** `NIDDE_MASTER_FILE_MANIFEST.md` (canonical; exact version governed by the verified canonical Manifest)
**Revision:** V2.0.4
**Architecture Gate:** AG-02 — Repository Structure
**Status:** VERIFIED
**Application implementation:** LOCKED
**Physical-file count:** NOT YET CALCULATED
**Purpose:** Lock repository boundaries before physical-file inventory and implementation.

---

## 1. Gate Objective

AG-02 locks the repository's top-level directories, module boundaries, naming conventions, configuration locations, test locations, documentation locations, and infrastructure boundaries.

This document does **not** create application source files and does **not** authorize application implementation. AG-01 is already VERIFIED, while AG-02 is the next architecture gate.

---

## 2. Repository Root

The canonical repository root is:

```text
NIDDE/
```

No application code is placed outside the repository root.

---

## 3. Canonical Top-Level Structure

The approved top-level structure is defined here at the boundary level. Exact physical-file inventory remains deferred until the required architecture gates are resolved and the canonical Manifest is locked.

```text
NIDDE/
├── README.md
├── NIDDE_PROJECT_CONTROL.md
├── NIDDE_MASTER_FILE_MANIFEST.md
├── .gitignore
├── .env.example
├── .github/
│   └── workflows/   # GitHub-native workflow location; exact files deferred to AG-11
│
├── backend/
├── database/
├── shared/
├── android/
├── admin/
├── tests/
├── docs/
└── infrastructure/
```

### `.github/` boundary

`.github/` is a controlled repository-platform boundary reserved only for GitHub-native repository configuration that GitHub requires at this canonical path, including `.github/workflows/` and repository automation metadata. It must not contain application runtime source code, business-domain implementation, or deployment infrastructure. The existence of `.github/` does not approve any CI/CD design; CI/CD architecture, workflow policy, validation order, security checks, artifact handling, and deployment gates remain exclusively subject to AG-11.

### Boundary rule

Only the directories explicitly defined by this gate may become canonical top-level implementation boundaries. New top-level directories require a formal Change Request and impact assessment before adoption.

---

## 4. Directory Responsibilities

### 4.1 `backend/`

Server-side application code, API interfaces, domain/application services, authentication enforcement, business rules, background jobs, and backend runtime concerns.

Backend code must not silently own database migration history that belongs in `database/`.

### 4.2 `database/`

Database schema artifacts, migrations, database-specific configuration that is not environment-secret material, seed strategy artifacts, and database verification support.

### 4.3 `shared/`

Only genuinely shared, contract-level or cross-client artifacts belong here. Shared code must not become a dumping ground for backend-only or Android-only implementation.

### 4.4 `android/`

The Android application and its Android-specific modules, resources, configuration, permissions, navigation, networking integration, local storage, notifications, location, payment integration, and Android tests as defined by the Android architecture gate.

### 4.5 `admin/`

Administrative interface/application artifacts and admin-specific presentation/integration code. Administrative authority and security rules remain governed by backend authorization.

### 4.6 `tests/`

Repository-level test assets that do not belong exclusively to one implementation module, including cross-domain, end-to-end, critical-path, security, and integration orchestration where applicable.

### 4.7 `docs/`

Architecture decisions, technical documentation, operational documentation, verification evidence, and other project documentation that is intended to live with the repository.

### 4.8 `infrastructure/`

Deployment, production infrastructure, monitoring, backup/recovery, environment orchestration, and infrastructure validation artifacts. CI/CD supporting configuration may live here only when it is not GitHub-native and does not duplicate or own files whose canonical path is under `.github/`. The final CI/CD ownership model is subject to AG-11.

---

## 5. Root File Responsibilities

| Path | Responsibility | Canonical? |
|---|---|---|
| `README.md` | Project entry documentation | YES |
| `NIDDE_PROJECT_CONTROL.md` | Central execution/status control | YES |
| `NIDDE_MASTER_FILE_MANIFEST.md` | Master physical-file planning/control | YES |
| `.gitignore` | Repository exclusion rules | YES |
| `.env.example` | Non-secret environment variable template | YES |

No production secret, private key, token, password, credential, or real environment file may be committed.

---

## 6. Module Boundary Rules

1. `backend/` owns server-side runtime behavior.
2. `database/` owns database evolution artifacts.
3. `android/` owns Android platform implementation.
4. `admin/` owns administrative UI/application implementation.
5. `shared/` is restricted to artifacts genuinely shared across boundaries.
6. `tests/` contains cross-boundary test assets; module-local tests remain with their owning module where the later testing architecture specifies this.
7. `docs/` contains documentation and evidence, not runtime source code.
8. `infrastructure/` contains deployment/operations infrastructure, not business-domain implementation.
9. `.github/` contains GitHub-native repository automation/configuration only.
10. `.github/` and `infrastructure/` must not contain duplicate CI/CD ownership; GitHub-required workflow files belong under `.github/`, while non-GitHub-native infrastructure/supporting configuration may belong under `infrastructure/`. AG-11 is the authority for the final CI/CD architecture.

A file must have one clear owning boundary. Cross-boundary reuse must be explicit through a dependency/contract relationship.

---

## 7. Naming Rules

### Files

- Use descriptive, stable names.
- Use the repository's established naming convention consistently within each technology.
- Do not use temporary names such as `new`, `final2`, `latest`, `test2`, or `copy` as canonical production filenames.
- Version numbers belong in controlled release/artifact naming where required; they must not be used to create uncontrolled duplicate source files.

### Directories

- Lowercase directory names are preferred for repository paths.
- Use stable semantic names.
- Avoid spaces in canonical paths.
- Avoid duplicate semantic directories such as `backend2/`, `old_backend/`, or `backup_backend/`.

### IDs

Physical file IDs are assigned later by the Master File Manifest after the architecture gates are resolved. AG-02 does not guess the final physical-file count.

---

## 8. Configuration Boundaries

Configuration is separated into:

1. **Committed templates** — safe examples such as `.env.example`.
2. **Non-secret repository configuration** — version-controlled configuration required to build/test.
3. **Environment secrets** — supplied only through a secure environment/secret manager.
4. **Production configuration** — controlled by deployment/infrastructure processes.

No secret is embedded in source code, documentation, test fixtures, or committed configuration.

---

## 9. Test Boundaries

Testing is layered:

```text
module-local tests
        ↓
integration tests
        ↓
API/database/auth/security tests
        ↓
critical-path tests
        ↓
Android/end-to-end tests
        ↓
production verification
```

Exact test tooling and physical test-file inventory remain subject to AG-10 and the final physical-file manifest.

---

## 10. Documentation Boundaries

`docs/` may contain:

- Architecture decisions
- Domain documentation
- API documentation
- Operational procedures
- Security documentation
- Testing evidence
- Release/final-audit evidence

The two central control documents remain at repository root:

```text
NIDDE_PROJECT_CONTROL.md
NIDDE_MASTER_FILE_MANIFEST.md
```

---

## 11. Infrastructure Boundary

All deployment and operational infrastructure belongs under:

```text
infrastructure/
```

This includes, when approved by later architecture gates:

- Non-GitHub-native CI/CD supporting configuration, where required by AG-11
- Deployment configuration
- Environment orchestration
- Monitoring configuration
- Logging infrastructure configuration
- Backup/recovery configuration
- Production validation tooling

Secrets remain outside Git and are injected securely.

---

## 12. Forbidden Repository Patterns

The following are prohibited as canonical project structure:

- duplicate repositories nested inside the repository;
- `old/`, `backup/`, `copy/`, `final/`, `final2/`, or similar uncontrolled source trees;
- generated build output committed as source;
- IDE caches and local machine artifacts;
- production secrets;
- arbitrary top-level directories;
- arbitrary files or runtime source under `.github/` outside approved GitHub-native automation/configuration;
- duplicated implementations of the same module;
- files with ambiguous ownership;
- temporary experiments presented as production source.

---

## 13. Dependency Direction

The repository structure must preserve clear dependency direction.

At a high level:

```text
Android ────────┐
Admin ──────────┼──→ Backend contracts/API
Shared ─────────┘

Backend ─────────→ Database contracts/storage

Tests ───────────→ approved system boundaries

Infrastructure ──→ deployment/runtime boundaries
```

No UI layer may bypass backend authorization or directly own privileged database operations.

The exact dependency graph is finalized by AG-03 and later architecture gates.

---

## 14. Change Control

A new top-level directory, boundary change, or canonical root-file change requires:

```text
CHANGE REQUEST
→ impact assessment
→ dependency impact
→ security impact
→ test impact
→ approval
→ manifest/control update
```

No structural change is accepted merely because it is convenient during implementation.

---

## 15. AG-02 Verification Checklist

| Check | Status |
|---|---|
| Top-level directories explicitly defined | PASS — VERIFIED |
| Module boundaries defined | PASS — VERIFIED |
| Naming rules defined | PASS — VERIFIED |
| Root configuration locations defined | PASS — VERIFIED |
| Test boundary defined | PASS — VERIFIED |
| Documentation boundary defined | PASS — VERIFIED |
| Infrastructure boundary defined | PASS — VERIFIED |
| GitHub-native `.github/` boundary defined | PASS — VERIFIED |
| Forbidden duplicate/temporary structures defined | PASS — VERIFIED |
| Secret boundary defined | PASS — VERIFIED |
| Physical-file count calculated | NOT YET — intentionally deferred |
| Application implementation unlocked | NO |

---

## 16. Patch Record

| Patch | Issue | Resolution | State |
|---|---|---|---|
| `AG-02-P01` | `.github/` was described as a repository-platform boundary but was not represented in the canonical top-level tree; CI/CD ownership with `infrastructure/` was ambiguous. | Added `.github/workflows/` to the canonical boundary tree; separated GitHub-native files from non-GitHub-native infrastructure/supporting configuration; reserved final CI/CD architecture decisions for AG-11. | PATCHED — RE-VERIFICATION REQUIRED |

## 16. Gate Status

**AG-02 STATUS: VERIFIED**

Verification completed for AG-02:

1. Static/document consistency check: PASS.
2. Compatibility with AG-01: PASS.
3. Boundary/dependency review: PASS.
4. Security/configuration review: PASS.
5. Repository-structure verification: PASS.
6. Verification evidence is ready to be recorded in `NIDDE_PROJECT_CONTROL.md` and `NIDDE_MASTER_FILE_MANIFEST.md`.

Until then:

```text
APPLICATION IMPLEMENTATION = LOCKED
PHYSICAL FILE COUNT = NOT YET CALCULATED
```

---

## 16A. Revision V2.0.4 — Boundary Clarification

This revision resolves the AG-02 boundary ambiguity identified during verification review:

1. `.github/` is explicitly represented in the canonical top-level structure because GitHub-native files require that repository path.
2. `.github/` is limited to GitHub-native repository configuration and workflow files; it is not an application-runtime or deployment-infrastructure boundary.
3. `infrastructure/` owns non-GitHub-native deployment/operations infrastructure and supporting configuration.
4. `.github/` and `infrastructure/` must not duplicate CI/CD ownership.
5. AG-11 remains the authority for the final CI/CD architecture, workflow policy, validation order, security checks, artifact handling, and deployment gates.
6. No physical CI/CD file inventory is created by AG-02.

This revision is **VERIFIED** for the repository-boundary definition. Evidence registration in the canonical Manifest and Project Control remains the required bookkeeping step.

---

## 17. Source-of-Truth Note

This AG-02 document is subordinate to the canonical Master Manifest and Project Control. Once verified and committed, GitHub becomes the official repository source for this artifact.

No unverified local copy overrides the GitHub version.
