NIDDE — SECURITY POLICY 

Project: NIDDE
Security Authority: AG-07 — Security Model
Architecture Baseline: AG-01 → AG-13
Status: ACTIVE
Implementation: CONTROLLED

1. Purpose 

This document defines the repository-level security rules for NIDDE.

It complements AG-07 and does not replace the detailed security architecture.

All application, infrastructure, CI/CD, Android, database, and integration changes must preserve the security boundaries established by AG-07.

2. Security Principles 

NIDDE follows:

server authority least privilege defense in depth secure-by-default behavior explicit trust boundaries minimum necessary data exposure secure secret management controlled authentication explicit authorization auditable sensitive operations safe failure behavior dependency and integration isolation 3. Trust Model 

The Android and other client applications are untrusted clients.

External providers are untrusted dependencies.

The backend/domain boundary remains authoritative for protected NIDDE business state.

The following must never be trusted solely because they originate from a client:

role permission ownership KYC status payment status service lifecycle administrative authority financial settlement service completion 4. Secrets 

The following must never be committed to Git:

passwords API keys access tokens refresh tokens JWT signing secrets private keys certificates containing private material database credentials payment credentials webhook secrets provider secret keys production credentials encryption keys 

Use approved secret-management mechanisms.

.env.example may contain only variable names and safe example values.

5. Environment Files 

Real environment files must not be committed.

Forbidden examples include:

.env .env.local .env.production .env.prod 

unless a specific file contains no secrets and is explicitly approved.

The preferred repository artifact is:

.env.example 

with safe placeholders only.

6. Authentication 

Authentication must follow AG-06.

Security-sensitive authentication material must:

use approved storage never appear in ordinary logs never be exposed through error messages never be hard-coded into source code be invalidated or rotated according to the approved authentication architecture 

Authentication proves identity.

Authentication does not automatically grant authorization.

7. Authorization 

Every protected operation must be authorized server-side.

Authorization must consider the applicable:

identity role permission ownership resource state lifecycle state administrative privilege 

Client-side checks may improve user experience but must never replace server authorization.

8. Role and Permission Protection 

The following are forbidden:

client_role = admin permission = * is_admin = true kyc_approved = true payment_success = true service_completed = true 

as client-supplied values that are accepted as authoritative without server validation.

Roles and permissions remain server-controlled.

9. Sensitive Data 

Sensitive personal and business data must be minimized.

Do not store, transmit, display, or log more information than required.

Sensitive information may include:

authentication material identity information KYC information payment information precise location private messages administrative information personal contact information security credentials 

Retention and access must follow the applicable architecture gates.

10. KYC Security 

KYC information is sensitive.

The system must:

restrict KYC access protect KYC transmission minimize local storage avoid unnecessary duplication avoid unrestricted document exposure validate provider results preserve server authority over KYC decisions 

An external KYC provider must not automatically become the authority for NIDDE permissions or roles.

11. Payment Security 

Payment operations must remain server-authoritative.

The client must not establish payment success.

The controlled authority chain is:

Client → Approved API → NIDDE Backend → AG-08 Payment Integration → Validated Provider Result → Server Payment State 

Payment webhooks must be authenticated and validated according to AG-08.

Sensitive payment credentials must remain outside the client application and repository.

12. Cash Security 

Cash settlement is separate from electronic payment.

Cash-related records must remain:

server-controlled auditable access-controlled validated against the applicable service and actor 

A client must not independently establish authoritative cash settlement.

13. Location Security 

Location information is sensitive.

The system must apply:

minimum necessary collection purpose limitation secure transport restricted access appropriate retention controlled presentation 

Location data must not independently prove:

service completion payment completion cash settlement 

Android location permissions remain governed by AG-09.

14. API Security 

All protected API operations must enforce:

authentication where required authorization input validation output validation resource ownership checks lifecycle validation rate/abuse controls where applicable idempotency where required safe error responses 

The API must not expose internal implementation details unnecessarily.

15. Input and Output Handling 

All external input must be treated as untrusted.

Validate:

type format size allowed values ownership authorization lifecycle compatibility 

Do not trust:

client-generated identifiers client-generated roles client-generated permissions client-generated payment status client-generated KYC status client-generated lifecycle state 

External provider responses must also be validated.

16. Error Handling 

Production errors must not expose:

passwords tokens private keys secrets SQL statements stack traces containing sensitive information internal infrastructure details provider credentials unnecessary personal information 

