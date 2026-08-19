# NIDDE — AG-04 DATA MODEL

**Project:** NIDDE  
**Phase:** 00 — ARCHITECTURE  
**Gate:** AG-04 — Data Model  
**Revision:** V1.0.0  
**Status:** READY FOR VERIFICATION  
**Implementation:** LOCKED  
**Physical-file count:** NOT YET CALCULATED

## 1. Purpose

AG-04 defines the logical data model required by NIDDE before implementation: entities, ownership, relationships, lifecycle state, constraints, indexes, audit fields, migration rules, and seed rules.

It is a design contract, not an implementation migration or application source file.

## 2. Data Ownership Principles

1. Every entity has one authoritative domain owner.
2. Foreign-key relationships must reflect approved domain ownership.
3. Business rules are enforced by the backend/domain layer, not only by clients.
4. Sensitive information is minimized and access-controlled.
5. Financial and audit records are append-oriented and traceable.
6. Lifecycle state changes are explicit and auditable.
7. Soft deletion is used only where required by business, legal, or audit needs; it must not replace proper lifecycle state.
8. No cross-domain direct database writes outside approved repository/data-access boundaries.

## 3. Identity and Account Model

### User

Represents the common identity record.

Core fields:
- id
- role/profile references
- email or phone identity
- credential/authentication references
- status
- created_at
- updated_at

Rules:
- identity is unique;
- role claims are never trusted from the client;
- sensitive authentication material is not stored in plaintext.

### Client Profile

Owns client-specific marketplace information and preferences.

### Artisan Profile

Owns artisan-specific professional information, availability, service area, and verification status.

### Company Profile

Owns company-specific business information, verification status, and service capabilities.

## 4. Marketplace Model

### Service Category

Defines marketplace classification.

Fields include:
- id
- parent_id where hierarchy is required
- name
- description
- status
- created_at
- updated_at

### Service Offering

Represents a service available in the marketplace.

Fields include:
- id
- category_id
- owner/profile reference
- title
- description
- pricing metadata
- availability metadata
- status
- created_at
- updated_at

## 5. Request and Offer Model

### Service Request

Authoritative record for a client's request.

Core fields:
- id
- client_id
- service/category reference
- location reference
- description
- requested schedule
- lifecycle_status
- created_at
- updated_at
- completed_at / cancelled_at where applicable

### Offer

Represents an artisan/company proposal against a request.

Core fields:
- id
- request_id
- provider/profile_id
- amount
- currency
- message/terms
- status
- expires_at where applicable
- created_at
- updated_at

Constraints:
- request must exist;
- provider must be eligible and authorized;
- duplicate active offers must be prevented according to the business rule;
- accepted offer must be uniquely identifiable for a request.

## 6. Service Lifecycle Model

The authoritative lifecycle is:

`REQUESTED → ACCEPTED → EN_ROUTE → ARRIVED → IN_PROGRESS → COMPLETED`

Cancellation and error states are modeled explicitly.

Every transition records:
- previous_state
- new_state
- actor_id
- timestamp
- reason where required
- correlation/reference id

A lifecycle history must be immutable after recording except through an approved correction/audit mechanism.

## 7. Location Model

### Location

Represents a reusable geographic address/location reference where appropriate.

Potential fields:
- id
- latitude
- longitude
- address components
- geocoding metadata
- created_at
- updated_at

Location precision and retention must follow the security/privacy model.

### Tracking Event

Represents time-stamped movement/status data when tracking is active.

Core fields:
- id
- service/order reference
- actor/device reference where required
- latitude
- longitude
- timestamp
- event_type

Tracking data must not be treated as authoritative proof of payment or service completion by itself.

## 8. Messaging Model

### Conversation

Defines a communication boundary between permitted participants.

### Message

Fields include:
- id
- conversation_id
- sender_id
- message_type
- content/reference
- created_at
- read_at where applicable
- status

Authorization must ensure participants can access only conversations they are permitted to access.

## 9. Payment and Cash Model

### Payment

Represents an attempted or completed financial transaction.

Core fields:
- id
- request/service reference
- payer reference
- payee/reference where applicable
- method
- provider/reference
- amount
- currency
- status
- idempotency/reference key
- created_at
- updated_at
- completed_at

Payment status must distinguish at least pending, successful, failed, cancelled, and rejected where applicable.

### Cash Transaction

Represents a cash settlement/record separate from electronic-provider state.

Cash records must be attributable, auditable, and reconcilable.

Rules:
- never mark electronic payment successful from client-side state;
- provider callbacks/webhooks must be validated by the integration boundary;
- duplicate transaction processing must be prevented through idempotency controls.

## 10. Review Model

### Review

Represents a completed-service review.

Fields include:
- id
- service/request reference
- author_id
- subject_id
- rating
- comment
- moderation_status
- created_at
- updated_at

Constraints:
- review eligibility must be validated server-side;
- rating range is constrained;
- duplicate reviews are prevented according to the business rule;
- moderation actions are auditable.

## 11. KYC Model

### KYC Case

Represents verification state for a person/company.

Fields include:
- id
- subject_id
- status
- verification_type
- reviewer reference where applicable
- submitted_at
- reviewed_at
- decision_reason/reference

### KYC Document

Represents a document metadata record.

Sensitive document contents are stored through the approved secure storage/integration boundary, not casually in ordinary tables or Git.

## 12. Notification Model

### Notification

