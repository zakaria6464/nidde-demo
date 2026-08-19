# NIDDE — AG-08 EXTERNAL INTEGRATIONS ARCHITECTURE

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-08 — External Integrations
Revision: V1.0.1
Status: READY FOR VERIFICATION
Implementation: LOCKED

## 1. Purpose

AG-08 defines the architecture boundary for external services and providers used by NIDDE.

This document is an architecture contract.

It does not implement provider SDKs, application source code, deployment configuration, or infrastructure.

## 2. Scope

AG-08 owns:

- external service boundaries
- provider adapters
- provider authentication
- maps, geocoding, and routing integrations
- electronic payment integrations
- notification providers
- email and SMS providers where approved
- secure storage providers
- identity and KYC providers
- provider webhooks
- provider failure handling
- timeout and retry behavior
- provider reconciliation
- integration observability

AG-08 does not redefine the scope of other architecture gates.

## 3. Integration Principles

All external providers are treated as untrusted dependencies.

Integrations must:

- use controlled boundaries
- use least-privilege credentials
- validate external responses
- handle provider failures explicitly
- prevent duplicate side effects
- protect provider credentials
- isolate provider-specific implementation details
- remain replaceable where practical

An external provider must not become the authoritative owner of NIDDE domain state.

## 4. Adapter Boundary

Provider-specific APIs and SDKs must be isolated behind an integration boundary.

Domain logic must not become tightly coupled to provider-specific implementation details.

The integration boundary translates:

- internal request to provider request
- provider response to validated internal result
- provider event to validated internal event

External data must be validated before affecting authoritative state.

## 5. Maps, Geocoding and Routing

Where required, mapping services may provide:

- geocoding
- reverse geocoding
- routing
- distance estimation
- map data

The integration must define:

- provider credentials
- request limits
- timeout behavior
- failure behavior
- retry behavior where safe
- caching where appropriate
- privacy constraints

Mapping-provider output is not automatically authoritative business data.

## 6. Location Privacy

Location and tracking information is sensitive.

Integration usage must follow:

- minimum necessary data
- authorized access
- purpose limitation
- secure transport
- controlled retention

Tracking data remains governed by AG-04 and protected by AG-07.

Tracking information alone cannot prove:

- payment completion
- service completion
- cash settlement

## 7. Electronic Payments

Electronic payment providers are isolated behind a controlled payment integration boundary.

The integration may support:

- payment creation
- payment status retrieval
- provider confirmation
- webhook handling
- cancellation
- refund or adjustment flows where approved
- reconciliation

Provider identifiers may be stored as external references but do not replace NIDDE's internal Payment identifier.

## 8. Payment Confirmation

The client must never be the authoritative source of electronic payment success.

The following pattern is prohibited:

client -> payment_success = true -> server accepts payment as successful

The approved pattern is:

provider
    ->
validated integration boundary
    ->
server-side payment state

Provider callbacks and webhooks must be authenticated and validated before changing authoritative payment state.

## 9. Payment Idempotency

Payment operations must support idempotency where duplicate requests or retries are possible.

The integration must prevent:

- duplicate charges
- duplicate payment records
- duplicate webhook effects
- duplicate refunds
- inconsistent payment state

Repeated processing of the same provider event must not create duplicate authoritative effects.

## 10. Webhook Security

Webhook endpoints are trust boundaries.

Webhook processing must consider:

- authenticity validation
- signature verification where supported
- timestamp validation where supported
- replay protection
- event identity
- idempotency
- payload validation
- safe retries
- auditability

A webhook must not be trusted merely because it reached the NIDDE server.

Security requirements are coordinated with AG-07.

## 11. Notification Providers

Notification providers may include:

- push notifications
- email
- SMS

where approved by the product requirements.

Notification delivery is not authoritative for the underlying business transaction.

For example, a failed notification must not automatically change a service or payment into a failed state.

Business state remains authoritative inside NIDDE.

## 12. Notification Reliability

Notification integrations should define:

- delivery attempts
- retry policy
- provider timeout
- failure recording
- deduplication where necessary
- delivery status

Retries must not create duplicate business actions.

## 13. Secure Storage

Sensitive files, including KYC documents where applicable, must use an approved secure storage boundary.

Git is not an approved location for:

- KYC documents
- identity documents
- private keys
- production credentials
- payment secrets
- provider secrets

Storage access must be:

- authenticated
- authorized
- restricted
- auditable where required

## 14. KYC and Identity Providers

