NIDDE 

NIDDE — On-Demand Services Marketplace

NIDDE is a multi-domain services marketplace connecting clients with service providers, including individual artisans and companies.

The platform is designed around server-authoritative business logic, controlled API contracts, secure authentication and authorization, service lifecycle management, payments and cash transactions, KYC, messaging, location/tracking, notifications, reviews, administration, testing, CI/CD, production operations, and controlled release management.

Project Status 

Current Phase: Phase 00 — Architecture
Architecture State: Completed / Baseline Established
Implementation State: Ready to begin controlled Phase 01 implementation
Repository Mode: Strict
Architecture Principle: Backend/domain authority

The architecture gates define the approved boundaries that implementation must follow.

Core Architecture Rules 

NIDDE follows these mandatory principles:

The backend/domain layer is authoritative for protected business state. Client applications are untrusted. Client-side state must never become authoritative for protected business decisions. Authentication and authorization are enforced server-side. Resource ownership is enforced server-side. Service lifecycle transitions are validated server-side. Electronic payment success is determined through the approved payment integration boundary. Cash transactions remain separate from electronic payment state. KYC approval remains server-authoritative. Sensitive data follows minimization and access-control requirements. External providers are isolated behind controlled integration boundaries. Critical operations use appropriate idempotency and replay protection. Secrets must never be committed to Git. Architecture boundaries must not be silently redefined by implementation. Service Lifecycle 

The authoritative service lifecycle is:

REQUESTED ↓ ACCEPTED ↓ EN_ROUTE ↓ ARRIVED ↓ IN_PROGRESS ↓ COMPLETED 

Cancellation and error states are explicitly modeled and validated.

The client may request an allowed transition, but the server determines whether the transition is valid.

Main User Roles Client 

Clients can use authorized marketplace functionality to:

discover services create service requests receive provider offers select an offer follow service progress use approved payment flows review completed services Artisan 

Artisans can, when authorized and eligible:

maintain their provider profile complete required KYC become available for service requests submit offers accept assigned work execute services complete services receive approved payout information Company 

Companies can, when authorized and eligible:

maintain company/provider information complete required verification receive service opportunities submit offers accept work execute services complete services receive approved payout information Admin 

Administrative functionality is restricted to explicitly authorized administrative identities.

Administrative actions must remain auditable and server-authorized.

Core Domain Areas 

The system architecture covers:

Users and profiles Client Artisan Company Services and categories Service offerings Service requests Offers Service lifecycle Locations and tracking Conversations and messages Payments Cash transactions Reviews KYC KYC documents Notifications Administrative and moderation records Audit records Analytics and reporting Repository Structure 

The repository follows the approved top-level boundaries:

NIDDE/ ├── README.md ├── NIDDE_PROJECT_CONTROL.md ├── NIDDE_MASTER_FILE_MANIFEST.md ├── .gitignore ├── .env.example │ ├── .github/ │ └── workflows/ │ ├── backend/ ├── database/ ├── shared/ ├── android/ ├── admin/ ├── tests/ ├── docs/ └── infrastructure/ 

These directories have separate responsibilities.

backend/ 

Contains server-side application implementation, API boundaries, domain/application services, authorization enforcement, business rules, and backend runtime concerns.

database/ 

Contains database schema artifacts, migrations, seed-related artifacts, and database verification support.

shared/ 

Contains only genuinely shared contract-level or cross-client artifacts.

android/ 

Contains the Android client and Android-specific architecture, UI, networking, storage, permissions, location, notifications, payment interaction, and Android testing.

admin/ 

Contains approved administrative interface/application artifacts.

Administrative authority remains enforced by the backend.

tests/ 

Contains repository-level testing assets that are not exclusively owned by a single implementation module.

docs/ 

Contains project documentation, architecture evidence, decisions, and operational documentation.

infrastructure/ 

Contains deployment, production infrastructure, monitoring, backup/recovery, environment orchestration, and infrastructure validation artifacts.

.github/ 

Reserved for GitHub-native repository configuration and workflows.

