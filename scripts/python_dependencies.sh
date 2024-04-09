#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/bus_resv/requirements.txt
sudo chmod 777 /home/ubuntu/bus_resv
sudo chmod 777 /home/ubuntu/bus_resv/db.sqlite3
