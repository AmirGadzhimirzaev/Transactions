from src.decorators import log


def test_log(capsys):
    @log()
    def log_testing_foo(a, b):
        return a / b

    log_testing_foo(10, 0)
    captured_err = capsys.readouterr()
    assert captured_err.out == "log_testing_foo division by zero. Inputs: (10, 0), {}\n"

    log_testing_foo(10, 2)
    captured_ok = capsys.readouterr()
    assert captured_ok.out == "log_testing_foo ok\n"

    @log('text.txt')
    def log_testing_foo_to_file(a, b):
        return a / b
