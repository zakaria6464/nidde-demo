NIDDE — AG-03 SYSTEM & DEPENDENCY ARCHITECTURE 

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-03 — System Architecture
Revision: V1.0.1
Status: READY FOR VERIFICATION
Implementation: LOCKED
Physical-file count: NOT YET CALCULATED

1. Objective 

AG-03 defines the logical system architecture required before implementation.

It establishes:

system boundaries logical application layers domain and capability boundaries ownership relationships dependency direction interface boundaries runtime responsibilities major data flows cross-domain communication rules security and failure boundaries 

AG-03 is an architecture contract.

It does not implement application source code, database migrations, Android source code, CI/CD workflows, deployment infrastructure, or production configuration.

2. System Boundary 

NIDDE is a multi-role services marketplace supporting:

Client Artisan Company Admin 

The backend/domain boundary remains authoritative for protected business decisions.

Clients are interaction layers and must never establish privileged authority through client-controlled state.

The system must preserve the architecture boundaries established by AG-01 and AG-02.

3. Logical Architecture CLIENT / ARTISAN / COMPANY / ADMIN | v CLIENT / API INTERFACE | v APPLICATION LAYER / USE CASES | v DOMAIN LAYER ^ | INTERFACES / PORTS ^ | INFRASTRUCTURE / ADAPTERS | | v v DATABASE EXTERNAL SERVICES 

Dependency inversion is intentional:

domain logic does not depend on infrastructure implementations; infrastructure implements approved interfaces required by application/domain logic; interface/API layers do not own core business rules; clients consume published contracts only. 4. Domain and Capability Boundaries 

AG-03 defines the logical boundaries of the system without overriding the authoritative ownership defined by AG-04 or the specialized architecture gates.

Core business domains Identity & Accounts Authentication / Authorization Client Artisan Company Services / Marketplace Requests Offers Service Lifecycle Messaging Location / Tracking Payments Cash Reviews / Ratings KYC / Verification Notifications Admin / Moderation Analytics / Reporting Cross-cutting capabilities 

The following are cross-cutting capabilities rather than independent authoritative business-state domains:

Security Audit / Logging Correlation / Observability Validation Abuse / Rate Control 

Their detailed ownership remains with the applicable architecture gates.

Security controls are governed by AG-07.

Audit data modeling is governed by AG-04, with security/audit controls coordinated with AG-07.

API-level correlation and error behavior are governed by AG-05.

Testing architecture is governed by AG-10.

CI/CD architecture is governed by AG-11.

Production observability and operational controls are governed by AG-12.

5. Ownership Principle 

Every authoritative business entity must have one authoritative domain owner.

AG-03 defines logical ownership boundaries.

AG-04 is authoritative for the concrete data entities, relationships, lifecycle fields, constraints, and persistence model.

AG-03 must not create a second authoritative owner for an AG-04 entity.

Examples:

Concern Logical owner User identity Identity / Accounts Authentication Authentication Authorization Authorization Client profile Client Artisan profile Artisan Company profile Company Marketplace services Services / Marketplace Service Request Requests Offer Offers Service lifecycle Service Lifecycle Conversation / Message Messaging Location / Tracking Location / Tracking Electronic Payment Payments Cash settlement record Cash Review Reviews / Ratings KYC Case / verification state KYC / Verification Notification record Notifications Administrative actions Admin / Moderation Analytics projections/events Analytics / Reporting 

No cross-cutting capability may silently become the authoritative owner of an existing business entity.

6. Application Layers Interface Layer 

Responsible for:

transport request parsing serialization boundary validation authentication-context extraction API error mapping 

The Interface Layer must not contain core business decisions.

Application Layer 

Responsible for:

use cases orchestration transaction boundaries coordination between domains authorization checks at use-case boundaries invoking domain policies coordinating external effects through approved interfaces Domain Layer 

Responsible for:

business rules invariants policies lifecycle transitions domain decisions 

The Domain Layer must not directly depend on:

HTTP implementations Android UI database implementations external provider SDKs infrastructure-specific implementations Infrastructure Layer 

Responsible for implementing approved technical interfaces, including:

database access external-provider adapters storage adapters notification adapters payment adapters mapping adapters KYC/integration adapters other approved infrastructure concerns 

Infrastructure must not silently redefine domain ownership.

7. Dependency Direction 

The approved dependency direction is:

Clients | v API / Interface | v Application | v Domain ^ | Infrastructure / Adapters 

Rules:

