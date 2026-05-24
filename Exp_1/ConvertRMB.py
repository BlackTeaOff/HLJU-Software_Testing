NUM_CHARS = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
# 人民币每4位一组, 1000是1000元. 1,0000就是1万元
GROUP_CHARS = ["元", "万", "亿"]
# 每组中不同位置的读法, 1000中, 1用仟; 10,0000中, 10用拾(对应数组中下标1的拾, 从右向左数, 1在第1个位置, 下标从0开始)
POS_CHARS = ["", "拾", "佰", "仟"]

def ConvertRMB(money):
    if "." in money:
        int_part, frac_part = money.split(".")
    else:
        int_part = money
        frac_part = "00"

    if (len(frac_part) != 2):
        print("格式错误...小数部分长度不为2...!\n")

    print(f"{int_part}.{frac_part}\n")

    res = ""

    # 整数部分
    if int_part != "0":
        zero_count = 0 # 记录连续出现的0的个数
        n = len(int_part) # 整数长度, 用于计算当前遍历的数字处于哪个组, 在组中的哪个位置

        # 遍历每一位数
        for i in range(n):
            digit = int(int_part[i])
            pos = n - i - 1 # 该数字距离末尾的位置, 用于计算组号与组中的位置
            unit_id = pos // 4 # 整数除法, 向下取整， 得到该数字在第几组
            sub_id = pos % 4 # 该数字在组内的位置

            if digit > 0:
                if (zero_count > 0):
                    res += "零" # 当前数字不是0, 而且前面有0, 加上零
                res += NUM_CHARS[digit] + POS_CHARS[sub_id] # 该数字变成大写人民币, 加上他组内的读法
                zero_count = 0
            else:
                zero_count += 1

            # 到了这个组的最后面, 看看要不要加这个组的单位
            if sub_id == 0:
                group_start = max(0, i - 3) # 向前找这个组的开始下标, 如果不满4位就是0
                group_val = int(int_part[group_start:i + 1]) # 提取从该组的数字(i + 1)是因为右面是开区间

                if group_val > 0 or unit_id == 0: # 如果该组没有为0的数字, 或者到了最后一组(需要加上元)
                    res += GROUP_CHARS[unit_id] # 加上对应组的单位

    if frac_part == "00":
        res += "整"
    else:
        jiao = int(frac_part[0])
        fen = int(frac_part[1])

        if jiao > 0:
            res += NUM_CHARS[jiao] + "角"
        elif jiao == 0 and fen > 0: # 角是0, 分不是0
            if int_part != "0":
                res += "零" # 整数部分不为零, 在元后面补零
        
        if fen > 0:
            res += NUM_CHARS[fen] + "分"

    print(f"人民币{res}\n")



def main():
    ConvertRMB(input("请输入人民币数字: "))

if (__name__ == "__main__"):
    main()