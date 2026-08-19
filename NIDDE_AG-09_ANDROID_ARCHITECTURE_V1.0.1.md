# NIDDE — AG-09 ANDROID ARCHITECTURE

Project: NIDDE  
Phase: 00 — ARCHITECTURE  
Gate: AG-09 — Android Architecture  
Revision: V1.0.1  
Status: READY FOR VERIFICATION  
Implementation: LOCKED

## 1. Purpose

AG-09 defines the Android client architecture required by NIDDE before implementation.

This document is an architecture contract.

It defines the Android application boundary, module responsibilities, navigation, state management, networking, local storage, permissions, location, notifications, payment interaction, security boundaries, testing structure, and integration responsibilities.

It does not implement Android source code, backend APIs, database migrations, CI/CD workflows, deployment configuration, or production infrastructure.

---

## 2. Scope

AG-09 owns:

- Android application architecture
- Android module/package boundaries
- UI architecture
- navigation
- client-side state management
- API client boundary
- local persistence requirements
- client-side caching rules
- Android permissions
- location access
- tracking presentation
- notifications
- client-side payment interaction
- authentication-session handling on Android
- client-side error handling
- offline/degraded behavior
- Android security requirements
- Android testing structure
- build/package responsibilities

The following remain owned by their respective gates:

- AG-03 — System / Dependency Architecture
- AG-04 — Data Model
- AG-05 — API Contract
- AG-06 — Authentication / Authorization
- AG-07 — Security Model
- AG-08 — External Integrations
- AG-10 — Testing Architecture
- AG-11 — CI/CD Architecture
- AG-12 — Production Architecture
- AG-13 — Release Architecture

AG-09 must not redefine the scope of another gate.

---

## 3. Android Trust Boundary

The Android application is an untrusted client.

The Android client must never be treated as an authoritative source for:

- role
- permission
- ownership
- administrative authority
- KYC approval
- payment success
- protected lifecycle state
- financial settlement
- service completion

The backend/domain boundary remains authoritative.

Client-side validation may improve usability but must never replace server-side validation or authorization.

---

## 4. Architectural Principles

The Android architecture follows:

- server authority
- least privilege
- explicit module boundaries
- separation of UI and domain concerns
- single-direction state flow where practical
- secure handling of authentication state
- minimal local sensitive-data storage
- explicit network failure handling
- controlled permission usage
- lifecycle-aware operations
- testable components
- replaceable external integrations
- no direct database authority
- no provider-specific business logic in UI

Android implementation must preserve the contracts established by AG-03 through AG-08.

---

## 5. Application Responsibilities

The Android application is responsible for:

- presenting marketplace functionality
- collecting user input
- displaying server-authoritative state
- requesting valid backend operations
- displaying requests and offers
- displaying service lifecycle state
- presenting authorized location/tracking information
- presenting conversations and notifications
- initiating approved payment flows
- displaying payment results received from the backend
- handling authentication/session interaction
- presenting KYC workflows where applicable
- presenting reviews
- providing appropriate user feedback for errors and degraded connectivity

The Android application is not responsible for deciding authoritative business outcomes.

---

## 6. User and Profile Model

The Android application must support the approved NIDDE identity model:

- Client
- Artisan
- Company
- Admin where an approved Android administrative client is explicitly required

The Android client must distinguish:

- authenticated identity
- active profile/context
- permissions returned by the trusted backend
- current domain state

The client must never activate an unauthorized profile by submitting an arbitrary profile identifier.

If an identity is permitted to operate through multiple profiles, the active profile/context must be established through a server-authorized mechanism.

---

## 7. Package and Module Boundary

The Android architecture must maintain clear separation between:

- presentation/UI
- application/domain coordination
- data/network access
- local persistence
- authentication/session handling
- notifications
- location/tracking
- payment interaction
- shared models/contracts where approved

The exact package/module names are implementation details and must be frozen during the implementation/compatibility phase.

No UI component may directly perform unrestricted database access.

