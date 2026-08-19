# NIDDE — AG-03 SYSTEM & DEPENDENCY ARCHITECTURE

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-03 — System & Dependency Architecture
Revision: V1.0.1
Status: READY FOR FORMAL GATE REVIEW
Implementation: LOCKED
Physical-file count: NOT YET CALCULATED

## 1. Objective

AG-03 defines the system boundaries, domain boundaries, application layers, dependency direction, service ownership, interfaces, runtime responsibilities, core data flows, security boundaries, and failure rules required before implementation.

This document is an architecture contract.

It does not authorize application implementation.

## 2. System Boundary

NIDDE is a multi-role services marketplace supporting:

- Client
- Artisan
- Company
- Admin

Backend authorization is authoritative.

Clients must never establish privileged authority through client-controlled state.

External providers are untrusted dependencies and must not become authoritative owners of NIDDE domain state.

## 3. Logical Architecture

The logical architecture is:

Client Applications
        |
        v
Interface / API Layer
        |
        v
Application / Use-Case Layer
        |
        v
Domain Layer
        |
        +----------------------+
        |                      |
        v                      v
Data Access Abstractions   Integration Abstractions
        |                      |
        v                      v
Database / Persistence    External Provider Adapters

The dependency rule is:

Interface -> Application -> Domain

Infrastructure implements or supports approved abstractions and must not become a dependency of Domain business logic.

## 4. Domain Boundaries

NIDDE domains include:

- Identity & Accounts
- Authentication & Authorization
- Client
- Artisan
- Company
- Services / Marketplace
- Requests
- Offers
- Service Lifecycle
- Messaging
- Location / Tracking
- Payments
- Cash
- Reviews / Ratings
- KYC / Verification
- Notifications
- Admin / Moderation
- Analytics / Reporting
- Security
- Audit / Logging

Each domain owns its business rules and exposes explicit contracts.

A domain must not silently transfer ownership of its authoritative state to another domain.

## 5. Application Layers

### 5.1 Interface Layer

The Interface Layer is responsible for:

- transport handling
- request parsing
- serialization
- boundary validation
- authentication-context extraction
- API error mapping

The Interface Layer must not contain authoritative core business decisions.

### 5.2 Application Layer

The Application Layer is responsible for:

- use-case orchestration
- application workflows
- transaction boundaries
- authorization at use-case boundaries
- coordination between domain services
- controlled cross-domain operations

The Application Layer must respect domain ownership.

It must not bypass domain rules or directly mutate another domain's authoritative state without an approved contract.

### 5.3 Domain Layer

The Domain Layer owns:

- business rules
- invariants
- policies
- domain state transitions
- authoritative business decisions

The Domain Layer must not directly depend on:

- HTTP
- Android UI
- database implementations
- external provider SDKs
- provider-specific implementations

### 5.4 Infrastructure Layer

Infrastructure is responsible for:

- database persistence
- repository implementations
- external-provider adapters
- storage adapters
- payment adapters
- notification adapters
- KYC adapters
- mapping and routing adapters
- other technical integrations

Infrastructure must implement approved contracts and abstractions.

## 6. Dependency Direction

The approved dependency direction is:

Client
    ->
Interface
    ->
Application
    ->
Domain

Infrastructure provides implementations for approved technical abstractions.

Rules:

1. Clients depend only on published contracts.
2. Domain logic must not depend directly on infrastructure implementations.
3. Database access must be behind approved data-access boundaries.
4. External providers must be isolated behind adapters.
5. Circular dependencies are prohibited unless explicitly approved through project control.
6. Cross-domain direct database writes are prohibited.
7. Dependency changes require impact analysis.
8. Provider-specific implementation details must not leak into domain contracts without explicit architectural approval.

## 7. Core Request Flow

A normal service-request flow is:

Client
    ->
Authenticate
    ->
Discover Services
    ->
Create Request
    ->
Validate
    ->
