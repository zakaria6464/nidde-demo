NIDDE — CONTRIBUTING GUIDE 

Project: NIDDE
Architecture Baseline: AG-01 → AG-13
Mode: STRICT
Implementation Status: CONTROLLED

1. Purpose 

This document defines the contribution rules for the NIDDE repository.

All contributions must preserve the approved architecture, repository boundaries, security requirements, testing requirements, and release controls.

Contributors must not introduce changes that silently redefine an approved architecture decision.

2. Before Making Changes 

Before modifying the repository:

Review README.md. Review NIDDE_PROJECT_CONTROL.md. Review NIDDE_MASTER_FILE_MANIFEST_V2.0.3_FIXED-2.md. Review NIDDE_ARCHITECTURE_ALIGNMENT_CONTROL_V1.0.1.md. Identify the architecture gate affected by the change. Confirm that the requested change does not contradict an approved gate. Check the existing repository structure before creating new files. 3. Architecture Gates 

NIDDE uses the following architecture sequence:

AG-01 — Technology Stack AG-02 — Repository / System Architecture AG-03 — System Dependency Architecture AG-04 — Data Model AG-05 — API Contract Architecture AG-06 — Authentication / Authorization Architecture AG-07 — Security Model AG-08 — External Integrations Architecture AG-09 — Android Architecture AG-10 — Testing Architecture AG-11 — CI/CD Architecture AG-12 — Production Architecture AG-13 — Release Architecture 

A change must be evaluated against the gate that owns the affected decision.

4. Repository Boundaries 

Approved implementation boundaries are:

backend/ database/ shared/ android/ admin/ tests/ docs/ infrastructure/ 

GitHub-native configuration belongs under:

.github/ 

Do not introduce unrelated top-level directories without controlled approval.

5. Ownership Rules 

Contributors must respect component ownership.

Backend 

Owns server-side business logic, authorization enforcement, lifecycle enforcement, and authoritative domain operations.

Database 

Owns database schema and migration artifacts.

Android 

Owns Android presentation and client-side interaction.

Android is an untrusted client.

Admin 

Owns approved administrative interface implementation.

Administrative authority remains server-controlled.

Tests 

Owns repository-level testing assets that are not exclusively owned by another implementation boundary.

Infrastructure 

Owns production and infrastructure implementation.

Shared 

Contains only genuinely shared contracts or approved shared artifacts.

6. Server Authority 

Client applications must never become authoritative for:

roles permissions ownership administrative authority KYC approval payment success service completion protected lifecycle state financial settlement 

The backend/domain boundary remains authoritative.

7. API Rules 

Backend communication must use approved API contracts.

Changes affecting:

endpoints request structures response structures error structures authentication requirements authorization behavior pagination idempotency versioning 

must be evaluated against AG-05 and the affected gates.

Do not introduce undocumented client/server contracts.

8. Authentication and Authorization 

Authentication and authorization changes must remain compatible with AG-06.

Contributors must not:

bypass authorization trust client-provided roles create local administrative authority expose authentication secrets treat possession of a token as permanent authorization 

Security requirements remain governed by AG-07.

9. External Integrations 

External providers are untrusted dependencies.

Provider-specific code must remain behind approved integration boundaries.

Do not place provider-specific business logic directly inside:

domain models UI components unrelated modules shared contracts 

Payment, maps, notification, storage, and KYC integrations must remain compatible with AG-08.

10. Android Rules 

Android implementation must follow AG-09.

The Android application must:

consume approved APIs respect server authorization handle authentication/session expiration protect local sensitive data respect Android permissions handle offline/degraded states prevent duplicate non-repeatable operations display server-authoritative state 

Android must not independently decide authoritative business outcomes.

11. Data Model Rules 

Changes affecting entities, relationships, ownership, lifecycle, payments, KYC, location, messaging, or notifications must be evaluated against AG-04.

Do not modify the data model only to make an implementation shortcut possible.

Database changes must remain compatible with the approved domain model and API contracts.

12. Security Rules 

Security is mandatory.

Never commit:

passwords API keys private keys payment secrets webhook secrets provider credentials database credentials production credentials real .env files KYC documents production database dumps sensitive user-data exports 

