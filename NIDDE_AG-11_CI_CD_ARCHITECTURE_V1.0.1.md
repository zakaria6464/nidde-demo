NIDDE — AG-11 CI/CD ARCHITECTURE 

Project: NIDDE
Phase: 00 — ARCHITECTURE
Gate: AG-11 — CI/CD Architecture
Revision: V1.0.1
Status: READY FOR VERIFICATION
Implementation: LOCKED

1. Purpose 

AG-11 defines the Continuous Integration and Continuous Delivery architecture required by NIDDE before implementation.

This document is an architecture contract.

It defines source-control integration, automated validation, test execution, build verification, artifact handling, security checks, dependency checks, environment separation, workflow responsibilities, failure behavior, and CI/CD evidence.

It does not implement application source code, production infrastructure, deployment configuration, release procedures, or production operations.

2. Scope 

AG-11 owns:

CI architecture CD architecture boundaries automated validation automated test execution build verification static analysis integration dependency/security checks artifact generation requirements workflow separation environment-aware pipeline behavior protected configuration requirements CI/CD evidence failure handling quality gates integration with AG-10 testing requirements compatibility checks required before implementation/release stages 

The following remain owned by their respective gates:

AG-03 — System / Dependency Architecture AG-04 — Data Model AG-05 — API Contract AG-06 — Authentication / Authorization AG-07 — Security Model AG-08 — External Integrations AG-09 — Android Architecture AG-10 — Testing Architecture AG-12 — Production Architecture AG-13 — Release Architecture 

AG-11 must not redefine the scope of another gate.

3. CI/CD Principles 

NIDDE CI/CD follows:

reproducibility automation least privilege controlled environments immutable or traceable artifacts fail-safe behavior explicit quality gates protected secrets deterministic validation where practical separation of development, verification, production, and release responsibilities auditable pipeline activity no bypass of approved architecture contracts 

CI/CD must verify the approved architecture rather than silently redefine it.

4. Source of Truth 

CI/CD must respect:

Canonical Master File Manifest NIDDE Project Control verified architecture gates approved repository structure AG-03 system/dependency boundaries AG-04 data model AG-05 API contract AG-06 authentication/authorization AG-07 security model AG-08 external integrations AG-09 Android architecture AG-10 testing architecture 

An unverified document must not override a verified architecture contract.

If CI/CD detects an architecture contradiction, the affected workflow or implementation must not silently work around it.

5. Repository Boundary 

The repository is the controlled source boundary for project artifacts.

CI/CD must operate only on approved repository content and dependencies.

Repository automation must not:

create unauthorized architecture modify authoritative domain state bypass security controls expose secrets silently rewrite verified architecture contracts deploy unapproved artifacts 

Repository structure remains governed by the approved architecture and project-control documents.

6. Workflow Separation 

CI/CD must separate responsibilities logically.

At minimum, the architecture must distinguish:

Validation 

Checks repository and project consistency.

Testing 

Executes the test requirements defined by AG-10.

Build 

Produces controlled build artifacts after required validation.

Security 

Executes approved security/dependency checks.

Artifact 

Stores or exposes only approved generated artifacts.

Delivery 

Moves approved artifacts toward the appropriate environment according to later architecture gates.

Release 

Release authority remains owned by AG-13.

The exact workflow files and implementation mechanisms remain implementation details.

7. Pull Request and Change Validation 

Changes entering the protected development flow should pass applicable automated checks before acceptance.

Checks may include:

syntax validation formatting validation where required static analysis dependency validation unit tests component tests API contract tests integration tests Android tests security tests repository consistency checks 

A failed required check must prevent the affected quality gate from being considered successful.

8. Testing Boundary 

AG-10 owns testing architecture.

AG-11 owns automated execution of those tests within CI/CD.

AG-11 must consume the test requirements defined by AG-10.

CI/CD must support execution of applicable:

unit tests component tests API contract tests integration tests security tests Android tests lifecycle tests idempotency tests webhook tests failure tests regression tests 

AG-11 must not redefine test semantics owned by AG-10.

9. Quality Gates 

A CI/CD quality gate must fail when a required condition is not satisfied.

Quality gates may include:

source validation build success test success contract compatibility security checks dependency checks secret detection artifact integrity repository consistency 

The exact thresholds must be defined by the approved implementation/testing/security configuration.

AG-11 must not invent thresholds that contradict AG-07 or AG-10.

10. Build Verification 

Build verification must confirm that an approved project state can produce the expected application artifact.

For Android, verification must remain compatible with AG-09 and the technology decisions established by earlier architecture.

Build validation should include:

dependency resolution compilation applicable static checks test execution variant/environment validation artifact generation artifact integrity verification 

Build success alone does not constitute release approval.

11. Android CI/CD Boundary 

AG-09 owns Android architecture.

AG-11 provides CI/CD execution for the approved Android architecture.

CI/CD must support, where applicable:

Android source validation dependency resolution unit tests Android-specific tests static analysis build verification debug/test artifacts controlled release candidates 

AG-11 must not change Android package/module ownership.

AG-11 must not introduce provider-specific Android architecture.

12. API and Backend Compatibility 

CI/CD should verify compatibility with approved API contracts where appropriate.

AG-05 owns the API contract.

CI/CD may validate:

contract compatibility request/response schemas generated contract artifacts where approved client/backend compatibility version compatibility 

A CI check must not silently modify an approved API contract to make a build pass.

Breaking contract changes require the appropriate architecture/contract update before implementation proceeds.

13. Security Boundary 

AG-07 owns the security model.

AG-11 must provide CI/CD mechanisms that help enforce the approved security requirements.

Security-related CI checks should include, where applicable:

secret detection dependency vulnerability checks unsafe configuration detection insecure artifact checks static security analysis credential exposure checks prohibited-file checks 

CI/CD must never print secrets into logs.

Security checks must not expose sensitive information through failure output.

14. Secrets and Credentials 

Production secrets must never be committed to Git.

CI/CD must not require secrets to be stored in source control.

Sensitive values must be supplied through approved secret/configuration mechanisms.

The following must not appear in repository files or ordinary CI logs:

passwords private keys API secrets payment credentials webhook secrets database credentials KYC provider credentials cloud credentials authentication tokens 

.env.example may contain variable names and safe placeholders only.

15. Secret Handling in Workflows 

CI/CD workflows must:

use least-privilege credentials minimize secret exposure avoid printing secret values avoid embedding secrets in artifacts avoid persisting secrets unnecessarily revoke or rotate compromised credentials through the appropriate security/production process prevent secrets from being included in generated logs 

Secret management implementation remains coordinated with AG-07 and AG-12.

16. Dependency Management 

CI/CD must validate project dependencies against approved architecture.

Checks should consider:

dependency resolution version compatibility vulnerability status prohibited dependencies license/policy requirements where applicable reproducibility transitive dependency changes 

AG-03 owns system/dependency architecture.

AG-11 verifies dependency behavior within CI/CD but must not silently replace approved architectural dependencies.

17. External Integration Testing 

AG-08 owns external integration architecture.

CI/CD may execute controlled integration tests using:

mocks fakes provider sandboxes test credentials contract tests 

Production credentials must not be required for ordinary automated testing.

Payment, webhook, KYC, maps, notification, and storage integration tests must respect the boundaries defined by AG-08.

18. Database and Migration Validation 

Database ownership remains governed by AG-04 and the approved implementation architecture.

CI/CD may validate:

migration consistency schema compatibility migration ordering migration reproducibility test database initialization rollback behavior where explicitly required 

CI/CD must not introduce database ownership rules that conflict with AG-04.

Production migration execution remains subject to AG-12 and AG-13.

19. Artifact Architecture 

CI/CD may generate controlled artifacts such as:

Android build artifacts test reports coverage reports static-analysis reports dependency reports verification evidence approved packaged outputs 

Artifacts must be:

traceable to a source revision identifiable by build context protected from unauthorized modification where required free from secrets reproducible where practical 

An artifact must not be considered release-approved solely because it was successfully built.

20. Artifact Integrity 

Important artifacts should have integrity evidence where required.

Integrity controls may include:

checksums immutable references signed artifacts where approved source revision references build metadata 

Integrity mechanisms must not replace AG-13 release authorization.

21. Environment Separation 

CI/CD must distinguish appropriately between:

local development automated test integration/sandbox staging/pre-production production 

Production credentials must not be copied into lower environments.

Lower environments must not be treated as production.

Environment-specific configuration must remain compatible with AG-07, AG-08, AG-12, and AG-13.

22. Production Boundary 

AG-12 owns production architecture.

AG-11 provides the CI/CD mechanisms required to interact with production only within approved boundaries.

AG-11 must not define:

production infrastructure production topology production data ownership production operational procedures 

Production deployment requirements must be consumed from AG-12.

23. Release Boundary 

AG-13 owns release architecture.

AG-11 may produce release candidates and verification evidence.

AG-11 does not independently authorize production release.

A successful CI/CD pipeline means that the defined pipeline checks passed.

It does not automatically mean:

architecture is VERIFIED production is READY release is APPROVED 

Release authority remains with AG-13.

24. Failure Behavior 

CI/CD must fail safely.

When a required quality gate fails:

the affected workflow must report failure downstream dependent stages must not incorrectly report success artifacts must not be falsely marked as approved deployment/release actions must not proceed when blocked by required gates failure evidence should remain available for investigation 

A transient infrastructure failure must be distinguishable from a failed application test where practical.

25. Retry Behavior 

CI/CD retries may be used for infrastructure operations where safe.

Retries must not conceal deterministic application failures.

Test retries must not convert a failing test into a false success.

