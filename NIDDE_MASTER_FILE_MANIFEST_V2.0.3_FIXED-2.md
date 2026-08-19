NIDDE — MASTER FILE MANIFEST 

Project: NIDDE
Phase: 00 — ARCHITECTURE / REPOSITORY BASELINE
Manifest Revision: V2.1.0
Status: READY FOR VERIFICATION
Implementation: CONTROLLED
Authority: Repository File and Boundary Control

1. Purpose 

This document defines the canonical repository file manifest for NIDDE.

It establishes:

approved repository boundaries canonical architecture-document locations required control files implementation directories testing boundaries infrastructure boundaries GitHub configuration boundaries file naming rules forbidden repository content physical-file inventory requirements 

This manifest does not implement application behavior.

2. Manifest Authority 

This manifest is the canonical reference for the planned repository structure.

It must remain consistent with:

NIDDE_PROJECT_CONTROL.md AG-01 through AG-13 architecture documents repository state approved implementation decisions 

If an implementation file is required but is not represented by the approved repository structure, the implementation must stop until the manifest is updated or the file is explicitly classified as an allowed implementation artifact.

3. Canonical Root 

The repository root is:

NIDDE/ 

The repository must not introduce unrelated top-level directories.

4. Required Root Files 

The following root files are approved:

README.md NIDDE_PROJECT_CONTROL.md NIDDE_MASTER_FILE_MANIFEST_V2.0.3_FIXED-2.md NIDDE_ARCHITECTURE_ALIGNMENT_CONTROL_V1.0.1.md .env.example .gitignore CONTRIBUTING.md SECURITY.md 

A future canonical rename of the manifest must be performed through controlled change management rather than by silently creating competing manifest files.

5. Architecture Documentation 

Architecture documents belong to the repository documentation/control layer.

Canonical architecture gates are:

AG-01 — Technology Stack AG-02 — Repository / System Architecture AG-03 — System Dependency Architecture AG-04 — Data Model AG-05 — API Contract Architecture AG-06 — Authentication / Authorization Architecture AG-07 — Security Model AG-08 — External Integrations Architecture AG-09 — Android Architecture AG-10 — Testing Architecture AG-11 — CI/CD Architecture AG-12 — Production Architecture AG-13 — Release Architecture 

Each gate must have one canonical active document.

Duplicate active versions of the same gate must not coexist.

Historical or superseded documents must be clearly identified as archived or superseded if retained.

6. Repository Boundaries 

Approved implementation boundaries:

backend/ database/ shared/ android/ admin/ tests/ docs/ infrastructure/ 

Approved GitHub configuration boundary:

.github/ 7. Backend Boundary backend/ 

Owns server-side implementation.

Expected responsibilities include:

API implementation application services domain services authorization enforcement lifecycle enforcement payment state handling KYC state handling messaging authorization notification coordination business validation integration orchestration 

Backend implementation must follow AG-03 through AG-08.

8. Database Boundary database/ 

Owns database-specific implementation artifacts.

Potential contents include:

database/ ├── migrations/ ├── seeds/ └── schema/ 

Database artifacts must remain consistent with AG-04.

The database must not silently redefine domain ownership or API behavior.

9. Shared Boundary shared/ 

Contains only artifacts that are genuinely shared between approved application boundaries.

Examples may include:

shared contract definitions generated API contract models where approved shared validation schemas where explicitly authorized 

Provider-specific implementation and backend-private logic must not be moved into shared/ merely for convenience.

10. Android Boundary android/ 

Owns Android implementation.

Expected responsibilities include:

Android application source UI navigation state management API client local persistence secure session handling permissions location presentation notifications approved payment interaction Android-specific testing 

Android remains an untrusted client.

AG-09 controls the Android architecture.

11. Admin Boundary admin/ 

Owns approved administrative interface implementation.

Administrative privileges remain backend-authorized.

The presence of an admin UI must never be interpreted as proof of administrative authority.

12. Testing Boundary tests/ 

Owns repository-level testing assets.

Testing must remain compatible with AG-10.

Tests may include:

unit tests integration tests contract tests security tests failure simulations end-to-end tests repository validation tests 

Tests must not require production credentials during ordinary automated execution.

13. Documentation Boundary docs/ 

Owns:

architecture evidence verification reports architecture decisions implementation notes operational documentation controlled project documentation 

Documentation must not silently become a second source of architectural authority.

14. Infrastructure Boundary infrastructure/ 

Owns production and infrastructure implementation artifacts.

Potential responsibilities include:

deployment configuration infrastructure definitions environment orchestration monitoring configuration backup/recovery configuration operational tooling production validation 

Infrastructure remains governed by AG-12.

15. GitHub Boundary .github/ 

Reserved for GitHub-native repository configuration.

Approved workflow location:

.github/workflows/ 

CI/CD implementation must follow AG-11.

Application runtime source code must not be placed inside .github/.

