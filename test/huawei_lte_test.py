#!/usr/bin/env python3
"""
Example code on how to print ~all info about your router, you can try it by running:
python3 data_dump.py http://admin:PASSWORD@192.168.8.1/
"""
from argparse import ArgumentParser
import os.path
import pprint
import sys
from typing import Any, Callable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))

from huawei_lte_api.Client import Client  # noqa: E402
from huawei_lte_api.Connection import Connection  # noqa: E402


parser = ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('--username', type=str)
parser.add_argument('--password', type=str)
args = parser.parse_args()


def dump(method: Callable[[], Any]) -> None:
    print("==== %s" % method.__qualname__)
    try:
        pprint.pprint(method())
     
    except Exception as e:
        print(str(e))
    print("")


with Connection(args.url, username=args.username, password=args.password) as connection:
    client = Client(connection)

    dump(client.device.information)
    print(client.device.information)

   