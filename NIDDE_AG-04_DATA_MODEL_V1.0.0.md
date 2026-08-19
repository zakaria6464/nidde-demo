# NIDDE — AG-04 DATA MODEL

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-04 — Data Model
Revision: V1.0.0
Status: READY FOR FORMAL GATE REVIEW
Implementation: LOCKED
Physical-file count: NOT YET CALCULATED

## 1. Purpose

AG-04 defines the logical data model required by NIDDE before implementation.

It defines:

- entities
- authoritative ownership
- relationships
- cardinality
- lifecycle state
- primary and foreign-key requirements
- uniqueness and integrity constraints
- indexes
- audit fields
- sensitive-data boundaries
- migration rules
- seed rules
- retention considerations

This document is a design contract.

It is not an implementation migration and is not application source code.

## 2. Data Ownership Principles

1. Every entity has one authoritative domain owner.
2. Foreign-key relationships must respect approved domain ownership.
3. Business rules are enforced by backend/domain logic and must not depend solely on client validation.
4. Sensitive information must be minimized and access-controlled.
5. Financial and audit records must be attributable and traceable.
6. Financial records must support append-oriented auditability where required.
7. Lifecycle state changes must be explicit and auditable.
8. Soft deletion must only be used where required by business, legal, or audit requirements.
9. Soft deletion must never replace an authoritative lifecycle state.
10. Cross-domain direct database writes are prohibited.
11. Persistence access must occur through approved data-access boundaries.
12. Referential integrity must not be bypassed by application shortcuts.

## 3. Common Data Conventions

Unless a specific entity requires another representation:

### 3.1 Primary Keys

Every persistent entity must have:

- `id`
- globally unique identifier semantics
- immutable identity after creation

### 3.2 Timestamps

Entities that change over time should contain:

- `created_at`
- `updated_at`

Immutable event/history records should contain:

- `created_at` or equivalent event timestamp

### 3.3 Audit Identity

Security-sensitive and administrative records should retain:

- `actor_id`
- operation/action
- timestamp
- reason where required
- correlation/reference identifier where applicable

### 3.4 Status

Status values must be explicit enumerations or controlled values.

Free-form status strings are prohibited for authoritative lifecycle states.

### 3.5 Money

Monetary records must define:

- integer/minor-unit or equivalent exact monetary representation
- currency code
- transaction status

Floating-point values must not be used as the authoritative representation of financial amounts.

### 3.6 Sensitive Data

Credentials, authentication secrets, KYC document contents, payment secrets, provider secrets, and similar sensitive material must not be stored casually in ordinary application tables or Git.

## 4. Identity and Account Model

### 4.1 User

Owner:
Identity / Accounts

Purpose:
Common identity record for all platform users.

Fields:

- `id`
- `status`
- `created_at`
- `updated_at`

Identity/contact references must be represented through approved identity/authentication boundaries.

Authentication credentials and secrets are not stored as plaintext in the User entity.

Rules:

- identity must be unique according to the approved authentication identity mechanism
- user identity is immutable
- client-supplied role claims are never authoritative

### 4.2 Client Profile

Owner:
Client

Fields:

- `id`
- `user_id`
- client-specific profile data
- preferences metadata
- `status`
- `created_at`
- `updated_at`

Relationship:

`Client Profile.user_id -> User.id`

Constraint:

One User may have at most one active Client Profile where the business model requires a single profile.

### 4.3 Artisan Profile

Owner:
Artisan

Fields:

- `id`
- `user_id`
- professional profile data
- availability metadata
- service-area metadata
- verification reference
- `status`
- `created_at`
- `updated_at`

Relationship:

`Artisan Profile.user_id -> User.id`

### 4.4 Company Profile

Owner:
Company

Fields:

- `id`
- company/account reference
- business information
- verification reference
- service capabilities
- `status`
- `created_at`
- `updated_at`

Relationships must reference the authoritative identity/account records.

## 5. Marketplace Model

### 5.1 Service Category

Owner:
Services / Marketplace

Fields:

- `id`
- `parent_id` nullable
- `name`
- `description` nullable
- `status`
- `created_at`
- `updated_at`

Relationship:

`Service Category.parent_id -> Service Category.id`

Rules:

- category hierarchy must not create cycles
- active categories must have valid ownership
- category names must satisfy the approved uniqueness scope

### 5.2 Service Offering

Owner:
Services / Marketplace

Fields:

- `id`
- `category_id`
- `owner_profile_id`
- `title`
- `description`
- pricing metadata
- availability metadata
- `status`
- `created_at`
- `updated_at`

Relationships:

