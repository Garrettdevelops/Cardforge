from click.testing import CliRunner
from flashcard.cli.main import cli

def test_order(tmp_path):
    runner = CliRunner()

    csv_file = tmp_path / "order.csv"
    csv_file.write_text("question,correct_answer\n1,1\n2,2\n3,3\n4,4\n5,5\n6,6\n7,7\n8,8\n9,9\n10,10\n11,11\n12,12\n13,13\n14,14\n15,15\n16,16\n17,17\n18,18\n19,19\n20,20\n")

    init_result = runner.invoke(cli, ["init", str(csv_file)])
    assert init_result.exit_code == 0
    json_file = tmp_path / "order.json"

    assert json_file.exists()
    test_counter = 0 
    order_test_result = runner.invoke(cli, ["run", str(json_file)], input = "fake answer \n 4 \n fake answer \n 4 fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4 \n fake answer \n 4")

    assert   "| 1 | 1 | 0 | 0 | 0 | 1\n | 2 | 2 | 0 | 0 | 0 | 1\n | 3 | 3 | 0 | 0 | 0 | 1\n | 4 | 4 | 0 | 0 | 0 | 1\n | 5 | 5 | 0 | 0 | 0 | 1\n | 6 | 6 | 0 | 0 | 0 | 1\n | 7 | 7 | 0 | 0 | 0 | 1\n | 8 | 8 | 0 | 0 | 0 | 1\n | 9 | 9 | 0 | 0 | 0 | 1\n | 10 | 10 | 0 | 0 | 0 | 1\n | 11 | 11 | 0 | 0 | 0 | 1\n | 12 | 12 | 0 | 0 | 0 | 1\n | 13 | 13 | 0 | 0 | 0 | 1\n | 14 | 14 | 0 | 0 | 0 | 1\n | 15 | 15 | 0 | 0 | 0 | 1\n | 16 | 16 | 0 | 0 | 0 | 1\n | 17 | 17 | 0 | 0 | 0 | 1\n | 18 | 18 | 0 | 0 | 0 | 1\n | 19 | 19 | 0 | 0 | 0 | 1\n | 20 | 20 | 0 | 0 | 0 | 1\n" not in order_test_result.output

