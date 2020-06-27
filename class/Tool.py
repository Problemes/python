class Tool(object):
    count = 3

    def __init__(self, name, num):
        Tool.count += 1
        print("Tool's count will be add 1 when create instance every time; count is %d" % Tool.count)
        self.name = name
        self.num = num

    @classmethod
    def show_tool_count(cls):
        print("this is a class method and show you count: %d" % cls.count)


Tool.show_tool_count() 