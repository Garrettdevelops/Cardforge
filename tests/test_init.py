import pytest
from click.testing import CliRunner
from flashcard.cli.main import cli
from flashcard.core.importer import initalize_storage

def test_init(tmp_path):
    runner = CliRunner()

    csv_file = tmp_path / "study.csv"
    csv_file.write_text("question,correct_answer\nhi,hello")

    result = runner.invoke(cli, ["init", str(csv_file)])
    assert result.exit_code == 0
    json_file = tmp_path / "study.json"

    assert json_file.exists()
