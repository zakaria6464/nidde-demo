NIDDE — AG-10 TESTING ARCHITECTURE 

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-10 — Testing Architecture
Revision: V1.0.1
Status: READY FOR VERIFICATION
Implementation: LOCKED

1. Purpose 

AG-10 defines the testing architecture required by NIDDE before implementation.

This document is an architecture contract.

It defines the testing boundaries, test responsibilities, verification layers, contract testing requirements, security testing requirements, integration testing requirements, Android testing requirements, data and environment isolation, failure testing, and architecture verification requirements.

It does not implement test code, application source code, database migrations, CI/CD workflows, deployment configuration, or production infrastructure.

2. Scope 

AG-10 owns:

testing architecture test-layer responsibilities unit testing requirements domain and business-rule testing API contract testing integration testing external-provider integration testing webhook testing security testing requirements authorization and ownership testing payment and financial-state testing KYC testing requirements lifecycle transition testing messaging authorization testing location/tracking testing notification behavior testing Android testing structure persistence/data-access testing failure and retry testing idempotency testing regression testing test data isolation test environment requirements architecture verification evidence 

The following remain owned by their respective gates:

AG-03 — System / Dependency Architecture AG-04 — Data Model AG-05 — API Contract AG-06 — Authentication / Authorization AG-07 — Security Model AG-08 — External Integrations AG-09 — Android Architecture AG-11 — CI/CD Architecture AG-12 — Production Architecture AG-13 — Release Architecture 

AG-10 must not redefine the scope of another gate.

3. Testing Principles 

NIDDE testing follows these principles:

test server authority verify authorization server-side verify domain ownership rules verify lifecycle transitions verify API contracts verify security boundaries isolate external dependencies prevent duplicate authoritative effects protect sensitive test data reproduce failure conditions verify both successful and rejected operations maintain deterministic automated tests where practical avoid production credentials in ordinary testing preserve architecture boundaries during testing 

Testing must verify the architecture rather than silently redefining it.

A test must not be considered valid merely because an implementation makes the test pass if that implementation violates an approved architecture contract.

4. Testing Authority Boundary 

Tests do not become authoritative business components.

The following remain authoritative according to earlier gates:

AG-04 — domain model and lifecycle ownership AG-05 — API contract AG-06 — authentication and authorization rules AG-07 — security requirements AG-08 — external integration boundaries AG-09 — Android client architecture 

AG-10 verifies these contracts.

It must not replace them.

5. Test Layers 

NIDDE testing should be organized into appropriate layers.

Where applicable:

unit tests domain/business-rule tests repository/data-access tests API contract tests integration tests external-provider adapter tests webhook tests security tests Android UI/state tests end-to-end critical-flow tests 

Not every test requires the complete application stack.

Tests should use the smallest appropriate layer capable of proving the required behavior.

6. Unit Testing 

Unit tests must verify isolated components and deterministic business behavior.

Where applicable, unit tests must cover:

validation rules state-transition decisions authorization decisions ownership checks pagination behavior filtering/sorting allowlists idempotency decisions error mapping retry classification provider-result mapping notification-result handling client state mapping 

Unit tests must not assume that client-controlled values are authoritative.

7. Domain and Business-Rule Testing 

Domain tests must verify the authoritative business rules defined by AG-04 and exposed through AG-05.

Testing must cover, where applicable:

entity ownership valid entity relationships request eligibility offer eligibility duplicate active-offer prevention service lifecycle transitions cancellation rules invalid transition rejection review eligibility payment-state rules cash-transaction separation KYC state rules notification non-authority administrative restrictions 

A test must verify both permitted and prohibited behavior.

8. Service Lifecycle Testing 

The authoritative lifecycle is:

REQUESTED
→ ACCEPTED
→ EN_ROUTE
→ ARRIVED
→ IN_PROGRESS
→ COMPLETED

Cancellation and error states are explicitly supported.

Testing must verify:

every valid transition every prohibited transition unauthorized transition attempts transition attempts from incorrect current states concurrent state changes repeated transition requests lifecycle history preservation invalid lifecycle manipulation from clients 

The server must remain authoritative for lifecycle state.

A client-side test must never treat a locally assigned lifecycle state as authoritative.

9. Request and Offer Testing 

Testing must verify Service Request and Offer behavior.

For Service Requests, tests must cover:

authorized creation unauthorized creation ownership enforcement valid service/category references invalid references lifecycle restrictions protected-field validation unauthorized access to private requests 

For Offers, tests must cover:

valid request reference eligible provider authorized provider action invalid provider invalid request state invalid amount/currency where applicable duplicate prohibited active offers accepted-offer uniqueness unauthorized offer modification 10. API Contract Testing 

