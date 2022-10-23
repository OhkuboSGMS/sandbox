import argparse

from switchbot import SwitchBot


def list_device(token):
    switchbot = SwitchBot(token=token)
    devices = switchbot.devices()
    for device in devices:
        print(device)
    for remote in switchbot.remotes():
        print(remote)


def main(token: str, remove_device: str, turn: bool):
    switchbot = SwitchBot(token=token)

    tv = switchbot.remote(remove_device)
    tv.command('turnOn' if turn else 'turnOff')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('switch-api')
    parser.add_argument('token', type=str)
    parser.add_argument('device', type=str)
    parser.add_argument('--on', action='store_true')
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()
    if args.list:
        list_device(args.token)
    else:
        main(args.token, args.device, args.on)