External KYC or identity providers may provide verification information.

Their results must be:

- authenticated
- validated
- mapped to NIDDE's internal KYC model
- recorded according to approved lifecycle rules

An external provider does not automatically control:

- NIDDE roles
- permissions
- account status
- administrative privileges

KYC authorization remains governed by AG-06.

## 15. Provider Failure

Every critical integration must define explicit failure behavior.

Failure categories may include:

- timeout
- unavailable provider
- invalid provider response
- authentication failure
- rate limit
- temporary network failure
- permanent provider rejection
- malformed webhook
- duplicate event

The system must not convert an external failure into a false successful business state.

## 16. Retry Policy

Retries are permitted only when safe.

Before retrying an operation, the system must determine whether the operation is idempotent or protected by an idempotency mechanism.

The system must not blindly retry financial or other non-repeatable operations.

## 17. Timeouts

External calls must use bounded timeouts.

No external provider request may block the application indefinitely.

Timeout behavior must produce a controlled application result.

## 18. Reconciliation

Critical external integrations, especially payments, must support reconciliation where required.

Reconciliation compares:

- internal state
- external provider state
- external references
- relevant transaction or event identifiers

Discrepancies must be detectable and reviewable.

## 19. Credentials and Secrets

Provider credentials must never be committed to Git.

Examples include:

- API keys
- secret keys
- private keys
- webhook secrets
- payment credentials
- KYC provider credentials
- cloud storage credentials

Credentials must be supplied through approved secret or environment management.

The `.env.example` file may contain variable names and safe placeholders only.

## 20. Provider Data

External data must be minimized and retained only as required.

Provider responses must not be copied wholesale into internal records when only a limited subset is required.

Sensitive provider data must follow AG-07 security requirements.

## 21. Observability

Critical integrations should provide enough operational information to diagnose failures.

Observability should support:

- request correlation
- provider reference tracking
- latency
- failure classification
- retry visibility
- webhook processing visibility
- reconciliation status

Logs must not expose provider secrets or sensitive user data.

## 22. API Boundary

AG-05 owns the public API contract.

AG-08 owns the external-provider boundary.

The public API must not expose provider-specific implementation details unless explicitly required by the approved contract.

Provider failures must be translated into controlled domain or API results.

## 23. Authentication Boundary

AG-06 owns NIDDE user authentication and authorization.

AG-08 owns authentication to external providers.

These are separate security concerns.

An external provider credential must never be treated as a user's NIDDE authentication credential.

## 24. Security Boundary

AG-07 defines the broader security controls.

AG-08 must comply with:

- secret protection
- input and output validation
- least privilege
- secure communication
- webhook verification
- replay protection
- sensitive-data minimization
- audit requirements

## 25. Android Boundary

AG-09 owns Android architecture.

The Android client must not bypass the approved backend integration boundary for operations requiring server authority.

Client-side SDK usage is permitted only where explicitly authorized and where it cannot bypass protected backend controls.

## 26. Testing Boundary

AG-10 owns testing architecture.

External integrations must be testable through:

- mocks
- fakes
- contract tests
- integration tests
- failure simulations
- webhook tests

Real production credentials must never be required for ordinary automated tests.

## 27. Production Boundary

AG-12 owns production architecture.

AG-08 defines only the integration requirements that production must satisfy, including:

- credentials
- network access
- provider endpoints
- monitoring
- failure handling
- reconciliation

## 28. Verification Criteria

AG-08 may become VERIFIED only when:

- its scope matches the canonical AG-08 definition
- required external providers or provider categories are identified
- provider boundaries are explicit
- payment confirmation is protected
- webhook validation is defined
- idempotency is defined where required
- failure and retry behavior is defined
- KYC and storage boundaries are defined
- security requirements align with AG-07
- API requirements align with AG-05
- authorization requirements align with AG-06
- no unresolved blocking contradiction exists
- required verification evidence is recorded

READY FOR VERIFICATION does not mean VERIFIED.

## 29. Implementation Lock

AG-08 does not authorize implementation.

Implementation remains:

LOCKED

until the complete canonical architecture sequence and final readiness conditions are satisfied.

## 30. Control Statement

This document is intentionally limited to External Integrations.

It must not replace or redefine:

- Data Model
- API Contract
- Authentication / Authorization
- Security Model
- Android Architecture
- Testing Architecture
- CI/CD Architecture
- Production Architecture
- Release Architecture

Any future conflict must be resolved through the canonical architecture control process.
