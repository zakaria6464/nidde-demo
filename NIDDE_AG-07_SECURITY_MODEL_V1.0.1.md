# NIDDE — AG-07 SECURITY MODEL

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-07 — Security Model
Revision: V1.0.1
Status: READY FOR VERIFICATION
Implementation: LOCKED

## 1. Purpose

AG-07 defines the security architecture required to protect NIDDE identities, data, APIs, financial operations, KYC information, communications, administration, and external integrations.

This document is an architecture contract.

It does not implement application code, infrastructure, database migrations, or security tooling.

## 2. Scope

AG-07 owns:

- application security principles
- data protection
- secret management requirements
- input validation requirements
- abuse prevention
- rate limiting requirements
- security logging
- audit security requirements
- sensitive-data protection
- secure integration boundaries
- security testing requirements
- security incident controls

The following remain owned by their respective gates:

- AG-04 — Data Model
- AG-05 — API Contract
- AG-06 — Authentication / Authorization
- AG-08 — External Integrations
- AG-09 — Android Architecture
- AG-10 — Testing Architecture
- AG-11 — CI/CD Architecture
- AG-12 — Production Architecture
- AG-13 — Release Architecture

AG-07 must not redefine another gate's scope.

## 3. Security Principles

NIDDE follows these core principles:

- least privilege
- defense in depth
- server-side authorization
- deny by default for protected resources
- explicit trust boundaries
- sensitive-data minimization
- secure secret handling
- input validation
- controlled error disclosure
- auditable critical operations
- external input treated as untrusted
- secure failure behavior

Security must be enforced by the backend/domain boundary and must not depend solely on client behavior.

## 4. Trust Boundaries

The principal trust boundaries are:

1. Client device → NIDDE API
2. NIDDE API → database
3. NIDDE backend → external providers
4. NIDDE backend → secure document/storage services
5. Administrative interface → administrative APIs
6. Webhook provider → integration boundary

Data crossing a trust boundary must be authenticated, validated, authorized, and handled according to its sensitivity.

## 5. Authentication Boundary

AG-06 owns authentication and authorization.

AG-07 defines the security requirements protecting those mechanisms.

Authentication material must:

- never be stored in plaintext
- never be logged
- never be exposed through ordinary API responses
- be protected in transit
- use approved credential/session mechanisms

Compromise of a client device must not automatically grant unrestricted backend authority.

## 6. Authorization Security

Authorization is enforced server-side.

The system must not trust client-controlled values for:

- roles
- permissions
- ownership
- administrative authority
- KYC approval
- payment success
- protected lifecycle state

AG-06 defines authorization decisions.

AG-07 defines the security controls that protect those decisions.

## 7. Input Validation

All external input is untrusted.

Validation must occur at the appropriate API/domain boundary.

Controls include:

- schema validation
- type validation
- length limits
- range limits
- allowlisted values
- identifier validation
- content validation where required
- state validation
- ownership validation
- authorization validation

Validation failures must not produce partial authoritative mutations.

## 8. Injection Protection

All database, command, query, template, and external-provider interactions must use safe parameterized or structured mechanisms.

User-controlled strings must never be treated as executable instructions.

Dynamic query expressions, shell commands, or provider requests must be explicitly controlled.

## 9. Sensitive Data

Sensitive information must be minimized.

Sensitive categories include, where applicable:

- authentication material
- personal identity information
- KYC information
- KYC documents
- payment-related information
- private messages
- precise location/tracking data
- administrative/security information
- integration credentials

Only the minimum information required for an operation should be exposed.

## 10. KYC Security

KYC document contents must not be stored casually in ordinary application tables or Git.

Approved secure storage/integration boundaries must be used.

KYC access must be:

- authenticated
- authorized
- minimized
- auditable

KYC approval is a server-side decision.

External verification providers are integration dependencies governed by AG-08.

## 11. Payment Security

Payment and Cash Transaction remain separate domain concepts.

The system must never accept electronic payment success solely from client state.

Payment provider callbacks/webhooks must be validated through AG-08.

Security controls must protect against:

- forged callbacks
- replay
- duplicate processing
- unauthorized access
- sensitive data leakage
- inconsistent financial state

Financial events must remain traceable.

## 12. Idempotency and Replay Protection

Operations capable of producing financial, lifecycle, or other non-repeatable side effects must support idempotency where retry or duplication is possible.

Replay protection must be applied to security-sensitive callbacks and commands where required.

Repeated delivery of the same valid event must not create duplicate authoritative effects.

## 13. Rate Limiting and Abuse Protection

Rate limiting and abuse controls are required for security-sensitive operations.

At minimum, the architecture must consider:

- authentication attempts
- account recovery
- request creation
- offer creation
- messaging
- payment operations
- KYC operations
- administrative operations
- webhook processing
- resource discovery

Controls may include:

- rate limits
- throttling
- progressive delays
- temporary lockouts
- anomaly detection
- abuse monitoring

Exact operational thresholds may be defined during implementation without changing this security boundary.

## 14. API Security

AG-05 defines the API contract.

AG-07 defines security requirements applied to that contract.

Protected APIs must enforce:

