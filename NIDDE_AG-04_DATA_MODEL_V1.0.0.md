# NIDDE — AG-04 DATA MODEL

Project: NIDDE  
Phase: 00 — ARCHITECTURE  
Gate: AG-04 — Data Model  
Revision: V1.0.1  
Status: READY FOR VERIFICATION  
Implementation: LOCKED

## 1. Purpose

AG-04 defines the authoritative domain data model required by NIDDE before implementation.

This document is an architecture contract.

It defines domain entities, ownership, relationships, lifecycle semantics, data responsibilities, financial boundaries, KYC boundaries, location/tracking boundaries, audit requirements, and data integrity rules.

It does not implement database schemas, migrations, repositories, API endpoints, Android code, external provider SDKs, deployment configuration, or production infrastructure.

---

## 2. Scope

AG-04 owns:

- authoritative domain entities
- entity ownership
- relationships between entities
- domain lifecycle semantics
- domain identifiers
- authoritative state
- financial domain separation
- KYC domain separation
- location/tracking data ownership
- messaging data ownership
- notification data ownership
- review data ownership
- audit-relevant domain records
- data integrity constraints
- domain-level uniqueness requirements
- domain-level deletion/retention principles

The following remain owned by their respective gates:

- AG-01 — Technology Stack
- AG-02 — Repository Structure
- AG-03 — System / Dependency Architecture
- AG-05 — API Contract
- AG-06 — Authentication / Authorization
- AG-07 — Security Model
- AG-08 — External Integrations
- AG-09 — Android Architecture
- AG-10 — Testing Architecture
- AG-11 — CI/CD Architecture
- AG-12 — Production Architecture
- AG-13 — Release Architecture

AG-04 must not redefine the scope of another gate.

---

## 3. Source of Truth

The authoritative data model must remain consistent with:

- NIDDE Project Control
- Canonical Master File Manifest
- verified AG-02 repository structure
- AG-03 system/dependency architecture
- AG-05 API contract
- AG-06 authentication/authorization architecture
- AG-07 security model
- AG-08 external integrations
- AG-09 Android architecture
- AG-10 through AG-13 requirements where applicable

A later gate may refine implementation details but must not silently redefine an authoritative AG-04 entity, ownership rule, or lifecycle.

If a conflict is discovered, the affected architecture decision must be resolved before implementation continues.

---

## 4. Domain Identity Model

NIDDE uses one authoritative User identity.

A User may operate through approved role-specific profiles:

- Client Profile
- Artisan Profile
- Company Profile

Administrative authority is not represented merely by client-controlled profile data.

Administrative authority is governed by AG-06.

The data model must distinguish:

- User identity
- profile identity
- role/context
- ownership
- permissions
- administrative authority

A client-provided role or profile identifier is never authoritative.

---

## 5. Core Domain Entities

The authoritative NIDDE domain includes, where applicable:

- User
- Client Profile
- Artisan Profile
- Company Profile
- Service Category
- Service
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
- KYC Document Reference
- Notification
- Administrative / Moderation Record
- Audit Record

External-provider records and identifiers remain integration references and do not replace NIDDE authoritative entities.

---

## 6. User

User is the authoritative identity record.

A User represents the authenticated identity within NIDDE.

User data may include, where approved:

- internal user identifier
- authentication-related references
- account status
- timestamps
- approved identity metadata
- profile relationships

Authentication credentials and secrets are governed by AG-06 and AG-07.

Authentication secrets must not be stored as ordinary plaintext domain data.

---

## 7. Client Profile

A Client Profile represents the marketplace client context associated with a User.

It may contain:

- profile identifier
- owning User identifier
- approved profile information
- client-specific preferences
- profile status
- timestamps

A Client Profile may own or authorize access to Service Requests according to AG-06.

The profile itself does not establish administrative authority.

---

## 8. Artisan Profile

An Artisan Profile represents an individual service provider.