No UI component may directly own provider-specific payment, maps, KYC, or notification business logic.

Provider-specific implementations belong behind the integration boundaries defined by AG-08.

---

## 8. UI Architecture

The Android UI must be organized around clear screens/features and state.

UI components should:

- render state
- dispatch user actions
- display validation and server errors
- observe lifecycle-aware state
- avoid direct ownership of business rules
- avoid direct network implementation details
- avoid direct persistence logic

Business decisions must be performed by trusted application/domain/backend components.

The UI must not infer authoritative state from visual state alone.

---

## 9. State Management

Application state must distinguish between:

- loading
- available/success state
- empty state
- validation failure
- authorization failure
- authentication/session failure
- network failure
- server failure
- provider/integration failure
- retryable operation
- non-retryable operation

Server-authoritative state must be refreshed when required.

The Android client must not permanently assume that locally cached state remains authoritative.

For lifecycle-sensitive resources, the application must account for concurrent changes made by another actor or device.

---

## 10. Navigation

Navigation must respect authentication and authorization boundaries.

At minimum, the architecture must distinguish:

- unauthenticated flows
- authenticated client flows
- authenticated artisan flows
- authenticated company flows
- administrative flows where explicitly supported

Protected screens must not be considered secure merely because they are hidden from navigation.

Backend authorization remains mandatory.

Navigation state must not be used as proof of permission.

---

## 11. Authentication and Session Handling

Authentication behavior must follow AG-06.

The Android client may:

- initiate authentication
- submit approved credentials/factors
- maintain approved session state
- refresh or renew sessions through approved mechanisms
- respond to expiration/revocation
- initiate account recovery

The Android client must not:

- manufacture authentication claims
- modify roles locally
- bypass server authorization
- treat locally stored tokens as proof of current permission
- expose authentication material through logs or ordinary UI state

Authentication secrets and session material must use secure Android storage mechanisms appropriate to the selected implementation.

Exact token/session technology is governed by AG-06 and the compatibility/implementation phase.

---

## 12. API Client Boundary

All backend communication must pass through a controlled API/data boundary.

The Android client must follow the contracts defined by AG-05.

The client must correctly handle:

- API versioning
- request validation
- response validation
- authentication failures
- authorization failures
- pagination
- filtering/sorting rules
- idempotency requirements
- controlled error structures
- correlation/reference identifiers where applicable

The client must not construct arbitrary database queries or provider-specific requests.

The API remains the authoritative boundary.

---

## 13. Service Request and Offer Flow

The Android client may provide interfaces for:

Client:

Registration
→ Login
→ Search
→ Request
→ Receive Offers
→ Select

Artisan/Company:

Registration
→ KYC
→ Approval
→ Online
→ Receive Request
→ Offer
→ Accept

The client must submit commands/actions to the backend.

The backend determines whether:

- the request is valid
- the actor is authorized
- the provider is eligible
- the lifecycle permits the action
- the offer is valid
- duplicate active offers are prohibited
- the requested state transition is allowed

The Android client must not enforce these as its sole authority.

---

## 14. Service Lifecycle Presentation

The authoritative lifecycle is:

REQUESTED
→ ACCEPTED
→ EN_ROUTE
→ ARRIVED
→ IN_PROGRESS
→ COMPLETED

Cancellation and error states are explicitly supported.

The Android application may display lifecycle state and request an allowed transition.

It must never directly assign an arbitrary lifecycle state.

The UI must be prepared for a state transition to be rejected because the server state changed concurrently.

Lifecycle history must remain server-authoritative.

---

## 15. Location and Tracking

Location functionality must follow AG-04, AG-07, and AG-08.

The Android client may request location permissions only when required for an approved feature.

Location access must follow:

- minimum necessary permission
- purpose limitation
- explicit user-facing explanation where appropriate
- secure transport
- controlled retention
- restricted exposure

Tracking data displayed by the Android client must not be treated as authoritative proof of:

- payment
- service completion
- cash settlement

