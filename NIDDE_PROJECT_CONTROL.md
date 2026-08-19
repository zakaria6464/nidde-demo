NIDDE — PROJECT CONTROL 

Project: NIDDE
Control Revision: V2.1.0
Phase: 00 — ARCHITECTURE
Mode: STRICT
Last Updated: 2026-08-19

1. Purpose 

This document is the central execution and status-control record for NIDDE.

It records:

current project phase architecture baseline architecture gate status repository control state implementation lock state physical-file inventory state next authorized execution step cross-document consistency requirements 

The canonical Master File Manifest remains the authority for physical-file planning and dependency identity.

2. Current Project State Control Status Project NIDDE Current Phase PHASE 00 — ARCHITECTURE Architecture Baseline AG-01 through AG-13 prepared Repository Structure ESTABLISHED Application Implementation LOCKED UNTIL FINAL BASELINE CHECK Physical-File Inventory NOT YET LOCKED Physical-File Count NOT YET CALCULATED Production Secrets in Git FORBIDDEN Application Runtime Upload LOCKED Next Execution Stage FINAL ARCHITECTURE / REPOSITORY BASELINE CHECK 3. Architecture Gate Sequence 

The canonical architecture sequence is:

AG-01 — TECHNOLOGY STACK ↓ AG-02 — REPOSITORY & SYSTEM ARCHITECTURE ↓ AG-03 — SYSTEM DEPENDENCY ARCHITECTURE ↓ AG-04 — DATA MODEL ↓ AG-05 — API CONTRACT ARCHITECTURE ↓ AG-06 — AUTHENTICATION & AUTHORIZATION ↓ AG-07 — SECURITY MODEL ↓ AG-08 — EXTERNAL INTEGRATIONS ↓ AG-09 — ANDROID ARCHITECTURE ↓ AG-10 — TESTING ARCHITECTURE ↓ AG-11 — CI/CD ARCHITECTURE ↓ AG-12 — PRODUCTION ARCHITECTURE ↓ AG-13 — RELEASE ARCHITECTURE 

No later gate may silently redefine an earlier gate.

4. Architecture Baseline 

The current architecture baseline consists of the prepared AG-01 through AG-13 documents.

The baseline establishes:

technology boundaries repository boundaries system dependencies data model API contract authentication and authorization security requirements external integrations Android architecture testing architecture CI/CD architecture production architecture release architecture 

Each gate remains subject to its own verification status.

READY FOR VERIFICATION must not be interpreted as VERIFIED.

5. Repository Control 

The canonical repository root is:

NIDDE/ 

Approved top-level boundaries are:

NIDDE/ ├── README.md ├── NIDDE_PROJECT_CONTROL.md ├── NIDDE_MASTER_FILE_MANIFEST.md ├── .gitignore ├── .env.example ├── .github/ │ └── workflows/ ├── backend/ ├── database/ ├── shared/ ├── android/ ├── admin/ ├── tests/ ├── docs/ └── infrastructure/ 

No new top-level implementation boundary may be introduced without an architecture/change-control decision.

6. Repository Boundary Rules backend/ 

Owns server-side application and domain implementation.

database/ 

Owns database schema artifacts, migrations, seed strategy, and database-specific implementation artifacts.

shared/ 

Owns only genuinely shared contract-level or cross-client artifacts.

android/ 

Owns Android application implementation and Android-specific modules, resources, networking, local storage, permissions, location, notifications, payment interaction, and Android testing.

admin/ 

Owns approved administrative application/interface artifacts.

Administrative authority remains server-controlled.

tests/ 

Owns repository-level testing assets that are not exclusively owned by a single implementation module.

docs/ 

Owns project documentation, architecture evidence, decisions, and verification documentation.

infrastructure/ 

Owns deployment, production infrastructure, monitoring, backup/recovery, environment orchestration, and infrastructure validation.

.github/ 

Owns GitHub-native repository configuration and workflows.

CI/CD behavior remains governed by AG-11.

7. Authority Model 

The backend/domain boundary remains authoritative for protected business state.

Client applications must never become authoritative for:

roles permissions ownership administrative authority KYC approval payment success protected lifecycle state financial settlement service completion 

External providers are also not authoritative owners of NIDDE domain state.

8. Security Control 

The following must never be committed to Git:

passwords API keys JWT secrets private keys payment credentials webhook secrets provider credentials database credentials production credentials real production environment files sensitive KYC documents sensitive production configuration 

.env.example may contain variable names and safe placeholders only.

Every repository implementation change must preserve the security requirements established by AG-07.

9. Architecture Lock 

The project follows an architecture-first approach.

Until the final architecture baseline and physical-file inventory are formally accepted:

APPLICATION IMPLEMENTATION = CONTROLLED / LOCKED PHYSICAL FILE COUNT = NOT YET LOCKED 

