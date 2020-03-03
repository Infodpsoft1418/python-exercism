from hello_world import hello


class TestHelloWorld:
    def test_say_hi(self):
        assert hello() == "Hello, World!"
