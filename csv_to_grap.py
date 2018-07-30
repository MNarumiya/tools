# csvファイルをグラフ化する

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Jupyter用で用いる時は以下をコメントアウトから復帰させる
# %matplotlib inline

import sys


def csv_to_grap(csv_file_name,save_name_pdf):
    # dataframe = dfとする
    df = pd.read_csv(csv_file_name)
    i = 0
    for df_name in df.columns:
        print(str(i)+":"+df_name)
        i += 1
    label_number = list(map(int,input("横軸 縦軸は?数字を入れる:").split()))
    side_label_number = label_number[0]
    df_col_name = df.columns # データの横軸ラベル(パラメーター名)を取得
    df_sorted = df.sort_values(by=df_col_name[side_label_number], ascending=True) # データを昇順でソート

    for depth_label_number in label_number[1:]:
        plt.plot(df_sorted[df_col_name[side_label_number]],df_sorted[df_col_name[depth_label_number]],marker="o")

    plt.xlabel(df_sorted[df_col_name[side_label_number]].name)
    plt.ylabel(df_sorted[df_col_name[depth_label_number]].name)
    plt.legend()
    plt.savefig(save_name_pdf) # pdfファイルとして保存


if __name__ == '__main__':
    args = sys.argv # コマンドライン引数を受け取る
    if (len(args) < 3): # csvファイル名とPDFファイル名がない場合受け付けない
        print("csv_to_grap.py csvファイル名 保存したいPDfファイル名 で呼び出してください")
    else:
        csv_file_name = args[1]
        save_name_pdf = args[2]
        csv_to_grap(csv_file_name,save_name_pdf)
