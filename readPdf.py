import pdfplumber
import pandas as pd
import re


def extract_stock_transactions(pdf_path):
    """
    提取A股交割单PDF数据并结构化
    :param pdf_path: PDF文件路径（本地文件路径，如"D:/交割单.pdf"）
    :return: 结构化的交易数据DataFrame
    """
    # 定义交割单字段（与PDF表格列对应）
    columns = [
        "发生日期", "币种", "证券账号", "证券名称", "证券代码",
        "交易类别", "发生数量", "成交均价", "成交金额", "印花税",
        "其他费用", "过户费", "发生金额", "业务备注"
    ]
    all_transactions = []

    # 读取PDF所有页面
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # 提取页面文本（按行分割）
            page_text = page.extract_text()
            if not page_text:
                continue  # 跳过无文本的页面
            lines = page_text.split("\n")

            # 过滤有效交易行（包含"证券买入"/"证券卖出"/"股息入账"等关键词，排除表头/空行）
            for line in lines:
                line = line.strip()
                # 跳过无效行（表头、页码、空行等）
                if any(keyword in line for keyword in ["资产账号", "证件类型", "第页", "客户名称", "东莞证券"]) or len(
                        line) < 50:
                    continue
                # 只保留核心交易类型（排除登记指定等非交易记录）
                if not any(trade_type in line for trade_type in ["证券买入", "证券卖出", "股息入账", "税补缴"]):
                    continue

                # 按空格分割数据（处理多个连续空格的情况）
                data = re.split(r"\s+", line)
                # 截取前14个字段（匹配columns定义的字段数量）
                if len(data) >= 14:
                    transaction = data[:14]
                    all_transactions.append(transaction)

    # 转换为DataFrame并处理数据类型
    df = pd.DataFrame(all_transactions, columns=columns)
    # 处理数值类型字段（去除非数字字符，转换为float）
    numeric_columns = ["发生数量", "成交均价", "成交金额", "印花税", "其他费用", "过户费", "发生金额"]
    for col in numeric_columns:
        df[col] = df[col].str.replace(r"[^\d.-]", "", regex=True)  # 清除非数字字符
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)  # 转换为数值，缺失值填0

    # 处理日期格式（确保为字符串格式，便于后续转换）
    df["发生日期"] = df["发生日期"].str.replace(r"[^\d]", "", regex=True).str[:8]

    return df


# ------------------- 执行代码 -------------------
if __name__ == "__main__":
    # 1. 替换为你的PDF文件本地路径（示例：Windows路径用反斜杠，Mac/Linux用正斜杠）
    pdf_file_path = "C:\\Users\\ELSEN\\Downloads\\东莞证券电子对账单-000180072471-2025-11-03 (1).pdf"

    # 2. 提取并结构化数据
    transaction_df = extract_stock_transactions(pdf_file_path)

    # 3. 保存为Excel/Csv（方便后续操作）
    transaction_df.to_excel("2025年11月03日-A股交割单_结构化数据.xlsx", index=False, engine="openpyxl")
    transaction_df.to_csv("2025年11月03日-A股交割单_结构化数据.csv", index=False, encoding="utf-8-sig")

    # 4. 打印前5条数据验证结果
    print("结构化数据预览（前5条）：")
    print(transaction_df.head())
    print(f"\n共提取到 {len(transaction_df)} 条交易记录")