import os
from pathlib import Path

import dictdiffer
import yaml
from addict import Dict


def all_keys(a):
    keys = list(a.keys())
    for parent, children in a.items():
        if isinstance(children, dict):
            keys.extend(parent + "." + child for child in all_keys(children))
    return keys


def update_config(config: Dict, config_file_path: str):
    after = config.deepcopy()
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(config_file_path)

    with open(config_file_path, "r") as f:
        yaml_config = yaml.load(f, Loader=yaml.SafeLoader)  # yamlのフォーマットが間違っている場合エラーを表示
        yaml_keys = all_keys(yaml_config)
        config_keys = all_keys(config)
        is_invalid_args = not (set(yaml_keys) <= set(config_keys))
        # 不要な変数がある場合はエラーを表示, yaml config内でCONFIGが対応していない変数を表示
        invalid_args = set(yaml_keys) - (set(yaml_keys) & set(config_keys))
        if is_invalid_args:
            raise ValueError(f"Invalid args {invalid_args} in {yaml_keys}.")
        after.update(yaml_config)
    return after


def diff(before: Dict, after: Dict):
    return dictdiffer.diff(before, after)


def write_config(config: Dict, config_file_path: str):
    with open(Path(config_file_path).with_suffix(".yaml"), "w") as f:
        yaml.dump(config.to_dict(), f)
