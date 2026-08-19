NIDDE — FINAL ARCHITECTURE BASELINE 

Project: NIDDE
Phase: 00 — ARCHITECTURE
Mode: STRICT
Revision: V1.0.0
Status: LOCKED AS CROSS-GATE REFERENCE
Implementation: LOCKED

1. PURPOSE 

This document defines the final cross-gate architecture baseline for NIDDE.

It is a consistency and control reference.

It does not replace, override, or merge AG-01 through AG-13.

Each architecture gate remains authoritative within its own defined scope.

The purpose of this document is to ensure that the complete NIDDE architecture remains coherent across system boundaries, data, API, authentication, security, integrations, Android, testing, CI/CD, production, and release.

2. CANONICAL ARCHITECTURE SEQUENCE 

The canonical architecture sequence is:

AG-01 — Technology Stack AG-02 — Repository / System Architecture AG-03 — System / Dependency Architecture AG-04 — Data Model Architecture AG-05 — API Contract Architecture AG-06 — Authentication / Authorization Architecture AG-07 — Security Model AG-08 — External Integrations Architecture AG-09 — Android Architecture AG-10 — Testing Architecture AG-11 — CI/CD Architecture AG-12 — Production Architecture AG-13 — Release Architecture 

No gate may silently redefine another gate.

Architecture progression does not mean that every implementation component may directly depend on every previous gate.

3. AUTHORITY OWNERSHIP Gate Authority AG-01 Technology decisions AG-02 Repository and system boundaries AG-03 System and dependency architecture AG-04 Domain and data model AG-05 Public API contract AG-06 Authentication and authorization AG-07 Security model AG-08 External integrations AG-09 Android architecture AG-10 Testing architecture AG-11 CI/CD architecture AG-12 Production architecture AG-13 Release architecture and release authority 4. MASTER AUTHORITY MODEL 

NIDDE follows a server-authoritative architecture.

The backend/domain boundary is authoritative for protected business state, including:

identity authentication context authorization roles permissions ownership service lifecycle payment state cash settlement records KYC state and decisions administrative authority protected business decisions financial state 

The following are never independent authorities for protected NIDDE business state:

Android/client UI state local cache local database state notifications external provider responses locally stored role or permission flags client-submitted business status 

Client-side validation exists for usability and early feedback only.

Client-side validation never replaces backend validation or authorization.

5. SYSTEM BOUNDARY 

The principal system boundary is:

Client Applications ↓ Approved API Boundary ↓ Backend / Domain Services ↓ Approved Data Persistence ↓ Approved External Integration Boundaries 

Supporting architecture includes:

security testing CI/CD production infrastructure observability backup and recovery release controls 

No infrastructure, client, provider, test fixture, or deployment mechanism may silently become a second business authority.

6. REPOSITORY BOUNDARY 

The canonical repository root is:

NIDDE/ 

Approved top-level boundaries are:

README.md NIDDE_PROJECT_CONTROL.md NIDDE_MASTER_FILE_MANIFEST.md .gitignore .env.example .github/workflows/ backend/ database/ shared/ android/ admin/ tests/ docs/ infrastructure/ 

Responsibilities:

backend/ — server application, domain logic, API boundaries, authorization enforcement and runtime concerns. database/ — schemas, migrations, seeds and database-specific artifacts. shared/ — genuinely shared contracts and approved cross-client artifacts. android/ — Android application and Android-specific architecture. admin/ — approved administrative interface artifacts; authority remains server-controlled. tests/ — repository-level testing assets. docs/ — architecture, decisions and verification evidence. infrastructure/ — deployment, production infrastructure, monitoring, backups, recovery and infrastructure validation. .github/ — GitHub-native repository configuration and workflows only. 

No unrelated top-level boundary may be introduced without controlled review.

7. MASTER FILE CONTROL 

The Master File Manifest remains the canonical control document for:

repository file identity architecture-document uniqueness ownership repository structure implementation traceability 

Only one active canonical document may represent each architecture gate.

Superseded documents must be explicitly marked:

STATUS: SUPERSEDED 

A planned file must never be considered physically present until verified against the actual repository.

Every implementation file must be traceable to:

repository boundary owning component architecture responsibility known dependencies implementation purpose applicable tests implementation status 

Generated artifacts must remain distinguishable from canonical source documents and must not contain secrets.

8. SOURCE-OF-TRUTH ORDER 

When documents conflict, the following authority order applies:

Canonical Master File Manifest NIDDE Project Control Verified architecture-gate documents Verified repository implementation state Unverified drafts and historical copies 

A lower-priority document must never silently override a higher-priority control document.

If a conflict is discovered:

Stop the affected implementation. Identify the exact conflicting requirement or file. Identify the owning gate. Determine whether the conflict is architectural or repository/document drift. Correct the owning artifact. Update the alignment/control document when required. Re-run consistency checks. Resume only after the conflict is resolved. 

No silent workaround is permitted.

9. CORE DOMAIN 

The architecture preserves separate concepts for:

Clients Artisans Companies Administrators Service Categories Services Service Requests Offers Location Tracking Events Conversations Messages Payments Cash Transactions Reviews KYC Cases KYC Document References Notifications Administrative / Moderation Records Audit Records Analytics / Reporting 

Separate domain concepts must not be silently merged for implementation convenience.

10. SERVICE LIFECYCLE 

The authoritative service lifecycle is:

REQUESTED ↓ ACCEPTED ↓ EN_ROUTE ↓ ARRIVED ↓ IN_PROGRESS ↓ COMPLETED 

Cancellation and error states are explicitly controlled by the applicable architecture contracts.

Clients may request transitions.

The backend determines whether a transition is:

valid authorized permitted by lifecycle state compatible with concurrent state eligible for execution 

Clients must never assign arbitrary authoritative lifecycle state.

Concurrent and stale-client operations must be handled safely.

Lifecycle history remains server-authoritative.

11. REQUESTS AND OFFERS 

Service Requests and Offers remain server-authoritative.

The backend determines:

request validity actor authorization ownership provider eligibility lifecycle compatibility offer validity duplicate active-offer prevention offer acceptance allowed state transitions 

Offer acceptance must remain uniquely controlled per Service Request according to the approved data/API contracts.

Clients may submit commands but cannot independently establish protected request or offer state.

12. PAYMENT AUTHORITY 

Electronic Payment remains separate from Cash Transaction.

The authoritative electronic payment chain is:

Android / Client ↓ Approved API ↓ NIDDE Backend ↓ AG-08 Payment Integration ↓ Validated Provider Result ↓ Server-side Payment State 

A client-provided value such as:

payment_status = successful 

is never authoritative proof of payment.

External provider identifiers remain external references.

NIDDE internal identifiers remain authoritative inside NIDDE.

Financial operations must respect the approved idempotency contract.

Duplicate requests, retries, webhook replays, and repeated provider events must not create duplicate authoritative financial effects.

13. CASH TRANSACTIONS 

Cash settlement is a separate domain concept.

Cash Transactions must remain:

server-authoritative auditable ownership-controlled lifecycle-compatible protected against duplicate effects 

Electronic Payment logic must not silently become Cash Transaction logic.

Client-submitted cash state is not authoritative unless the approved backend contract explicitly authorizes and validates the operation.

14. KYC AUTHORITY 

The KYC authority chain is:

Client / Admin ↓ Approved API ↓ NIDDE KYC State ↓ Approved KYC Integration ↓ Validated Provider Result ↓ Authorized NIDDE Decision 

External KYC providers do not automatically control:

NIDDE roles NIDDE permissions account authorization administrative authority 

The client may initiate approved KYC workflows and display approved status.

The client must not approve KYC or fabricate KYC approval.