The application must handle denied, revoked, unavailable, or degraded location access.

Background location, if required, must be separately justified and explicitly approved by the architecture and platform requirements.

---

## 16. Maps and External Providers

The Android application must not bypass the approved integration boundary defined by AG-08 for protected backend operations.

Where Android SDKs are used for maps or presentation:

- provider-specific functionality must remain isolated
- provider credentials must not be exposed through unsafe client configuration
- provider output must not automatically become authoritative NIDDE business state
- sensitive location information must be minimized

The backend remains responsible for authoritative business decisions involving external provider data.

---

## 17. Messaging

The Android client may provide:

- conversation list
- conversation view
- message creation
- read state
- approved message/reference types
- moderation or restriction feedback where applicable

The backend remains responsible for:

- participant authorization
- conversation membership
- message permissions
- content/reference validation
- lifecycle restrictions
- moderation rules

A conversation identifier alone must never be treated as authorization.

The Android client must not expose conversations that the server has not authorized.

---

## 18. Notifications

The Android application may receive and display approved:

- push notifications
- notification state
- service updates
- offer updates
- payment-related notifications
- messaging notifications
- KYC notifications
- administrative notifications where authorized

Notification delivery is not authoritative for business state.

If a notification is delayed, duplicated, lost, or rejected, the application must retrieve authoritative state from the backend when required.

A notification must never independently change:

- service state
- payment state
- KYC approval
- financial settlement

---

## 19. Payment Interaction

The Android application may initiate approved payment operations.

The client must never declare an electronic payment successful as an authoritative business result.

The correct authority chain is:

Android Client
→ approved API/payment operation
→ NIDDE backend
→ AG-08 payment integration
→ validated provider result/webhook
→ server-side Payment state

The Android client may display payment status received from the backend.

The client must not accept a locally supplied:

`payment_status = successful`

as proof of payment.

Payment retries must respect the idempotency contract defined by AG-05 and AG-08.

---

## 20. Cash Transactions

Cash settlement is a separate domain concept.

The Android client may display or submit an approved cash-related action.

It must not independently mark a cash transaction as authoritative unless the backend contract explicitly authorizes the action and validates the actor and conditions.

Cash records remain server-authoritative and auditable.

---

## 21. KYC

The Android client may support approved KYC workflows.

Possible client functions include:

- initiating KYC submission
- collecting approved information
- selecting/capturing required documents
- submitting document references through approved mechanisms
- displaying KYC status
- displaying approved decision information

The Android client must not:

- approve KYC locally
- expose unrestricted KYC documents
- store sensitive documents unnecessarily
- treat an external provider result as automatic NIDDE authorization

KYC storage and provider boundaries remain governed by AG-08.

KYC security remains governed by AG-07.

---

## 22. Local Storage

Local persistence may be used for:

- non-sensitive application preferences
- controlled caches
- UI state where appropriate
- approved offline data
- secure session material where required by the authentication architecture

Sensitive data must not be stored locally unless explicitly required and protected.

The local database/cache must never become an independent authoritative source for:

- payment success
- KYC approval
- administrative privilege
- protected lifecycle state
- ownership
- role assignment

Cached state must have an explicit invalidation/refresh strategy.

---

## 23. Offline and Degraded Network Behavior

The Android client must distinguish between:

- offline state
- timeout
- temporary server failure
- authorization failure
- authentication expiration
- validation failure
- permanent business rejection

Read-only cached information may be shown where approved.

Operations that produce non-repeatable side effects must not be blindly replayed after reconnecting.

Retry behavior must respect API idempotency rules.

Financial and other non-repeatable operations must use the approved server-side idempotency mechanism.

---

## 24. Error Handling

Android error handling must map backend errors into safe user-facing states.

The application must not display:

- stack traces
- raw SQL errors
- secrets
- tokens
- private keys
- provider credentials
- sensitive internal infrastructure details
- unrestricted KYC information

