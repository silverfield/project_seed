CUR_DIR=`pwd`
SCRIPT_PATH=`realpath $0`
ROOT_PATH=`dirname $SCRIPT_PATH`
SRC_PATH="$ROOT_PATH/src"

cd $ROOT_PATH

export PYTHONPATH="$PYTHONPATH;$SRC_PATH"
pipenv shell

cd $CUR_DIR

