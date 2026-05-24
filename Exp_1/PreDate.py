def PreDate(date):
    # 每个月的天数, 下标从0开始, 闰年则将二月(daysOfMonth[2])改为29
    daysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    print(date)
    if (len(date) != 8):
        print("输入日期不合法...日期长度必须为8...!\n")
        return
    
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    print(f"{year} {month} {day}\n")

    # 判断闰年
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        print(f"{year}是闰年\n")
        daysOfMonth[2] = 29

    if (year < 1000 or year > 2020):
        print("输入日期不合法...输入年份必须在1000-2020之间...!")
        return
    if (month < 1 or month > 12):
        print("输入日期不合法...输入月份必须在1-12之间...!")
        return
    if (day < 1 or day > daysOfMonth[month]):
        print(f"输入日期不合法...输入日期必须在1-{daysOfMonth[month]}之间...!")
        return
    
    # 计算
    # 不跨月
    if (day > 1):
        print(f"前一天: {year}年{month}月{day - 1}日\n")
        return
    # 跨月, 但不用跨年(月数-1, 天数直接就是上一个月的最后一天)
    if (day == 1 and month > 1):
        print(f"前一天: {year}年{month - 1}月{daysOfMonth[month - 1]}日\n")
    # 跨月也跨年(年数-1, 月数直接是12月, 天数就是12月的最后一天)
    if (day == 1 and month == 1):
        print(f"前一天: {year - 1}年12月{daysOfMonth[12]}日\n")
def main():
    PreDate(input("请输入日期: "))

if __name__ == "__main__":
    main()