Clients depend only on published contracts. Interface code may depend on application interfaces/use cases. Application code may coordinate domain and approved infrastructure interfaces. Domain code must not depend on infrastructure implementations. Database access must remain behind approved data-access boundaries. External providers must remain isolated behind adapters. Provider-specific SDKs must not become domain dependencies. Circular dependencies are forbidden unless explicitly approved. Cross-domain direct database writes are forbidden. Dependency changes require impact analysis. A later gate must not silently reverse an approved dependency direction. Android dependencies remain governed by AG-09. CI/CD dependencies remain governed by AG-11. Production dependencies remain governed by AG-12. 8. Domain Interaction 

Domains must communicate through explicit contracts.

Preferred order:

Explicit domain contract | v Application orchestration | +---- synchronous result | +---- event/message when asynchronous behavior is required 

Cross-domain communication must define:

owner caller input output authorization requirement transaction/consistency expectation failure behavior audit/correlation requirement where applicable 

Hidden cross-domain side effects are forbidden.

9. Database Boundary 

The database is a protected infrastructure resource.

Rules:

domain logic does not directly access database implementations; database access is performed through approved repository/data-access boundaries; cross-domain direct writes are forbidden; ownership constraints are enforced through the application/domain architecture and appropriate database constraints; migrations are governed by AG-04; production database operations are governed by AG-12. 

AG-03 does not define physical database tables.

AG-04 is authoritative for the logical data model.

10. External Integration Boundary 

External providers are isolated behind infrastructure adapters.

Potential integrations include:

maps geocoding routing electronic payment providers push notification providers email/SMS where approved secure storage identity/KYC providers other explicitly approved external services 

Each critical integration must define:

adapter boundary provider authentication input/output validation timeout behavior failure behavior retry behavior where safe idempotency where required reconciliation where applicable audit/correlation requirements secure credential handling 

AG-08 is authoritative for the external integration architecture.

11. Authorization Boundary 

Authentication establishes identity.

Authorization determines permission.

All protected operations require server-side authorization.

The system must never trust client-provided values as authoritative for:

role permission ownership administrative authority KYC approval payment success protected lifecycle state service completion 

AG-06 defines authentication and authorization architecture.

AG-07 defines the security controls protecting those mechanisms.

AG-05 defines the API contract through which these decisions are enforced.

12. Service Lifecycle Authority 

The authoritative lifecycle is:

REQUESTED -> ACCEPTED -> EN_ROUTE -> ARRIVED -> IN_PROGRESS -> COMPLETED 

Cancellation and error states are modeled explicitly.

Service Lifecycle is the authoritative owner of lifecycle transitions.

Other domains may request an approved transition but must not silently mutate lifecycle state.

The server must validate:

actor authorization current state transition eligibility domain conditions concurrency requirements 

AG-04 defines the authoritative lifecycle data representation.

AG-05 defines the API contract for lifecycle operations.

AG-06 defines authorization requirements.

AG-07 defines security protections.

AG-09 defines Android lifecycle presentation and interaction.

13. Request and Offer Flow Request Client -> Authenticate -> Discover -> Create Request -> Validate -> Persist -> Notify eligible providers -> Receive Offers -> Select Offer -> Request approved service transition Offer Provider -> Authenticate / Authorize -> Validate eligibility -> Access eligible Request -> Submit Offer -> Validate -> Persist Offer 

The server determines whether each operation is permitted.

AG-04 defines the underlying request and offer entities.

AG-05 defines their API contracts.

AG-06 defines authorization.

14. Payment Boundary 

Electronic Payments and Cash are separate concepts.

The approved logical flow is:

Payment Trigger -> Authorization -> Cash OR Approved Electronic Flow -> Validated Result -> Financial Record -> Notification where applicable -> Audit 

The client is never authoritative for electronic payment success.

Provider failure must never be interpreted as payment success.

Electronic payment confirmation must pass through the approved AG-08 integration boundary.

AG-04 owns the Payment and Cash data model.

AG-05 owns payment API contracts and idempotency requirements.

AG-07 owns payment-related security controls.

AG-08 owns provider integration and webhook processing.

15. KYC Boundary 

KYC / Verification is a protected domain.

The architecture must distinguish:

KYC submission document/reference handling review approval rejection verification state 

External KYC providers do not become authoritative owners of NIDDE roles or permissions.

KYC authorization is governed by AG-06.

KYC security is governed by AG-07.

External KYC integration is governed by AG-08.

KYC data modeling is governed by AG-04.

Android KYC interaction is governed by AG-09.

