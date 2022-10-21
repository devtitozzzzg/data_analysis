import numpy as np
import pandas as pd

# 時系列データ作成（date_range関数）
dates = pd.date_range(start="2021-01-01", end="2021-12-31")
print(dates)
"""
実行結果
DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
               '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08',
               '2021-01-09', '2021-01-10',
               ...
               '2021-12-22', '2021-12-23', '2021-12-24', '2021-12-25',
               '2021-12-26', '2021-12-27', '2021-12-28', '2021-12-29',
               '2021-12-30', '2021-12-31'],
              dtype='datetime64[ns]', length=365, freq='D')
"""

print(end='\n')

df = pd.DataFrame(np.random.randint(1, 100, 365),
                  index=dates, columns=["ランダムな値"])
print(df)
"""
実行結果
            ランダムな値
2021-01-01      97
2021-01-02      88
2021-01-03      77
2021-01-04      54
2021-01-05      59
...            ...
2021-12-27      25
2021-12-28      39
2021-12-29      95
2021-12-30      18
2021-12-31       1

[365 rows x 1 columns]
"""

print(end='\n')

# groupbyメソッド
# Grouper関数
print(df.groupby(pd.Grouper(freq='M')).mean())
"""
実行結果
               ランダムな値
2021-01-31  43.774194
2021-02-28  49.642857
2021-03-31  56.129032
2021-04-30  49.100000
2021-05-31  55.774194
2021-06-30  56.866667
2021-07-31  43.032258
2021-08-31  44.516129
2021-09-30  50.500000
2021-10-31  51.483871
2021-11-30  43.400000
2021-12-31  50.193548
"""

print(end='\n')

print(df.resample('M').mean())
"""
実行結果
               ランダムな値
2021-01-31  47.193548
2021-02-28  49.607143
2021-03-31  52.032258
2021-04-30  44.700000
2021-05-31  41.580645
2021-06-30  46.466667
2021-07-31  43.096774
2021-08-31  52.258065
2021-09-30  51.233333
2021-10-31  46.903226
2021-11-30  53.066667
2021-12-31  57.612903
"""

print(end='\n')

# 欠損値
df = pd.read_csv("data/sales_data_contains_nan.csv")
print(df)
"""
実行結果
            日付      売り上げ     客数     客単価
0   2021-01-01  549342.0  125.0  4395.0
1   2021-01-02  577869.0  150.0  3852.0
2   2021-01-03  328030.0  184.0  1783.0
3   2021-01-04  317730.0  156.0  2037.0
4   2021-01-05  492476.0  149.0     NaN
5   2021-01-06  494278.0  112.0  4413.0
6   2021-01-07  446449.0    NaN  3783.0
7   2021-01-08  429130.0  181.0  2371.0
8   2021-01-09  346203.0  101.0     NaN
9   2021-01-10       NaN  151.0  3446.0
10  2021-01-11  453313.0  144.0  3148.0
11  2021-01-12  365632.0  148.0  2470.0
12  2021-01-13  549903.0  156.0  3525.0
13  2021-01-14       NaN  191.0  2193.0
14  2021-01-15  371200.0  149.0  2491.0
15  2021-01-16  464782.0  186.0  2499.0
16  2021-01-17  496719.0  103.0  4823.0
17  2021-01-18  532857.0    NaN  3191.0
18  2021-01-19  335662.0  111.0  3024.0
19  2021-01-20  527748.0  121.0  4362.0
20  2021-01-21  430256.0  189.0     NaN
21  2021-01-22  457698.0  198.0  2312.0
22  2021-01-23  545799.0  103.0  5299.0
23  2021-01-24  514338.0  111.0  4634.0
24  2021-01-25  330255.0  103.0  3206.0
25  2021-01-26       NaN  194.0  1581.0
26  2021-01-27  519069.0  106.0  4897.0
27  2021-01-28  585872.0    NaN  5375.0
28  2021-01-29  383079.0  187.0  2049.0
29  2021-01-30  566339.0  114.0  4968.0
30  2021-01-31  564572.0  183.0  3085.0
"""

print(end='\n')