`Service Offering.category_id -> Service Category.id`

`Service Offering.owner_profile_id -> approved provider profile`

Rules:

- owner must be an authorized provider
- category must exist
- inactive offerings must not be treated as active marketplace inventory

## 6. Service Request

Owner:
Requests

Fields:

- `id`
- `client_id`
- `service_category_id` or approved service reference
- `location_id`
- `description`
- requested schedule
- `lifecycle_status`
- `created_at`
- `updated_at`
- `completed_at` nullable
- `cancelled_at` nullable

Relationships:

`Service Request.client_id -> Client Profile.id`

`Service Request.location_id -> Location.id`

Category/service references must resolve to an approved marketplace entity.

Rules:

- request must have an authorized client owner
- lifecycle status must use controlled values
- completion timestamps are only valid for completed requests
- cancellation timestamps are only valid for cancelled requests

## 7. Offer

Owner:
Offers

Fields:

- `id`
- `request_id`
- `provider_profile_id`
- `amount`
- `currency`
- message/terms
- `status`
- `expires_at` nullable
- `created_at`
- `updated_at`

Relationships:

`Offer.request_id -> Service Request.id`

`Offer.provider_profile_id -> approved provider profile`

Constraints:

- request must exist
- provider must be eligible and authorized
- amount must be valid
- currency must be explicitly defined
- duplicate active offers must be prevented according to the approved business rule
- an accepted request must have at most one authoritative accepted offer

## 8. Service Lifecycle

Owner:
Service Lifecycle

### 8.1 Authoritative States

The primary lifecycle is:

`REQUESTED`
→ `ACCEPTED`
→ `EN_ROUTE`
→ `ARRIVED`
→ `IN_PROGRESS`
→ `COMPLETED`

Cancellation and error states must be explicit.

### 8.2 Lifecycle History

Fields:

- `id`
- service/request reference
- `previous_state`
- `new_state`
- `actor_id`
- `timestamp`
- `reason` nullable
- `correlation_id` or reference identifier

Rules:

- history is append-oriented
- recorded history must be immutable except through approved correction/audit mechanisms
- invalid state transitions must be rejected
- actor must be authorized for the transition

## 9. Location Model

### 9.1 Location

Owner:
Location / Tracking

Fields:

- `id`
- latitude
- longitude
- address components where required
- geocoding metadata where required
- `created_at`
- `updated_at`

Rules:

- coordinate precision must follow privacy requirements
- unnecessary location precision must not be retained
- retention must follow approved security/privacy policy

### 9.2 Tracking Event

Owner:
Location / Tracking

Fields:

- `id`
- service/order reference
- actor/device reference where required
- latitude
- longitude
- timestamp
- `event_type`

Rules:

Tracking events are operational evidence only.

Tracking data must not independently prove:

- payment success
- service completion
- financial settlement

## 10. Messaging Model

### 10.1 Conversation

Owner:
Messaging

Fields:

- `id`
- conversation type
- created_at
- updated_at
- status

Participants must be represented through an approved participant relationship.

### 10.2 Message

Fields:

- `id`
- `conversation_id`
- `sender_id`
- `message_type`
- content/reference
- `created_at`
- `read_at` nullable
- `status`

Relationships:

`Message.conversation_id -> Conversation.id`

`Message.sender_id -> User.id`

Rules:

- sender must be a permitted participant
- participants may access only authorized conversations
- message records must preserve auditability

## 11. Payment and Cash Model

### 11.1 Payment

Owner:
Payments

Fields:

- `id`
- request/service reference
- payer reference
- payee reference where applicable
- method
- provider/reference
- amount
- currency
- status
- idempotency/reference key
- `created_at`
- `updated_at`
- `completed_at` nullable

Minimum statuses:

- `PENDING`
- `SUCCESSFUL`
- `FAILED`
- `CANCELLED`
- `REJECTED`

Rules:

- payment success must never originate solely from client state
- provider callbacks/webhooks must be validated
- duplicate processing must be prevented through idempotency controls
- provider references must be traceable

### 11.2 Cash Transaction

Owner:
Cash

Fields:

- `id`
- service/request reference
- payer reference
- payee reference
- amount
- currency
- status
- recorded_by
- recorded_at
- reference/correlation identifier

Cash records must be attributable, auditable, and reconcilable.

Cash must remain distinct from electronic-provider transaction state.

## 12. Review Model

Owner:
Reviews / Ratings

### Review

Fields:

- `id`
- service/request reference
- `author_id`
- `subject_id`
- `rating`
- `comment`
- `moderation_status`
- `created_at`
- `updated_at`

