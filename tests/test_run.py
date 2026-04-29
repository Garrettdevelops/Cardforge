from click.testing import CliRunner
from flashcard.cli.main import cli

def test_run(tmp_path):
    runner = CliRunner()

    csv_file = tmp_path / "study.csv"
    csv_file.write_text("question,correct_answer\nhi,hello")

    init_result = runner.invoke(cli, ["init", str(csv_file)])
    assert init_result.exit_code == 0
    json_file = tmp_path / "study.json"
    
    assert json_file.exists()

    correct_test_result = runner.invoke(cli, ["run", "study"], input = "hello") # simulates correct answer

    assert correct_test_result.exit_code == 0
    assert "Correct" in correct_test_result.output

    empty_entry_result = runner.invoke(cli, ["run", "study"], input = "\r") # simulates the user pressing enter

    assert empty_entry_result.exit_code == 0 
    assert "Incorrect" in empty_entry_result.output

    incorrect_test_result = runner.invoke(cli, ["run", "study"], input = "WRONG ANSWER") # simulates incorrect answer

    assert incorrect_test_result.exit_code == 0 
    assert "Incorrect" in incorrect_test_result.output








