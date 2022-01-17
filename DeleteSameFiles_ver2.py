import os

def checkFileName(aPath, bPath):
    aList = os.listdir(aPath)

    for a, b, c in os.walk(bPath):
        for i in aList:
            if i in c:
                print(aPath + "/" + i)
                os.remove(aPath + "/" + i)
            else:
                continue

if __name__ == "__main__":

    answer = 0
    answer2 = 0
    print("输入1继续")
    answer = int(input())
    while(answer == 1):
        pathA = input("请输入路径1（被删除的）：")
        pathB = input("请输入路径2：")
        print("您的路径是(被删除的)：" + pathA + " 和查询的：" + pathB + "   输入1确认执行")
        answer2 = int(input())
        if (answer2 == 1):
            print("执行中")
            checkFileName(pathA,pathB)
            print("执行结束")
        answer = int(input("输入1继续 输入0退出:"))

    print("执行结束")
    answer = input("回车退出")

