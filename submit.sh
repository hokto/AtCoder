#!/bin/sh

# $1: コンテスト種
# $2: コンテスト名
# $3: 問題名
# ($4: 提出時の言語選択，デフォルトはpypy)

cd ./$1/$2/$3/
if [ $# != 4 ]
then
    acc submit $3.py -- -l 5078
else
    if [ $4 == "pypy" ]
    then
        acc submit $3.py -- -l 5078
    elif [ $4 == "python" ]
    then
        acc submit $3.py -- -l 5055
    fi
fi
cd ../../../