External integration retries must respect AG-08 and AG-10 requirements.

Release/deployment retries must remain subject to AG-12 and AG-13 controls.

26. Concurrency and Duplicate Execution 

CI/CD must account for duplicate or concurrent workflow execution.

Where appropriate:

obsolete runs may be cancelled protected environments must prevent unsafe concurrent deployment artifact identity must remain unambiguous release candidates must remain traceable repeated workflow execution must not create ambiguous release state 

The exact deployment concurrency policy belongs to AG-12 and AG-13.

27. Repository Security Checks 

CI/CD should detect prohibited repository content where applicable.

Examples include:

committed secrets private keys production credentials prohibited sensitive documents unexpected generated artifacts unauthorized configuration malformed architecture-control files 

Repository security checks support AG-07 but do not replace the security architecture.

28. Architecture Consistency Checks 

Where practical, CI/CD may verify architectural consistency.

Checks may include:

required canonical files exist prohibited duplicate architecture files are detected expected naming conventions are respected required status/control fields exist manifest references resolve protected files are not silently removed architecture revision references are consistent 

Such checks must validate the approved control documents rather than invent new architecture.

29. Verification Evidence 

CI/CD must preserve sufficient evidence for important verification activities.

Evidence may include:

source revision workflow result test result build result security check result dependency check result artifact identifier artifact checksum where required environment timestamp relevant failure information 

Evidence must not contain secrets or unnecessary sensitive data.

30. Observability 

CI/CD diagnostics should support troubleshooting.

Useful information may include:

workflow identifier source revision stage name test category failure category artifact identifier environment correlation/reference identifier where applicable 

Logs must not expose:

credentials authentication tokens private keys payment secrets webhook secrets KYC documents unnecessary personal information 31. Access Control 

CI/CD permissions must follow least privilege.

Different workflow stages should receive only the permissions they require.

Production-related credentials and deployment permissions must be restricted.

CI/CD must not provide broad administrative access merely for convenience.

Administrative access remains subject to AG-06 and AG-07.

Production permissions remain subject to AG-12 and AG-13.

32. Protected Branch and Approval Boundaries 

Where protected repository controls are used, they should support:

required checks controlled changes to protected branches review requirements where applicable prevention of unauthorized workflow changes controlled modification of security-sensitive configuration 

Repository governance must remain compatible with the project's approved control documents.

33. Workflow Change Security 

CI/CD workflow definitions are security-sensitive.

Changes to workflow behavior must be treated as controlled changes.

A workflow must not be allowed to:

expose secrets bypass required tests disable security checks without authorization deploy to protected environments without required approval modify release authority silently bypass architecture gates 34. Testing and CI/CD Compatibility 

AG-10 defines what must be tested.

AG-11 defines how automated testing participates in CI/CD.

Therefore:

AG-10 → Test Requirements
AG-11 → Automated Execution

Neither gate replaces the other.

Any test required by AG-10 and designated as a CI quality gate must be executed according to the approved CI/CD implementation.

35. Production and Release Compatibility 

AG-11 must remain compatible with:

AG-12 — Production Architecture 

CI/CD must consume approved production environment and deployment boundaries.

AG-13 — Release Architecture 

CI/CD must provide release candidates and evidence required by the release process.

Neither AG-12 nor AG-13 may be silently redefined by CI/CD workflows.

36. Implementation Boundary 

AG-11 defines CI/CD architecture requirements.

It does not authorize implementation by itself.

Implementation remains:

LOCKED

until the canonical architecture sequence and final readiness conditions are satisfied.

CI/CD workflow files must not be treated as architecture approval.

37. Verification Criteria 

AG-11 may become VERIFIED only when:

its scope matches the canonical AG-11 definition repository boundaries are clear AG-03 dependency ownership is preserved AG-04 data/migration ownership is preserved AG-05 API contracts are respected AG-06 authentication/authorization boundaries are preserved AG-07 security requirements are enforced through appropriate CI controls AG-08 integration boundaries are preserved AG-09 Android build requirements are supported AG-10 testing requirements are executable through CI/CD artifact handling is controlled secrets are protected environments are separated production ownership remains with AG-12 release ownership remains with AG-13 failure and retry behavior is controlled no unresolved blocking contradiction exists required verification evidence is recorded 

READY FOR VERIFICATION does not mean VERIFIED.

38. Control Statement 

AG-11 establishes the CI/CD architecture boundary for NIDDE.

CI/CD validates, tests, builds, and delivers approved project artifacts through controlled workflows.

CI/CD does not become the authority for:

domain state authentication authorization data ownership payment state KYC approval production architecture release authorization 

AG-11 must remain compatible with AG-03 through AG-10 and must provide the controlled automation boundary required by AG-12 and AG-13.

No CI/CD workflow may silently redefine an approved NIDDE architecture contract.

AG-11 STATUS: READY FOR VERIFICATION

IMPLEMENTATION: LOCKED


