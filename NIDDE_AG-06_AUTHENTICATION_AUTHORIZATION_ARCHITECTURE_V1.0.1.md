# NIDDE — AG-06 AUTHENTICATION & AUTHORIZATION ARCHITECTURE

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-06 — Authentication / Authorization
Revision: V1.0.1
Status: READY FOR VERIFICATION
Implementation: LOCKED

## 1. Purpose

AG-06 defines the authentication and authorization architecture required by NIDDE before implementation.

This document is an architecture contract.

It does not implement authentication code, token handling code, database migrations, Android code, or external provider integrations.

## 2. Scope

AG-06 owns:

- identity authentication
- authentication flows
- sessions and tokens
- roles and permissions
- authorization
- resource ownership enforcement
- account recovery
- identity verification requirements
- privilege boundaries
- administrative authorization

The following remain owned by their respective gates:

- AG-04 — Data Model
- AG-05 — API Contract
- AG-07 — Security Model
- AG-08 — External Integrations
- AG-09 — Android Architecture
- AG-10 — Testing Architecture
- AG-11 — CI/CD Architecture
- AG-12 — Production Architecture
- AG-13 — Release Architecture

AG-06 must not redefine another gate's scope.

## 3. Identity Model

NIDDE uses a common User identity with role-specific profiles.

The principal profile types are:

- Client Profile
- Artisan Profile
- Company Profile

Administrative authority is associated with an authorized administrative identity.

Authentication establishes that an identity controls the approved authentication factor.

Authorization determines what that authenticated identity is allowed to access or perform.

## 4. Authentication Principles

Authentication must:

- establish a unique identity
- protect authentication credentials
- prevent unauthorized account access
- support secure session/token handling
- support controlled account recovery
- provide appropriate verification mechanisms
- prevent authentication material from being exposed to clients or logs

Authentication material must never be stored in plaintext.

Detailed security controls belong to AG-07.

## 5. Client-Provided Claims

Client-provided values are never authoritative for:

- role
- permissions
- ownership
- administrative status
- KYC approval
- payment success
- protected lifecycle state

The server derives effective authorization from trusted server-side identity and domain state.

## 6. Roles

The application roles are:

### Client

May perform client-authorized marketplace operations.

### Artisan

May perform artisan-authorized provider operations.

### Company

May perform company-authorized provider operations.

### Admin

May perform explicitly authorized administrative and moderation operations.

Role assignment and administrative privilege are server-controlled.

## 7. Authorization Model

Authorization evaluates the complete security context.

Where applicable it considers:

- authenticated user
- effective role
- explicit permission
- resource ownership
- participant relationship
- lifecycle state
- domain eligibility
- administrative authority
- KYC/verification state where required

A valid authentication session does not automatically grant permission to every resource.

## 8. Resource Ownership

Authorization must respect the authoritative ownership model defined by AG-04.

Examples:

- a client may access only requests and resources they are authorized to access
- an artisan/company may access only provider resources they are authorized to access
- a conversation is accessible only to authorized participants
- administrative resources require explicit administrative authority

Ownership must be checked server-side.

## 9. Service Lifecycle Authorization

The authoritative lifecycle is:

REQUESTED → ACCEPTED → EN_ROUTE → ARRIVED → IN_PROGRESS → COMPLETED

Cancellation and error states are explicit.

A user may request an operation only when:

- the identity is authenticated
- the actor is authorized
- the resource is accessible
- the current state permits the transition
- all domain conditions are satisfied

The client cannot directly assign arbitrary lifecycle state.

## 10. Request and Offer Authorization

For Service Requests:

- only authorized clients may create or modify their requests
- protected fields require server validation
- lifecycle restrictions apply
- unauthorized users cannot access private request information

For Offers:

- the provider must be eligible
- the provider must be authorized to act for the applicable profile
- the request must exist
- the request must accept the operation according to its lifecycle
- duplicate prohibited active offers must be prevented

## 11. Payment Authorization

Authentication and authorization do not make a client-side payment result authoritative.

The application must not accept:

`payment_status = successful`

merely because a client submits that value.

Electronic payment confirmation is accepted through the controlled integration boundary defined by AG-08.

Financial permissions must be enforced server-side.

## 12. KYC Authorization

KYC operations are separated by authority.

Possible operations include:

- submit verification
- upload/reference documents
- review
- approve
- reject
- access verification information

KYC approval requires explicit authorized server-side action.

A normal client cannot approve its own KYC case.

Sensitive KYC document access is restricted.

## 13. Administrative Authorization

Admin operations require explicit administrative authorization.

Administrative privileges must not be inferred from:

- client input
- profile text
- UI state
- local application storage
- unsigned metadata

Every administrative action must be attributable to an authenticated authorized actor.

## 14. Conversation Authorization

Conversation access is restricted to permitted participants.

Before reading or modifying a conversation/message, the server must verify the actor's relationship to that conversation.

A conversation identifier alone is never sufficient authorization.

## 15. Location and Tracking Authorization

Location and tracking information is sensitive.

Access must be restricted according to:

- service/request relationship
- actor role
- lifecycle state
- business need
- privacy requirements

Historical tracking information must not become universally accessible merely because the user was once involved in a service.

## 16. Account Recovery

Account recovery must use an approved recovery mechanism.

Recovery operations should:

- verify the required identity factor
- use expiring recovery credentials
- invalidate used recovery credentials
- prevent credential reuse
- minimize account-enumeration leakage
- record security-relevant events where required

Recovery must not silently grant administrative privileges.

## 17. Session and Token Principles

The selected implementation mechanism must provide:

- secure issuance
- controlled lifetime
- expiration
- revocation where required
- protection against replay where applicable
- secure storage on supported clients
- server-side validation

Tokens must not be accepted solely because they are syntactically valid.

The server must validate their authenticity and authorization context.

## 18. Permission Changes

Changes to permissions or administrative authority require server-side authorization.

A change in role or verification state must take effect according to the approved domain lifecycle.

Existing sessions must not automatically retain privileges that have been revoked when the security design requires immediate or bounded revocation.

## 19. Multi-Profile Considerations

Where an identity can operate through more than one approved profile, the server must distinguish:

- authenticated identity
- active profile/context
- profile ownership
- permissions for that context

The client cannot activate an unauthorized profile by submitting an arbitrary profile identifier.

## 20. API Boundary

AG-05 defines the API contract.

AG-06 defines the authentication and authorization rules enforced through that API.

Every protected API operation must map to an authorization decision.

A public API endpoint does not imply public access to the underlying resource.

## 21. Security Boundary

AG-07 defines the broader security controls.

AG-06 must therefore provide the authorization requirements that AG-07 protects, including:

- least privilege
- secure credential handling
- abuse controls
- auditability
- sensitive-data protection

AG-06 must not duplicate or contradict AG-07.

## 22. External Identity Providers

Where external identity or KYC providers are used, their integration boundary belongs to AG-08.

External provider responses must be validated before being mapped to internal identity or verification state.

External provider identity does not automatically grant an internal NIDDE role.

## 23. Audit Requirements

The following actions must be traceable where applicable:

- authentication events
- recovery events
- permission changes
- administrative access
- administrative actions
- KYC authorization decisions
- security-sensitive authorization changes

Audit implementation details remain coordinated with AG-04 and AG-07.

## 24. Authorization Failure

When authorization fails, the API must return a controlled response.

The system must not disclose unnecessary information about:

- existence of protected resources
- internal permissions
- security controls
- credentials
- administrative configuration

Error-contract details are governed by AG-05 and security requirements by AG-07.

## 25. Verification Criteria

AG-06 may become VERIFIED only when:

- its scope matches the canonical AG-06 definition
- identity responsibilities are clear
- role boundaries are explicit
- ownership rules align with AG-04
- API requirements align with AG-05
- security requirements align with AG-07
- external identity/KYC boundaries align with AG-08
- lifecycle authorization is consistent
- no unresolved blocking contradiction exists
- required verification evidence is recorded

`READY FOR VERIFICATION` does not mean `VERIFIED`.

## 26. Implementation Lock

AG-06 does not authorize implementation.

Implementation remains:

`LOCKED`

until the complete canonical architecture sequence and final readiness conditions are satisfied.

## 27. Control Statement

This document is intentionally limited to Authentication and Authorization.

It must not be used to redefine:

- data model
- API contract
- security model
- external integrations
- Android architecture
- testing architecture
- CI/CD architecture
- production architecture
- release architecture

Any conflict must be resolved through the canonical architecture control process.