Fields include:
- id
- recipient_id
- type
- payload/reference
- channel
- status
- created_at
- delivered_at / read_at where applicable

Notification delivery is not authoritative for the underlying business transaction.

## 13. Admin and Moderation Model

Administrative actions must be attributable to an admin identity.

Moderation records should capture:
- target entity
- action
- actor
- reason
- previous status where relevant
- resulting status
- timestamp

Admin authority is enforced by backend authorization.

## 14. Analytics Model

Operational analytics should use event records or controlled projections rather than allowing analytics logic to mutate transactional source-of-truth records.

Analytics records must identify:
- event type
- actor/entity reference where appropriate
- timestamp
- source/correlation reference
- non-sensitive event metadata

## 15. Audit Model

### Audit Event

Critical operations must generate auditable events.

Core fields:
- id
- actor_id where applicable
- action
- entity_type
- entity_id
- timestamp
- result
- correlation_id
- metadata appropriate to the security policy

Secrets, credentials, and unnecessary sensitive values must never be written to audit logs.

## 16. Common Data Constraints

The model must enforce, where applicable:

- primary keys;
- foreign keys;
- unique constraints;
- not-null constraints;
- valid enum/state values;
- non-negative monetary amounts;
- valid currency identifiers;
- valid timestamps;
- ownership constraints;
- lifecycle transition rules;
- idempotency uniqueness;
- referential integrity.

Database constraints complement, but do not replace, domain validation.

## 17. Indexing Strategy

Indexes must be created from verified access patterns rather than added blindly.

Expected index classes include:

- unique identity fields;
- foreign keys used for joins;
- request lifecycle/status queries;
- provider availability queries;
- offer lookup by request;
- payment/provider reference lookup;
- notification recipient/status lookup;
- message conversation/time lookup;
- audit entity/time lookup;
- location queries where supported and required.

Composite indexes must match actual query predicates and ordering.

## 18. Lifecycle and Retention

Every major transactional entity must define:

- creation timestamp;
- update timestamp;
- lifecycle status;
- completion/cancellation timestamp where applicable;
- actor/reason for sensitive transitions where required.

Retention and deletion rules must respect audit, financial, legal, privacy, and security requirements.

## 19. Migration Strategy

Schema changes follow:

`PLAN → MIGRATION → STATIC CHECK → APPLY IN TEST → INTEGRATION CHECK → VERIFY → REGISTER`

Rules:

1. Migrations are versioned and ordered.
2. Applied migrations are immutable.
3. Destructive changes require explicit impact analysis.
4. Production migrations require backup/recovery consideration.
5. Rollback strategy must be defined for risky changes.
6. Data transformations must be deterministic and tested.
7. No manual production schema changes outside the approved migration process.

## 20. Seed Strategy

Seeds are divided into:

- required system/reference data;
- development/test data;
- controlled demonstration data.

Rules:

- production seeds must never contain real personal secrets;
- passwords/credentials must not be hard-coded in repository seeds;
- deterministic reference data should use stable identifiers where appropriate;
- test data must be clearly separated from production data.

## 21. Relationship Summary

```text
User
├── Client Profile
├── Artisan Profile
├── Company Profile
└── Admin authority

Client
└── Service Request
    ├── Offers ← Artisan/Company
    ├── Service Lifecycle
    ├── Location
    ├── Payment / Cash
    ├── Conversation / Messages
    └── Review

Artisan/Company
└── Service Offering

KYC Subject
└── KYC Case
    └── KYC Documents

Any critical operation
└── Audit Event
```

## 22. Data Integrity Rules

1. No orphan transactional records.
2. No cross-user access through predictable identifiers alone.
3. Ownership must be checked in the application authorization layer.
4. Financial totals must not be derived from untrusted client values.
5. Lifecycle transitions must be atomic where required.
6. Audit events must identify the operation and actor where applicable.
7. Sensitive fields must have explicit protection and retention rules.
8. Referential integrity must survive retries and partial external failures.

## 23. Verification Checklist

| Check | Status |
|---|---|
| Core entities identified | PASS — PENDING FORMAL VERIFICATION |
| Domain ownership mapped | PASS — PENDING FORMAL VERIFICATION |
| Relationships mapped | PASS — PENDING FORMAL VERIFICATION |
| Lifecycle fields defined | PASS — PENDING FORMAL VERIFICATION |
| Constraints defined | PASS — PENDING FORMAL VERIFICATION |
| Index strategy defined | PASS — PENDING FORMAL VERIFICATION |
| Audit fields defined | PASS — PENDING FORMAL VERIFICATION |
| Migration strategy defined | PASS — PENDING FORMAL VERIFICATION |
| Seed strategy defined | PASS — PENDING FORMAL VERIFICATION |
| Security/privacy boundary considered | PASS — PENDING FORMAL VERIFICATION |
| Physical-file count | NOT YET CALCULATED |

## 24. Verification Requirement

AG-04 becomes `VERIFIED` only after compatibility with the verified technology/repository/system architecture gates, database design review, integrity review, security review, migration/seed review, and evidence registration in the canonical control documents.

Until then:

`APPLICATION IMPLEMENTATION = LOCKED`

`PHYSICAL FILE COUNT = NOT YET CALCULATED`

## 25. Next Gate

After AG-04 is verified:

`AG-05 — API CONTRACT`

No implementation file is authorized merely because this architecture document is uploaded.