16. Messaging Boundary 

Messaging owns:

conversations messages message lifecycle where applicable 

Access requires participant authorization.

A conversation identifier alone is never sufficient authorization.

The messaging domain must not bypass AG-06 authorization or AG-07 security controls.

The API boundary is governed by AG-05.

The Android presentation boundary is governed by AG-09.

17. Location and Tracking Boundary 

Location / Tracking owns the logical handling of:

location references tracking events tracking-related business interactions 

Tracking information is operational data.

Tracking alone is not authoritative proof of:

payment completion service completion cash settlement 

Location privacy and security requirements are coordinated with AG-04, AG-07, AG-08, and AG-09.

18. Notifications Boundary 

Notifications are a supporting capability around authoritative business events.

Notification delivery is never the source of truth for:

request state service lifecycle payment state KYC approval financial settlement 

A notification failure must not automatically mutate the underlying business state.

Notification provider integration belongs to AG-08.

Notification API contracts belong to AG-05.

Android notification behavior belongs to AG-09.

19. Analytics Boundary 

Analytics / Reporting consumes approved operational information.

Analytics must not become the authoritative owner of transactional business state.

Analytics may use:

events controlled projections approved reporting views aggregated operational data 

Analytics logic must not directly mutate transactional source-of-truth records.

AG-04 defines the analytics-related data model.

Later analytics implementation must preserve all domain ownership boundaries.

20. Administrative Boundary 

Administrative and moderation operations require explicit server-side administrative authorization.

Administrative actions must be attributable and auditable.

The administrative layer must not bypass:

AG-05 API contracts AG-06 authorization AG-07 security AG-04 audit/data requirements 

An administrative UI or client must never become authoritative merely because it is hidden from normal users.

21. Security and Audit Boundary 

Security and Audit / Logging are cross-cutting capabilities.

They are not independent owners of ordinary business entities.

Security 

AG-07 owns:

security principles secret handling input/security validation abuse controls rate limiting requirements sensitive-data protection security logging security testing incident-security requirements Audit 

AG-04 owns the logical Audit Event data model.

AG-07 owns audit security requirements.

Critical operations must remain traceable.

Audit records must not contain:

credentials secrets tokens unnecessary sensitive information 22. Correlation and Observability 

Important operations should support a correlation/reference identifier where required.

Correlation identifiers must:

allow related events to be traced; remain non-sensitive; be propagated only through approved interfaces; not become authorization credentials. 

API-level correlation behavior is governed by AG-05.

Security logging is governed by AG-07.

Production observability is governed by AG-12.

Android diagnostic presentation is governed by AG-09.

23. Core Data Flows Request Flow Client -> Authentication -> Authorization -> Request API -> Application Use Case -> Domain Validation -> Persistence -> Eligible Provider Notification -> Offers -> Selection -> Lifecycle Service Flow REQUESTED -> ACCEPTED -> EN_ROUTE -> ARRIVED -> IN_PROGRESS -> COMPLETED Payment Flow Authorized Operation -> Payment Domain -> Cash OR Approved Provider Adapter -> Validated Result -> Payment State -> Audit / Notification KYC Flow KYC Submission -> Validated KYC Operation -> Approved Storage / Provider Boundary -> Validated Result -> KYC State -> Authorized Review -> Decision -> Audit 

External failures must never silently become successful internal business states.

24. Failure and Consistency Rules 

The system must distinguish at minimum:

success pending failure rejected cancelled expired 

Retry behavior must be bounded and safe.

Operations capable of producing duplicate side effects must use explicit idempotency where required.

Financial operations require particular protection against:

duplicate processing replay inconsistent state unauthorized confirmation 

External provider failures must be translated into controlled application/domain outcomes.

No failure path may silently grant authorization or create a false authoritative state.

25. Forbidden Patterns 

The following are prohibited:

client-only authorization client-controlled role assignment client-controlled ownership direct privileged database access from clients domain dependency on infrastructure implementations provider SDK dependency inside core domain logic hidden cross-domain database writes duplicated authoritative business rules across clients business logic hidden inside transport controllers unapproved circular dependencies payment success inferred from client state client-controlled KYC approval unauthorized lifecycle mutation untracked financial mutations secrets in source control analytics mutation of transactional source-of-truth records arbitrary new architecture boundaries bypassing a later gate's ownership through AG-03 26. Cross-Gate Ownership Rules 

AG-03 must remain compatible with:

AG-01 — Technology Stack 

AG-03 does not override approved technology choices.

AG-02 — Repository Structure 