It may contain:

- profile identifier
- owning User identifier
- professional information
- service eligibility information
- availability information
- KYC relationship
- profile status
- timestamps

Artisan eligibility and authorization are governed by AG-06.

KYC state is authoritative only through the approved KYC domain.

---

## 9. Company Profile

A Company Profile represents an organizational service provider.

It may contain:

- profile identifier
- owning User or approved organization relationship
- company information
- service eligibility information
- availability information
- KYC relationship
- profile status
- timestamps

Company authorization must be enforced server-side.

A Company Profile must not silently grant administrative authority.

---

## 10. Service Category

A Service Category organizes marketplace services.

A category may contain:

- category identifier
- name
- description
- status
- ordering metadata
- timestamps

Category identifiers are server-authoritative.

Category deletion or deactivation must preserve historical references where required.

---

## 11. Service

A Service represents an approved marketplace service definition.

A Service may contain:

- service identifier
- category relationship
- name
- description
- status
- approved service metadata
- timestamps

A Service is not the same as a Service Request.

A Service defines an available offering/type of work.

A Service Request represents a client's actual requested work.

---

## 12. Service Request

A Service Request represents a client's request for service.

A Service Request must identify:

- request identifier
- authorized client/profile
- applicable service/category
- request details
- requested location/reference
- lifecycle state
- timestamps
- cancellation information where applicable
- completion information where applicable

The owning client remains the authoritative owner of the request unless the approved domain model explicitly assigns another relationship.

The server determines whether an actor may create, modify, view, cancel, or otherwise operate on the request.

---

## 13. Service Request Lifecycle

The authoritative service lifecycle is:

REQUESTED
→ ACCEPTED
→ EN_ROUTE
→ ARRIVED
→ IN_PROGRESS
→ COMPLETED

Cancellation and error states are explicit domain states.

The exact implementation representation may use controlled state values, but the semantic lifecycle must remain equivalent.

Clients may request transitions.

The server determines whether a transition is permitted.

The client must never assign arbitrary lifecycle state.

Every accepted lifecycle transition must be traceable according to the audit requirements.

---

## 14. Lifecycle Transition Rules

A transition is valid only when:

- the actor is authenticated
- the actor is authorized
- the actor has access to the request
- the current state permits the requested transition
- required domain conditions are satisfied

The data model must preserve sufficient information to determine the current authoritative state.

Concurrent updates must not silently overwrite an already accepted authoritative transition.

Rejected transitions must not partially mutate authoritative state.

---

## 15. Offer

An Offer represents a provider's response to a Service Request.

An Offer must reference:

- offer identifier
- Service Request
- eligible Artisan or Company provider
- amount where applicable
- currency where applicable
- offer status
- timestamps

An Offer cannot exist without its applicable Service Request.

A provider must be eligible and authorized to submit the Offer.

The model must prevent prohibited duplicate active offers according to the approved business rules.

---

## 16. Accepted Offer

When an Offer is accepted, the accepted Offer must be uniquely identifiable.

The Service Request must not contain multiple simultaneously authoritative accepted offers unless a future approved architecture explicitly defines such behavior.

Acceptance must preserve the relationship between:

- Service Request
- accepted Offer
- provider
- resulting service lifecycle

The API and authorization gates must enforce the corresponding business rules.

---

## 17. Location

Location represents location information associated with an approved domain purpose.

Location may be associated with:

- Service Request
- service execution
- approved tracking activity
- other explicitly authorized domain relationships

Location data is sensitive.

The model must distinguish operational location information from authoritative business outcomes.

Location alone cannot establish:

- payment success
- financial settlement
- service completion

Privacy and access controls are governed by AG-07.

External mapping/provider relationships are governed by AG-08.

---

## 18. Tracking Event

A Tracking Event represents time-based operational location/tracking information.

A Tracking Event should identify, where applicable:

