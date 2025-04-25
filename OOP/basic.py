class Dog:
    species = "Canis familiaris"  # 類別屬性 (Attribute)，所有狗都一樣

    def __init__(self, name, age):  # __init__ 是初始化方法
        self.name = name  # 實例屬性，每隻狗的名字不同
        self.age = age    # 實例屬性，每隻狗的年齡不同

    def bark(self):  # 一個自定義方法
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 3)

print(my_dog.name)  # 輸出: Buddy
print(my_dog.age)   # 輸出: 3
my_dog.bark()       # 輸出: Buddy says woof!

# Inheritance
class Puppy(Dog):  # Puppy 繼承自 Dog
    def play(self):
        print(f"{self.name} is playing!")

# Encapsulation
class Dog:
    def __init__(self, name, age):
        self._name = name  # 受保護
        self.__age = age   # 私有

    def get_age(self):  # 用方法訪問私有屬性
        return self.__age

# Polymorphism
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

def make_animal_speak(animal):
    animal.speak()

cat = Cat()
dog = Dog()
make_animal_speak(cat)  # 輸出: Meow
make_animal_speak(dog)  # 輸出: Woof