Persist Request
    ->
Notify Eligible Providers
    ->
Receive Offers
    ->
Select Offer
    ->
Start Service

Each operation must pass through the appropriate authorization and domain rules.

## 8. Offer Flow

The offer flow is:

Provider
    ->
Authenticate
    ->
Authorize
    ->
Check Eligibility
    ->
Submit Offer
    ->
Validate Offer
    ->
Persist Offer
    ->
Request Receives Offer

The server remains authoritative for eligibility, ownership, offer state, and acceptance.

## 9. Service Lifecycle

The authoritative service lifecycle is:

REQUESTED
    ->
ACCEPTED
    ->
EN_ROUTE
    ->
ARRIVED
    ->
IN_PROGRESS
    ->
COMPLETED

Cancellation and error states must be modeled explicitly.

Every protected transition must define:

- previous state
- new state
- authorized actor
- timestamp
- reason where required
- correlation or reference identifier where required

Service Lifecycle owns authoritative service-state transitions.

Other domains may request a transition through an approved interface but may not silently mutate lifecycle state.

## 10. Payment Flow

The payment flow is:

Payment Trigger
    ->
Authorization
    ->
Approved Cash or Electronic Payment Flow
    ->
Provider / Transaction Result
    ->
Validated Financial State
    ->
Notification
    ->
Audit

Electronic payment success must never be accepted solely from client-side state.

Provider callbacks and webhooks must be validated before they affect authoritative payment state.

## 11. Financial Boundary

Payments and Cash are separate concepts.

Financial operations must be:

- attributable
- auditable
- protected against duplicate processing
- explicit about pending, successful, failed, rejected, and cancelled states
- linked to appropriate internal references

Cash settlement must not be represented as electronic-provider success.

Payment and Cash records remain under their approved financial ownership boundaries.

## 12. Domain Ownership

The authoritative owners are:

| Concern | Authoritative Owner |
|---|---|
| Identity | Identity / Accounts |
| Sessions and authentication state | Authentication / Authorization |
| Roles and permissions | Authentication / Authorization |
| Marketplace services | Services / Marketplace |
| Requests | Requests |
| Offers | Offers |
| Service state | Service Lifecycle |
| Messages | Messaging |
| Location and tracking | Location / Tracking |
| Electronic financial transactions | Payments |
| Cash settlement records | Cash |
| Reviews | Reviews / Ratings |
| Verification state | KYC / Verification |
| Notifications | Notifications |
| Privileged moderation actions | Admin / Moderation |
| Operational metrics | Analytics / Reporting |
| Security controls | Security |
| Audit evidence | Audit / Logging |

Cross-domain operations must use approved interfaces and must preserve the authoritative ownership of each domain.

## 13. Authorization Boundary

Authentication establishes identity.

Authorization determines permission.

Server-side authorization is mandatory for privileged operations.

The server must never trust client-controlled values for:

- role
- ownership
- payment success
- KYC approval
- service completion
- administrative authority

Authorization must be evaluated according to the authenticated identity, requested operation, resource ownership, and applicable domain rules.

## 14. Cross-Domain Communication

The preferred communication order is:

1. Explicit domain contract
2. Application orchestration
3. Event or message when asynchronous behavior is required

Every cross-domain operation must define:

- owning domain
- requesting domain
- input
- output
- authorization requirement
- failure behavior
- transaction or consistency expectation

Hidden side effects are prohibited.

A cross-domain call must not silently mutate unrelated authoritative state.

## 15. External Integration Boundary

Potential external integrations include:

- maps
- geocoding
- routing
- electronic payment providers
- push notification providers
- email providers where approved
- SMS providers where approved
- secure storage
- KYC providers

Each integration must be isolated behind an adapter or approved integration boundary.

Integration requirements include, where applicable:

- authentication
- secure secret handling
- timeout policy
- failure policy
- retry policy
- idempotency policy
- webhook validation
- audit requirements
- provider-reference tracking