- authentication
- authorization
- validation
- safe errors
- bounded requests
- rate controls
- sensitive-data minimization

An identifier supplied by a client must never be treated as proof of ownership.

## 15. Error Handling

Security-sensitive failures must not disclose unnecessary internal information.

Responses must not expose:

- stack traces
- raw SQL errors
- credentials
- secrets
- internal tokens
- private keys
- infrastructure details
- sensitive KYC contents

The API should provide controlled error codes and safe messages.

Detailed error structure is owned by AG-05.

## 16. Logging

Security-relevant events must be observable without exposing sensitive data.

Logs must not contain:

- passwords
- private keys
- access tokens
- payment secrets
- webhook secrets
- complete sensitive KYC documents
- unnecessary personal data

Security logs should support investigation while respecting data minimization.

## 17. Audit Security

Critical events must remain traceable.

Examples include:

- authentication security events
- permission changes
- administrative actions
- lifecycle transitions
- financial events
- KYC decisions
- security configuration changes
- integration security events

Audit records are append-oriented and must not be casually rewritten.

## 18. Messaging Security

Messaging must enforce participant authorization.

Security controls must consider:

- unauthorized conversation access
- message enumeration
- malicious content
- oversized payloads
- abusive automation
- sensitive information leakage

The notification system must not expose message content beyond approved recipients.

## 19. Location Security

Location and tracking information is sensitive.

The system must enforce:

- authorized access
- purpose limitation
- minimum necessary precision
- appropriate retention
- controlled exposure
- secure transport

Tracking information is not independently authoritative proof of payment or service completion.

## 20. External Integration Security

AG-08 owns external integration architecture.

AG-07 requires:

- authenticated provider communication
- secure credentials
- webhook authenticity validation
- replay protection
- timeout controls
- safe retries
- controlled failure behavior
- least-privilege provider access
- provider data minimization

External systems must be treated as untrusted dependencies.

## 21. Secret Management

Real secrets must never be committed to Git.

Prohibited examples include:

- production passwords
- API keys
- private keys
- payment credentials
- webhook secrets
- database credentials
- cloud credentials
- KYC provider secrets

`.env.example` may contain variable names and safe placeholders only.

Actual secret storage belongs to approved environment and production controls.

## 22. Client Security

The Android client must not be treated as a trusted authority.

Client-side controls may improve user experience but cannot replace backend authorization.

The client must not be authoritative for:

- role
- ownership
- payment success
- KYC approval
- protected lifecycle state
- administrative privilege

Android-specific security architecture is coordinated with AG-09.

## 23. Database Security

The database must be protected through:

- controlled access
- least privilege
- parameterized queries
- migration discipline
- backup protection
- sensitive-data controls
- audit requirements where appropriate

No cross-domain direct database writes are permitted outside approved repository/data-access boundaries.

The database remains a protected backend resource.

## 24. Production Security

Production security requirements include:

- secure configuration
- secret management
- access control
- protected logs
- monitoring
- backup protection
- recovery controls
- dependency monitoring
- controlled administrative access

Detailed production architecture belongs to AG-12.

## 25. Security Testing

Security testing must cover, as applicable:

- authentication
- authorization
- ownership enforcement
- injection protection
- input validation
- rate limiting
- payment webhook validation
- replay protection
- KYC access
- administrative authorization
- sensitive-data exposure
- secret leakage
- API abuse

Testing architecture is owned by AG-10.

## 26. Security Incident Principles

Security incidents must be handled through a controlled process.

The architecture must support:

- detection
- containment
- investigation
- credential/secret rotation
- affected-session invalidation where required
- recovery
- audit evidence
- post-incident correction

Operational incident procedures may be expanded during production architecture and implementation.

## 27. Cross-Gate Consistency

AG-07 must remain consistent with:

- AG-04 data ownership and lifecycle
- AG-05 API contracts
- AG-06 authentication/authorization
- AG-08 external integrations
- AG-09 Android security boundaries
- AG-10 security testing
- AG-11 CI/CD security checks
- AG-12 production security
- AG-13 release security criteria

A contradiction with a verified gate must be resolved before AG-07 verification.

## 28. Verification Criteria

AG-07 may become VERIFIED only when:

- its scope matches the canonical AG-07 definition
- security trust boundaries are explicit
- sensitive-data rules are defined
- authentication and authorization responsibilities align with AG-06
- API requirements align with AG-05
- payment and KYC security align with AG-08
- testing requirements align with AG-10
- no unresolved blocking contradiction exists
- required verification evidence is recorded

`READY FOR VERIFICATION` does not mean `VERIFIED`.

## 29. Implementation Lock

AG-07 does not authorize implementation.

Implementation remains:

`LOCKED`

until the complete canonical architecture sequence and final readiness conditions are satisfied.

## 30. Control Statement

This document is intentionally limited to the Security Model gate.

It must not replace or redefine:

- Data Model
- API Contract
- Authentication / Authorization
- External Integrations
- Android Architecture
- Testing Architecture
- CI/CD Architecture
- Production Architecture
- Release Architecture

Any future conflict must be resolved through the canonical architecture control process.
