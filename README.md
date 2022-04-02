# OverView

情報検索プログラミングの学習用レポ兼FastAPIのキャッチアップ用レポ

## 使用技術

- Python
- FastAPI(PythonのAPIフレームワーク)
- SQLite3
- MeCab(形態素解析エンジン)
- Docker

## 数式メモ

<img src=
"https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bblack%7D%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Asim%28q%2Cd_i%29+%3D+%5Cfrac%7B%5Csum_%7Bj%3D1%7D%5Et+w_%7Bqj%7Dw_%7Bij%7D%7D%7B%5Csqrt%7B%5Csum_%7Bj%3D1%7D%5Et+w_%7Bqj%7D%5E2%7D+%5Csqrt%7B%5Csum_%7Bj%3D1%7D%5Et+w_%7Bij%7D%5E2%7D%7D%0A%5Cend%7Balign%2A%7D%0A"
alt="\begin{align*}
sim(q,d_i) = \frac{\sum_{j=1}^t w_{qj}w_{ij}}{\sqrt{\sum_{j=1}^t w_{qj}^2} \sqrt{\sum_{j=1}^t w_{ij}^2}}
\end{align*}
">
