import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def calculate_savings(living_expenses, discretionary_spending):
    # サンプルデータの生成
    df = pd.read_csv(
        "/content/d2-1-5.csv", encoding="latin1", skiprows=10, parse_dates=True
    )
    data = df.iloc[3, 1:].tolist()
    data = [x * 42230 for x in data]
    date = pd.date_range(start="1/1/1991", end="31/12/2020", freq="Y")
    df = pd.DataFrame(data, index=date, columns=["Real_Wage"])

    # 線形回帰モデルを使って将来の値を予測
    years_to_predict = 10
    future_dates = pd.date_range(
        start=df.index[-1], periods=years_to_predict + 1, freq="Y"
    )[
        1:
    ]  # 最後の日から10年後までの日付
    X = df.index.year.values.reshape(-1, 1)  # インデックスから年を抽出
    y = df["Real_Wage"]

    model = LinearRegression()
    model.fit(X, y)

    future_X = future_dates.year.values.reshape(-1, 1)
    future_y = model.predict(future_X)

    # 10年後までの貯金を計算
    projected_income = future_y[-1]  # 10年後の予測された賃金
    total_expenses = (
        living_expenses * 10 + discretionary_spending * 10
    )  # 10年間の総費用
    savings = projected_income - total_expenses  # 貯金

    # プロット
    plt.figure(figsize=(12, 8))

    # 実際の賃金データをプロット
    plt.plot(df.index, df["Real_Wage"], label="Actual Data", color="blue")

    # 賃金の予測値をプロット
    plt.plot(future_dates, future_y, "r--", label="Predicted Data")

    # 10年後までの貯金額を表示
    plt.text(
        future_dates[-1],
        future_y[-1],
        f"Savings: {savings:.2f}",
        verticalalignment="bottom",
        horizontalalignment="right",
        color="green",
        fontsize=12,
    )

    plt.title("Real Wage Prediction and Savings Calculation")
    plt.xlabel("Year")
    plt.ylabel("Real Wage")
    plt.legend()
    plt.grid(True)
    plt.show()

    return savings


# 生活費と自由に使いたい金額を指定
living_expenses = 360000  # 生活費
discretionary_spending = 60000  # 自由に使いたい金額

# 貯金を計算
savings = calculate_savings(living_expenses, discretionary_spending)

print("10年後までの貯金: ", savings)
