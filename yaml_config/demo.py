from ymlc import update_config,write_config
from addict import Dict

if __name__ == '__main__':
    CONFIG = Dict()

    CONFIG.OPTIMIZER.ALPHA = 0.1
    CONFIG.OPTIMIZER.BETA = 0.2

    CONFIG.BATCH_SIZE = 16
    yaml_file = "demo.yaml"
    print(CONFIG)
    update_config(CONFIG, yaml_file)
    print(CONFIG)

    write_config(CONFIG,"demo2.yaml")