16. Environment Configuration 

The repository may contain:

.env.example 

This file may contain:

variable names safe placeholders documentation comments 

It must not contain:

real credentials production secrets private keys payment secrets provider secrets real database credentials 

Real environment files remain outside the repository.

17. Git Ignore Requirements 

.gitignore must protect against accidental inclusion of:

local environment files secrets build outputs IDE files generated local artifacts caches temporary files signing material 

The exact .gitignore content must remain compatible with AG-07 and AG-11.

18. Security Restrictions 

The following are forbidden in the repository:

Production credentials Private keys Payment secrets Webhook secrets Provider secret keys Real authentication secrets KYC identity documents Sensitive production exports Unapproved personal data dumps Production database dumps 

Security requirements are controlled by AG-07.

19. Duplicate Gate Protection 

Only one active canonical document may represent each architecture gate.

For example, the repository must not contain two active AG-08 architecture contracts.

If an older document is retained:

STATUS: SUPERSEDED 

must be clearly indicated.

The active document must be unambiguous.

20. Naming Rules 

Architecture documents should follow the pattern:

NIDDE_AG-XX_<DESCRIPTIVE_NAME>_V<MAJOR>.<MINOR>.<PATCH>.md 

Verification reports should use an explicitly distinguishable name.

Repository control documents must not be confused with implementation source files.

File names must remain stable after implementation begins unless a controlled change is recorded.

21. Physical File Inventory 

Before large-scale implementation begins, the repository must undergo a physical-file inventory.

The inventory must record:

path filename file type owner boundary architecture gate dependency role implementation status verification status whether the file is required, generated, or optional 

The inventory must be generated from the actual repository state.

It must not be based only on assumptions or planned filenames.

22. Dependency Ownership 

Every implementation file must have a clear ownership boundary.

Dependencies must not create unauthorized coupling between:

Android and database internals UI and provider SDK business logic client and administrative internals backend and Android private implementation application code and infrastructure secrets 

Cross-boundary dependencies must be explicitly justified.

23. Source-of-Truth Rules 

When documents appear to conflict, resolve them in this order:

1. Canonical Master File Manifest 2. NIDDE_PROJECT_CONTROL.md 3. Verified architecture gates 4. Repository implementation state 5. Unverified drafts / historical copies 

A lower-priority artifact must not silently override a higher-priority control document.

24. Implementation Readiness 

The manifest does not authorize unrestricted implementation.

Before implementation proceeds, the following must be confirmed:

architecture gates are consistent repository structure is consistent active gate documents are unique required control files exist forbidden files are absent physical-file inventory is complete dependency ownership is understood security restrictions are enforced implementation sequence is approved 25. Change Control 

Changes to this manifest require explicit review when they affect:

repository boundaries architecture-document identity canonical file names implementation ownership dependency ownership security boundaries testing boundaries CI/CD boundaries production boundaries release boundaries 

Do not create a second manifest to bypass a conflict.

Update the canonical manifest through controlled change.

26. Repository Readiness Checklist 

Before implementation:

[ ] Root control files verified [ ] Active architecture documents identified [ ] Duplicate active gates removed or marked superseded [ ] .env.example contains no real secrets [ ] .gitignore is present [ ] No production credentials are committed [ ] Repository boundaries match this manifest [ ] Physical-file inventory completed [ ] Dependency ownership reviewed [ ] Cross-gate consistency reviewed [ ] Implementation authorization confirmed 27. Implementation Sequence 

The repository implementation should proceed in controlled stages:

Architecture Baseline ↓ Physical File Inventory ↓ Dependency Graph ↓ Backend Foundation ↓ Database Foundation ↓ Authentication / Authorization ↓ Marketplace Foundation ↓ Requests / Offers ↓ Service Lifecycle ↓ Messaging ↓ Location / Tracking ↓ Payments / Cash ↓ KYC ↓ Notifications ↓ Reviews ↓ Administration ↓ Android Integration ↓ Testing ↓ CI/CD ↓ Production ↓ Release 

Each stage must satisfy its relevant architecture gate.

28. Final Manifest Rule 

This manifest controls repository structure and file identity.

It does not override:

domain authority API contracts security requirements authentication rules external integration requirements Android architecture testing requirements CI/CD requirements production requirements release requirements 

Those responsibilities remain owned by their respective architecture gates.

29. Control Statement 

NIDDE must maintain one coherent repository structure with one active canonical document per architecture gate.

Implementation files must be physically present, correctly owned, and traceable to the approved architecture.

No duplicate active architecture contract, undocumented repository boundary, secret-bearing file, or silent architecture workaround is permitted.

NIDDE MASTER FILE MANIFEST — ACTIVE

MANIFEST STATUS: READY FOR VERIFICATION

IMPLEMENTATION: CONTROLLED

ARCHITECTURE BASELINE: AG-01 → AG-13


