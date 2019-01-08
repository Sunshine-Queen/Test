class Dog(object):
    def print_set(self):
        print("大家好，我是小猪佩奇，请大家多多关照.....")

class Xiaotq(Dog):
    def print_set(self):
        print("hello everybody,我是你们的老大，我是哮天犬...")

def introduce(temp):
    temp.print_set()

dog1=Dog()
dog2=Xiaotq()

introduce(dog1)
introduce(dog2)