# 欠損値を含む行を削除する（dropnaメソッド）
dropna_df = df.dropna()
print(dropna_df)
"""
実行結果
            日付      売り上げ     客数     客単価
0   2021-01-01  549342.0  125.0  4395.0
1   2021-01-02  577869.0  150.0  3852.0
2   2021-01-03  328030.0  184.0  1783.0
3   2021-01-04  317730.0  156.0  2037.0
5   2021-01-06  494278.0  112.0  4413.0
7   2021-01-08  429130.0  181.0  2371.0
10  2021-01-11  453313.0  144.0  3148.0
11  2021-01-12  365632.0  148.0  2470.0
12  2021-01-13  549903.0  156.0  3525.0
14  2021-01-15  371200.0  149.0  2491.0
15  2021-01-16  464782.0  186.0  2499.0
16  2021-01-17  496719.0  103.0  4823.0
18  2021-01-19  335662.0  111.0  3024.0
19  2021-01-20  527748.0  121.0  4362.0
21  2021-01-22  457698.0  198.0  2312.0
22  2021-01-23  545799.0  103.0  5299.0
23  2021-01-24  514338.0  111.0  4634.0
24  2021-01-25  330255.0  103.0  3206.0
26  2021-01-27  519069.0  106.0  4897.0
28  2021-01-29  383079.0  187.0  2049.0
29  2021-01-30  566339.0  114.0  4968.0
30  2021-01-31  564572.0  183.0  3085.0
"""

print(end='\n')

# 欠損値を指定した値で補完（fillnaメソッド）
fillna_df = df.fillna(0)
print(fillna_df)
"""
実行結果
            日付      売り上げ     客数     客単価
0   2021-01-01  549342.0  125.0  4395.0
1   2021-01-02  577869.0  150.0  3852.0
2   2021-01-03  328030.0  184.0  1783.0
3   2021-01-04  317730.0  156.0  2037.0
4   2021-01-05  492476.0  149.0     0.0
5   2021-01-06  494278.0  112.0  4413.0
6   2021-01-07  446449.0    0.0  3783.0
7   2021-01-08  429130.0  181.0  2371.0
8   2021-01-09  346203.0  101.0     0.0
9   2021-01-10       0.0  151.0  3446.0
10  2021-01-11  453313.0  144.0  3148.0
11  2021-01-12  365632.0  148.0  2470.0
12  2021-01-13  549903.0  156.0  3525.0
13  2021-01-14       0.0  191.0  2193.0
14  2021-01-15  371200.0  149.0  2491.0
15  2021-01-16  464782.0  186.0  2499.0
16  2021-01-17  496719.0  103.0  4823.0
17  2021-01-18  532857.0    0.0  3191.0
18  2021-01-19  335662.0  111.0  3024.0
19  2021-01-20  527748.0  121.0  4362.0
20  2021-01-21  430256.0  189.0     0.0
21  2021-01-22  457698.0  198.0  2312.0
22  2021-01-23  545799.0  103.0  5299.0
23  2021-01-24  514338.0  111.0  4634.0
24  2021-01-25  330255.0  103.0  3206.0
25  2021-01-26       0.0  194.0  1581.0
26  2021-01-27  519069.0  106.0  4897.0
27  2021-01-28  585872.0    0.0  5375.0
28  2021-01-29  383079.0  187.0  2049.0
29  2021-01-30  566339.0  114.0  4968.0
30  2021-01-31  564572.0  183.0  3085.0
"""

print(end='\n')

# method='ffill'
ffill_df = df.fillna(method='ffill')
print(ffill_df)
"""
実行結果
            日付      売り上げ     客数     客単価
0   2021-01-01  549342.0  125.0  4395.0
1   2021-01-02  577869.0  150.0  3852.0
2   2021-01-03  328030.0  184.0  1783.0
3   2021-01-04  317730.0  156.0  2037.0
4   2021-01-05  492476.0  149.0  2037.0
5   2021-01-06  494278.0  112.0  4413.0
6   2021-01-07  446449.0  112.0  3783.0
7   2021-01-08  429130.0  181.0  2371.0
8   2021-01-09  346203.0  101.0  2371.0
9   2021-01-10  346203.0  151.0  3446.0
10  2021-01-11  453313.0  144.0  3148.0
11  2021-01-12  365632.0  148.0  2470.0
12  2021-01-13  549903.0  156.0  3525.0
13  2021-01-14  549903.0  191.0  2193.0
14  2021-01-15  371200.0  149.0  2491.0
15  2021-01-16  464782.0  186.0  2499.0
16  2021-01-17  496719.0  103.0  4823.0
17  2021-01-18  532857.0  103.0  3191.0
18  2021-01-19  335662.0  111.0  3024.0
19  2021-01-20  527748.0  121.0  4362.0
20  2021-01-21  430256.0  189.0  4362.0
21  2021-01-22  457698.0  198.0  2312.0
22  2021-01-23  545799.0  103.0  5299.0
23  2021-01-24  514338.0  111.0  4634.0
24  2021-01-25  330255.0  103.0  3206.0
25  2021-01-26  330255.0  194.0  1581.0
26  2021-01-27  519069.0  106.0  4897.0
27  2021-01-28  585872.0  106.0  5375.0
28  2021-01-29  383079.0  187.0  2049.0
29  2021-01-30  566339.0  114.0  4968.0
30  2021-01-31  564572.0  183.0  3085.0
"""

