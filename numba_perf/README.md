# Numbaパフォーマンス計測　
- python 3.7.10
- numba 0.54.0
- llvmlite 0.37.0
- numpy 1.20.3

### perf_sum.py

単純な総和による比較

関数実行の一度目はJITによるコンパイルのため，若干時間が必要だが，
それ以降であれば，計算処理時間に明確な違いが生じている
```text

python numba_perf/perf_sum.py

Count: 10
Python:0.0000056  seconds
Numba 0.1846470  seconds <- JITによる影響が高い
Count: 10
Python:0.0000048  seconds
Numba 0.0000021  seconds <- コンパイル済みであれば明確に性能向上
Count: 1000
Python:0.0002117  seconds
Numba 0.0000007  seconds
Over Time Limit
Count: 100000000
Python:10.0000378  seconds　<- 10秒で打ち切っているためそれ以上かかっていると想定される
Numba 0.0000051  seconds
Over Time Limit
Count: 1000000000
Python:10.0000377  seconds
Numba 0.0000050  seconds

```