Constraints:

- service completion must be verified server-side
- author must be eligible
- subject must be valid
- rating must be within the approved range
- duplicate reviews must be prevented according to business rules
- moderation actions must be auditable

## 13. KYC Model

Owner:
KYC / Verification

### 13.1 KYC Case

Fields:

- `id`
- `subject_id`
- `status`
- `verification_type`
- reviewer reference where applicable
- `submitted_at`
- `reviewed_at` nullable
- decision reason/reference where applicable

Rules:

- status transitions must be authorized
- approval must not originate from client state
- decisions must be auditable

### 13.2 KYC Document

Fields:

- `id`
- `kyc_case_id`
- document type
- secure-storage reference
- status
- created_at
- updated_at

Sensitive document contents must remain in the approved secure storage/integration boundary.

Git must never contain KYC document contents.

## 14. Notification Model

Owner:
Notifications

### Notification

Fields:

- `id`
- `recipient_id`
- `type`
- payload/reference
- `channel`
- `status`
- `created_at`
- `delivered_at` nullable
- `read_at` nullable

Rules:

Notification delivery is not authoritative for the underlying business transaction.

A failed notification must not automatically roll back the business transaction unless an explicitly approved workflow requires it.

## 15. Admin and Moderation Model

Owner:
Admin / Moderation

Administrative and moderation records must be attributable.

Fields:

- `id`
- target entity/reference
- action
- actor_id
- reason
- previous status where relevant
- resulting status where relevant
- timestamp
- correlation/reference identifier

Rules:

- only authorized admins may perform privileged actions
- administrative actions are auditable
- client-supplied admin authority is never trusted

## 16. Analytics Model

Owner:
Analytics / Reporting

Analytics must consume approved events, records, or controlled projections.

Analytics logic must not mutate transactional source-of-truth records.

Analytics projections may be rebuilt from authoritative source records where architecture permits.

Analytics data must respect privacy, retention, and access-control requirements.

## 17. Relationships and Referential Integrity

The following relationships are authoritative at the logical-model level:

- Client Profile -> User
- Artisan Profile -> User
- Company Profile -> approved identity/account owner
- Service Category -> parent Service Category
- Service Offering -> Service Category
- Service Offering -> Provider Profile
- Service Request -> Client Profile
- Service Request -> Service Category / Service Offering as approved
- Service Request -> Location
- Offer -> Service Request
- Offer -> Provider Profile
- Lifecycle History -> Service Request / Service reference
- Tracking Event -> Service reference
- Message -> Conversation
- Message -> User
- Payment -> Request/Service
- Cash Transaction -> Request/Service
- Review -> Request/Service
- Review -> Author User/Profile
- Review -> Subject User/Profile
- KYC Case -> Subject
- KYC Document -> KYC Case
- Notification -> Recipient User
- Moderation Record -> Target entity
- Moderation Record -> Admin actor

Foreign keys must point only to authoritative entities.

## 18. Constraints

The implementation data layer must enforce, where applicable:

- primary-key uniqueness
- foreign-key integrity
- required-field constraints
- controlled status values
- valid monetary amounts
- valid currency codes
- lifecycle transition integrity
- uniqueness rules
- idempotency-key uniqueness within the approved scope
- prevention of duplicate active offers where required
- prevention of duplicate reviews where required
- valid timestamps
- valid ownership references

Business authorization rules remain backend/domain responsibilities and must not be delegated exclusively to database constraints.

## 19. Indexing Principles

Indexes must be created based on approved access patterns.

Expected indexing areas include:

- user identity lookup
- profile ownership
- service category hierarchy
- active service offerings
- request status
- request client ownership
- request location/search references where applicable
- offer request lookup
- offer provider lookup
- lifecycle history service lookup
- tracking event service/time lookup
- conversation participants
- message conversation/time lookup
- payment reference/idempotency lookup
- cash transaction references
- review subject/service lookup
- KYC subject/status lookup
- notification recipient/status lookup
- audit actor/time lookup

Indexes must not be added blindly.

Final physical indexes require implementation-level review against actual database technology and measured access patterns.

## 20. Audit Fields and Immutability

The following records require strong auditability:

- lifecycle transitions
- payments
- cash transactions
- KYC decisions
- moderation actions
- security-sensitive operations

Where a record represents historical evidence, it should be append-oriented.

Corrections must create an auditable correction trail rather than silently rewriting historical truth.

Secrets must never be included in audit records.

## 21. Soft Deletion

Soft deletion is not a substitute for lifecycle state.

It may be used only where:

- business requirements require recoverability
- legal requirements require retention
- audit requirements require historical visibility

