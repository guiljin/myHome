#!/bin/sh
export PYTHONPATH=${WORKDIR}/Source
export LD_LIBRARY_PATH=${SVNCPP_LIB}
export DYLD_LIBRARY_PATH=${SVNCPP_LIB}
${PYTHON} $*
