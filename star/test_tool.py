class Test():
    def test(self):
        import time
        print(str(time.time()))
        import hashlib
        md = hashlib.md5()
        md.update(('a' + 'q').encode('utf-8'))
        print(md.hexdigest())


if __name__ == '__main__':
    test = Test()
    test.test()
