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
        marker = "-----BEGIN " + "PRIVATE KEY-----"
        findings = security_gate.scan_text(pathlib.Path("demo.txt"), marker)
        self.assertTrue(any("private_key" in item for item in findings))

    def test_detects_secret_assignment(self):
        key_name = "api" + "_key"
        synthetic_value = "A" * 32
        sample = f'{key_name} = "{synthetic_value}"'
        findings = security_gate.scan_text(pathlib.Path("config.py"), sample)
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
