import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).parents[1] / "scripts" / "security_gate.py"
spec = importlib.util.spec_from_file_location("security_gate", MODULE_PATH)
security_gate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(security_gate)


class SecurityGateTests(unittest.TestCase):
    def test_detects_private_key_header(self):
        findings = security_gate.scan_text(pathlib.Path("demo.txt"), "-----BEGIN PRIVATE KEY-----")
        self.assertTrue(any("private_key" in item for item in findings))

    def test_detects_secret_assignment(self):
        findings = security_gate.scan_text(
            pathlib.Path("config.py"),
            'api_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"',
        )
        self.assertTrue(any("generic_api_key" in item for item in findings))

    def test_benign_text_passes(self):
        findings = security_gate.scan_text(pathlib.Path("README.md"), "No credentials are stored here.")
        self.assertEqual(findings, [])

    def test_detects_risky_workflow_permission(self):
        findings = security_gate.scan_text(
            pathlib.Path(".github/workflows/demo.yml"),
            "permissions: write-all\n",
        )
        self.assertTrue(any("broad_write_permissions" in item for item in findings))


if __name__ == "__main__":
    unittest.main()
