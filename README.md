# DevSecOps Pipeline Lab

A defensive software-supply-chain security project showing how security policy, validation, and least-privilege CI controls can be integrated into a delivery pipeline without production credentials or external infrastructure.

## Recruiter quick review

For a focused technical review:

1. `scripts/security_gate.py` — policy-as-code implementation.
2. `tests/test_security_gate.py` — unit validation of detections and benign cases.
3. `.github/workflows/security.yml` — least-privilege CI enforcement.
4. `docs/methodology.md` — architecture, trust boundaries, severity, and validation principles.
5. `docs/control-validation-matrix.md` — remediation and revalidation evidence model.
6. `docs/recruiter-review.md` — capability-to-evidence map and review questions.

## Problem statement

Modern delivery pipelines can become security-critical execution environments. Excessive token permissions, unsafe workflow triggers, leaked credentials, weak dependency governance, and unenforced security tests can turn CI/CD into a supply-chain risk multiplier.

This lab demonstrates a small, transparent control layer designed around three principles: **fail on configured high-confidence violations, preserve least privilege, and require technical revalidation before closure**.

## Architecture

```text
Repository change
      |
      v
GitHub Actions (contents: read)
      |
      +--> security_gate.py
      |      +--> secret-pattern checks
      |      +--> workflow policy checks
      |
      +--> unittest suite
      |
      v
Pass / fail evidence for the exact commit
      |
      v
Remediation -> revalidation -> validated closure
```

## Recruiter signal at a glance

| Capability | Evidence in this repository |
|---|---|
| DevSecOps / policy-as-code | deterministic Python security gate |
| CI/CD security engineering | least-privilege GitHub Actions workflow |
| Secrets hygiene | high-confidence synthetic secret-pattern checks |
| Workflow hardening | checks for broad write permissions and risky trigger usage |
| Security testing | repeatable unit tests |
| Risk communication | documented severity and control rationale |
| Remediation governance | evidence-based closure and revalidation model |
| Secure design | explicit trust boundaries, scope, and limitations |

## Controls demonstrated

- Dependency hygiene and lock-file expectations.
- Secret-pattern detection for accidental credential commits.
- Static policy checks for dangerous workflow settings.
- Test execution before merge.
- Least-privilege GitHub Actions permissions.
- Reproducible security validation using only repository content.
- Evidence-based remediation and revalidation expectations.

## Repository structure

```text
.github/workflows/security.yml      CI security workflow
scripts/security_gate.py            lightweight policy/security checks
tests/test_security_gate.py         unit tests for the gate
docs/pipeline-controls.md           control rationale and remediation guidance
docs/methodology.md                 architecture, trust boundaries, validation method
docs/control-validation-matrix.md   remediation/revalidation evidence model
docs/recruiter-review.md            recruiter-focused review path
```

## Security gate

The included gate scans supported text files for high-confidence secret-like patterns and checks workflow files for configured risky constructs such as broad write permissions or `pull_request_target` usage. A configured violation produces a non-zero exit code so the pipeline fails closed.

The gate is intentionally narrow and explainable. It does **not** pretend to replace mature SAST, SCA, secret-scanning, container-scanning, artifact-signing, provenance, or cloud-native policy products.

## CI design

The sample workflow uses read-only repository permissions, checks out the repository, runs the security gate, and executes tests. A mature production pipeline should additionally consider:

- immutable commit pinning for third-party actions;
- protected branches/rulesets and required reviews;
- dependency review and SCA;
- SBOM generation;
- build provenance and artifact signing;
- container/IaC scanning where relevant;
- environment protection and scoped deployment credentials;
- owned finding-routing and exception workflows.

CI status should be interpreted **per exact commit**. Historical successful runs are not evidence that a later revision is green.

## Risk model

- **Critical:** exposed production credential or untrusted code executing with highly privileged credentials.
- **High:** broad workflow permissions, unsafe privileged triggers, or materially exploitable dependency findings.
- **Medium:** missing hardening controls, weak governance, or incomplete validation coverage.
- **Low:** hygiene and maintainability gaps with limited direct impact.

Pattern presence alone does not prove exploitability. Severity requires context.

## Remediation and revalidation

A security finding is not considered technically closed merely because a ticket is marked complete. The preferred lifecycle is:

`open -> remediation_in_progress -> revalidation_pending -> validated`

If revalidation fails or the condition recurs, the finding is reopened. Risk acceptance is tracked separately as an exception with an accountable owner and expiry; it is not presented as remediation.

See `docs/control-validation-matrix.md` for expected evidence by control family.

## ATT&CK context

Where software-supply-chain ATT&CK techniques are referenced in supporting documentation, they are used only as defensive threat-model context. A mapping does not demonstrate compromise, exploitation, or attribution.

## Design limitations

- Pattern-based secret detection can produce false positives and false negatives.
- Only configured file types and workflow patterns are evaluated.
- The project does not query live dependency, vulnerability, or cloud services.
- CI policy coverage is illustrative rather than enterprise-complete.
- Production effectiveness depends on branch protection, repository governance, identity controls, and the wider software-delivery architecture.

## Scope and safety

This repository is a defensive DevSecOps and software-supply-chain security demonstration. It uses synthetic examples only and contains no real credentials, proprietary code, confidential employer/client information, offensive payloads, or production deployment targets.

## Roadmap

- Add structured finding output for downstream reporting.
- Add synthetic dependency-policy fixtures and validation tests.
- Demonstrate SBOM/provenance verification using non-sensitive fixtures.
- Add an example exception record with expiry and revalidation criteria.
- Expand policy tests while keeping checks deterministic and explainable.