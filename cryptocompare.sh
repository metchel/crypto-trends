#!/usr/bin/env bash

curl -sS https://www.cryptocompare.com/api/data/coinlist | python -m json.tool > cryptocompare.json
