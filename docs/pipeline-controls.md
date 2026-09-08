# Pipeline Security Controls

## 1. Least-privilege workflow token

**Risk:** Broad repository write permissions increase impact if a workflow, dependency, or third-party action is compromised.

**Control:** Default the workflow token to `contents: read` and grant job-specific write permissions only when required.

**Validation:** Inspect generated workflow permissions and reject `write-all` unless an approved exception exists.

## 2. Secret exposure prevention

**Risk:** Committed credentials can be harvested from repository history and abused outside the CI environment.

**Control:** Scan commits and pull requests for high-confidence secret patterns, use repository/environment secret stores, and rotate any credential that is exposed.

**Validation:** Test the scanner with synthetic key-like material; never use a real secret for testing.

## 3. Dependency governance

**Risk:** Vulnerable or malicious dependencies can introduce exploitable code or supply-chain compromise.

**Control:** Pin direct dependencies, review transitive dependency changes, run SCA, and maintain an SBOM for releasable artifacts.

**Validation:** Fail builds on policy-defined exploitable findings rather than raw vulnerability count alone.

## 4. Third-party action integrity

**Risk:** Mutable action tags can change after review.

**Control:** In higher-assurance pipelines, pin third-party actions to reviewed immutable commit SHAs and use an allowlist for approved publishers.

## 5. Untrusted pull-request execution

**Risk:** Workflows triggered with elevated permissions on untrusted fork content may expose secrets or permit repository modification.

**Control:** Prefer `pull_request` for untrusted contributions. Treat `pull_request_target` as high risk and require explicit architectural justification and strict checkout controls.

## 6. Remediation ownership

Every failed security gate should have an owning team, severity, remediation target, documented exception path, and retest evidence. Exceptions should expire automatically rather than becoming permanent bypasses.
