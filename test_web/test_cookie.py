class TestCookie:
    def test_cookie1(self):
        with open('data.yaml', 'r', encoding='utf-8') as f:
            print(f.read())
    def test_cookie2(self):
        with open('data.yaml', 'w', encoding='utf-8') as f:
            f.write("123")
    def test_cookie3(self):
        with open('data.yaml', 'a', encoding='utf-8') as f:
            f.write("456")

    def test_cookie4(self):
        with open('data2.yaml', 'r+', encoding='utf-8') as f:
            # f.write("456")
            print(f.read())


    def test_cookie5(self):
        with open('data2.yaml', 'w+', encoding='utf-8') as f:
            # f.write("123")
            print(f.read())


    def test_cookie6(self):
        with open('data2.yaml', 'a+', encoding='utf-8') as f:
            # f.write("456")
            print(f.read())
