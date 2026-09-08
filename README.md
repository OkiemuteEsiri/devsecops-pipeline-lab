# DevSecOps Pipeline Lab

A defensive software-supply-chain project showing how security controls can be integrated into CI without exposing secrets or depending on production infrastructure.

## Controls demonstrated

- Dependency hygiene and lock-file expectations
- Secret-pattern detection for accidental credential commits
- Static policy checks for dangerous workflow settings
- Test execution before merge
- Least-privilege GitHub Actions permissions
- Reproducible security validation using only repository content

## Repository structure

```text
.github/workflows/security.yml   CI security workflow
scripts/security_gate.py         lightweight policy/security checks
tests/test_security_gate.py      unit tests for the gate
docs/pipeline-controls.md        control rationale and remediation guidance
```

## Security gate

The included gate scans text files for high-confidence secret-like patterns and checks workflow files for risky constructs such as broad write permissions or use of pull_request_target without an explicit justification. It intentionally avoids pretending to replace mature SAST, SCA, secret-scanning, or container-scanning products.

## CI design

The sample workflow uses read-only repository permissions, checks out code, runs the security gate, and executes tests. A production pipeline should additionally pin third-party actions by immutable commit SHA, enforce branch protection, require reviewed dependency updates, generate an SBOM, verify provenance, and route findings to an owned remediation workflow.

## Risk model

Pipeline findings are classified by potential impact:

- **Critical:** exposed production credential or untrusted code executing with sensitive write/token permissions
- **High:** broad workflow permissions, unpinned high-risk actions, or exploitable dependency findings
- **Medium:** missing hardening controls or weak dependency governance
- **Low:** maintainability and hygiene gaps

## Scope

This repository is for defensive DevSecOps and software-supply-chain security demonstration. It uses synthetic examples and does not contain real credentials, proprietary code, or production deployment configuration.