Sensitive KYC documents and references remain subject to AG-07 and AG-08.

15. LOCATION AND TRACKING 

Location and tracking are sensitive application capabilities.

They must follow:

least privilege purpose limitation minimization secure transport restricted exposure controlled retention 

Location/tracking information must never independently prove:

payment completion service completion cash settlement 

Tracking remains subject to AG-04, AG-07, AG-08 and AG-09.

16. MESSAGING 

Messaging is server-authorized.

The backend remains authoritative for:

conversation membership participant authorization message permissions content/reference validation lifecycle restrictions moderation restrictions 

A conversation identifier alone is never authorization.

Unauthorized conversations and messages must not be exposed to clients.

17. NOTIFICATIONS 

Notifications are delivery mechanisms, not authoritative business state.

A notification may communicate:

service updates offers payment information messages KYC updates administrative information where authorized 

A delayed, duplicated, lost, rejected, or failed notification must never independently change:

service state payment state KYC state financial settlement administrative authority 

When required, the client retrieves authoritative state from the backend.

18. ANDROID BOUNDARY 

Android is an untrusted client.

Android may:

present marketplace functionality collect user input consume approved APIs display server-authoritative state initiate approved operations handle authentication/session interaction present KYC workflows present location/tracking information initiate approved payment flows present notifications provide offline/degraded-network behavior 

Android must not:

manufacture roles manufacture permissions bypass backend authorization establish payment success establish KYC approval establish service completion establish cash settlement become an authoritative source of lifecycle state bypass AG-08 provider boundaries 

Protected screens being hidden from navigation does not constitute security.

Backend authorization remains mandatory.

19. API BOUNDARY 

All backend communication must use the approved API boundary defined by AG-05.

Clients must respect:

request structures response structures validation rules authentication requirements authorization requirements pagination filtering sorting error structures idempotency versioning correlation/reference identifiers where applicable 

Clients must not:

construct arbitrary database queries bypass approved APIs invent undocumented fields invent undocumented states silently redefine API semantics 

Breaking API changes require an approved AG-05 change.

20. EXTERNAL INTEGRATION BOUNDARY 

AG-08 owns external integrations.

Provider-specific functionality must remain behind approved integration boundaries.

External provider outputs are not automatically NIDDE business truth.

Provider results must be:

validated authenticated where required mapped into approved NIDDE states protected against replay protected against duplication handled safely on failure 

Production provider credentials must never be required for ordinary automated tests.

21. SECURITY BASELINE 

AG-07 owns the security model.

All implementation and infrastructure must preserve:

least privilege secure transport secure authentication/session handling protected secrets minimal sensitive local storage controlled logging controlled administrative access abuse protection safe failure auditability where required 

The following must never be committed to Git:

passwords API secrets access tokens private keys payment credentials webhook secrets database credentials KYC provider credentials cloud/service credentials production credentials real .env files KYC documents production database dumps 

No secret may be exposed through ordinary CI/CD output or release artifacts.

22. LOCAL STORAGE AND CACHE 

Local storage may support:

non-sensitive preferences controlled caches appropriate UI state approved offline data secure session material where required 

Local storage must never become authoritative for:

roles permissions ownership payment success KYC approval administrative privilege protected lifecycle state 

Cached state requires explicit invalidation and refresh behavior.

Logout and session changes must clear or invalidate applicable sensitive state.

23. OFFLINE AND FAILURE BEHAVIOR 

The system must distinguish between:

offline state timeout temporary server failure authentication expiration authorization failure validation failure permanent business rejection provider failure 

Reconnect behavior must not blindly replay non-repeatable operations.

Side-effect-producing operations must respect approved idempotency requirements.

Failure must never be converted into false success.

24. TESTING BASELINE 

AG-10 owns testing architecture.

Testing must verify approved architecture rather than redefine it.

Required coverage includes, where applicable:

unit behavior component behavior API contracts authentication authorization ownership lifecycle transitions concurrent state changes payment cash transactions idempotency webhook processing KYC messaging notifications location/tracking Android behavior local persistence cache invalidation offline behavior degraded connectivity failure and recovery security-sensitive client behavior regression behavior 

Negative authorization cases are mandatory for protected operations.

Tests never become production authority.

25. CI/CD BASELINE 

AG-11 owns CI/CD architecture.

CI/CD may perform:

repository validation static analysis dependency checks automated tests security checks contract checks build verification artifact generation controlled deployment execution 

CI/CD must preserve:

reproducibility least privilege protected secrets traceable artifacts environment separation auditable activity fail-safe quality gates 

CI/CD success does not equal:

architecture verification production readiness release approval 26. PRODUCTION BASELINE 

AG-12 owns production architecture.

Production must provide controlled boundaries for:

public ingress backend runtime protected data services secure storage external integrations administrative access observability backup and recovery 

Production must preserve:

secure transport least privilege restricted data-service access secret management monitoring alerting logging safety backups restoration testing recovery capability environment separation failure isolation controlled scaling 

Production infrastructure must never become an independent business authority.

27. RELEASE BASELINE 

AG-13 owns release architecture and release authority.

The authority distinction is:

AG-10 → Testing Architecture AG-11 → CI/CD Execution AG-12 → Production Environment AG-13 → Release Architecture / Release Authority 

The following never equal release authorization:

successful tests successful build generated artifact successful CI/CD pipeline successful deployment application startup 

Release approval must be explicit and evidence-based.

28. RELEASE TRACEABILITY 

Every release must identify, where applicable:

release version application version backend version source revision branch/tag build identifier artifact identifier environment configuration reference dependency state release timestamp release authority verification evidence 

Unknown or untraceable artifacts must not be released.

An artifact materially changed after approval requires reassessment.

29. RELEASE BLOCKING CONDITIONS 

Release approval must be blocked when applicable if:

a required architecture gate is unresolved a blocking security issue exists a blocking test failure exists an artifact is not traceable required production configuration is missing required secrets are unavailable or unsafe API compatibility is unresolved data compatibility is unresolved critical integration readiness is unresolved rollback/recovery capability is inadequate for the release risk required approval evidence is missing a known blocking architecture contradiction exists 

Exceptions must be:

explicit justified risk-assessed approved documented traceable 

Critical security and data-integrity requirements must not be silently bypassed.

30. ROLLBACK AND RECOVERY 

Production-impacting releases require an appropriate rollback or recovery strategy.

The strategy must consider:

application rollback configuration rollback database compatibility migrations external integration state Android compatibility payment state financial state data integrity 

Irreversible financial or domain events must never be blindly reversed.

Where rollback is unsafe, controlled forward recovery must be used.

31. POST-RELEASE VERIFICATION 

Post-release verification must use safe and controlled checks.

Verification may cover:

service health API availability authentication authorization database health critical application flows payment integration webhook processing KYC operations notifications Android connectivity monitoring alerting 

Unexpected critical behavior may trigger rollback or controlled recovery according to AG-12 and AG-13.

32. CRITICAL USER FLOWS Client Registration → Login → Search → Request → Receive Offers → Select → Service → Payment → Review Artisan Registration → KYC → Approval → Online → Receive Request → Offer → Accept → Execute → Complete → Payout Company Registration → KYC → Approval → Provider Operations → Receive Request → Offer → Accept → Execute → Complete → Payout Admin 

Only where an approved administrative interface exists:

Login → Administrative Authentication → Authorized Management → Orders → KYC → Payments → Complaints / Moderation → Logs → Analytics 

Administrative authority remains server-controlled.

33. IMPLEMENTATION SEQUENCE 

The controlled implementation sequence is:

