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

    easy_answer_result = runner.invoke(cli, ["run", str(json_file), "--verbose=True"], input = "hello \n 1" )# simulates easy answer

    assert easy_answer_result.exit_code == 0
    assert "1 | 0 | 0 | 0" in easy_answer_result.output

    empty_entry_result = runner.invoke(cli, ["run", str(json_file)], input = "fake answer \n \r \n 4") # simulates the user pressing enter on the difficulty assesment 

    assert empty_entry_result.exit_code == 0 
    assert "Invalid entry" in empty_entry_result.output


    num_too_high_result = runner.invoke(cli, ["run", str(json_file)], input = "fake answer \n 5 \n 4") # simulates the user using a number above 4 on the difficulty assesment 

    assert num_too_high_result.exit_code == 0 
    assert "Invalid entry" in num_too_high_result.output
 

    num_too_low_result = runner.invoke(cli, ["run", str(json_file)], input = "fake answer \n 0 \n 4") # simulates the user using a number above 4 on the difficulty assesment 

    assert num_too_low_result.exit_code == 0 
    assert "Invalid entry" in num_too_low_result.output
 

    num_negative_result = runner.invoke(cli, ["run", str(json_file)], input = "fake answer \n -2 \n 4") # simulates the user using a negative number on the difficulty assesment 

    assert num_negative_result.exit_code == 0 
    assert "Invalid entry" in num_negative_result.output
 
    text_difficulty_result = runner.invoke(cli, ["run", str(json_file)], input = "fake answer \n some text \n 4") # simulates the user using text on the difficulty assesment 

    assert text_difficulty_result.exit_code == 0 
    assert "Invalid entry" in text_difficulty_result.output

