from client_code import messaging


def test_default_logging(capsys):
    from client_code.logging import DEBUG, Logger

    publisher = messaging.Publisher(logger=Logger(level=DEBUG, format="{msg}"))
    publisher.publish("test_channel", "test_message")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Published 'test_message' message on 'test_channel' channel to 0 subscriber(s)\n"
    )


def test_no_logging_default(capsys):
    publisher = messaging.Publisher()
    publisher.publish("test_channel", "test_message")
    captured = capsys.readouterr()
    assert captured.out == ""