Use safe configuration mechanisms.

.env.example may contain variable names and safe placeholders only.

13. Sensitive Data 

Sensitive data must be minimized.

Do not unnecessarily:

duplicate sensitive data log sensitive data store sensitive data locally expose provider responses wholesale include credentials in source code expose KYC documents through unrestricted paths 

Follow AG-07 and AG-08 requirements.

14. Payment Safety 

Electronic payment success must be established through the server-authoritative payment flow.

The following pattern is prohibited:

client → payment_success = true → server accepts payment as successful 

The approved authority chain is:

client → approved API → NIDDE backend → AG-08 payment integration → validated provider result → server payment state 

Payment retries must respect idempotency requirements.

15. Lifecycle Safety 

The authoritative service lifecycle is:

REQUESTED → ACCEPTED → EN_ROUTE → ARRIVED → IN_PROGRESS → COMPLETED 

Cancellation and error states are explicitly controlled.

Clients may request an allowed transition but may not assign an arbitrary authoritative state.

16. Testing Requirements 

Changes must include appropriate tests.

Depending on the change, this may include:

unit tests integration tests API contract tests security tests Android tests failure simulations webhook tests end-to-end tests 

Testing architecture is governed by AG-10.

Real production credentials must never be required for ordinary automated tests.

17. CI/CD 

CI/CD changes must remain compatible with AG-11.

Contributors must not bypass required:

tests security validation build validation artifact validation deployment controls 

GitHub workflows belong under:

.github/workflows/ 18. Production 

Production-related changes must remain compatible with AG-12.

Do not commit production secrets or uncontrolled production configuration.

Production changes must preserve:

security observability database integrity backup/recovery requirements deployment safety access control 19. Release 

Release-related changes must remain compatible with AG-13.

A successful build alone does not constitute release readiness.

Required release evidence must be available before an approved release.

20. File Creation Rules 

Before creating a new file:

Check whether the file already exists. Check whether an equivalent file already exists. Identify the owning repository boundary. Identify the architecture gate that authorizes the file. Confirm that the file does not duplicate an active canonical document. Add the file only when its purpose is clear. 

Do not create duplicate architecture documents.

21. Change Management 

If a change appears to conflict with an architecture gate:

Stop the affected implementation. Identify the exact conflict. Identify the owning gate. Resolve the architecture decision. Update the appropriate documentation. Re-check cross-gate alignment. Continue implementation only after the conflict is resolved. 

Do not solve architecture conflicts through hidden client-side or implementation workarounds.

22. Commit Guidelines 

Commits should be:

focused traceable understandable limited in scope free of secrets consistent with the architecture baseline 

Avoid combining unrelated architecture and implementation changes in one commit.

Commit messages should describe the actual change.

23. Pull Request Requirements 

A pull request should identify:

what changed why it changed affected architecture gate(s) affected repository boundary tests performed security implications migration implications where applicable API compatibility implications where applicable 

If the change modifies an architecture contract, the affected architecture documentation must be updated through controlled change.

24. Review Checklist 

Before requesting review:

[ ] Architecture compatibility checked [ ] Repository boundary checked [ ] No duplicate canonical file created [ ] API compatibility checked [ ] Authentication/authorization impact checked [ ] Security impact checked [ ] External integration impact checked [ ] Android impact checked where applicable [ ] Tests added or updated [ ] No secrets committed [ ] No sensitive production data committed [ ] CI/CD impact checked [ ] Production/release impact checked where applicable 25. Definition of Acceptable Contribution 

A contribution is acceptable only when it:

has a clear purpose respects repository ownership preserves server authority follows the applicable architecture gate does not introduce forbidden secrets does not create unauthorized dependencies does not silently redefine business rules includes appropriate validation remains compatible with the architecture alignment control 26. Final Rule 

When in doubt, do not introduce a silent workaround.

Stop the affected implementation, identify the responsible architecture gate, resolve the decision through controlled change, and then continue.

NIDDE CONTRIBUTION CONTROL — ACTIVE

ARCHITECTURE BASELINE: AG-01 → AG-13

IMPLEMENTATION: CONTROLLED

