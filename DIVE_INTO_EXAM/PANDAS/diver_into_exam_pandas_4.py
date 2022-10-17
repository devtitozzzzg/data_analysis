import numpy as np
import pandas as pd

# read_csvメソッド
df = pd.read_csv("data/sales_data.csv")
print(df)
"""
実行結果
            日付    売り上げ   客数   客単価
0   2021-01-01  549342  125  4395
1   2021-01-02  577869  150  3852
2   2021-01-03  328030  184  1783
3   2021-01-04  317730  156  2037
4   2021-01-05  492476  149  3305
5   2021-01-06  494278  112  4413
6   2021-01-07  446449  118  3783
7   2021-01-08  429130  181  2371
8   2021-01-09  346203  101  3428
9   2021-01-10  520374  151  3446
10  2021-01-11  453313  144  3148
11  2021-01-12  365632  148  2470
12  2021-01-13  549903  156  3525
13  2021-01-14  418857  191  2193
14  2021-01-15  371200  149  2491
15  2021-01-16  464782  186  2499
16  2021-01-17  496719  103  4823
17  2021-01-18  532857  167  3191
18  2021-01-19  335662  111  3024
19  2021-01-20  527748  121  4362
20  2021-01-21  430256  189  2276
21  2021-01-22  457698  198  2312
22  2021-01-23  545799  103  5299
23  2021-01-24  514338  111  4634
24  2021-01-25  330255  103  3206
25  2021-01-26  306648  194  1581
26  2021-01-27  519069  106  4897
27  2021-01-28  585872  109  5375
28  2021-01-29  383079  187  2049
29  2021-01-30  566339  114  4968
30  2021-01-31  564572  183  3085
"""

print(end='\n')

# 売り上げが500,000以上のデータを抽出
print(df["売り上げ"] >= 500000)
"""
実行結果
0      True
1      True
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9      True
10    False
11    False
12     True
13    False
14    False
15    False
16    False
17     True
18    False
19     True
20    False
21    False
22     True
23     True
24    False
25    False
26     True
27     True
28    False
29     True
30     True
Name: 売り上げ, dtype: bool
"""

print(end='\n')

# 条件を満たす行を抽出
matched_df = df[df["売り上げ"] >= 500000]
print(matched_df)
"""
実行結果
            日付    売り上げ   客数   客単価
0   2021-01-01  549342  125  4395
1   2021-01-02  577869  150  3852
9   2021-01-10  520374  151  3446
12  2021-01-13  549903  156  3525
17  2021-01-18  532857  167  3191
19  2021-01-20  527748  121  4362
22  2021-01-23  545799  103  5299
23  2021-01-24  514338  111  4634
26  2021-01-27  519069  106  4897
27  2021-01-28  585872  109  5375
29  2021-01-30  566339  114  4968
30  2021-01-31  564572  183  3085
"""

print(end='\n')

# queryメソッド
print(df.query('売り上げ >= 500000'))
"""
実行結果
            日付    売り上げ   客数   客単価
0   2021-01-01  549342  125  4395
1   2021-01-02  577869  150  3852
9   2021-01-10  520374  151  3446
12  2021-01-13  549903  156  3525
17  2021-01-18  532857  167  3191
19  2021-01-20  527748  121  4362
22  2021-01-23  545799  103  5299
23  2021-01-24  514338  111  4634
26  2021-01-27  519069  106  4897
27  2021-01-28  585872  109  5375
29  2021-01-30  566339  114  4968
30  2021-01-31  564572  183  3085
"""

print(end='\n')

# 客数が150以上で、かつ客単価が3,500以上のデータを抽出
print(df.query('客数 >= 150 and 客単価 >= 3500'))
"""
実行結果
            日付    売り上げ   客数   客単価
1   2021-01-02  577869  150  3852
12  2021-01-13  549903  156  3525
"""

print(end='\n')

# 各カラムのデータ型
print(df.dtypes)
"""
実行結果
日付      object
売り上げ     int64
客数       int64
客単価      int64
dtype: object
"""

