# Methodology

## Objective

Demonstrate how small, deterministic security controls can be integrated into a CI/CD workflow while preserving least privilege, explainability, and repeatable validation.

## Assessment flow

1. **Inventory the pipeline trust boundaries**: source, workflow definitions, dependencies, tokens, build environment, and artifacts.
2. **Classify controls**: preventive, detective, or validation controls.
3. **Run deterministic repository checks**: inspect supported text files and workflow definitions for configured policy violations.
4. **Execute unit tests**: validate expected detections and benign cases.
5. **Fail closed for configured high-confidence violations**: the gate returns a non-zero exit code when a configured policy violation is present.
6. **Remediate at the source**: remove the insecure condition rather than suppressing evidence without justification.
7. **Revalidate on the exact revised commit**: repeat the gate and unit tests before claiming closure.

## Trust boundaries

The repository models four principal trust boundaries:

- contributor-controlled source changes;
- CI workflow definitions and triggers;
- GitHub token permissions available to a workflow;
- third-party dependencies/actions used during validation.

The sample workflow intentionally uses `contents: read`. A production design should additionally consider immutable action pinning, environment protections, provenance, artifact signing, SBOM generation, dependency review, and protected merge requirements.

## Severity model

- **Critical**: credible exposure of a production secret or execution of untrusted code with highly privileged credentials.
- **High**: broad write permissions, unsafe privileged triggers, or materially exploitable dependency conditions.
- **Medium**: missing hardening controls, weak governance, or incomplete validation coverage.
- **Low**: hygiene and maintainability issues with limited direct security impact.

Severity is contextual; this repository does not claim that pattern presence alone proves exploitability.

## Validation principles

- Prefer reproducible automated evidence over administrative statements.
- Keep policy checks explainable enough for engineers to remediate.
- Separate technical remediation from risk acceptance.
- Do not claim CI success without checking the exact commit.
- Treat scanner/gate coverage as bounded by the configured patterns and file types.

## Safety

All examples are synthetic. The project contains no real credentials, proprietary source, offensive payloads, or production deployment targets.