print(end='\n')

# 平均値、中央値、最頻値
""" 平均値 """
fill_mean_df = df.fillna(df.mean())
print(fill_mean_df)
"""
実行結果
            日付      売り上げ          客数          客単価
0   2021-01-01  549342.0  125.000000  4395.000000
1   2021-01-02  577869.0  150.000000  3852.000000
2   2021-01-03  328030.0  184.000000  1783.000000
3   2021-01-04  317730.0  156.000000  2037.000000
4   2021-01-05  492476.0  149.000000  3400.428571
5   2021-01-06  494278.0  112.000000  4413.000000
6   2021-01-07  446449.0  146.642857  3783.000000
7   2021-01-08  429130.0  181.000000  2371.000000
8   2021-01-09  346203.0  101.000000  3400.428571
9   2021-01-10  463450.0  151.000000  3446.000000
10  2021-01-11  453313.0  144.000000  3148.000000
11  2021-01-12  365632.0  148.000000  2470.000000
12  2021-01-13  549903.0  156.000000  3525.000000
13  2021-01-14  463450.0  191.000000  2193.000000
14  2021-01-15  371200.0  149.000000  2491.000000
15  2021-01-16  464782.0  186.000000  2499.000000
16  2021-01-17  496719.0  103.000000  4823.000000
17  2021-01-18  532857.0  146.642857  3191.000000
18  2021-01-19  335662.0  111.000000  3024.000000
19  2021-01-20  527748.0  121.000000  4362.000000
20  2021-01-21  430256.0  189.000000  3400.428571
21  2021-01-22  457698.0  198.000000  2312.000000
22  2021-01-23  545799.0  103.000000  5299.000000
23  2021-01-24  514338.0  111.000000  4634.000000
24  2021-01-25  330255.0  103.000000  3206.000000
25  2021-01-26  463450.0  194.000000  1581.000000
26  2021-01-27  519069.0  106.000000  4897.000000
27  2021-01-28  585872.0  146.642857  5375.000000
28  2021-01-29  383079.0  187.000000  2049.000000
29  2021-01-30  566339.0  114.000000  4968.000000
30  2021-01-31  564572.0  183.000000  3085.000000
"""

print(end='\n')

# 最頻値で欠損値を補完（modeメソッド）
print(df.mode())
"""
実行結果
            日付      売り上げ     客数     客単価
0   2021-01-01  317730.0  103.0  1581.0
1   2021-01-02  328030.0    NaN  1783.0
2   2021-01-03  330255.0    NaN  2037.0
3   2021-01-04  335662.0    NaN  2049.0
4   2021-01-05  346203.0    NaN  2193.0
5   2021-01-06  365632.0    NaN  2312.0
6   2021-01-07  371200.0    NaN  2371.0
7   2021-01-08  383079.0    NaN  2470.0
8   2021-01-09  429130.0    NaN  2491.0
9   2021-01-10  430256.0    NaN  2499.0
10  2021-01-11  446449.0    NaN  3024.0
11  2021-01-12  453313.0    NaN  3085.0
12  2021-01-13  457698.0    NaN  3148.0
13  2021-01-14  464782.0    NaN  3191.0
14  2021-01-15  492476.0    NaN  3206.0
15  2021-01-16  494278.0    NaN  3446.0
16  2021-01-17  496719.0    NaN  3525.0
17  2021-01-18  514338.0    NaN  3783.0
18  2021-01-19  519069.0    NaN  3852.0
19  2021-01-20  527748.0    NaN  4362.0
20  2021-01-21  532857.0    NaN  4395.0
21  2021-01-22  545799.0    NaN  4413.0
22  2021-01-23  549342.0    NaN  4634.0
23  2021-01-24  549903.0    NaN  4823.0
24  2021-01-25  564572.0    NaN  4897.0
25  2021-01-26  566339.0    NaN  4968.0
26  2021-01-27  577869.0    NaN  5299.0
27  2021-01-28  585872.0    NaN  5375.0
28  2021-01-29       NaN    NaN     NaN
29  2021-01-30       NaN    NaN     NaN
30  2021-01-31       NaN    NaN     NaN
"""

