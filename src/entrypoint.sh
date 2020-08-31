#!/bin/bash
wait_for () {
    for _ in `seq 0 50`; do
        (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
        if [[ $? -eq 0 ]]; then
            echo "$1:$2 accepts connections"
            break
        fi
        sleep 1
    done
}
populate_env_variables () {
  set -o allexport
  [[ -f core/.env ]] && source core/.env
  set +o allexport
  echo "env variables are populated"
}
populate_env_variables
case "$MODE" in
"DEV")
    wait_for "${DB_HOST}" "${DB_PORT}"
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
    ;;
*)
    echo "NO MODE SPECIFIED!"
    exit 1
    ;;
esac
