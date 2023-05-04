#!/bin/env/python

import os

from subprocess import call


if __name__ == '__main__' and 'TRAVIS' in os.environ:
    rc = call('coveralls')
    raise SystemExit(rc)