- tracking event identifier
- related service/request
- authorized actor/provider
- timestamp
- location reference/data
- event type
- creation metadata

Tracking events are operational records.

They are not independent proof of:

- payment completion
- service completion
- cash settlement

Retention and exposure must follow approved security and privacy requirements.

---

## 19. Conversation

A Conversation represents an authorized communication context.

A Conversation must have a stable internal identifier and controlled participant relationships.

Participant authorization is governed by AG-06.

A conversation identifier alone is never proof of access.

The model must preserve sufficient information to determine authorized participation.

---

## 20. Message

A Message belongs to an authorized Conversation.

A Message may contain:

- message identifier
- conversation relationship
- sender relationship
- approved message content
- approved message/reference type
- creation timestamp
- moderation/status metadata where applicable

Message creation must verify:

- authenticated sender
- conversation membership
- allowed message type
- content/reference validity
- applicable lifecycle/moderation restrictions

Security requirements are governed by AG-07.

---

## 21. Payment

Payment represents an electronic or otherwise approved payment domain record.

Payment is authoritative inside NIDDE.

A Payment may contain:

- internal Payment identifier
- related Service Request/service
- payer reference
- amount
- currency
- status
- external provider reference where applicable
- timestamps
- reconciliation metadata where applicable

External provider identifiers must never replace the internal Payment identifier.

The client cannot directly make Payment successful.

Electronic payment confirmation must originate from the approved integration boundary defined by AG-08.

---

## 22. Payment Status

Applicable payment states may include:

- PENDING
- SUCCESSFUL
- FAILED
- CANCELLED
- REJECTED

The exact implementation representation may vary, but the semantic distinction must remain intact.

A client-submitted payment result is not authoritative.

Provider confirmation must pass through the controlled integration boundary.

Payment operations must support idempotency where required.

---

## 23. Cash Transaction

Cash Transaction is a separate domain concept from Payment.

A Cash Transaction represents an approved cash settlement record.

It may contain:

- cash transaction identifier
- related Service Request/service
- payer/payee references
- amount
- currency
- status
- settlement information
- timestamps
- audit references

Cash settlement must not be represented as an electronic Payment merely because both involve money.

The server remains authoritative for cash settlement state.

---

## 24. Payment and Cash Separation

The following distinction is mandatory:

Payment
= electronic/approved payment domain state

Cash Transaction
= cash settlement domain state

Neither domain may silently become the other.

An electronic provider event must not automatically create a cash settlement.

A cash action must not automatically become electronic payment success.

---

## 25. Review

A Review represents an authorized review of a completed service.

A Review must identify, where applicable:

- review identifier
- completed Service Request/service
- author
- reviewed subject
- rating
- content
- moderation status
- timestamps

Review creation requires server-side eligibility validation.

At minimum, the server must verify:

- completed-service eligibility
- rating range
- author identity
- subject identity
- duplicate-review rules

Moderation actions must remain auditable.

---

## 26. KYC Case

A KYC Case represents the verification lifecycle associated with an identity/profile.

A KYC Case may contain:

- KYC case identifier
- subject User/profile
- verification status
- submission metadata
- review metadata
- decision metadata
- timestamps
- external provider references where applicable

Possible semantic states include:

- NOT_SUBMITTED
- SUBMITTED
- UNDER_REVIEW
- APPROVED
- REJECTED

The exact state representation may be refined without changing the semantic lifecycle.

KYC approval is a server-side authorized decision.

---

## 27. KYC Document Reference

Sensitive KYC documents must be represented through controlled document references rather than unrestricted raw document content in ordinary domain records.

A KYC Document Reference may contain:

- document reference identifier
- related KYC Case
- document type
- secure-storage reference
- status
- timestamps

Raw sensitive document content must not be exposed through unrestricted API responses.

Secure storage and provider boundaries belong to AG-08.

Security requirements belong to AG-07.

---

## 28. Notification

