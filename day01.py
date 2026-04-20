#任务1：变量和输出
name = "你的名字"
age = 20
print("我叫",name,"今年",age,"岁")
#任务2：输入和简单计算
your_name = input("请输入你的名字：")
print("你好，",your_name)
#任务3：条件判断（猜数字）
number = 5
guess = int(input("猜一个数字（1-10）:"))
if guess == number:
    print("恭喜你猜对了！")
else:
    print("猜错了，正确的数字是",number)
#任务4：循环（打印5次）
for i in range(5):
    print(f"这是第{i+1}次循环")
#任务5：列表和简单操作
fruits = ["苹果","香蕉","橘子"]
print("第一个水果是",fruits[0])
fruits.append("葡萄")
print("添加后的列表",fruits)