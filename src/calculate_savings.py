import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression


def calculate_savings(living_expenses, discretionary_spending):
    df = pd.read_csv("hon-maikin-k-jissu.csv", encoding="Shift JIS")

    filtered_df = df[df["産業分類"] == "TL  "]
    filtered_df = filtered_df[filtered_df["就業形態"] != 2]
    new_df = filtered_df[["年", "現金給与総額"]]

    # 規模別に対してその年の平均をとる
    df = new_df.groupby("年", as_index=False)["現金給与総額"].mean()

    data = df["現金給与総額"].tolist()
    start = datetime(df["年"][0], 1, 1).strftime("%Y-%m-%d")
    end = datetime(df["年"].iloc[-1], 12, 31).strftime("%Y-%m-%d")
    date = pd.date_range(start=start, end=end, freq="Y")
    df = pd.DataFrame(data, index=date, columns=["Salary"])

    # 線形回帰モデルを使って将来の値を予測
    years_to_predict = 10
    future_dates = pd.date_range(
        start=df.index[-1], periods=years_to_predict + 1, freq="Y"
    )[
        1:
    ]  # 最後の日から10年後までの日付
    X = df.index.year.values.reshape(-1, 1)  # インデックスから年を抽出
    y = df["Salary"]

    model = LinearRegression()
    model.fit(X, y)

    future_X = future_dates.year.values.reshape(-1, 1)
    future_y = model.predict(future_X)

    # 10年後までの貯金を計算
    savings = 0
    for projected_income in future_y:
        savings += projected_income - (living_expenses + discretionary_spending)
        print(
            f"{savings} = {projected_income} - {living_expenses} - {discretionary_spending}"
        )

    # プロット
    plt.figure(figsize=(12, 8))

    # 実際の賃金データをプロット
    plt.plot(df.index, df["Salary"], label="Actual Data", color="blue")

    # 給料の予測値をプロット
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

    plt.title("Salary prediction and savings calculation")
    plt.xlabel("Year")
    plt.ylabel("Salary")
    plt.legend()
    plt.grid(True)
    plt.show()

    return savings


def main():
    # Asking the user for living expenses and discretionary spending
    try:
        living_expenses = float(input("Enter your living expenses for 1 year: "))
        discretionary_spending = float(
            input("Enter your discretionary spending for 1 year: ")
        )
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculating savings
    savings = calculate_savings(living_expenses, discretionary_spending)
    print("Savings till 10 years(yen): ", savings)

    # Saving the graph
    plt.savefig("result.png")
    plt.show()


if __name__ == "__main__":
    main()
