#!/bin/zsh

IFS=$'\n'
readonly PY="aaaaa/.env/bin/python3"
# 環境に応じた^^^^^^記入が必要

readonly CMD_NAME="${0##*/}"
readonly CMD_DIR="${0%/${CMD_NAME}}"
readonly TMP_DIR="/tmp"
readonly SHADE_DIR="${TMP_DIR}/${CMD_NAME%.*}_"$$
readonly DEST_DIR="$1/../${1##*/}_"
readonly PY_DIR="${CMD_DIR}/py"
readonly PROCESS_0="${PY_DIR}/threshold_otsu.py"
readonly PROCESS_1="${PY_DIR}/graphics.py"
readonly PROCESS_2="${PY_DIR}/threshold.py"
trap 'rm -rf "${SHADE_DIR}" && exit' 0 1 2 3 15 && mkdir -p "${SHADE_DIR}"


if [ $# -ne 1 ]; then
    echo "${CMD_NAME}: Please specify 1 directory." 1>&2
    exit
elif [ ! -d "$1" ]; then
    echo "${CMD_NAME}: $1: No such directory." 1>&2
    exit
else
    if [ -d "${DEST_DIR}" ]; then
        rm -rf "${DEST_DIR}"
        mkdir "${DEST_DIR}"
    else
        mkdir "${DEST_DIR}"
    fi
    for file in $(ls "$1/"*.(png|PNG|jpg|jpeg|JPG|JPEG)); do
        # echo "${file}"
        shade_name="${SHADE_DIR}/${${file##*/}%.*}.png"
        dest_name="${DEST_DIR}/${shade_name##*/}"
        eval \""${PY}"\" \""${PROCESS_0}"\" \""${file}"\" \""${shade_name}"\"
        eval \""${PY}"\" \""${PROCESS_1}"\" \""${shade_name}"\" \""${shade_name}"\"
        eval \""${PY}"\" \""${PROCESS_2}"\" \""${shade_name}"\" \""${dest_name}"\"
    done
fi
