# NIDDE — AG-03 SYSTEM & DEPENDENCY ARCHITECTURE

**Phase:** 00 — ARCHITECTURE  
**Gate:** AG-03 — System Architecture  
**Revision:** V1.0.0  
**Status:** READY FOR VERIFICATION  
**Implementation:** LOCKED  
**Physical-file count:** NOT YET CALCULATED

## 1. Objective
Define domain boundaries, application layers, service ownership, dependency direction, interfaces, runtime responsibilities, data flow, security boundaries, and failure rules before implementation.

## 2. System Boundary
NIDDE is a multi-role services marketplace for Client, Artisan, Company, and Admin. Backend authorization is authoritative; clients never establish privileged authority.

## 3. Logical Architecture
```text
CLIENT / ARTISAN / COMPANY / ADMIN
              |
              v
        CLIENT / API UI
              |
              v
      INTERFACE / API LAYER
              |
              v
       APPLICATION / USE CASES
              |
              v
          DOMAIN LAYER
              ^
              |
     INFRASTRUCTURE / ADAPTERS
          |           |
          v           v
      DATABASE    EXTERNAL SERVICES
```

## 4. Domain Boundaries
1. Identity & Accounts
2. Authentication & Authorization
3. Client
4. Artisan
5. Company
6. Services / Marketplace
7. Requests
8. Offers
9. Service Lifecycle
10. Messaging
11. Location / Tracking
12. Payments
13. Cash
14. Reviews / Ratings
15. KYC / Verification
16. Notifications
17. Admin / Moderation
18. Analytics / Reporting
19. Security
20. Audit / Logging

Each domain owns its business rules and exposes explicit contracts.

## 5. Application Layers

### Interface
Transport, request parsing, serialization, boundary validation, authentication-context extraction, and error mapping. No core business decisions.

### Application
Use cases, orchestration, transaction boundaries, authorization at use-case boundaries, and coordination.

### Domain
Business rules, invariants, policies, and state transitions. No direct dependency on HTTP, Android UI, databases, or provider implementations.

### Infrastructure
Database access and adapters for maps, payments, notifications, storage, KYC, and other external systems.

## 6. Dependency Direction
```text
Clients -> API/Interface -> Application -> Domain
                                      ^
                                      |
                           Infrastructure/Adapters
```

Rules:
- Clients depend only on published contracts.
- Domain does not depend on infrastructure implementations.
- Database access is behind data-access abstractions.
- External providers are isolated behind adapters.
- Circular dependencies are forbidden unless explicitly approved.
- Cross-domain database writes are forbidden.
- Dependency changes require impact analysis.

## 7. Core Data Flows

### Request
```text
Client -> Authenticate -> Discover -> Create Request
-> Validate -> Store -> Notify eligible providers
-> Receive Offers -> Select Offer -> Start Service
```

### Offer
```text
Provider -> Authenticate/Authorize -> Eligible Request
-> Submit Offer -> Validate -> Request receives Offer
```

### Service lifecycle
```text
REQUESTED -> ACCEPTED -> EN_ROUTE -> ARRIVED
-> IN_PROGRESS -> COMPLETED
```

Cancellation and error transitions must define actor, state, financial, notification, and audit effects.

### Payment
```text
Payment trigger -> Authorization -> Cash/Approved Electronic Flow
-> Result -> Financial Record -> Notification -> Audit
```

Provider failure must never be interpreted as payment success.

## 8. Ownership

| Concern | Authoritative owner |
|---|---|
| Identity | Identity / Accounts |
| Sessions / tokens | Authentication |
| Roles / permissions | Authorization |
| Marketplace services | Services |
| Requests | Requests |
| Offers | Offers |
| Service states | Service Lifecycle |
| Messages | Messaging |
| Location / tracking | Location |
| Financial transactions | Payments / Cash |
| Reviews | Reviews |
| Verification | KYC |
| Notifications | Notifications |
| Moderation / privileged actions | Admin |
| Metrics | Analytics |
| Security controls | Security |
| Evidence | Audit / Logging |

## 9. Authorization Boundary
Authentication proves identity. Authorization decides permission.

Server-side authorization is mandatory for privileged operations. Client-supplied role, ownership, payment success, KYC approval, service completion, or admin authority is never trusted.

## 10. Service Lifecycle Authority
Service Lifecycle owns state transitions. Other domains may request transitions through approved interfaces but may not silently mutate lifecycle state.

## 11. Financial Boundary
Payments and Cash remain separate from ordinary service execution. Financial operations must be attributable, auditable, protected against duplicates, and explicit about success, failure, and pending states.

## 12. External Integration Boundary
Potential integrations include maps/geocoding/routing, payment providers, push notifications, email/SMS where approved, storage, and KYC providers.

Every integration requires an adapter, failure policy, retry policy where safe, idempotency policy where required, audit rules, and secure secret handling.

## 13. Cross-Domain Communication
Preferred order:
```text
Explicit domain contract
        -> Application orchestration
        -> Event/message when asynchronous behavior is required
```

No hidden side effects. Every cross-domain operation must define owner, input, output, authorization, and failure behavior.

## 14. Security / Audit
Required controls include validation, authorization, rate limiting, secure secrets handling, sensitive-data protection, audit logging, abuse controls, and security testing.

Real secrets must never enter Git.

## 15. Failure / Consistency
The system must distinguish success, failure, pending, rejected, cancelled, and expired states.

Retries must be bounded and safe. Repeatable operations require explicit idempotency behavior.

## 16. Forbidden Patterns
- Client-only authorization
- Direct privileged database access from clients
- Duplicated business rules across clients
- Business logic hidden in controllers
- Hidden cross-domain database writes
- Unapproved circular dependencies
- Payment success inferred from client state
- Client-controlled KYC approval
- Unauthorized lifecycle mutation
- Untracked financial mutations
- Secrets in source control
- Arbitrary new architecture boundaries

## 17. Verification Checklist
- Domain boundaries defined
- Application layers defined
- Dependency direction defined
- Runtime ownership defined
- Critical data flows defined
- Authorization boundary defined
- Lifecycle authority defined
- Financial boundary defined
- External integration boundary defined
- Failure/idempotency rules defined
- Security/audit boundary defined

**Verification status:** READY FOR FORMAL GATE REVIEW.

## 18. Verification Requirement
AG-03 may become `VERIFIED` only after:
1. Static/document consistency check.
2. Compatibility with AG-01.
3. Compatibility with AG-02 repository boundaries.
4. Domain ownership review.
5. Dependency-direction review.
6. Critical-flow review.
7. Security/authorization review.
8. Evidence recorded in Project Control and Manifest.

Until then:
```text
APPLICATION IMPLEMENTATION = LOCKED
PHYSICAL FILE COUNT = NOT YET CALCULATED
```

## 19. Next Gate
After AG-03 verification: **AG-04 — DATA MODEL**.

No implementation file is authorized merely because this gate document is uploaded.