API tests must follow AG-05.

Testing must verify:

request schemas required fields data types allowed values validation errors authorization failures controlled error structure pagination stable ordering allowlisted filtering allowlisted sorting API versioning idempotency behavior correlation/reference identifiers where applicable 

Tests must verify that clients cannot provide arbitrary database expressions or protected authoritative values.

Breaking contract changes must be detected by tests rather than silently accepted.

11. Authentication Testing 

Authentication tests must follow AG-06 and security requirements from AG-07.

Where applicable, testing must cover:

valid authentication invalid credentials/factors expired authentication state revoked session/token invalid session/token account recovery recovery credential expiration recovery credential reuse authentication enumeration resistance authentication material protection session lifecycle behavior 

Tests must verify that syntactically valid but unauthorized authentication material cannot grant unintended access.

12. Authorization Testing 

Authorization testing is mandatory for protected operations.

Tests must verify:

role boundaries permission boundaries resource ownership participant relationships lifecycle eligibility administrative authority KYC-dependent authorization where applicable profile/context authorization unauthorized resource access horizontal privilege escalation vertical privilege escalation 

The test suite must include negative authorization cases.

A successful authentication test alone is insufficient to prove authorization correctness.

13. Security Testing 

Security testing must follow AG-07.

Where applicable, tests must cover:

authentication security authorization security ownership enforcement input validation injection protection sensitive-data exposure secret leakage unsafe error disclosure rate-limit behavior abuse controls replay protection webhook authenticity administrative authorization KYC access restrictions payment security boundaries logging safety 

Security tests must verify that protected information is not exposed through ordinary responses, logs, or error paths.

14. Input Validation Testing 

All externally supplied input must be treated as untrusted.

Testing must cover:

missing fields invalid types invalid identifiers invalid lengths numeric boundary violations invalid enum values malformed content unauthorized fields invalid ownership invalid lifecycle state invalid business conditions malicious input patterns 

Validation failures must not produce partial authoritative mutations.

15. Sensitive Data Testing 

Testing must verify data minimization.

Tests must ensure that ordinary API responses and logs do not expose:

passwords access tokens private keys provider secrets database credentials payment secrets complete KYC documents unnecessary personal information unnecessary precise location data internal infrastructure details 

Sensitive test fixtures must not contain real production secrets or unnecessary real personal information.

16. Payment Testing 

Payment testing must preserve the boundaries established by AG-05, AG-07, and AG-08.

Tests must verify that:

the client cannot declare payment success provider confirmation is required for authoritative electronic payment success payment state transitions are validated unauthorized payment operations are rejected duplicate payment effects are prevented idempotency keys behave correctly repeated requests do not create duplicate authoritative effects duplicate webhooks do not create duplicate effects invalid webhooks are rejected replayed events are rejected where required refunds/adjustments are controlled where applicable reconciliation discrepancies can be detected 

The following must fail as an authoritative payment result:

payment_status = successful

when supplied solely by the client.

17. Cash Transaction Testing 

Cash Transaction and electronic Payment must remain separate concepts.

Testing must verify:

cash records are not silently converted into electronic payment state electronic payment status does not automatically become cash settlement unauthorized cash actions are rejected cash actions follow approved authorization and lifecycle rules cash records remain auditable 18. KYC Testing 

KYC testing must follow AG-06, AG-07, and AG-08.

Tests must cover:

KYC submission KYC document/reference handling authorized KYC access unauthorized KYC access KYC review KYC approval KYC rejection duplicate or invalid operations protected KYC document exposure external provider result validation prevention of client-side KYC approval 

A client must never be able to make its own KYC approval authoritative.

19. External Integration Testing 

External integrations must be tested behind the boundaries defined by AG-08.

Testing should use:

mocks fakes contract tests integration tests failure simulations provider sandbox environments where approved 

Tests must cover:

valid provider response malformed provider response timeout unavailable provider authentication failure rate limiting temporary network failure permanent provider rejection duplicate provider event invalid webhook replayed webhook provider reconciliation mismatch 

Production provider credentials must never be required for ordinary automated tests.

20. Webhook Testing 

Webhook processing must be explicitly tested.

Tests must verify:

authenticity validation signature verification where supported timestamp validation where supported replay protection event identity idempotency payload validation safe retry behavior duplicate event handling auditability controlled failure behavior 

A webhook must not be accepted merely because it reached an exposed endpoint.

21. Idempotency and Retry Testing 

Testing must verify all operations where retries could create duplicate side effects.

Where applicable:

payment mutations payment webhook processing financial settlement non-repeatable commands lifecycle commands notification actions external-provider operations 

