NIDDE — FINAL ARCHITECTURE BASELINE 

Project: NIDDE
Phase: 00 — ARCHITECTURE
Revision: V1.0.0
Status: READY FOR VERIFICATION
Implementation: CONTROLLED

1. Purpose 

This document provides the final cross-gate architecture baseline for NIDDE.

It consolidates the approved architectural boundaries established by AG-01 through AG-13.

This document is a cross-gate reference.

It does not replace, modify, or override any individual architecture gate.

The individual AG documents remain authoritative for their respective responsibilities.

2. Architecture Sequence 

The canonical architecture sequence is:

AG-01 — Technology Stack AG-02 — Repository / System Architecture AG-03 — System Dependency Architecture AG-04 — Data Model Architecture AG-05 — API Contract Architecture AG-06 — Authentication / Authorization Architecture AG-07 — Security Model AG-08 — External Integrations Architecture AG-09 — Android Architecture AG-10 — Testing Architecture AG-11 — CI/CD Architecture AG-12 — Production Architecture AG-13 — Release Architecture 

No additional architecture gate is introduced by this document.

3. Authority Model 

NIDDE follows a server-authoritative architecture.

The backend/domain boundary remains authoritative for protected business decisions.

The client must never become authoritative for:

identity roles permissions ownership administrative authority KYC approval payment success financial settlement protected service lifecycle state service completion 

Client-side validation exists for usability and early feedback only.

It does not replace backend validation or authorization.

4. System Boundary 

NIDDE is organized around controlled boundaries between:

Client Applications ↓ Approved API Boundary ↓ Backend / Domain Services ↓ Data Persistence ↓ Approved External Integrations 

Supporting architecture includes:

Testing CI/CD Production Release Security Observability 

Each boundary is governed by its owning architecture gate.

5. Repository Authority 

Repository structure and canonical document identity are governed by the Master File Manifest.

The repository must maintain:

one active canonical architecture document per AG explicit status for superseded documents controlled repository boundaries clear ownership of implementation files traceable dependencies protected secrets physical-file verification 

A planned file must not be treated as physically present until verified against the repository.

6. Domain Authority 

The approved NIDDE domain includes, where applicable:

clients artisans companies administrators service requests offers service lifecycle messaging location/tracking payments cash transactions KYC notifications reviews complaints/moderation administrative operations 

The authoritative domain model is governed by AG-04.

This document does not redefine entity fields, relationships, constraints, or migrations.

7. API Boundary 

All client-to-backend communication must use approved API contracts.

AG-05 governs:

endpoints request structures response structures validation errors pagination filtering versioning idempotency API compatibility 

Clients must not bypass the API boundary to access database internals or private backend implementation details.

8. Authentication and Authorization 

AG-06 governs authentication and authorization.

The system must distinguish:

authenticated identity active profile/context roles permissions ownership authorization decisions 

Authorization must be enforced server-side.

The Android application and other clients must not manufacture or locally elevate privileges.

Administrative or owner-level operations require server-authorized credentials and permissions.

No administrative secret or owner credential may be embedded in source code or committed to Git.

9. Security Boundary 

AG-07 governs security requirements.

The system must protect:

authentication material session material private keys payment secrets webhook secrets provider credentials KYC information sensitive personal information production credentials infrastructure credentials 

The repository must not contain real production secrets.

Security controls must remain effective across:

development testing CI/CD production release 10. External Integrations 

AG-08 governs external integrations.

External providers may include, where approved:

payments maps/location notifications KYC storage communication providers 

Provider-specific logic must remain behind controlled integration boundaries.

External provider results do not automatically become authoritative NIDDE state.

The backend validates and applies provider results according to the approved contracts.

Provider credentials must remain outside source-controlled code.

11. Android Architecture 

AG-09 defines the Android architecture.

Android is an untrusted client.

Android responsibilities include:

presentation user interaction approved API requests server-state presentation local controlled caching approved location presentation notifications payment-flow initiation KYC presentation client-side error handling 

Android must not independently decide:

payment success KYC approval ownership role assignment protected lifecycle transitions financial settlement 

Local state must never become authoritative domain state.

12. Service Lifecycle 

The authoritative service lifecycle is:

REQUESTED ↓ ACCEPTED ↓ EN_ROUTE ↓ ARRIVED ↓ IN_PROGRESS ↓ COMPLETED 

Cancellation and error states are supported according to the domain and API contracts.

Clients may request valid transitions.

The backend determines whether a requested transition is authorized and valid.

Concurrent state changes must be handled safely.

13. Payments 

Payment authority remains server-side.

The approved authority chain is:

Client ↓ Approved API Operation ↓ NIDDE Backend ↓ Approved Payment Integration ↓ Validated Provider Result ↓ Server Payment State 

The client must never treat a locally supplied success value as authoritative payment confirmation.

Payment operations must respect approved idempotency requirements.

Cash settlement remains a separate domain concept and must also remain server-authoritative.

14. KYC 

KYC workflows are controlled by AG-06, AG-07, and AG-08 according to responsibility.

The client may:

initiate KYC collect approved information capture/select approved documents submit approved references display KYC status 

The client must not:

approve KYC fabricate approval expose unrestricted KYC information store sensitive documents unnecessarily 

KYC decisions remain server-authoritative.

15. Location and Tracking 

Location functionality must follow least privilege and purpose limitation.

The system must account for:

permission granted permission denied permission revoked unavailable location degraded location approved background access where explicitly required 

Location information must not independently prove:

payment service completion cash settlement 

Sensitive location data must be minimized and protected.

16. Messaging 

Messaging must use server-authorized conversations.