User-facing errors should be safe and understandable.

Internal diagnostic information must remain controlled.

17. Logging 

Logs must support troubleshooting and security investigation without unnecessarily exposing sensitive data.

Never log:

passwords access tokens refresh tokens private keys payment secrets webhook secrets provider secret credentials complete KYC documents unnecessary sensitive personal information 

Where appropriate, logs may contain:

operation type timestamp application/service version non-sensitive error category correlation/reference identifier request outcome 18. Correlation and Auditability 

Security-sensitive operations should remain traceable through controlled identifiers where appropriate.

Examples include:

request/reference identifiers payment references KYC references audit identifiers operation identifiers 

Identifiers must not be treated as authorization credentials.

19. External Integrations 

External providers are untrusted.

Provider integrations must:

protect credentials validate responses authenticate webhooks prevent replay where applicable use appropriate timeouts retry only when safe respect idempotency isolate provider-specific logic prevent provider state from becoming uncontrolled NIDDE state 

AG-08 remains the primary integration boundary.

20. Android Security 

Android is an untrusted client.

The Android application must:

protect session material use secure transport avoid hard-coded production secrets minimize local sensitive data avoid exposing sensitive information through logs handle session expiration safely respect server authorization avoid treating local state as authoritative 

AG-09 defines the Android architecture boundary.

21. Database Security 

Database access must remain controlled by the backend and approved infrastructure boundaries.

Client applications must never have unrestricted direct database authority.

Database credentials must never be embedded in client applications.

Production database access must be restricted and auditable.

22. CI/CD Security 

CI/CD must follow AG-11.

Pipelines must not expose secrets through:

logs artifacts source files pull-request output generated reports 

Production deployment credentials must use approved secret-management mechanisms.

CI/CD must not bypass required security checks.

23. Production Security 

Production security remains governed by AG-12.

Production environments must protect:

secrets databases application services infrastructure administrative access monitoring backups deployment credentials 

Production access must follow least privilege.

24. Release Security 

Release requirements remain governed by AG-13.

Before release, the project must verify:

required security checks passed no known blocking security issue remains secrets are not included in artifacts production configuration is controlled release artifacts are traceable rollback procedures are available where required 25. Dependency Security 

Dependencies must be:

identified reviewed version-controlled compatible with the architecture monitored for known security issues where appropriate 

Do not introduce dependencies solely to bypass an architecture boundary.

Provider SDKs must remain isolated where required by AG-08.

26. Vulnerability Reporting 

Security vulnerabilities should not be disclosed publicly before they are assessed and addressed.

When reporting a suspected vulnerability, provide:

affected component affected version or commit reproduction information where safe security impact relevant logs or evidence without secrets suggested mitigation if known 

Do not include passwords, tokens, private keys, or production credentials in a vulnerability report.

27. Security Incident Handling 

If a serious security issue is discovered:

Stop the affected implementation or deployment. Protect affected credentials and data. Determine the affected boundary. Assess the scope. Rotate compromised secrets where applicable. Preserve appropriate evidence. Patch the underlying issue. Re-run security and regression checks. Update the relevant architecture/security documentation. Resume normal operation only after the issue is controlled. 28. Repository Security Checklist 

Before committing:

[ ] No passwords [ ] No API keys [ ] No access tokens [ ] No private keys [ ] No payment secrets [ ] No webhook secrets [ ] No provider secret keys [ ] No production credentials [ ] No real .env file [ ] No KYC documents [ ] No production database dump [ ] No unnecessary sensitive personal data [ ] No secrets embedded in Android source [ ] No secrets exposed through CI/CD output 29. Security Change Control 

Any change affecting:

authentication authorization roles permissions secrets encryption sensitive data payment security KYC security location security external integrations API security logging production access CI/CD credentials 

must be evaluated against AG-07 and all affected architecture gates.

No security boundary may be weakened through an undocumented implementation workaround.

30. Final Security Statement 

Security is a cross-cutting requirement across the entire NIDDE architecture.

AG-07 is the primary security authority.

All other architecture gates and implementation components must preserve its requirements.

The repository must remain free of production secrets and sensitive production data.

The backend remains authoritative for protected business decisions.

NIDDE SECURITY POLICY — ACTIVE

SECURITY AUTHORITY: AG-07

ARCHITECTURE BASELINE: AG-01 → AG-13

IMPLEMENTATION: CONTROLLED