Where a correlation/reference identifier is returned and safe to display, it may be shown to assist support or troubleshooting.

Internal diagnostic details belong in controlled logs, subject to AG-07.

---

## 25. Permissions

Android permissions must follow least privilege.

Permissions must be requested only when required for an approved feature.

Potential permission categories include:

- location
- notifications
- camera
- storage/media where required
- other platform permissions only when explicitly justified

The application must handle:

- permission granted
- permission denied
- permission revoked
- restricted access
- unavailable platform capability

Permission possession does not itself grant NIDDE authorization.

---

## 26. Android Security Requirements

The Android application must follow AG-07 security principles.

At minimum:

- do not hard-code production secrets
- do not log credentials/tokens
- do not trust local role flags
- do not trust local payment state
- do not trust local KYC state
- use secure transport
- minimize sensitive local storage
- protect authentication/session material
- validate server responses
- avoid exposing sensitive data through logs or screenshots where appropriate
- use platform security mechanisms where applicable
- fail safely when security assumptions are violated

Client security improves protection but never replaces backend security.

---

## 27. Configuration

Android configuration must separate:

- safe public application configuration
- environment-specific configuration
- sensitive credentials

Production secrets must not be committed to Git.

The Android application must not embed provider secret keys or backend administrative credentials.

Public client configuration must not be confused with secrets.

Environment configuration requirements must remain compatible with AG-07, AG-08, AG-11, and AG-12.

---

## 28. Backend Compatibility

The Android application must consume only approved API contracts.

Any breaking API change requires coordination with AG-05.

The Android client must not silently assume fields or states that are not part of the approved contract.

When API and Android expectations conflict:

- stop the affected implementation
- identify the contract conflict
- resolve the architecture/contract decision
- update the appropriate gate
- then continue implementation

No client-side workaround may silently redefine backend architecture.

---

## 29. External Integration Boundary

AG-08 owns external provider integrations.

The Android application must not directly bypass AG-08 for protected server-authoritative operations.

Where direct client SDK usage is permitted:

- it must be explicitly approved
- it must not expose protected credentials
- it must not bypass backend authorization
- its output must not independently become authoritative NIDDE state
- failures must be safely handled

Provider-specific logic must remain isolated from core domain logic.

---

## 30. Testing Boundary

AG-09 defines Android-specific testing requirements.

The Android architecture must support testing of:

- UI state
- navigation
- authentication/session behavior
- authorization-aware presentation
- API integration
- request/offer flows
- lifecycle presentation
- location behavior
- notification handling
- payment interaction
- KYC presentation
- local persistence
- offline behavior
- error handling
- security-sensitive client behavior

Detailed testing architecture is owned by AG-10.

Real production credentials must never be required for ordinary automated tests.

---

## 31. Critical Android Flows

The Android architecture must support the following critical paths.

### Client

Registration
→ Login
→ Search
→ Request
→ Receive Offers
→ Select
→ Service
→ Payment
→ Review

### Artisan

Registration
→ KYC
→ Approval
→ Online
→ Receive Request
→ Offer
→ Accept
→ Execute
→ Complete
→ Payout

### Company

Registration
→ KYC
→ Approval
→ Provider Operations
→ Receive Request
→ Offer
→ Accept
→ Execute
→ Complete
→ Payout

### Admin

Only if an approved Android administrative interface exists:

Login
→ Administrative Authentication
→ Authorized Management
→ Orders
→ KYC
→ Payments
→ Complaints/Moderation
→ Logs
→ Analytics

Administrative operations remain subject to AG-06 authorization and AG-07 security controls.

---

## 32. Lifecycle and Process Safety

Android lifecycle events such as:

- app backgrounding
- process death
- configuration changes
- connectivity changes
- permission changes
- token expiration

must not cause accidental duplicate authoritative operations.

Long-running operations must use Android lifecycle-aware mechanisms appropriate to the selected implementation.

Financial and non-repeatable operations require particular protection against duplicate submission.

---

## 33. Dependency Rules