print(end='\n')

# fillnaメソッドの引数にSeries
fill_freq_df = df.fillna(df.mode().iloc[0, :])
print(fill_freq_df)
"""
実行結果
            日付      売り上げ     客数     客単価
0   2021-01-01  549342.0  125.0  4395.0
1   2021-01-02  577869.0  150.0  3852.0
2   2021-01-03  328030.0  184.0  1783.0
3   2021-01-04  317730.0  156.0  2037.0
4   2021-01-05  492476.0  149.0  1581.0
5   2021-01-06  494278.0  112.0  4413.0
6   2021-01-07  446449.0  103.0  3783.0
7   2021-01-08  429130.0  181.0  2371.0
8   2021-01-09  346203.0  101.0  1581.0
9   2021-01-10  317730.0  151.0  3446.0
10  2021-01-11  453313.0  144.0  3148.0
11  2021-01-12  365632.0  148.0  2470.0
12  2021-01-13  549903.0  156.0  3525.0
13  2021-01-14  317730.0  191.0  2193.0
14  2021-01-15  371200.0  149.0  2491.0
15  2021-01-16  464782.0  186.0  2499.0
16  2021-01-17  496719.0  103.0  4823.0
17  2021-01-18  532857.0  103.0  3191.0
18  2021-01-19  335662.0  111.0  3024.0
19  2021-01-20  527748.0  121.0  4362.0
20  2021-01-21  430256.0  189.0  1581.0
21  2021-01-22  457698.0  198.0  2312.0
22  2021-01-23  545799.0  103.0  5299.0
23  2021-01-24  514338.0  111.0  4634.0
24  2021-01-25  330255.0  103.0  3206.0
25  2021-01-26  317730.0  194.0  1581.0
26  2021-01-27  519069.0  106.0  4897.0
27  2021-01-28  585872.0  103.0  5375.0
28  2021-01-29  383079.0  187.0  2049.0
29  2021-01-30  566339.0  114.0  4968.0
30  2021-01-31  564572.0  183.0  3085.0
"""

print(end='\n')
print("#------------------------------------#", end='\n')
print("# 確認問題")

"""
2021-04-01から2021-04-30までの合計30個のデータを作成したい。
pandasの関数を使った場合に適切なものを選べ。
"""
print(pd.date_range(start="2021-04-01", end="2021-04-30"))
"""
実行結果
DatetimeIndex(['2021-04-01', '2021-04-02', '2021-04-03', '2021-04-04',
               '2021-04-05', '2021-04-06', '2021-04-07', '2021-04-08',
               '2021-04-09', '2021-04-10', '2021-04-11', '2021-04-12',
               '2021-04-13', '2021-04-14', '2021-04-15', '2021-04-16',
               '2021-04-17', '2021-04-18', '2021-04-19', '2021-04-20',
               '2021-04-21', '2021-04-22', '2021-04-23', '2021-04-24',
               '2021-04-25', '2021-04-26', '2021-04-27', '2021-04-28',
               '2021-04-29', '2021-04-30'],
              dtype='datetime64[ns]', freq='D')
"""

print(end='\n')

dates = pd.date_range(start="2021-01-01", end="2021-12-31")
print(pd.DataFrame(np.arange(0, 365), index=dates,
                   columns=["日数"]).resample("M").count())
"""
実行結果
            日数
2021-01-31  31
2021-02-28  28
2021-03-31  31
2021-04-30  30
2021-05-31  31
2021-06-30  30
2021-07-31  31
2021-08-31  31
2021-09-30  30
2021-10-31  31
2021-11-30  30
2021-12-31  31
"""

print(end='\n')

df = pd.DataFrame([('窓', 2), ('窓', np.nan), ('机', 4),
                  ('本棚', np.nan)], columns=('家財', '部品数'))
print(df.fillna(df.mode().iloc[0, :]))
"""
実行結果
   家財  部品数
0   窓  2.0
1   窓  2.0
2   机  4.0
3  本棚  2.0
"""