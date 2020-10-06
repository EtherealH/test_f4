import unittest
import f4
t1 = True
class test(unittest.TestCase):
    #对功能一和二进行测试
    def test_f4(self):
        pass
    def test_answer(self):
        print("f4的answer函数的单元测试")
        equation = input("请输入四则运算表达式")
        equation_answer = input("请输入正确答案")
        self.assertEqual(equation_answer,f4.answer(eq = equation))
        print("success")
    def test_deft_input(self):
        print("f4的deft_input函数单元测试开始")
        #输入参数
        x = input("请输入有效参数")
        self.assertEqual(f4.deft_input(x),0)
        print("success")
    def test_fixed(self):
        print("f4的fixed函数单元测试开始")
        self.assertEqual(None,f4.fixed())
        print("success")
if __name__ == '__main__':
    unittest.main()