print(end='\n')

df.loc[:, '日付'] = df.loc[:, '日付'].apply(pd.to_datetime)
print(df.dtypes)
"""
実行結果
日付      datetime64[ns]
売り上げ             int64
客数               int64
客単価              int64
dtype: object
"""

print(end='\n')

df.loc[:, '客単価'] = df.loc[:, '客単価'].astype(np.float32)
print(df)
"""
実行結果
           日付    売り上げ   客数     客単価
0  2021-01-01  549342  125  4395.0
1  2021-01-02  577869  150  3852.0
2  2021-01-03  328030  184  1783.0
3  2021-01-04  317730  156  2037.0
4  2021-01-05  492476  149  3305.0
5  2021-01-06  494278  112  4413.0
6  2021-01-07  446449  118  3783.0
7  2021-01-08  429130  181  2371.0
8  2021-01-09  346203  101  3428.0
9  2021-01-10  520374  151  3446.0
10 2021-01-11  453313  144  3148.0
11 2021-01-12  365632  148  2470.0
12 2021-01-13  549903  156  3525.0
13 2021-01-14  418857  191  2193.0
14 2021-01-15  371200  149  2491.0
15 2021-01-16  464782  186  2499.0
16 2021-01-17  496719  103  4823.0
17 2021-01-18  532857  167  3191.0
18 2021-01-19  335662  111  3024.0
19 2021-01-20  527748  121  4362.0
20 2021-01-21  430256  189  2276.0
21 2021-01-22  457698  198  2312.0
22 2021-01-23  545799  103  5299.0
23 2021-01-24  514338  111  4634.0
24 2021-01-25  330255  103  3206.0
25 2021-01-26  306648  194  1581.0
26 2021-01-27  519069  106  4897.0
27 2021-01-28  585872  109  5375.0
28 2021-01-29  383079  187  2049.0
29 2021-01-30  566339  114  4968.0
30 2021-01-31  564572  183  3085.0
"""

print(end='\n')

# sort_valueメソッド
print(df.sort_values(by="売り上げ"))
"""
実行結果
           日付    売り上げ   客数     客単価
25 2021-01-26  306648  194  1581.0
3  2021-01-04  317730  156  2037.0
2  2021-01-03  328030  184  1783.0
24 2021-01-25  330255  103  3206.0
18 2021-01-19  335662  111  3024.0
8  2021-01-09  346203  101  3428.0
11 2021-01-12  365632  148  2470.0
14 2021-01-15  371200  149  2491.0
28 2021-01-29  383079  187  2049.0
13 2021-01-14  418857  191  2193.0
7  2021-01-08  429130  181  2371.0
20 2021-01-21  430256  189  2276.0
6  2021-01-07  446449  118  3783.0
10 2021-01-11  453313  144  3148.0
21 2021-01-22  457698  198  2312.0
15 2021-01-16  464782  186  2499.0
4  2021-01-05  492476  149  3305.0
5  2021-01-06  494278  112  4413.0
16 2021-01-17  496719  103  4823.0
23 2021-01-24  514338  111  4634.0
26 2021-01-27  519069  106  4897.0
9  2021-01-10  520374  151  3446.0
19 2021-01-20  527748  121  4362.0
17 2021-01-18  532857  167  3191.0
22 2021-01-23  545799  103  5299.0
0  2021-01-01  549342  125  4395.0
12 2021-01-13  549903  156  3525.0
30 2021-01-31  564572  183  3085.0
29 2021-01-30  566339  114  4968.0
1  2021-01-02  577869  150  3852.0
27 2021-01-28  585872  109  5375.0
"""

print(end='\n')

