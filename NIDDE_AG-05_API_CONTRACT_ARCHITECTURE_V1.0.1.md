# NIDDE — AG-05 API CONTRACT ARCHITECTURE

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-05 — API Contract
Revision: V1.0.1
Status: READY FOR VERIFICATION
Implementation: LOCKED

## 1. Purpose

AG-05 defines the API contract boundary required by NIDDE before implementation.

This document is an architecture contract.

It does not implement endpoints, application source code, database migrations, deployment configuration, or client code.

## 2. Scope

AG-05 owns:

- API resources and interfaces
- request and response contracts
- authentication requirements at the API boundary
- authorization requirements at the API boundary
- validation and error contracts
- pagination
- filtering and sorting
- idempotency
- API versioning
- webhook contract requirements

The following remain owned by their respective gates:

- AG-06 — Authentication / Authorization
- AG-07 — Security Model
- AG-08 — External Integrations
- AG-09 — Android Architecture
- AG-10 — Testing Architecture
- AG-11 — CI/CD Architecture
- AG-12 — Production Architecture
- AG-13 — Release Architecture

AG-05 must not redefine the scope of another gate.

## 3. Source of Truth

API contracts must respect:

1. Canonical Master File Manifest
2. NIDDE Project Control
3. Verified AG-03 System / Dependency Architecture
4. Verified AG-04 Data Model
5. Verified AG-06 through AG-13 constraints where applicable

An unverified document cannot override a verified architecture contract.

## 4. Domain Boundary

AG-05 must respect the authoritative ownership defined by AG-04.

The API may expose operations around:

- User
- Client Profile
- Artisan Profile
- Company Profile
- Service Category
- Service Offering
- Service Request
- Offer
- Location
- Tracking Event
- Conversation
- Message
- Payment
- Cash Transaction
- Review
- KYC Case
- KYC Document
- Notification
- Administrative / Moderation records

No API operation may silently introduce a new authoritative owner for an existing domain entity.

## 5. Authentication and Authorization

Protected API operations require server-side authentication and authorization.

Authentication establishes identity.

Authorization determines permission.

The API must never trust client-provided values as authoritative for:

- role
- ownership
- administrative privilege
- protected lifecycle state
- payment success
- KYC approval

Detailed authentication and authorization architecture belongs to AG-06.

## 6. Request Validation

Every externally supplied request must be validated before domain processing.

Validation must cover, where applicable:

- required fields
- data types
- allowed values
- length limits
- numeric ranges
- identifiers
- state compatibility
- ownership
- authorization
- business-rule eligibility

Validation failures must not partially mutate authoritative state.

## 7. Service Request and Offer Contracts

A Service Request must reference an existing authorized client and valid service/category information.

An Offer must:

- reference an existing request
- reference an eligible provider
- contain a valid amount and currency where applicable
- respect request lifecycle
- respect provider eligibility
- prevent prohibited duplicate active offers
- identify the accepted offer uniquely when one is accepted

The server is authoritative for all protected offer and request state.

## 8. Service Lifecycle

The authoritative lifecycle defined by AG-04 is:

REQUESTED → ACCEPTED → EN_ROUTE → ARRIVED → IN_PROGRESS → COMPLETED

Cancellation and error states are modeled explicitly.

Clients request valid actions.

The server determines whether a transition is permitted.

Every accepted transition must preserve the lifecycle history and audit requirements defined by AG-04.

The API must not provide a generic unrestricted endpoint that allows clients to assign arbitrary lifecycle states.

## 9. Location and Tracking

Location operations must respect the privacy and ownership rules defined by AG-04 and AG-07.

Tracking data is time-based operational information.

Tracking data alone is not authoritative proof of:

- payment
- service completion
- financial settlement

Access to location and tracking information must be authorized.

## 10. Messaging

Conversation and Message APIs must enforce participant authorization.

A user may access only conversations they are permitted to access.

Message creation must verify:

- authenticated sender
- conversation membership
- allowed message type
- content/reference validation
- lifecycle or moderation restrictions where applicable

## 11. Payment and Cash

Payment and Cash Transaction are separate domain concepts.

The API must not allow a client to declare an electronic payment successful.

Electronic payment confirmation is accepted only through the approved integration boundary defined by AG-08.

Payment operations must support appropriate:

- idempotency
- status validation
- authorization
- auditability
- reconciliation

Payment status must distinguish applicable states such as:

- pending
- successful
- failed
- cancelled
- rejected

