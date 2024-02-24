import lab7q4
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('4\n22\n76\n32\n12\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab7q4.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    anslist = [22.0, 76.0, 32.0, 12.0]
    assert captured_stdout.strip().find(str(anslist)) != -1
    assert captured_stdout.strip().replace(str(anslist), "").find(f'76') != -1
    assert captured_stdout.strip().replace(str(anslist), "").find(f'12') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab7q4.py") as tf:
    head = [next(tf) for _ in range(19)]
    s = tf.read()
    assert(s.find("for") != -1 )

def test_case3(monkeypatch, capsys):
  with open(f"lab7q4.py") as tf:
    head = [next(tf) for _ in range(19)]
    s = tf.read()
    assert(s.find("min(") == -1 )

def test_case4(monkeypatch, capsys):
  with open(f"lab7q4.py") as tf:
    head = [next(tf) for _ in range(19)]
    s = tf.read()
    assert(s.find("max(") == -1 )

def test_case5(monkeypatch, capsys):
    number_inputs = StringIO('4\n22\n76\n32\n12\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    mylist = lab7q4.read_number(5)
    captured_stdout, captured_stderr = capsys.readouterr()

    assert len(mylist) == 5

def test_case6(monkeypatch, capsys):
    
    result = lab7q4.find_max_number([1,2,3,4,5])
 
    assert result == 5

def test_case7(monkeypatch, capsys):
    
    result = lab7q4.find_min_number([1,2,3,4,5])
 
    assert result == 1