The backend remains responsible for:

participant authorization conversation membership message permissions lifecycle restrictions validation moderation rules 

A conversation identifier alone is never authorization.

The client displays only server-authorized conversations and messages.

17. Notifications 

Notifications are informational delivery mechanisms.

They may communicate:

service updates offers messages payments KYC status administrative events 

A notification must never independently change authoritative:

service state payment state KYC state financial settlement 

When notification delivery is delayed, duplicated, or lost, the client must retrieve authoritative state from the backend when necessary.

18. Local Storage and Offline Behavior 

Local persistence is limited to approved use cases.

Permitted examples include:

non-sensitive preferences controlled cache approved UI state approved offline information securely protected session material where required 

Local storage must never become authoritative for:

payment success KYC approval ownership roles administrative privilege protected lifecycle state 

Offline operations must respect API idempotency.

Non-repeatable operations must not be blindly replayed after reconnecting.

19. Error Handling 

Errors must be represented safely across the system.

Clients must not expose:

stack traces SQL errors tokens passwords private keys provider credentials payment secrets internal infrastructure details unrestricted KYC information 

Where approved, correlation/reference identifiers may be displayed for support.

Internal diagnostic information remains subject to AG-07 and observability requirements.

20. Testing 

AG-10 governs testing architecture.

The architecture must support testing of:

domain behavior API contracts authentication authorization lifecycle payments KYC location messaging notifications Android behavior persistence offline behavior security-sensitive behavior integration boundaries failure scenarios 

Production credentials must never be required for ordinary automated testing.

21. CI/CD 

AG-11 governs CI/CD architecture.

CI/CD must preserve:

architecture boundaries security requirements controlled configuration test execution artifact integrity secret protection environment separation controlled deployment 

CI/CD secrets must be supplied through the approved CI/CD secret mechanism.

Secrets must not be committed to the repository.

22. Production 

AG-12 governs production architecture.

Production must maintain appropriate separation between:

application runtime data persistence external integrations secrets observability operational controls 

Production configuration must not be copied into source-controlled example files.

Production authority remains server-side.

23. Release 

AG-13 governs release architecture.

Release processes must preserve:

artifact integrity version traceability environment separation controlled configuration rollback/recovery requirements release authorization security requirements 

A release must not silently introduce an architecture-breaking change.

24. Cross-Gate Compatibility 

The following dependency direction must remain valid:

AG-01 ↓ AG-02 ↓ AG-03 ↓ AG-04 ↓ AG-05 ↓ AG-06 ↓ AG-07 ↓ AG-08 ↓ AG-09 ↓ AG-10 ↓ AG-11 ↓ AG-12 ↓ AG-13 

This sequence represents architecture progression.

It does not mean that every implementation component may directly depend on every previous gate.

Implementation dependencies must follow the boundaries defined by the individual gates.

25. Conflict Resolution 

If this baseline conflicts with an individual architecture gate:

Identify the conflicting requirement. Determine the owning gate. Treat the owning verified gate as authoritative for that responsibility. Resolve the cross-gate contradiction through controlled review. Update this baseline only after the authoritative decision is established. 

This document must never silently override an individual gate.

26. Repository Security Baseline 

The repository must not contain:

production credentials private keys payment secrets webhook secrets provider secret keys real authentication secrets KYC identity documents production database dumps sensitive production exports unapproved personal-data dumps 

.env.example may contain only safe placeholders and documentation.

Real environment configuration remains outside the repository.

27. Implementation Readiness 

Architecture completion does not by itself authorize unrestricted implementation.

Before implementation begins, the following must be verified:

[ ] AG-01 through AG-13 are uniquely identified [ ] Active architecture documents are unambiguous [ ] Superseded documents are clearly marked [ ] Master File Manifest is canonical [ ] Project control document is consistent [ ] Repository structure is verified [ ] Physical-file inventory is completed [ ] Dependency ownership is reviewed [ ] Security restrictions are enforced [ ] .gitignore is present [ ] .env.example contains no real secrets [ ] Cross-gate consistency is verified [ ] Implementation sequence is approved 28. Implementation Sequence 

The controlled implementation sequence is:

Architecture Baseline ↓ Physical File Inventory ↓ Dependency Graph ↓ Backend Foundation ↓ Database Foundation ↓ Authentication / Authorization ↓ Marketplace Foundation ↓ Requests / Offers ↓ Service Lifecycle ↓ Messaging ↓ Location / Tracking ↓ Payments / Cash ↓ KYC ↓ Notifications ↓ Reviews ↓ Administration ↓ Android Integration ↓ Testing ↓ CI/CD ↓ Production ↓ Release 

Each stage must satisfy its applicable architecture requirements.

29. Document Authority 

This document is a final cross-gate baseline and reference.

It is not:

a replacement for AG-01 through AG-13 an implementation specification a backend API specification a database migration specification a security secrets store a deployment configuration a production configuration a release artifact 

Individual architecture gates remain authoritative for their defined responsibilities.

30. Control Statement 

NIDDE maintains one coherent architecture baseline across AG-01 through AG-13.

The architecture preserves:

server authority explicit ownership controlled dependencies secure client boundaries protected external integrations controlled payments controlled KYC controlled location controlled notifications testability CI/CD separation production separation release control 

No client-side behavior may silently redefine an approved architecture contract.

No cross-gate contradiction may be resolved through an undocumented workaround.

NIDDE FINAL ARCHITECTURE BASELINE — ACTIVE

STATUS: READY FOR VERIFICATION

IMPLEMENTATION: CONTROLLED

ARCHITECTURE BASELINE: AG-01 → AG-13


