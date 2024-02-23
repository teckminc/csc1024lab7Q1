import lab7q1
from io import StringIO
from sys import stderr

def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('5\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'1') != -1
    assert captured_stdout.strip().find(f'2') != -1
    assert captured_stdout.strip().find(f'3') != -1
    assert captured_stdout.strip().find(f'4') != -1
    assert captured_stdout.strip().find(f'5') != -1


def test_case2(monkeypatch, capsys):
    number_inputs = StringIO('4\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    num = lab7q1.ask_number()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert  num == 4

def test_case3(monkeypatch, capsys):
    number_inputs = StringIO('4\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    
    lab7q1.display_count(3)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'1') != -1
    assert captured_stdout.strip().find(f'2') != -1
    assert captured_stdout.strip().find(f'3') != -1
    





