#!/bin/bash

read -p "username: " USERNAME
read -sp "password: " PASSWORD

expect -c "
set timeout 3
spawn acc login
expect \"? username:\"
send \"${USERNAME}\n\"
expect \"? password:\"
send \"${PASSWORD}\n\"
expect \"$\"
exit 0
"

expect -c "
set timeout 3
spawn oj login https://atcoder.jp
expect \"Username:\"
send \"${USERNAME}\n\"
expect \"Password:\"
send \"${PASSWORD}\n\"
expect \"$\"
exit 0
"