Android components must depend on approved interfaces and boundaries.

The Android layer must not create unauthorized dependencies on:

- database internals
- backend private implementation details
- provider-specific domain state
- administrative backend internals
- production secrets

Direct dependencies must be documented during the physical-file/dependency inventory phase.

The final Android dependency graph will be frozen only after all architecture gates are complete.

---

## 34. Build and Package Architecture

The Android project must define:

- application identity
- build variants/environments
- package namespace
- dependency management
- resource organization
- test source sets
- release/debug separation
- secure configuration handling

Exact technology versions and package/build tooling are governed by AG-01 and subsequent compatibility/implementation gates.

AG-09 does not override AG-01 technology decisions.

---

## 35. Observability

Android diagnostic information must support troubleshooting without exposing sensitive information.

Where appropriate, diagnostics may include:

- application version
- environment
- non-sensitive error category
- request/correlation reference
- operation type
- timing information
- failure category

Diagnostics must not contain:

- passwords
- authentication tokens
- private keys
- payment secrets
- provider secrets
- complete KYC documents
- unnecessary sensitive personal information

Production observability requirements remain coordinated with AG-12.

---

## 36. Accessibility and User Safety

The Android UI architecture should support:

- accessible controls
- readable content
- clear validation errors
- understandable permission explanations
- safe confirmation for consequential actions
- clear payment status
- clear service-state presentation
- prevention of accidental duplicate actions

Accessibility and UX implementation details must not weaken security or authorization boundaries.

---

## 37. Cross-Gate Consistency

AG-09 must remain consistent with:

AG-03:
- system boundaries
- service responsibilities
- dependency ownership

AG-04:
- entities
- ownership
- lifecycle
- location
- payments
- KYC
- notifications

AG-05:
- API contracts
- errors
- pagination
- idempotency
- versioning
- webhook-related client behavior

AG-06:
- identity
- roles
- permissions
- ownership
- authentication/session requirements

AG-07:
- security
- secrets
- sensitive data
- rate/abuse controls
- logging
- secure failure behavior

AG-08:
- provider boundaries
- payments
- maps
- notifications
- KYC
- storage
- external-provider failure handling

AG-09 must not introduce a contradiction with any approved earlier gate.

---

## 38. Verification Criteria

AG-09 may become VERIFIED only when:

- its scope matches the canonical AG-09 definition
- Android responsibilities are clearly separated from backend authority
- identity and profile handling aligns with AG-06
- API usage aligns with AG-05
- domain ownership aligns with AG-04
- lifecycle behavior aligns with AG-04
- security requirements align with AG-07
- external integrations align with AG-08
- payment handling preserves server authority
- KYC handling preserves server authority
- location/tracking handling preserves privacy requirements
- notification behavior does not become business-state authority
- local storage does not become authoritative domain storage
- offline/retry behavior preserves idempotency requirements
- Android testing requirements are mapped to AG-10
- CI/CD/build requirements remain compatible with AG-11
- production requirements remain compatible with AG-12
- release requirements remain compatible with AG-13
- no unresolved blocking contradiction exists
- required verification evidence is recorded

READY FOR VERIFICATION does not mean VERIFIED.

---

## 39. Implementation Lock

AG-09 does not authorize implementation.

Implementation remains:

LOCKED

until the complete canonical architecture sequence and final readiness conditions are satisfied.

No Android source files should be created solely because AG-09 has been written.

---

## 40. Control Statement

AG-09 establishes the Android client architecture boundary for NIDDE.

The Android client is a presentation and interaction layer operating through approved backend contracts.

The backend/domain layer remains authoritative for identity authorization, ownership, lifecycle, payments, KYC, financial state, and other protected business decisions.

Android implementation must follow AG-03 through AG-08 and must remain compatible with AG-10 through AG-13.

No client-side behavior may silently redefine an approved architecture contract.

**AG-09 STATUS: READY FOR VERIFICATION**

**IMPLEMENTATION: LOCKED**
