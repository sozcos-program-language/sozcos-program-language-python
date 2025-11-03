import pandas as pd
import numpy as np
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')


def calculate_stock_performance(df):
    """
    计算每只股票的持仓天数和最终盈利
    """

    # 复制数据避免修改原数据
    df_analysis = df.copy()

    # 转换日期格式
    df_analysis['发生日期'] = pd.to_datetime(df_analysis['发生日期'], format='%Y%m%d')

    # 只分析证券买入和卖出的交易
    df_trades = df_analysis[df_analysis['交易类别'].isin(['证券买入', '证券卖出'])].copy()

    # 计算单笔交易金额（买入为负，卖出为正）
    df_trades['交易金额'] = np.where(
        df_trades['交易类别'] == '证券买入',
        -df_trades['发生金额'],
        df_trades['发生金额']
    )

    # 计算单笔交易数量（买入为正，卖出为负）
    df_trades['交易数量'] = np.where(
        df_trades['交易类别'] == '证券买入',
        df_trades['发生数量'],
        -df_trades['发生数量']
    )

    # 按证券代码分组计算
    stock_performance = []

    for code, group in df_trades.groupby('证券代码'):
        stock_name = group['证券名称'].iloc[0]

        # 按日期排序
        group = group.sort_values('发生日期')

        # 计算累计持仓
        group['累计持仓'] = group['交易数量'].cumsum()
        group['持仓变动'] = group['交易数量']

        # 计算每笔交易后的持仓成本
        group['累计成本'] = 0.0
        current_cost = 0.0
        current_shares = 0

        for idx, row in group.iterrows():
            if row['交易类别'] == '证券买入':
                # 买入：增加持仓和成本
                current_cost += -row['交易金额']  # 交易金额为负，取反得到正的成本
                current_shares += row['交易数量']
            else:
                # 卖出：按比例减少成本
                if current_shares > 0:
                    sell_ratio = row['交易数量'] / current_shares
                    current_cost *= (1 - sell_ratio)
                    current_shares -= row['交易数量']

            group.loc[idx, '累计成本'] = current_cost
            group.loc[idx, '实时持仓'] = current_shares

        # 计算盈利情况
        total_buy_amount = group[group['交易类别'] == '证券买入']['交易金额'].sum()
        total_sell_amount = group[group['交易类别'] == '证券卖出']['交易金额'].sum()

        # 最终盈利 = 卖出总额 + 买入总额（买入总额为负，所以实际是卖出-买入）
        final_profit = total_sell_amount + total_buy_amount

        # 计算持仓天数
        if len(group) > 1:
            first_trade_date = group['发生日期'].min()
            last_trade_date = group['发生日期'].max()
            holding_days = (last_trade_date - first_trade_date).days
        else:
            holding_days = 0

        # 计算交易统计
        buy_trades = len(group[group['交易类别'] == '证券买入'])
        sell_trades = len(group[group['交易类别'] == '证券卖出'])
        total_trades = len(group)

        # 当前持仓
        current_position = group['实时持仓'].iloc[-1]
        avg_cost = current_cost / current_position if current_position > 0 else 0

        stock_performance.append({
            '证券代码': code,
            '证券名称': stock_name,
            '首次交易日期': group['发生日期'].min(),
            '最后交易日期': group['发生日期'].max(),
            '持仓天数': holding_days,
            '买入次数': buy_trades,
            '卖出次数': sell_trades,
            '总交易次数': total_trades,
            '总买入金额': -total_buy_amount,  # 转换为正数
            '总卖出金额': total_sell_amount,
            '最终盈利': final_profit,
            '当前持仓': current_position,
            '平均成本': avg_cost,
            '盈利比例': (final_profit / -total_buy_amount * 100) if total_buy_amount < 0 else 0
        })

    return pd.DataFrame(stock_performance)