A Notification represents a notification record associated with an authorized recipient.

It may contain:

- notification identifier
- recipient relationship
- notification type
- safe payload/reference
- read/delivery state
- timestamps

Notification delivery is not authoritative for business state.

A failed notification must not automatically change:

- Service Request state
- Payment state
- KYC state
- Cash Transaction state

The underlying domain record remains authoritative.

---

## 29. Administrative and Moderation Records

Administrative and moderation records represent controlled administrative actions or decisions.

They must identify, where applicable:

- record identifier
- authorized administrative actor
- affected resource
- action/decision
- reason/reference
- timestamp
- resulting state/reference

Administrative authority is governed by AG-06.

Security and audit requirements are governed by AG-07.

Administrative operations must be attributable to an authorized actor.

---

## 30. Audit Record

Audit records preserve traceability for important domain and security-sensitive actions.

Applicable events include:

- lifecycle transitions
- financial events
- KYC decisions
- administrative actions
- permission/authority changes
- security-sensitive operations
- important integration events

Audit records should be append-oriented.

They must not be casually rewritten to erase historical authoritative events.

Audit implementation details are coordinated with AG-07 and the testing/production gates.

---

## 31. Ownership Rules

Authoritative ownership must remain explicit.

At minimum:

- User owns its identity
- Client Profile belongs to its User
- Artisan Profile belongs to its User/approved provider identity
- Company Profile belongs to its approved organizational identity
- Service Request belongs to its authorized client
- Offer belongs to its provider and references one Service Request
- Conversation has controlled participants
- Message belongs to one Conversation and one sender
- Payment references its applicable service/request and payer
- Cash Transaction references its applicable service/request and settlement parties
- Review references its completed service and authorized author/subject
- KYC Case belongs to its subject identity/profile
- KYC Document Reference belongs to a KYC Case
- Notification belongs to its recipient
- Administrative records belong to authorized administrative actions

Ownership does not automatically grant every permission.

Authorization remains governed by AG-06.

---

## 32. Referential Integrity

Authoritative relationships must be internally consistent.

The implementation must prevent:

- orphaned Offers
- orphaned Messages
- orphaned Reviews
- orphaned KYC Document References
- orphaned Notifications
- invalid Payment references
- invalid Cash Transaction references
- invalid lifecycle relationships

Deletion or archival must preserve required historical relationships.

Hard deletion must not silently destroy required financial, KYC, audit, or service-history evidence.

---

## 33. Uniqueness and Duplicate Prevention

Where applicable, the data model must enforce uniqueness or controlled duplicate prevention for:

- authoritative identity identifiers
- profile ownership relationships
- active prohibited duplicate Offers
- accepted Offer relationship
- applicable Review uniqueness
- idempotency references
- external integration event identifiers
- webhook/event processing references

The exact database mechanism is implementation-owned.

The domain invariant itself is owned by AG-04.

---

## 34. Idempotency Data

Operations capable of producing non-repeatable effects may require an idempotency record/reference.

Applicable areas include:

- payments
- financial settlement
- webhook processing
- retryable commands
- other non-repeatable side effects

Repeated processing of the same approved idempotency reference must not create duplicate authoritative effects.

API-level requirements are defined by AG-05.

External integration requirements are defined by AG-08.

Security requirements are defined by AG-07.

---

## 35. External Provider References

External providers may return identifiers such as:

- payment provider transaction ID
- KYC provider reference
- map/provider reference
- notification provider reference
- webhook event ID

These are external references only.

They must not replace authoritative NIDDE identifiers.

External provider data must be validated before affecting authoritative state.

External integration architecture belongs to AG-08.

---

## 36. Data Minimization

The data model must store only information required for approved domain purposes.

Sensitive categories include:

- authentication-related information
- personal identity information
- KYC information
- KYC document references
- payment information
- private messages
- precise location/tracking information
- administrative/security information

