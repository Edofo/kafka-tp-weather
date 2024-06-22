#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kafka import KafkaConsumer
import json
import time
import argparse
import uuid
import random

parser = argparse.ArgumentParser(description='Kafka consumer test')
parser.add_argument('-topic', type=str, help='Name of the topic', required=True)
parser.add_argument('-kafka_host', type=str, help='Kafka host', required=True)
parser.add_argument('-kafka_port', type=str, help='Kafka port', required=True)

args = parser.parse_args()
if args.topic is None or args.kafka_host is None or args.kafka_port is None:
  parser.print_help()

print(args)

class KafkaSource:

  def __init__(self, host, port):
    self.consumer = KafkaConsumer(
      args.topic,
      auto_offset_reset='latest',  # 'latest',
      bootstrap_servers=f'{host}:{port}')

  def ingest(self):
    for datum in self.source:
      print(f"Receiived {datum}, yay")


k = KafkaSource(args.kafka_host, args.kafka_port)
k.ingest()