def calculate_detailed_trades(df):
    """
    计算详细的买卖配对和单次交易盈利
    """
    df_detailed = df.copy()
    df_detailed['发生日期'] = pd.to_datetime(df_detailed['发生日期'], format='%Y%m%d')

    # 只处理买卖交易
    df_trades = df_detailed[df_detailed['交易类别'].isin(['证券买入', '证券卖出'])].copy()

    detailed_results = []

    for code, group in df_trades.groupby('证券代码'):
        stock_name = group['证券名称'].iloc[0]
        group = group.sort_values('发生日期')

        # 使用FIFO方法匹配买卖
        buy_queue = []

        for idx, row in group.iterrows():
            if row['交易类别'] == '证券买入':
                # 加入买入队列
                buy_queue.append({
                    '日期': row['发生日期'],
                    '数量': row['发生数量'],
                    '价格': row['成交均价'],
                    '成本': -row['发生金额']  # 转换为正数
                })
            else:
                # 卖出：从最早的买入开始匹配
                sell_quantity = row['发生数量']
                sell_price = row['成交均价']
                sell_amount = row['发生金额']
                sell_date = row['发生日期']

                while sell_quantity > 0 and buy_queue:
                    buy_record = buy_queue[0]

                    if buy_record['数量'] <= sell_quantity:
                        # 完全匹配这次买入
                        matched_quantity = buy_record['数量']
                        buy_cost = buy_record['成本']
                        buy_price = buy_record['价格']
                        buy_date = buy_record['日期']

                        # 计算这次匹配的盈利
                        profit = (sell_price - buy_price) * matched_quantity
                        holding_days = (sell_date - buy_date).days

                        detailed_results.append({
                            '证券代码': code,
                            '证券名称': stock_name,
                            '买入日期': buy_date,
                            '卖出日期': sell_date,
                            '持仓天数': holding_days,
                            '买入价格': buy_price,
                            '卖出价格': sell_price,
                            '交易数量': matched_quantity,
                            '盈利金额': profit,
                            '盈利比例': (profit / (buy_price * matched_quantity)) * 100
                        })

                        sell_quantity -= matched_quantity
                        buy_queue.pop(0)  # 移除已匹配的买入记录
                    else:
                        # 部分匹配
                        matched_quantity = sell_quantity
                        buy_cost_per_share = buy_record['成本'] / buy_record['数量']
                        buy_price = buy_record['价格']
                        buy_date = buy_record['日期']

                        profit = (sell_price - buy_price) * matched_quantity
                        holding_days = (sell_date - buy_date).days

                        detailed_results.append({
                            '证券代码': code,
                            '证券名称': stock_name,
                            '买入日期': buy_date,
                            '卖出日期': sell_date,
                            '持仓天数': holding_days,
                            '买入价格': buy_price,
                            '卖出价格': sell_price,
                            '交易数量': matched_quantity,
                            '盈利金额': profit,
                            '盈利比例': (profit / (buy_price * matched_quantity)) * 100
                        })

                        # 更新买入记录
                        buy_queue[0]['数量'] -= matched_quantity
                        buy_queue[0]['成本'] -= buy_cost_per_share * matched_quantity
                        sell_quantity = 0

    return pd.DataFrame(detailed_results)


def generate_comprehensive_report(df):
    """
    生成全面的股票交易分析报告
    """

    # 1. 股票总体表现
    stock_perf = calculate_stock_performance(df)

    # 2. 详细交易配对
    detailed_trades = calculate_detailed_trades(df)

    # 3. 月度统计
    df_monthly = df.copy()
    df_monthly['发生日期'] = pd.to_datetime(df_monthly['发生日期'], format='%Y%m%d')
    df_monthly['年月'] = df_monthly['发生日期'].dt.strftime('%Y-%m')

    monthly_stats = df_monthly[df_monthly['交易类别'].isin(['证券买入', '证券卖出'])].groupby('年月').agg({
        '发生金额': 'sum',
        '发生数量': 'sum',
        '证券代码': 'count'
    }).rename(columns={
        '发生金额': '月资金流动',
        '发生数量': '月交易数量',
        '证券代码': '月交易次数'
    }).reset_index()

    # 4. 生成Excel报告
    with pd.ExcelWriter('股票交易详细分析报告.xlsx', engine='openpyxl') as writer:
        # 总体表现
        stock_perf.to_excel(writer, sheet_name='股票总体表现', index=False)

        # 详细交易配对
        if not detailed_trades.empty:
            detailed_trades.to_excel(writer, sheet_name='详细交易配对', index=False)

        # 月度统计
        monthly_stats.to_excel(writer, sheet_name='月度交易统计', index=False)

        # 原始数据
        df.to_excel(writer, sheet_name='原始交易数据', index=False)

        # 盈利排名
        profitable_stocks = stock_perf[stock_perf['最终盈利'] > 0].sort_values('最终盈利', ascending=False)
        profitable_stocks.to_excel(writer, sheet_name='盈利股票排名', index=False)

        # 亏损排名
        loss_stocks = stock_perf[stock_perf['最终盈利'] < 0].sort_values('最终盈利')
        loss_stocks.to_excel(writer, sheet_name='亏损股票排名', index=False)

    print("=" * 60)
    print("股票交易分析报告生成完成!")
    print(f"共分析 {len(stock_perf)} 只股票")
    print(f"总盈利股票: {len(profitable_stocks)} 只")
    print(f"总亏损股票: {len(loss_stocks)} 只")
    print(f"总盈利金额: {stock_perf['最终盈利'].sum():.2f} 元")
    print("=" * 60)

    # 显示表现最好的5只股票
    print("\n表现最好的5只股票:")
    top_stocks = stock_perf.nlargest(5, '最终盈利')[['证券名称', '证券代码', '最终盈利', '盈利比例']]
    for idx, row in top_stocks.iterrows():
        print(f"{row['证券名称']}({row['证券代码']}): {row['最终盈利']:.2f}元 ({row['盈利比例']:.1f}%)")

    return stock_perf, detailed_trades


# 执行分析
if __name__ == "__main__":
    # 读取数据
    df = pd.read_excel('2025年11月03日-A股交割单_结构化数据.xlsx')

    # 生成报告
    stock_perf, detailed_trades = generate_comprehensive_report(df)