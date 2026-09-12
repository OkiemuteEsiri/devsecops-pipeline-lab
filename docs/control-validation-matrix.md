# DevSecOps Control Validation Matrix

This matrix separates detection, remediation, revalidation, and risk acceptance so that administrative closure is not treated as proof that a technical weakness is resolved.

| Control family | Risk condition | Impact | Expected remediation evidence | Revalidation condition |
|---|---|---|---|---|
| Secrets hygiene | credential-like material committed to source | credential exposure and unauthorized access | secret removed, credential rotated where applicable, repository history reviewed | gate and dedicated secret scanner report no active exposure |
| Workflow permissions | broad write permissions granted without need | supply-chain or repository modification risk | explicit least-privilege permissions | workflow review confirms only required scopes remain |
| Trigger safety | privileged workflow executes untrusted contribution context | token or repository abuse | safer trigger or isolated trusted execution design | synthetic pull-request path executes without privileged untrusted code |
| Dependency governance | unreviewed or unpinned dependency/action change | dependency compromise or unexpected behavior | reviewed version policy, lock state, provenance/SCA evidence where available | dependency checks and policy tests pass on the remediated revision |
| Test enforcement | security/unit tests can be bypassed or omitted | insecure changes can merge undetected | required CI job and branch/ruleset enforcement | protected-path change cannot meet merge criteria without successful checks |
| Artifact integrity | build output lacks traceability or provenance | tampering and uncertain origin | SBOM/provenance/signing evidence in mature environments | artifact identity maps to reviewed source and expected build workflow |
| Finding ownership | security finding has no accountable owner | prolonged exposure and ambiguous remediation | owner, due date, remediation decision | owner and evidence remain present through closure |

## Evidence maturity

1. **Administrative evidence** — ticket/comment states that work was completed.
2. **Implementation evidence** — configuration or code change is visible.
3. **Technical validation** — automated or independent check confirms the condition is absent.
4. **Sustained validation** — subsequent builds/releases continue to enforce the control.

For recruiter-facing examples, this project targets level 3 where the repository can validate the condition locally. Production programs should pursue level 4 for material controls.

## Closure states

- `open`: condition is present and requires action.
- `remediation_in_progress`: an owner is implementing a change.
- `revalidation_pending`: implementation evidence exists but has not been technically verified.
- `validated`: the control has been re-tested successfully.
- `exception`: risk is explicitly accepted with rationale, owner, and expiry; this is not equivalent to remediation.
- `reopened`: revalidation failed or the condition recurred.

## ATT&CK context

Where software-supply-chain techniques are discussed, mappings are threat-model context only. They describe plausible adversary behavior that motivates defensive controls; they do not demonstrate compromise, attribution, or exploitation.