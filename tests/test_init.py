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

    incorrect_csv_file = tmp_path / "incorrect.csv"
    csv_file.write_text("q,a\nhi,hello")

    incorrect_csv_result = runner.invoke(cli, ["init", str(incorrect_csv_file)])
    assert incorrect_csv_result.exit_code == 1 
    
