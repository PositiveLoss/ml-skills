import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from scripts.release_skills import package


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.output = self.root / "dist" / "skills.zip"
        self.write("README.md", "# Test skills\n")
        self.write("test-skill/SKILL.md", (
            '---\nname: test-skill\ndescription: "A test skill"\n---\n'
            '# Test\nRead [notes](references/notes.md).\n'
        ))
        self.write("test-skill/references/notes.md", "# Notes\n")
        self.write("test-skill/agents/openai.yaml", (
            'interface:\n  display_name: Test skill\n'
            '  short_description: Test packaging of standalone skills\n'
            '  default_prompt: Use $test-skill to test packaging.\n'
        ))

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_archive_preserves_resources_and_excludes_tooling_and_generated_files(self):
        self.write("test-skill/scripts/helper.py", "print('hello')\n")
        self.write("test-skill/examples/input.json", '{"value": 1}\n')
        for name in (".github/workflows/ci.yml", "scripts/tool.py", "test-skill/.DS_Store",
                     "test-skill/__pycache__/helper.pyc", "test-skill/dist/old.zip"):
            self.write(name, "excluded")
        package(self.root, self.output)
        with ZipFile(self.output) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), {
                "README.md", "test-skill/SKILL.md", "test-skill/agents/openai.yaml",
                "test-skill/references/notes.md", "test-skill/scripts/helper.py",
                "test-skill/examples/input.json",
            })
            self.assertEqual(archive.read("test-skill/examples/input.json"), b'{"value": 1}\n')

    def test_rejects_mismatched_skill_name_before_creating_archive(self):
        path = self.root / "test-skill/SKILL.md"
        path.write_text(path.read_text().replace("name: test-skill", "name: wrong"))
        with self.assertRaisesRegex(ValueError, "name must match"):
            package(self.root, self.output)
        self.assertFalse(self.output.exists())

    def test_rejects_link_to_resource_missing_from_archive(self):
        (self.root / "test-skill/references/notes.md").unlink()
        with self.assertRaisesRegex(ValueError, "link missing from package"):
            package(self.root, self.output)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