# ascendingオプション
df.sort_values(by="売り上げ", ascending=False)
print(df)
"""
実行結果
           日付    売り上げ   客数     客単価
0  2021-01-01  549342  125  4395.0
1  2021-01-02  577869  150  3852.0
2  2021-01-03  328030  184  1783.0
3  2021-01-04  317730  156  2037.0
4  2021-01-05  492476  149  3305.0
5  2021-01-06  494278  112  4413.0
6  2021-01-07  446449  118  3783.0
7  2021-01-08  429130  181  2371.0
8  2021-01-09  346203  101  3428.0
9  2021-01-10  520374  151  3446.0
10 2021-01-11  453313  144  3148.0
11 2021-01-12  365632  148  2470.0
12 2021-01-13  549903  156  3525.0
13 2021-01-14  418857  191  2193.0
14 2021-01-15  371200  149  2491.0
15 2021-01-16  464782  186  2499.0
16 2021-01-17  496719  103  4823.0
17 2021-01-18  532857  167  3191.0
18 2021-01-19  335662  111  3024.0
19 2021-01-20  527748  121  4362.0
20 2021-01-21  430256  189  2276.0
21 2021-01-22  457698  198  2312.0
22 2021-01-23  545799  103  5299.0
23 2021-01-24  514338  111  4634.0
24 2021-01-25  330255  103  3206.0
25 2021-01-26  306648  194  1581.0
26 2021-01-27  519069  106  4897.0
27 2021-01-28  585872  109  5375.0
28 2021-01-29  383079  187  2049.0
29 2021-01-30  566339  114  4968.0
30 2021-01-31  564572  183  3085.0
"""

print(end='\n')

# カラムの削除（dropメソッド）
df = df.drop("客単価", axis=1)
print(df)
"""
実行結果
           日付    売り上げ   客数
0  2021-01-01  549342  125
1  2021-01-02  577869  150
2  2021-01-03  328030  184
3  2021-01-04  317730  156
4  2021-01-05  492476  149
5  2021-01-06  494278  112
6  2021-01-07  446449  118
7  2021-01-08  429130  181
8  2021-01-09  346203  101
9  2021-01-10  520374  151
10 2021-01-11  453313  144
11 2021-01-12  365632  148
12 2021-01-13  549903  156
13 2021-01-14  418857  191
14 2021-01-15  371200  149
15 2021-01-16  464782  186
16 2021-01-17  496719  103
17 2021-01-18  532857  167
18 2021-01-19  335662  111
19 2021-01-20  527748  121
20 2021-01-21  430256  189
21 2021-01-22  457698  198
22 2021-01-23  545799  103
23 2021-01-24  514338  111
24 2021-01-25  330255  103
25 2021-01-26  306648  194
26 2021-01-27  519069  106
27 2021-01-28  585872  109
28 2021-01-29  383079  187
29 2021-01-30  566339  114
30 2021-01-31  564572  183
"""

print(end='\n')

df = df.drop(0, axis=0)
print(df)
"""
実行結果
           日付    売り上げ   客数
1  2021-01-02  577869  150
2  2021-01-03  328030  184
3  2021-01-04  317730  156
4  2021-01-05  492476  149
5  2021-01-06  494278  112
6  2021-01-07  446449  118
7  2021-01-08  429130  181
8  2021-01-09  346203  101
9  2021-01-10  520374  151
10 2021-01-11  453313  144
11 2021-01-12  365632  148
12 2021-01-13  549903  156
13 2021-01-14  418857  191
14 2021-01-15  371200  149
15 2021-01-16  464782  186
16 2021-01-17  496719  103
17 2021-01-18  532857  167
18 2021-01-19  335662  111
19 2021-01-20  527748  121
20 2021-01-21  430256  189
21 2021-01-22  457698  198
22 2021-01-23  545799  103
23 2021-01-24  514338  111
24 2021-01-25  330255  103
25 2021-01-26  306648  194
26 2021-01-27  519069  106
27 2021-01-28  585872  109
28 2021-01-29  383079  187
29 2021-01-30  566339  114
30 2021-01-31  564572  183
"""

print(end='\n')