Entities subject to mandatory historical retention must not be physically deleted without an approved retention/deletion policy.

## 22. Migration Rules

Database migrations must:

1. be versioned
2. be deterministic
3. be reviewable
4. preserve existing data unless an approved destructive change exists
5. include rollback or recovery strategy where technically possible
6. respect foreign-key ordering
7. preserve domain ownership
8. avoid undocumented schema changes
9. be tested before production execution
10. be traceable to an approved change

Destructive migrations require explicit approval.

No manual production schema modification outside the migration/change-control process is authorized.

## 23. Seed Rules

Seed data must be classified as:

- required baseline data
- development/test data
- optional demonstration data

Rules:

1. Production seed data must be explicitly approved.
2. Secrets must never be seeded.
3. Real personal information must not be used as test seed data.
4. Seed operations must be deterministic or idempotent.
5. Seed data must not bypass domain constraints.
6. Reference data must have stable identifiers where required.
7. Demo/test records must remain distinguishable from real production records.

## 24. Retention and Privacy

Data retention must follow the approved security/privacy policy.

Sensitive data must have:

- purpose limitation
- access control
- minimum necessary retention
- deletion/anonymization rules where legally and technically applicable

Location, KYC, payment, messaging, and audit records require particular care.

## 25. Cross-Domain Data Access

Domains may read or modify data only through approved contracts and data-access boundaries.

Forbidden:

- direct cross-domain table mutation
- bypassing domain invariants
- undocumented database coupling
- client-driven authoritative database changes

Cross-domain operations must preserve ownership defined in AG-03.

## 26. Data Security

The data model must support:

- least-privilege access
- sensitive-data minimization
- encrypted transport
- protected secret storage
- controlled KYC storage
- financial auditability
- secure audit logging
- protection against unauthorized modification

Actual security mechanisms are governed jointly with AG-06 and AG-07.

## 27. Compatibility With AG-03

AG-04 must remain compatible with AG-03.

The following AG-03 ownership rules are authoritative:

- Identity owns identity
- Authentication / Authorization owns authentication and permissions
- Services owns marketplace services
- Requests owns requests
- Offers owns offers
- Service Lifecycle owns lifecycle transitions
- Messaging owns messaging
- Location / Tracking owns location and tracking
- Payments owns electronic financial transactions
- Cash owns cash settlement records
- Reviews owns reviews
- KYC owns verification
- Notifications owns notification delivery
- Admin / Moderation owns privileged administrative actions
- Analytics owns projections/reporting
- Security owns security controls
- Audit / Logging owns audit evidence

AG-04 must not introduce ownership that contradicts AG-03.

## 28. Compatibility With AG-05 Through AG-08

The logical data model must provide stable references for:

- API resources and contracts
- authentication and authorization subjects
- security controls
- external provider references

AG-05 owns API contract details.

AG-06 owns authentication/authorization details.

AG-07 owns security model details.

AG-08 owns external integration details.

AG-04 does not replace those gates.

## 29. Verification Requirements

AG-04 may become VERIFIED only after:

1. Static/document consistency check.
2. Compatibility with AG-01.
3. Compatibility with AG-02 repository boundaries.
4. Compatibility with AG-03 ownership and dependency architecture.
5. Entity completeness review.
6. Relationship and cardinality review.
7. Constraint review.
8. Indexing review.
9. Audit and immutability review.
10. Migration review.
11. Seed review.
12. Security/privacy review.
13. Cross-domain access review.
14. Evidence recorded in Project Control.
15. Evidence recorded in the Master File Manifest.

Until then:

APPLICATION IMPLEMENTATION = LOCKED

PHYSICAL FILE COUNT = NOT YET CALCULATED

## 30. Verification Status

Current status:

READY FOR FORMAL GATE REVIEW

This document is not VERIFIED merely because it is present in the repository.

Formal verification requires the checks defined in Section 29.

## 31. Next Gate

After successful AG-04 verification:

AG-05 — API CONTRACT ARCHITECTURE

No application implementation is authorized merely because AG-04 is verified.

## 32. Change Control

Changes affecting:

- entity ownership
- relationships
- lifecycle state
- financial records
- security-sensitive data
- cross-domain references
- migration rules
- retention rules

require impact analysis against affected architecture gates.

No silent data-model changes are permitted.

## 33. Control Statement

AG-04 establishes the logical data model contract for NIDDE.

It does not authorize implementation.

The physical schema, migrations, repositories, indexes, and application models must be implemented only after the architecture/file-count lock and Phase 01 authorization requirements are satisfied.

---

END OF AG-04
