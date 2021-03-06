from addict import Dict

from ymlc import update_config


# try:
#     from absl import app
#     from absl import flags
#
#     can_import_absl = True
# except ImportError as e:
#     warnings.warn(e)
#     flags.DEFINE_string("config", "", "Config File Path")
#     FLAGS = flags.FLAGS


def test_update_config():
    config_yaml_file = "config.yaml"
    CONFIG = Dict()
    CONFIG.NUM_CLASSES = 30
    CONFIG.Hi.C = "500ml"
    CONFIG.Hi.B = "250ml"
    assert CONFIG.Hi.C == "500ml"
    assert CONFIG.NUM_CLASSES == 30
    # ファイルベースでのアップデート
    CONFIG = update_config(CONFIG, config_yaml_file)
    assert CONFIG.Hi.C == "250ml"
    assert CONFIG.NUM_CLASSES == 12
    # インスタンスベースでのアップデータ　
    new_config = Dict()
    new_config.Hi.C = '300ml'
    new_config.NUM_CLASSES = 6
    print(CONFIG)
    CONFIG = update_config(CONFIG, new_config)

    assert CONFIG.Hi.C == '300ml'
    assert CONFIG.NUM_CLASSES == 6
    print(CONFIG)