# カラム同士の計算
df.loc[:, "客単価"] = df.loc[:, "売り上げ"] / df.loc[:, "客数"]
print(df)
"""
実行結果
           日付    売り上げ   客数          客単価
1  2021-01-02  577869  150  3852.460000
2  2021-01-03  328030  184  1782.771739
3  2021-01-04  317730  156  2036.730769
4  2021-01-05  492476  149  3305.208054
5  2021-01-06  494278  112  4413.196429
6  2021-01-07  446449  118  3783.466102
7  2021-01-08  429130  181  2370.883978
8  2021-01-09  346203  101  3427.752475
9  2021-01-10  520374  151  3446.185430
10 2021-01-11  453313  144  3148.006944
11 2021-01-12  365632  148  2470.486486
12 2021-01-13  549903  156  3525.019231
13 2021-01-14  418857  191  2192.968586
14 2021-01-15  371200  149  2491.275168
15 2021-01-16  464782  186  2498.827957
16 2021-01-17  496719  103  4822.514563
17 2021-01-18  532857  167  3190.760479
18 2021-01-19  335662  111  3023.981982
19 2021-01-20  527748  121  4361.553719
20 2021-01-21  430256  189  2276.486772
21 2021-01-22  457698  198  2311.606061
22 2021-01-23  545799  103  5299.019417
23 2021-01-24  514338  111  4633.675676
24 2021-01-25  330255  103  3206.359223
25 2021-01-26  306648  194  1580.659794
26 2021-01-27  519069  106  4896.877358
27 2021-01-28  585872  109  5374.972477
28 2021-01-29  383079  187  2048.550802
29 2021-01-30  566339  114  4967.885965
30 2021-01-31  564572  183  3085.092896
"""

print(end='\n')

df.loc[:, "客単価"] = df.loc[:, "客単価"].round().astype(int)
print(df)
"""
実行結果
           日付    売り上げ   客数   客単価
1  2021-01-02  577869  150  3852
2  2021-01-03  328030  184  1783
3  2021-01-04  317730  156  2037
4  2021-01-05  492476  149  3305
5  2021-01-06  494278  112  4413
6  2021-01-07  446449  118  3783
7  2021-01-08  429130  181  2371
8  2021-01-09  346203  101  3428
9  2021-01-10  520374  151  3446
10 2021-01-11  453313  144  3148
11 2021-01-12  365632  148  2470
12 2021-01-13  549903  156  3525
13 2021-01-14  418857  191  2193
14 2021-01-15  371200  149  2491
15 2021-01-16  464782  186  2499
16 2021-01-17  496719  103  4823
17 2021-01-18  532857  167  3191
18 2021-01-19  335662  111  3024
19 2021-01-20  527748  121  4362
20 2021-01-21  430256  189  2276
21 2021-01-22  457698  198  2312
22 2021-01-23  545799  103  5299
23 2021-01-24  514338  111  4634
24 2021-01-25  330255  103  3206
25 2021-01-26  306648  194  1581
26 2021-01-27  519069  106  4897
27 2021-01-28  585872  109  5375
28 2021-01-29  383079  187  2049
29 2021-01-30  566339  114  4968
30 2021-01-31  564572  183  3085
"""

print(end='\n')

# DataFrameをndarrayに変換