Sensitive data must follow AG-07.

External-provider data must be minimized according to AG-08.

---

## 37. Data State vs Derived State

Authoritative domain state must be distinguishable from derived or cached information.

Examples of non-authoritative derived information may include:

- cached UI state
- notification delivery state
- map presentation
- temporary provider status
- client-side role display
- locally cached lifecycle state

Derived state must not overwrite authoritative domain state without an approved server-side operation.

---

## 38. Historical Integrity

Historical records that are necessary for:

- financial reconciliation
- service history
- lifecycle auditing
- KYC decisions
- administrative actions
- security investigations

must remain traceable.

A current state change must not erase the historical fact that a prior authoritative state existed.

The implementation must provide appropriate audit/history mechanisms.

---

## 39. Concurrency and State Integrity

The domain model must account for concurrent actions.

Examples include:

- two providers submitting offers
- multiple actors attempting lifecycle transitions
- repeated payment requests
- duplicate webhook delivery
- concurrent cancellation/acceptance
- simultaneous administrative actions

The server must preserve one authoritative outcome according to the approved business rules.

Rejected concurrent operations must not partially mutate authoritative state.

---

## 40. Privacy and Location Boundary

Location and tracking data are sensitive operational data.

The model must distinguish:

- requested service location
- operational tracking information
- historical tracking information

Access and retention are governed by AG-06 and AG-07.

Location information must not become an independent authority for payment or service completion.

---

## 41. Financial Integrity

Financial records must remain auditable and internally consistent.

The model must preserve:

- amount
- currency
- applicable party relationships
- authoritative status
- internal identifiers
- external references where applicable
- relevant timestamps
- reconciliation references where applicable

A client must never be able to mutate financial authority merely by changing local state.

---

## 42. KYC Integrity

KYC state must remain server-authoritative.

The data model must distinguish:

- submission
- review
- approval
- rejection
- document/reference access

A client cannot approve its own KYC case.

An external KYC provider does not automatically become the owner of NIDDE authorization or role state.

---

## 43. Notification Integrity

Notification records are secondary to their underlying domain events.

The following principle is mandatory:

Business event
→ authoritative domain state
→ notification generation/delivery

Not:

Notification
→ authoritative business state

A notification failure must never roll back or redefine the underlying business transaction unless an explicitly approved domain operation does so.

---

## 44. Messaging Integrity

Messaging data must preserve:

- conversation membership
- sender relationship
- message ordering/timestamps
- approved content/reference type
- moderation status where applicable

The existence of a Message or Conversation identifier does not grant access.

Authorization remains server-side.

---

## 45. Data Access Boundary

AG-04 defines the domain data model.

It does not authorize arbitrary direct database access.

Repository/data-access boundaries must follow AG-03 and AG-02.

No client or UI component may directly mutate authoritative domain records.

API, application, repository, and integration layers must preserve the ownership rules defined here.

---

## 46. API Compatibility

AG-05 must expose only operations compatible with this data model.

API requests must not:

- create invalid domain relationships
- assign arbitrary lifecycle states
- assign unauthorized ownership
- declare payment success
- approve KYC
- bypass financial separation
- bypass authorization

API responses must preserve data minimization and security requirements.

---

## 47. Authentication and Authorization Compatibility

AG-06 defines authentication and authorization.

AG-04 provides the authoritative resources and relationships against which authorization decisions operate.

The data model must therefore preserve enough information to determine:

- identity
- ownership
- profile relationship
- participant relationship
- lifecycle state
- eligibility
- administrative action target

AG-04 does not define authentication mechanisms.

---

## 48. Security Compatibility

AG-07 defines the broader security model.

AG-04 must support:

- least privilege
- sensitive-data minimization
- secure data boundaries
- auditability
- safe failure
- protection of KYC/payment/location data
- controlled access to administrative records

Secrets and credentials are not ordinary domain data.

---

