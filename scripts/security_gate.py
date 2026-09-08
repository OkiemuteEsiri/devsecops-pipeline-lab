from __future__ import annotations

import re
import sys
from pathlib import Path

SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "generic_api_key": re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{24,}['\"]"),
}

RISKY_WORKFLOW_PATTERNS = {
    "broad_write_permissions": re.compile(r"permissions:\s*write-all"),
    "pull_request_target": re.compile(r"\bpull_request_target\b"),
}

TEXT_SUFFIXES = {".py", ".md", ".yml", ".yaml", ".json", ".txt", ".toml", ".ini"}


def scan_text(path: Path, text: str) -> list[str]:
    findings: list[str] = []
    for name, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            findings.append(f"{path}: secret-pattern:{name}")

    if path.suffix in {".yml", ".yaml"} and ".github/workflows" in path.as_posix():
        for name, pattern in RISKY_WORKFLOW_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{path}: workflow-risk:{name}")
    return findings


def scan_repository(root: Path) -> list[str]:
    findings: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        findings.extend(scan_text(path.relative_to(root), text))
    return findings


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    findings = scan_repository(root.resolve())
    if findings:
        print("Security gate failed:")
        for item in findings:
            print(f"- {item}")
        raise SystemExit(1)
    print("Security gate passed: no configured policy violations detected.")


if __name__ == "__main__":
    main()