print(df.values)
"""
実行結果
[[Timestamp('2021-01-02 00:00:00') 577869 150 3852]
 [Timestamp('2021-01-03 00:00:00') 328030 184 1783]
 [Timestamp('2021-01-04 00:00:00') 317730 156 2037]
 [Timestamp('2021-01-05 00:00:00') 492476 149 3305]
 [Timestamp('2021-01-06 00:00:00') 494278 112 4413]
 [Timestamp('2021-01-07 00:00:00') 446449 118 3783]
 [Timestamp('2021-01-08 00:00:00') 429130 181 2371]
 [Timestamp('2021-01-09 00:00:00') 346203 101 3428]
 [Timestamp('2021-01-10 00:00:00') 520374 151 3446]
 [Timestamp('2021-01-11 00:00:00') 453313 144 3148]
 [Timestamp('2021-01-12 00:00:00') 365632 148 2470]
 [Timestamp('2021-01-13 00:00:00') 549903 156 3525]
 [Timestamp('2021-01-14 00:00:00') 418857 191 2193]
 [Timestamp('2021-01-15 00:00:00') 371200 149 2491]
 [Timestamp('2021-01-16 00:00:00') 464782 186 2499]
 [Timestamp('2021-01-17 00:00:00') 496719 103 4823]
 [Timestamp('2021-01-18 00:00:00') 532857 167 3191]
 [Timestamp('2021-01-19 00:00:00') 335662 111 3024]
 [Timestamp('2021-01-20 00:00:00') 527748 121 4362]
 [Timestamp('2021-01-21 00:00:00') 430256 189 2276]
 [Timestamp('2021-01-22 00:00:00') 457698 198 2312]
 [Timestamp('2021-01-23 00:00:00') 545799 103 5299]
 [Timestamp('2021-01-24 00:00:00') 514338 111 4634]
 [Timestamp('2021-01-25 00:00:00') 330255 103 3206]
 [Timestamp('2021-01-26 00:00:00') 306648 194 1581]
 [Timestamp('2021-01-27 00:00:00') 519069 106 4897]
 [Timestamp('2021-01-28 00:00:00') 585872 109 5375]
 [Timestamp('2021-01-29 00:00:00') 383079 187 2049]
 [Timestamp('2021-01-30 00:00:00') 566339 114 4968]
 [Timestamp('2021-01-31 00:00:00') 564572 183 3085]]
"""

print(end='\n')

df.loc[:, ["売り上げ", "客単価"]].values
print(df)
"""
実行結果
           日付    売り上げ   客数   客単価
1  2021-01-02  577869  150  3852
2  2021-01-03  328030  184  1783
3  2021-01-04  317730  156  2037
4  2021-01-05  492476  149  3305
5  2021-01-06  494278  112  4413
6  2021-01-07  446449  118  3783
7  2021-01-08  429130  181  2371
8  2021-01-09  346203  101  3428
9  2021-01-10  520374  151  3446
10 2021-01-11  453313  144  3148
11 2021-01-12  365632  148  2470
12 2021-01-13  549903  156  3525
13 2021-01-14  418857  191  2193
14 2021-01-15  371200  149  2491
15 2021-01-16  464782  186  2499
16 2021-01-17  496719  103  4823
17 2021-01-18  532857  167  3191
18 2021-01-19  335662  111  3024
19 2021-01-20  527748  121  4362
20 2021-01-21  430256  189  2276
21 2021-01-22  457698  198  2312
22 2021-01-23  545799  103  5299
23 2021-01-24  514338  111  4634
24 2021-01-25  330255  103  3206
25 2021-01-26  306648  194  1581
26 2021-01-27  519069  106  4897
27 2021-01-28  585872  109  5375
28 2021-01-29  383079  187  2049
29 2021-01-30  566339  114  4968
30 2021-01-31  564572  183  3085
"""

print(end='\n')
print("#------------------------------------#", end='\n')
print("# 確認問題")

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [2, 4, 6]])

print(a == b)
"""
実行結果
[[ True  True  True]
 [False False  True]]
"""

print(end='\n')

df = pd.DataFrame({"商品名": ["apple", "orange", "banana"], "単価": [
                  100, 150, 80], "在庫数": [10, 20, 100]})
print(df.query("単価 <= 100 and 在庫数 >= 50"))
"""
実行結果
(A)には、"単価 <= 100 and 在庫数 >= 50"が入る
      商品名  単価  在庫数
2  banana  80  100
"""

print(end='\n')

df = pd.DataFrame({"商品名": ["apple", "orange", "banana"], "単価": [
                  100, 150, 80], "在庫数": [10, 20, 100]})
df = (A)
# df = df.drop("在庫数", axis=1)
print(df)
"""
実行結果
(A)には、df.drop("在庫数", axis=1)が入る
      商品名   単価
0   apple  100
1  orange  150
2  banana   80
"""