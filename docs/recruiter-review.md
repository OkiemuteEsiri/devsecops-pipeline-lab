# Recruiter Review Guide

This repository demonstrates a defensive DevSecOps control pattern for integrating lightweight policy checks into CI/CD without using production credentials or external infrastructure.

## Five-minute review path

1. Read `README.md` for the problem statement, architecture, and security boundaries.
2. Inspect `scripts/security_gate.py` to see how repository and workflow policy is evaluated.
3. Review `tests/test_security_gate.py` for positive, negative, and workflow-policy test cases.
4. Read `docs/pipeline-controls.md` and `docs/control-validation-matrix.md` for control rationale, remediation, and revalidation expectations.
5. Inspect `.github/workflows/security.yml` to confirm least-privilege workflow permissions and automated validation.

## Capability-to-evidence map

| Capability | Evidence |
|---|---|
| DevSecOps policy-as-code | `scripts/security_gate.py` |
| Secret exposure prevention | high-confidence synthetic secret-pattern checks |
| CI workflow hardening | workflow-risk checks plus read-only GitHub Actions permissions |
| Security testing | `tests/test_security_gate.py` |
| Control governance | `docs/pipeline-controls.md` |
| Remediation and revalidation | `docs/control-validation-matrix.md` |
| Automated enforcement | `.github/workflows/security.yml` |

## Engineering questions this project addresses

- Which security controls should fail a build versus create follow-up work?
- How can policy checks remain deterministic and explainable?
- How should false positives and tool limitations be documented?
- What evidence is required before a pipeline security finding can be considered remediated?
- How can CI permissions be minimized so security tooling does not itself expand the attack surface?

## Scope and limitations

The project is intentionally offline and synthetic. It does not claim to replace enterprise SAST, SCA, secret scanning, artifact signing, provenance, container scanning, or cloud-native policy engines. It demonstrates control design, validation logic, secure CI integration, and remediation governance.