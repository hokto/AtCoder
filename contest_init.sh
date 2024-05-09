#!/bin/sh
# $1: コンテスト種(ABC,AHC等)
# $2: コンテスト名(ABC系ならabc+コンテスト番号)

cd ./$1
acc new $2 # ここでコンテスト名に対応したテストケースを取得する

for i in {a..z}
do
    if [ -d ./$2/$i ] 
    then
        cp ../mylib/template.py ./$2/$i/$i.py
    fi
done

cd ../