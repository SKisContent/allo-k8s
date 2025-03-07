from allo import main

class TestMain:
    def test_hello(self):
        hello_message = "<p>Allô, le monde!</p>"
        assert main.hello() == hello_message