Architecture Baseline ↓ Physical File Inventory ↓ Dependency Graph ↓ Backend Foundation ↓ Database Foundation ↓ Authentication / Authorization ↓ Marketplace Foundation ↓ Requests / Offers ↓ Service Lifecycle ↓ Messaging ↓ Location / Tracking ↓ Payments / Cash ↓ KYC ↓ Notifications ↓ Reviews ↓ Administration ↓ Android Integration ↓ Testing ↓ CI/CD ↓ Production ↓ Release 

No implementation stage may silently bypass an architectural dependency.

34. STATUS SAFETY 

The following meanings are mandatory:

DRAFT = document under development READY FOR VERIFICATION = prepared for consistency and verification review VERIFIED = passed the required formal verification LOCKED = relevant decision cannot change without formal change control 

Therefore:

READY FOR VERIFICATION != VERIFIED 

The existence of this baseline does not convert any gate from READY FOR VERIFICATION to VERIFIED.

35. CURRENT CONTROL STATE 

The supplied control reference records:

Project: NIDDE Phase: 00 — ARCHITECTURE Mode: STRICT Architecture baseline: AG-01 → AG-13 Implementation: CONTROLLED / LOCKED Physical-file inventory: NOT YET LOCKED / NOT YET CALCULATED 

The supplied verification point records:

AG-02 = VERIFIED Verified architecture gates = 2 Verified implementation files = 0 Next architecture item = AG-03 

Later supplied AG-03 through AG-13 architecture materials remain:

READY FOR VERIFICATION IMPLEMENTATION: LOCKED 

unless a separate formal verification record states otherwise.

36. READINESS CONDITIONS 

Before implementation proceeds, the project must establish:

AG-01 through AG-13 uniquely identified one active canonical document per gate superseded documents clearly marked Master File Manifest canonical Project Control consistent repository structure verified physical-file inventory completed dependency ownership reviewed security restrictions enforced .gitignore present .env.example contains no real secrets cross-gate consistency verified implementation sequence approved rollback/recovery requirements defined post-release verification defined required verification evidence recorded 37. NON-NEGOTIABLE ARCHITECTURE RULES Backend/domain remains authoritative. Clients remain untrusted. External providers remain isolated and untrusted. No client-side authorization bypass is permitted. No silent API-contract changes are permitted. No silent data-model changes are permitted. No silent lifecycle changes are permitted. No unauthorized dependency changes are permitted. No secrets may be committed to Git. Provider-specific business logic must remain behind approved integration boundaries. Financial operations require server authority and approved idempotency. KYC approval requires server-authorized state. Notifications never become business-state authority. Location/tracking never proves payment, service completion, or cash settlement. Cash Transactions remain separate from electronic Payment. Tests never become production authority. CI/CD success never equals release approval. Deployment success never equals release approval. Release authority belongs to AG-13. No implementation shortcut may silently redefine an approved architecture contract. 38. FINAL CONTROL STATEMENT 

This document is the final cross-gate consistency baseline for NIDDE.

It does not replace the canonical architecture gates.

The authority chain remains:

AG-01 → Technology AG-02 → Repository / System AG-03 → System / Dependencies AG-04 → Data Model AG-05 → API Contract AG-06 → Authentication / Authorization AG-07 → Security AG-08 → External Integrations AG-09 → Android AG-10 → Testing AG-11 → CI/CD AG-12 → Production AG-13 → Release / Release Authority 

No lower-priority artifact may silently override a higher-priority authoritative document.

No client-side state, provider response, infrastructure state, test state, CI/CD result, deployment result, or application UI state may silently replace the approved NIDDE authority model.

Architecture completion does not automatically authorize unrestricted implementation.

Implementation remains locked until the required architecture verification, physical-file baseline, dependency/control conditions, and final readiness requirements are satisfied.

NIDDE — ARCHITECTURE FIRST. SERVER AUTHORITY. CONTROLLED IMPLEMENTATION.

STATUS: LOCKED AS CROSS-GATE REFERENCE
IMPLEMENTATION: LOCKED