AG-03 consumes the repository boundaries established by AG-02.

AG-03 does not create new top-level repository boundaries without an approved architecture change.

AG-04 — Data Model 

AG-04 is authoritative for:

entities fields relationships constraints indexes lifecycle persistence audit data model migration strategy seed strategy AG-05 — API Contract 

AG-05 is authoritative for:

API resources request/response contracts error contracts pagination filtering/sorting idempotency API versioning webhook contract requirements AG-06 — Authentication / Authorization 

AG-06 is authoritative for:

identity authentication sessions/tokens roles permissions authorization account recovery privilege boundaries AG-07 — Security Model 

AG-07 is authoritative for:

application security secrets security validation abuse prevention rate limiting security logging sensitive-data protection security testing requirements security incident controls AG-08 — External Integrations 

AG-08 is authoritative for:

external providers adapters provider authentication payments integration maps notifications storage KYC/identity providers webhooks provider retry/failure behavior reconciliation AG-09 — Android Architecture 

AG-09 is authoritative for the Android client architecture.

AG-10 — Testing Architecture 

AG-10 is authoritative for the system testing architecture.

AG-11 — CI/CD Architecture 

AG-11 is authoritative for CI/CD architecture and workflow policy.

AG-12 — Production Architecture 

AG-12 is authoritative for production topology and operational infrastructure.

AG-13 — Release Architecture 

AG-13 is authoritative for release and production-readiness architecture.

AG-03 must not silently override any of these boundaries.

27. Dependency Change Control 

Any proposed dependency change must identify:

affected component current dependency proposed dependency reason security impact data impact API impact testing impact operational impact affected architecture gates 

A dependency change that creates an architecture contradiction must block the affected implementation until the contradiction is resolved.

No silent dependency changes are permitted.

28. Implementation Boundary 

AG-03 does not authorize implementation.

The following remain locked:

APPLICATION IMPLEMENTATION = LOCKED PHYSICAL FILE COUNT = NOT YET CALCULATED 

No implementation file may be created merely because AG-03 has been written or uploaded.

The final physical-file inventory remains deferred until all required architecture gates are resolved.

29. Verification Checklist 

AG-03 may become VERIFIED only when all applicable checks pass:

system boundary defined logical layers defined domain/capability boundaries defined authoritative ownership preserved AG-02 repository boundaries respected dependency direction validated database boundary validated external integration boundary validated authorization boundary validated lifecycle authority validated payment/cash separation validated KYC boundary validated messaging boundary validated location/tracking boundary validated notification boundary validated analytics boundary validated administrative boundary validated security cross-cutting boundary validated audit ownership validated failure/idempotency rules validated AG-01 compatibility confirmed AG-04 compatibility confirmed AG-05 compatibility confirmed AG-06 compatibility confirmed AG-07 compatibility confirmed AG-08 compatibility confirmed AG-09 compatibility confirmed AG-10 compatibility confirmed AG-11 compatibility confirmed AG-12 compatibility confirmed AG-13 compatibility confirmed no unresolved blocking contradiction exists verification evidence is recorded Project Control and Manifest are updated 30. Verification Requirement 

AG-03 becomes:

VERIFIED 

only after:

static/document consistency review; AG-01 compatibility review; AG-02 repository-boundary review; domain ownership review; dependency-direction review; critical-flow review; security/authorization review; cross-gate compatibility review; evidence registration in the canonical control documents. 

Until then:

AG-03 = READY FOR VERIFICATION APPLICATION IMPLEMENTATION = LOCKED PHYSICAL FILE COUNT = NOT YET CALCULATED 31. Next Gate 

After AG-03 is formally verified:

NEXT = AG-04 — DATA MODEL 

No implementation file is authorized merely because AG-03 is uploaded.

32. Control Statement 

AG-03 establishes the logical system architecture and dependency boundaries for NIDDE.

It defines how the system is divided without creating competing ownership of business entities.

AG-04 remains authoritative for the logical data model.

AG-05 through AG-13 remain authoritative for their respective specialized architecture boundaries.

Security and Audit / Logging are treated as cross-cutting capabilities rather than independent owners of ordinary business entities.

The backend/domain boundary remains authoritative for protected business decisions.

No client, provider, analytics component, notification mechanism, or infrastructure implementation may silently redefine an approved NIDDE architecture contract.

AG-03 STATUS: READY FOR VERIFICATION

IMPLEMENTATION: LOCKED

PHYSICAL-FILE COUNT: NOT YET CALCULATED


