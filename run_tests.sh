#!/bin/bash
_status=0

_message() {
  _length=$(expr length "$1")
  echo "$1"
  while [[ $_length -gt 0 ]]; do
    printf "-"
    let _length-=1
  done
  printf "\n"
}

_update_status() {
  _status=$(($_status + $1))
}

_message "RUNNING UNIT TESTS"
python2 unit_tests.py
_update_status $?

printf "\n\n"

_message "RUNNING ACCEPTANCE TESTS"
behave
_update_status $?