External provider output must be validated before affecting authoritative NIDDE state.

## 16. Security and Audit Boundary

Required system controls include:

- input validation
- authorization
- rate limiting
- secure secret handling
- sensitive-data protection
- audit logging
- abuse controls
- security testing
- controlled external integration boundaries

Real secrets must never be committed to Git.

Security-specific requirements remain governed by AG-07.

Authentication and authorization-specific requirements remain governed by AG-06.

AG-03 defines the system-level boundaries and must not replace those gates.

## 17. Failure and Consistency

The system must distinguish at minimum:

- success
- failure
- pending
- rejected
- cancelled
- expired

External provider failures must never be interpreted as successful business operations.

Retries are allowed only when safe.

Non-idempotent operations must not be blindly retried.

Financial operations require appropriate idempotency and duplicate-processing protection.

## 18. Data Access Boundary

Application and domain logic must not perform uncontrolled direct database operations.

Persistence must occur through approved data-access boundaries.

Cross-domain database writes are prohibited.

Each authoritative domain must retain control of its own persisted business state.

Database implementation details remain infrastructure concerns.

## 19. Observability and Audit

Critical operations should produce sufficient information for operational diagnosis and audit.

Where applicable, records should support:

- correlation identifiers
- actor identification
- domain identification
- operation identification
- timestamps
- provider references
- failure classification
- lifecycle transitions
- financial events
- administrative actions

Logs must not expose secrets or unnecessary sensitive data.

## 20. Compatibility Rules

AG-03 must remain compatible with:

- AG-01 Technology Stack
- AG-02 Repository Structure
- AG-04 Data Model
- AG-05 API Contract
- AG-06 Authentication / Authorization
- AG-07 Security Model
- AG-08 External Integrations

Compatibility does not transfer ownership between gates.

AG-03 defines system and dependency architecture while referenced gates retain ownership of their respective contracts.

## 21. Implementation Boundary

AG-03 does not authorize implementation.

The following remain locked until the architecture and file-count conditions are satisfied:

APPLICATION IMPLEMENTATION = LOCKED

PHYSICAL FILE COUNT = NOT YET CALCULATED

Uploading an architecture document does not authorize application source-code implementation.

## 22. Verification Requirements

AG-03 may become VERIFIED only after all applicable checks pass:

1. Static document consistency check.
2. Compatibility with AG-01.
3. Compatibility with AG-02 repository boundaries.
4. Domain ownership review.
5. Dependency-direction review.
6. Critical-flow review.
7. Security and authorization review.
8. Compatibility review against dependent architecture contracts.
9. Evidence recorded in Project Control.
10. Evidence recorded in the Master File Manifest.

Until verification is complete:

APPLICATION IMPLEMENTATION = LOCKED

PHYSICAL FILE COUNT = NOT YET CALCULATED

## 23. Verification Status

Current status:

READY FOR FORMAL GATE REVIEW

This status does not mean VERIFIED.

AG-03 becomes VERIFIED only after the verification requirements in Section 22 have been completed and recorded.

## 24. Next Gate

After successful AG-03 verification:

AG-04 — DATA MODEL

No implementation file is authorized merely because AG-03 is verified.

## 25. Change Control

Any change affecting:

- domain ownership
- dependency direction
- lifecycle authority
- financial boundaries
- authorization boundaries
- external integration boundaries
- data-access boundaries

requires impact analysis against affected architecture gates.

No silent architecture changes are permitted.

## 26. Control Statement

AG-03 establishes the system and dependency architecture for NIDDE.

It does not replace:

- AG-01 Technology Stack
- AG-02 Repository Structure
- AG-04 Data Model
- AG-05 API Contract
- AG-06 Authentication / Authorization
- AG-07 Security Model
- AG-08 External Integrations

The architecture remains implementation-locked until the complete project control process authorizes Phase 01.

---

End of AG-03