## 49. External Integration Compatibility

AG-08 owns external integrations.

AG-04 provides internal authoritative entities that external provider results may update only through approved integration boundaries.

External systems cannot directly write arbitrary domain state.

Provider identifiers remain references.

Provider failures must not create false successful domain states.

---

## 50. Android Compatibility

AG-09 consumes the domain model through approved API contracts.

The Android client may display and request operations involving:

- Users/profiles
- Services
- Requests
- Offers
- lifecycle state
- location/tracking
- conversations/messages
- payments
- cash transactions
- reviews
- KYC
- notifications

The Android client is never authoritative for these protected domain states.

Local Android storage must not become an independent authoritative copy.

---

## 51. Testing Compatibility

AG-10 must test the domain invariants defined by AG-04.

Testing must cover, where applicable:

- entity relationships
- ownership
- lifecycle transitions
- duplicate prevention
- payment/cash separation
- KYC state integrity
- review eligibility
- messaging authorization
- notification independence
- idempotency
- concurrency
- external reference handling
- auditability

AG-04 defines the invariant.

AG-10 defines the testing architecture.

---

## 52. CI/CD Compatibility

AG-11 must validate the implementation against the approved architecture and repository constraints.

No CI/CD process may silently modify the authoritative data model.

Database migrations must be versioned, reviewable, and compatible with the approved domain model.

---

## 53. Production Compatibility

AG-12 owns production architecture.

Production systems must preserve:

- authoritative data ownership
- financial integrity
- KYC protection
- auditability
- backup/recovery requirements
- secure database access
- controlled migrations
- data retention requirements

Production infrastructure must not redefine domain ownership.

---

## 54. Release Compatibility

AG-13 owns release architecture.

A release must not be considered architecture-compatible if it introduces:

- an unauthorized entity
- an unauthorized ownership model
- a conflicting lifecycle
- a payment/cash contradiction
- a KYC authority contradiction
- a security-sensitive data contradiction
- an API/domain mismatch

Architecture-affecting changes require controlled review.

---

## 55. Verification Criteria

AG-04 may become VERIFIED only when:

- its scope matches the canonical AG-04 definition
- all authoritative entities are defined
- entity ownership is explicit
- relationships are internally consistent
- lifecycle semantics are consistent
- Service Request and Offer rules are consistent
- Payment and Cash Transaction remain separate
- KYC authority remains server-side
- location/tracking remains non-authoritative for financial/service completion
- messaging relationships are defined
- notification records remain non-authoritative
- review eligibility is defined
- administrative records remain controlled
- audit requirements are preserved
- idempotency requirements are represented
- external references do not replace internal authority
- AG-05 API requirements align
- AG-06 authorization requirements align
- AG-07 security requirements align
- AG-08 integration requirements align
- AG-09 Android requirements align
- AG-10 testing requirements are mapped
- AG-11 CI/CD requirements remain compatible
- AG-12 production requirements remain compatible
- AG-13 release requirements remain compatible
- no unresolved blocking contradiction exists
- required verification evidence is recorded

READY FOR VERIFICATION does not mean VERIFIED.

---

## 56. Implementation Lock

AG-04 does not authorize implementation.

Implementation remains:

LOCKED

until the complete canonical architecture sequence and final readiness conditions are satisfied.

No database migrations, repositories, API implementations, or Android data layers should be created solely because AG-04 has been written.

---

## 57. Control Statement

AG-04 establishes the authoritative NIDDE domain data model.

All later architecture gates must preserve the entities, ownership, lifecycle semantics, financial separation, KYC boundaries, location/tracking boundaries, messaging relationships, notification behavior, and data integrity rules established by AG-04.

Where a conflict exists between implementation assumptions and this architecture contract, implementation must stop for the affected area until the architecture decision is resolved.

**AG-04 STATUS: READY FOR VERIFICATION**

**IMPLEMENTATION: LOCKED**
