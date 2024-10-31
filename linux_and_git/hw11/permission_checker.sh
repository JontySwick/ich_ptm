#!/bin/bash

set -e

GROUP_NAME="290724-ptm"

ls -la /opt/$GROUP_NAME/ | awk -F ' ' '{print $1}'

chmod u+x /opt/$GROUP_NAME/*.sh
