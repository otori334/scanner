#!/bin/zsh

IFS=$'\n'
readonly PY="aaaaa/.env/bin/python3"
# 環境に応じた^^^^^^記入が必要

readonly CMD_NAME="${0##*/}"
readonly CMD_DIR="${0%/${CMD_NAME}}"
readonly TMP_DIR="/tmp/${CMD_NAME%.*}_"$$
readonly DEST_DIR="${1%/}/../${1##*/}_"
readonly PY_DIR="${CMD_DIR}/py"
readonly PROCESS_010="${PY_DIR}/homography.py"
readonly PROCESS_020="${PY_DIR}/threshold_otsu.py"
readonly PROCESS_030="${PY_DIR}/graphics.py"
readonly PROCESS_040="${PY_DIR}/threshold.py"
readonly PROCESS_050="${PY_DIR}/trim.py"
readonly PROCESS_060="${PY_DIR}/closing.py"
trap 'rm -rf "${TMP_DIR}" && exit' 0 1 2 3 15 && mkdir -p "${TMP_DIR}"


if [ $# -ne 1 ]; then
    echo "${CMD_NAME}: Please specify 1 directory." 1>&2
    exit
elif [ ! -d "$1" ]; then
    echo "${CMD_NAME}: $1: No such directory." 1>&2
    exit
fi

if [ -d "${DEST_DIR}" ]; then
    rm -rf "${DEST_DIR}"
    mkdir "${DEST_DIR}"
else
    mkdir "${DEST_DIR}"
fi

for file in $(ls "${1%/}/"*.(png|PNG|jpg|jpeg|JPG|JPEG)); do
    # echo "${file}"
    tmp_name="${TMP_DIR}/${${file##*/}%.*}.png"
    dest_name="${DEST_DIR}/${tmp_name##*/}"
    eval \"${PY}\" \"${PROCESS_010}\" \"${file}\" \"${tmp_name}\"
    eval \"${PY}\" \"${PROCESS_020}\" \"${tmp_name}\" \"${tmp_name}\"
    eval \"${PY}\" \"${PROCESS_030}\" \"${tmp_name}\" \"${tmp_name}\"
    #eval \"${PY}\" \"${PROCESS_040}\" \"${tmp_name}\" \"${tmp_name}\"
    eval \"${PY}\" \"${PROCESS_040}\" \"${tmp_name}\" \"${dest_name}\"
    #eval \"${PY}\" \"${PROCESS_050}\" \"${file}\" \"${dest_name}\"
    #eval \"${PY}\" \"${PROCESS_060}\" \"${file}\" \"${dest_name}\"
done
