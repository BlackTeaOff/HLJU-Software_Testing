def VerifyTEL(num):
    if (len(num) != 10 and len(num) != 7):
        print("电话号码不合法...号码长度必须为10或7...!")
        return

    reg = ""
    pre = ""
    suf = ""

    if (len(num) == 10):
        if (num[3] == '0' or num[3] == '1'):
            print("电话号码不合法...前缀码不能以0或1开头...!")
            return
        reg = int(num[0:3])
        pre = int(num[3:6])
        suf = int(num[6:10])
        print(f"{reg}-{pre}-{suf}\n")
    else:
        if (num[0] == '0' or num[0] == '1'):
            print("电话号码不合法...前缀码不能以0或1开头...!")
            return
        pre = int(num[0:3])
        suf = int(num[3:7])
        print(f"{pre}-{suf}\n")
    print("电话号码合法\n")

def main():
    VerifyTEL(input("请输入电话号码: "))

if (__name__ == "__main__"):
    main()