CI/CD policy remains governed by the CI/CD architecture.

Critical Paths Client Registration → Login → Search → Request → Receive Offers → Select → Service → Payment → Review Artisan Registration → KYC → Approval → Online → Receive Request → Offer → Accept → Execute → Complete → Payout Company Registration → KYC → Approval → Provider Operations → Receive Request → Offer → Accept → Execute → Complete → Payout Admin 

Where an approved administrative interface exists:

Login → Administrative Authentication → Authorized Management → Orders → KYC → Payments → Complaints / Moderation → Logs → Analytics 

Any critical-path failure prevents production readiness.

Security 

NIDDE treats all external input and client-controlled values as untrusted.

The following must never be accepted solely from client state:

role permissions ownership administrative privilege KYC approval payment success protected lifecycle state financial settlement service completion 

Production secrets, credentials, private keys, payment secrets, provider secrets, and real environment files must never be committed to Git.

.env.example contains only safe variable names and placeholders.

External Integrations 

External services are treated as untrusted dependencies.

Provider-specific implementations must remain behind controlled integration boundaries.

Potential integration categories include:

maps geocoding routing electronic payments notifications email/SMS where approved secure storage identity/KYC providers 

External provider responses must be validated before they can affect authoritative NIDDE state.

Android 

The Android application is an untrusted client.

It is responsible for presentation and user interaction, while the backend remains authoritative for:

identity authorization ownership lifecycle payments KYC financial state administrative authority protected business decisions 

Local storage and cached state must never become an independent authoritative source.

Testing 

Testing must cover the architecture-defined critical areas, including:

backend/domain behavior API contracts database behavior authentication authorization ownership lifecycle transitions payments cash transactions KYC security external integrations Android behavior offline/degraded behavior critical end-to-end flows 

Real production credentials must never be required for ordinary automated tests.

CI/CD 

CI/CD is responsible for controlled validation and delivery according to the approved CI/CD architecture.

Implementation must not bypass:

validation testing security checks artifact controls deployment gates release requirements Production 

Production architecture must provide controlled:

deployment environment separation database operation monitoring logging backups recovery migrations rollback operational access 

Production readiness is not established merely because the application builds successfully.

Release 

A release requires successful completion of the approved:

implementation checks test requirements security checks critical-path validation production-readiness checks final audit release acceptance criteria rollback criteria Development Rule 

Implementation must proceed from the approved architecture.

Do not:

create random top-level directories introduce undocumented dependencies bypass the backend authority create client-side authoritative business logic introduce provider-specific business logic into the UI commit secrets silently change API contracts silently change domain ownership silently change lifecycle semantics 

When an implementation conflict is discovered, stop the affected work and resolve the architecture/contract conflict before continuing.

Source of Truth 

When project documents disagree, use the project's defined source-of-truth order:

Canonical Master File Manifest NIDDE_PROJECT_CONTROL.md Verified architecture-gate documents Repository state Unverified drafts or local copies 

Conversation history must not override the repository's canonical control documents.

Implementation Roadmap 

The controlled implementation sequence is:

Architecture Baseline ↓ Physical File Inventory ↓ Dependency Graph ↓ Backend Foundation ↓ Database Foundation ↓ Authentication / Authorization ↓ Marketplace / Services ↓ Requests / Offers ↓ Service Lifecycle ↓ Messaging ↓ Location / Tracking ↓ Payments / Cash ↓ KYC ↓ Notifications ↓ Reviews ↓ Admin ↓ Android Integration ↓ Testing ↓ CI/CD ↓ Production ↓ Release 

Each implementation stage must remain compatible with the approved architecture.

Project Principle 

NIDDE is built as a controlled system rather than a collection of independent screens and endpoints.

The backend/domain boundary owns authoritative business decisions.

The Android and administrative clients interact through approved contracts.

External providers remain isolated.

Security, testing, CI/CD, production, and release requirements remain part of the system lifecycle rather than being added after implementation.

NIDDE — Architecture First. Server Authority. Controlled Implementation.