Tests must verify that repeated processing of the same valid idempotency key or provider event does not create duplicate authoritative effects.

Unsafe retries must be rejected or controlled.

22. Messaging Testing 

Messaging tests must verify:

conversation membership participant authorization unauthorized conversation access unauthorized message creation invalid message types invalid references oversized payload handling moderation restrictions where applicable message enumeration resistance notification recipient restrictions 

A conversation identifier alone must never provide access.

23. Location and Tracking Testing 

Location testing must respect AG-04, AG-07, AG-08, and AG-09.

Tests must verify:

permission denial handling permission revocation handling unavailable location behavior authorized tracking access unauthorized tracking access purpose limitation minimum necessary exposure secure transport expectations retention behavior where applicable protection against treating tracking as proof of payment protection against treating tracking as proof of service completion 

Background location behavior, if approved, must be separately tested.

24. Notification Testing 

Notification tests must verify:

authorized recipients notification generation duplicate notification handling where required delivery failure handling retry behavior notification state delayed notification behavior lost notification behavior 

Tests must verify that notification failure does not automatically mutate authoritative:

service state payment state KYC state financial settlement 

The backend remains authoritative.

25. Android Testing Boundary 

AG-09 defines Android-specific testing requirements.

Android testing must cover, where applicable:

UI state navigation authentication/session behavior authorization-aware presentation API client behavior request/offer flows lifecycle presentation location permissions tracking presentation notification handling payment interaction KYC presentation local persistence cache invalidation offline behavior retry behavior error handling security-sensitive client behavior lifecycle/process-death behavior 

Android tests must not treat client-side state as authoritative business state.

26. Local Storage Testing 

Persistence and cache tests must verify:

correct storage behavior cache invalidation stale-data handling offline behavior secure handling of sensitive material unauthorized local access protections where applicable recovery after process death consistency after reconnect 

Tests must verify that local storage cannot become authoritative for:

payment success KYC approval role assignment administrative privilege ownership protected lifecycle state financial settlement 27. Offline and Degraded-Network Testing 

Tests must simulate:

complete offline state intermittent connectivity timeout temporary server failure authentication expiration authorization failure validation failure permanent business rejection provider failure 

The client must not blindly replay non-repeatable operations after reconnecting.

Retry behavior must respect the API idempotency contract.

28. Concurrency Testing 

Testing must account for concurrent actors and devices.

Where applicable, tests must verify:

simultaneous offer creation simultaneous offer acceptance concurrent lifecycle transitions duplicate payment submission duplicate webhook delivery concurrent KYC actions concurrent administrative actions stale client state resource ownership changes session/permission changes during active operations 

The server must resolve authoritative conflicts according to the approved domain and API contracts.

29. Database and Persistence Testing 

Data-access tests must verify the boundaries defined by AG-04 and AG-07.

Testing must cover:

entity relationships ownership constraints required fields valid references invalid references transaction integrity rollback behavior duplicate prevention migration compatibility where applicable protected access boundaries 

Tests must verify that unauthorized components cannot directly mutate protected domain state.

30. Error and Failure Testing 

The system must be tested for controlled failure.

Tests should cover:

malformed requests authorization failures authentication failures unavailable dependencies database failures provider failures timeout duplicate events invalid state transitions invalid external responses unexpected but controlled domain conditions 

Failure handling must not create false successful business state.

31. Test Data Isolation 

Testing environments must be isolated from production data.

Test data must:

be synthetic where practical avoid unnecessary personal information never contain production secrets use dedicated credentials use controlled fixtures be reproducible where practical be disposable where appropriate 

Production data must not be copied into ordinary development or automated test environments without an explicitly approved security process.

32. Test Environment Boundaries 

Test environments must preserve the same architectural boundaries as the application.

Testing must not bypass:

API authorization domain ownership payment integration boundaries KYC boundaries security controls Android/backend boundaries 

Test-only shortcuts must not be allowed to become production architecture.

33. Test Doubles and External Providers 

Mocks, fakes, and stubs may be used to isolate dependencies.

They must preserve the relevant contract.

A mock must not falsely guarantee behavior that the real integration cannot provide.

Critical provider behavior must also be covered by appropriate contract or integration testing.

34. Critical End-to-End Flows 

The testing architecture must support end-to-end verification of critical paths.

Client 

Registration
→ Login
→ Search
→ Request
→ Receive Offers
→ Select
→ Service
→ Payment
→ Review

Artisan 

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

Company 

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

Admin 

Only where an approved administrative interface exists:

Login
→ Administrative Authentication
→ Authorized Management
→ Orders
→ KYC
→ Payments
→ Complaints/Moderation
→ Logs
→ Analytics

