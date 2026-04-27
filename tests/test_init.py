import pytest
from click.testing import CliRunner
from flashcard.cli.main import cli

def test_init(tmp_path):
    runner = CliRunner()

    csv_file = tmp_path / "study.csv"
    csv_file.write_text("question,correct_answer\nhi,hello")

    result = runner.invoke(cli, ["init", str(csv_file)])
    print(result.output)
    print(result.exception)
    assert result.exit_code == 0
