## About

addictで作成されたデフォルトの設定データに対して、yamlファイル用いて 設定を更新するライブラリ

用途としては、深層学習などで学習設定を色々変更して試す際などに、pythonコードを変更するのではなく、

yamlファイルの変更によって設定を反映させる

## Getting Started

### Install

`pip install git+https://github.com/OhkuboSGMS/sandbox.git#subdirectory=yaml_config`

## Usage

デフォルト設定がされたconfigにyamlの設定を反映

```python
from ymlc import update_config
from addict import Dict

CONFIG = Dict()

CONFIG.OPTIMIZER.ALPHA = 0.1
CONFIG.OPTIMIZER.BETA = 0.2
CONFIG.BATCH_SIZE = 16
yaml_file = "demo.yaml"
> "demo.yaml"
"""
OPTIMIZER:
  ALPHA : 0.01
  BETA : 10
BATCH_SIZE: 32
"""
print(CONFIG)
> {'OPTIMIZER': {'ALPHA': 0.1, 'BETA': 0.2}, 'BATCH_SIZE': 16}
update_config(CONFIG, yaml_file)
print(CONFIG)
# 設定を反映
> {'OPTIMIZER': {'ALPHA': 0.01, 'BETA': 10}, 'BATCH_SIZE': 32}

```

デフォルト設定のconfigをyamlに出力

```python
from ymlc import write_config
from addict import Dict

CONFIG = Dict()
CONFIG.OPTIMIZER.ALPHA = 0.1
write_config(CONFIG, "demo2.yaml")

```