Cash settlement is recorded separately from electronic provider state.

## 12. KYC

KYC operations must enforce server-side authorization.

The API must distinguish:

- KYC submission
- KYC review
- KYC approval
- KYC rejection
- KYC document access

KYC approval cannot be assigned by a client.

Sensitive KYC document contents must not be returned through unrestricted API responses.

Secure storage and provider boundaries belong to AG-08.

## 13. Reviews

Review creation requires server-side validation of eligibility.

The API must enforce:

- completed-service eligibility
- rating range
- author identity
- subject identity
- duplicate-review rules
- moderation status

Moderation actions must remain auditable.

## 14. Notifications

Notification APIs expose notification information only to authorized recipients or administrative actors where explicitly permitted.

Notification delivery is not authoritative for the underlying business transaction.

A failed notification must not automatically change the state of a request, service, or payment.

## 15. Administrative Operations

Administrative API operations require explicit server-side administrative authorization.

Administrative operations must be auditable.

The API must not expose unrestricted administrative mutation endpoints to normal users.

## 16. Error Contract

API errors must use a consistent machine-readable structure.

Where applicable, an error response should contain:

- error code
- human-readable message
- safe validation details
- correlation/reference identifier

Errors must never expose:

- secrets
- credentials
- access tokens
- private keys
- database credentials
- raw SQL errors
- stack traces
- sensitive KYC contents
- unnecessary internal implementation details

## 17. Pagination

Collection endpoints must use bounded pagination.

Pagination must use a stable ordering strategy.

Page size must be server-bounded.

Filtering and sorting fields must be explicitly allowlisted.

Clients must not provide arbitrary database expressions.

## 18. Idempotency

Idempotency is required for operations where retries could produce duplicate side effects.

This includes, where applicable:

- payment mutations
- payment webhook processing
- financial settlement
- externally retried commands
- other non-repeatable side effects

Repeated processing of the same idempotency key must not create duplicate authoritative effects.

## 19. Webhooks

Webhook contracts must be designed with AG-08.

Webhook processing must include, where supported:

- authenticity verification
- signature verification
- replay protection
- idempotency
- event validation
- safe retry behavior
- auditability

Webhook payloads must not be trusted merely because they reached an exposed endpoint.

## 20. API Versioning

The API must use an explicit versioning strategy.

Breaking contract changes require controlled versioning or migration.

A breaking change must not silently alter an already approved contract.

## 21. Sensitive Data

API responses must follow data minimization.

Sensitive information must be returned only when:

- required for the operation
- authorized for the requesting actor
- allowed by the security model

Secrets and authentication material must never be returned through ordinary API responses.

## 22. Correlation and Audit References

Important operations should carry a correlation/reference identifier that allows related application, integration, and audit events to be traced.

The correlation identifier must not itself expose sensitive information.

## 23. Rate and Abuse Controls

AG-05 defines the API contract requirement for controlled request rates.

Actual security policy and enforcement strategy belongs to AG-07.

API design must allow appropriate controls for:

- authentication attempts
- recovery
- request creation
- offers
- messaging
- payment operations
- KYC operations
- administrative operations

## 24. Compatibility Rules

Later gates and implementation must preserve:

- AG-04 entity ownership
- AG-04 lifecycle semantics
- AG-06 authorization boundaries
- AG-07 security controls
- AG-08 integration boundaries

If a conflict is discovered, implementation must stop for the affected contract until the architecture conflict is resolved.

## 25. Verification Criteria

AG-05 may become VERIFIED only when:

- its scope matches the canonical AG-05 definition
- AG-04 ownership is respected
- lifecycle rules are consistent
- payment and cash boundaries are preserved
- KYC boundaries are preserved
- AG-06 authorization requirements are mapped
- AG-07 security requirements are mapped
- AG-08 webhook/integration requirements are mapped
- no unresolved blocking contradiction exists
- required verification evidence is recorded

`READY FOR VERIFICATION` does not mean `VERIFIED`.

## 26. Implementation Lock

AG-05 does not authorize implementation.

Implementation remains:

`LOCKED`

until the complete canonical architecture sequence and final readiness conditions are satisfied.

## 27. Control Statement

This document is intentionally limited to the API Contract gate.

It must not be used to redefine:

- authentication architecture
- security architecture
- external integration architecture
- Android architecture
- testing architecture
- CI/CD architecture
- production architecture
- release architecture

Any future change affecting those areas must be handled by the appropriate canonical gate.
