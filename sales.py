def calculate_total_sales(sales_data):
    total_sales = sum(sales_data)
    return total_sales

def main():

    input_name = input("輸入銷售員代號： ")
    
    #輸入銷售額資料，以逗號分隔
    input_str = input("輸入銷售額資料（以逗號分隔）: ")
    
    #將輸入的字符串分割成數字列表
    sales_data = [float(s) for s in input_str.split(',')]

    #計算總銷售額
    total_sales = calculate_total_sales(sales_data)

    #顯示結果
    print("銷售員", input_name, "的總銷售額:", total_sales)

if __name__ == "__main__":
    main()