The existence of architecture documents does not automatically authorize arbitrary application source creation.

Implementation must begin only through the approved implementation sequence.

10. Cross-Gate Consistency 

Every implementation decision must remain consistent with:

AG-01 technology decisions AG-02 repository boundaries AG-03 system dependencies AG-04 data model AG-05 API contracts AG-06 authentication and authorization AG-07 security model AG-08 external integrations AG-09 Android architecture AG-10 testing architecture AG-11 CI/CD architecture AG-12 production architecture AG-13 release architecture 

If two gates appear to conflict:

stop the affected implementation identify the exact conflicting requirement determine which gate owns the decision patch the appropriate architecture document update the control record resume implementation only after consistency is restored 

No silent workaround is permitted.

11. Critical Business Authority 

The following remain server-authoritative:

Identity 

Authentication establishes identity.

Authorization determines permitted actions.

Ownership 

Resource ownership is validated server-side.

Lifecycle 

The authoritative service lifecycle is:

REQUESTED → ACCEPTED → EN_ROUTE → ARRIVED → IN_PROGRESS → COMPLETED 

Cancellation and error states are explicitly controlled.

Payment 

Electronic payment authority follows:

Client → Approved API → NIDDE Backend → AG-08 Integration Boundary → Validated Provider Result → Server Payment State KYC 

KYC approval requires authorized server-side action.

Location 

Location and tracking are sensitive and must not independently prove payment, service completion, or cash settlement.

12. Implementation Sequence 

After the architecture baseline is accepted, implementation proceeds in controlled stages:

1. Repository / Physical File Baseline 2. Backend Foundation 3. Database Foundation 4. Authentication / Authorization 5. Marketplace Foundation 6. Service Requests 7. Offers 8. Service Lifecycle 9. Messaging 10. Location / Tracking 11. Payments / Cash 12. KYC 13. Notifications 14. Reviews 15. Administration 16. Android Integration 17. Full Testing 18. CI/CD Validation 19. Production Preparation 20. Release Preparation 

A stage must not silently bypass requirements belonging to another gate.

13. Critical Flow Protection 

The following flows are considered critical:

Client Registration → Login → Search → Request → Receive Offers → Select → Service → Payment → Review Artisan Registration → KYC → Approval → Online → Receive Request → Offer → Accept → Execute → Complete → Payout Company Registration → KYC → Approval → Provider Operations → Receive Request → Offer → Accept → Execute → Complete → Payout Admin 

Only where an approved administrative interface exists:

Login → Administrative Authentication → Authorized Management → Orders → KYC → Payments → Complaints / Moderation → Logs → Analytics 

Failure of a critical path must block the affected readiness stage.

14. Change Control 

Any change affecting:

architecture repository boundaries domain ownership API contracts authentication authorization security boundaries payment authority KYC authority lifecycle semantics external integration boundaries testing obligations CI/CD behavior production architecture release requirements 

must be explicitly evaluated against the affected architecture gate.

No implementation shortcut may redefine an architecture contract.

15. GitHub Control 

GitHub is the repository hosting and collaboration boundary.

The repository must preserve:

canonical filenames architecture evidence controlled commit history protected configuration boundaries secret-free repository state approved workflow locations 

.github/workflows/ is reserved for GitHub-native workflow definitions.

Application runtime source code must not be placed in .github/.

16. Verification Language 

The following statuses have distinct meanings:

DRAFT 

Document is under development.

READY FOR VERIFICATION 

Document is prepared for consistency and verification review.

VERIFIED 

Document has passed its required verification criteria.

LOCKED 

The relevant decision must not be changed without formal change control.

READY FOR VERIFICATION must never be represented as VERIFIED.

17. Current Authorized Action 

The immediate task after establishing this control file is:

FINAL ARCHITECTURE BASELINE CHECK ↓ PHYSICAL FILE INVENTORY ↓ DEPENDENCY / OWNERSHIP CHECK ↓ IMPLEMENTATION BASELINE ↓ CONTROLLED IMPLEMENTATION 

No arbitrary application source files should be created before the physical-file and dependency baseline is established.

18. Final Control Statement 

NIDDE is controlled through architecture gates, repository boundaries, explicit ownership, server-authoritative business logic, security controls, testing requirements, CI/CD requirements, production requirements, and release requirements.

The purpose of this control file is to prevent implementation drift and silent architectural contradictions.

Any future implementation must preserve the approved architecture unless an explicit architecture change is made and recorded.

NIDDE PROJECT CONTROL — ACTIVE

MODE: STRICT

APPLICATION IMPLEMENTATION: CONTROLLED

ARCHITECTURE BASELINE: AG-01 → AG-13

PHYSICAL-FILE INVENTORY: NOT YET LOCKED