Every critical flow must verify both successful and prohibited paths.

35. Regression Testing 

Regression testing must protect previously verified architecture contracts.

Regression coverage must include, where applicable:

API contract compatibility authorization boundaries ownership rules lifecycle semantics payment authority KYC authority security controls integration boundaries Android/backend compatibility idempotency error contracts 

A new implementation must not silently invalidate an earlier approved gate.

36. Architecture Contract Testing 

The test suite should provide automated evidence that implementation remains compatible with approved architecture.

Where applicable, architecture checks should verify:

forbidden dependencies forbidden direct database access forbidden provider coupling API contract compatibility package/module boundaries secret-handling rules unauthorized state mutation paths prohibited client authority assumptions 

Architecture tests must fail when implementation crosses an approved boundary.

37. Test Coverage Principles 

Coverage must be risk-based rather than based only on a numeric percentage.

Highest-priority coverage includes:

authentication authorization ownership lifecycle transitions payment operations KYC authorization webhook processing idempotency sensitive-data handling administrative operations external integration failures Android security-sensitive behavior 

A high coverage percentage does not compensate for missing critical security or business-rule tests.

38. Test Evidence 

Verification evidence should identify:

test scope test environment test version relevant architecture gate test results failed tests resolved failures known limitations contract verification evidence security verification evidence where applicable 

Evidence must be traceable to the architecture requirement being verified.

39. CI/CD Boundary 

AG-11 owns CI/CD architecture.

AG-10 defines the testing requirements that CI/CD must execute or enforce.

These may include:

automated unit tests domain tests contract tests integration tests security tests Android tests architecture checks regression tests 

AG-10 must not define the CI/CD implementation itself.

40. Production Boundary 

AG-12 owns production architecture.

AG-10 defines testing requirements that production readiness must satisfy, including where applicable:

production-like integration verification migration verification backup/recovery testing monitoring-related validation security validation critical-flow verification 

Production testing must not use unsafe shortcuts that bypass production security boundaries.

41. Release Boundary 

AG-13 owns release architecture.

AG-10 provides test evidence required for release readiness.

A release must not be considered technically ready when required critical tests remain unresolved.

AG-10 does not define release approval authority.

42. Cross-Gate Consistency 

AG-10 must remain consistent with:

AG-03:

system boundaries dependency ownership service responsibilities 

AG-04:

entities relationships ownership lifecycle location payment cash transactions KYC notifications 

AG-05:

API contracts validation errors pagination idempotency versioning webhook-related requirements 

AG-06:

identity authentication roles permissions ownership session requirements administrative authorization 

AG-07:

security controls sensitive data secrets abuse controls logging audit requirements secure failure behavior 

AG-08:

provider boundaries payment integrations maps notifications KYC secure storage webhook handling retries reconciliation 

AG-09:

Android architecture client authority boundary local storage offline behavior permissions location notifications payment interaction Android testing 

AG-10 must not introduce a contradiction with any approved earlier gate.

43. Verification Criteria 

AG-10 may become VERIFIED only when:

its scope matches the canonical AG-10 definition testing responsibilities are clearly separated from implementation domain tests align with AG-04 API tests align with AG-05 authentication and authorization tests align with AG-06 security tests align with AG-07 external integration tests align with AG-08 Android testing aligns with AG-09 lifecycle testing preserves AG-04 authority payment testing preserves server authority KYC testing preserves server authority webhook testing preserves integration security idempotency and retry behavior are tested sensitive test data is protected test environments remain isolated CI/CD requirements remain compatible with AG-11 production requirements remain compatible with AG-12 release requirements remain compatible with AG-13 no unresolved blocking contradiction exists required verification evidence is recorded 

READY FOR VERIFICATION does not mean VERIFIED.

44. Implementation Lock 

AG-10 does not authorize implementation.

Implementation remains:

LOCKED

until the complete canonical architecture sequence and final readiness conditions are satisfied.

No production application, backend, Android, database, CI/CD, or infrastructure implementation should be created solely because AG-10 has been written.

45. Control Statement 

AG-10 establishes the testing architecture boundary for NIDDE.

Testing exists to verify that implementation conforms to the approved architecture and domain contracts.

Testing must preserve backend authority for identity, authorization, ownership, lifecycle, payments, KYC, financial state, and other protected business decisions.

Testing must preserve the external integration boundaries defined by AG-08 and the Android client boundary defined by AG-09.

AG-10 must remain compatible with AG-03 through AG-09 and provide the testing requirements consumed by AG-11 through AG-13.

No test-only shortcut may silently redefine an approved architecture contract.

AG-10 STATUS: READY FOR VERIFICATION

IMPLEMENTATION: LOCKED


