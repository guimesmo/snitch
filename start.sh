#!/bin/bash
# see scripts/debian-init.d for production deployments

export PYTHONPATH=`dirname $0`
twistd -n cyclone -p 8000 -l 0.0.0.0 \
       -r snitch.web.Application -c snitch.conf $*
