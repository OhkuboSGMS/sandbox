import os

import yaml
from absl import app
from absl import flags
from addict import Dict

flags.DEFINE_string("config", "", "Config File Path")
FLAGS = flags.FLAGS
CONFIG = Dict()
CONFIG.NUM_CLASSES = 30
CONFIG.Hi.C = "500ml"
CONFIG.Hi.B = "250ml"


def allkeys(a):
    keys = list(a.keys())
    for parent, children in a.items():
        if isinstance(children, dict):
            keys.extend(parent + "." + child for child in allkeys(children))
    return keys


def update_config(config: Dict, config_file_path: str):
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(config_file_path)

    with open(config_file_path, "r") as f:
        yaml_config = yaml.load(f, Loader=yaml.FullLoader)
        yaml_keys = allkeys(yaml_config)
        config_keys = allkeys(config)
        is_invalid_args = not (set(yaml_keys) <= set(config_keys))
        # 不要な変数がある場合はエラーを表示, yaml config内でCONFIGが対応していない変数を表示
        invalid_args = set(yaml_keys) - (set(yaml_keys) & set(config_keys))
        if is_invalid_args:
            raise ValueError(f"Invalid args {invalid_args} in {yaml_keys}.")
        CONFIG.update(yaml_config)


def main(argv):
    del argv
    print(CONFIG)
    update_config(CONFIG, FLAGS.config)
    print(CONFIG)


if __name__ == '__main__':
    app.run(main)
