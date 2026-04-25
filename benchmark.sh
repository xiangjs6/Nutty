MODE="${1:-}" # wrap / nowrap
if [ "$MODE" != "wrap" ] && [ "$MODE" != "nowrap" ]; then
    echo "Usage: $0 [wrap|nowrap]"
    exit 1
fi

OS="$(uname -s)"

case "$OS" in
Linux*)
    if [ "$MODE" = "wrap" ]; then
        BASE64_CMD="base64 -w 76"
        SUFFIX="wrap"
    else
        BASE64_CMD="base64 -w 0"
        SUFFIX="nowrap"
    fi
    ;;
Darwin*)
    if [ "$MODE" = "wrap" ]; then
        BASE64_CMD="base64 -b 76"
        SUFFIX="wrap"
    else
        BASE64_CMD="base64 -b 0"
        SUFFIX="nowrap"
    fi
    ;;
*)
    echo "Unsupported OS: $OS"
    exit 1
    ;;
esac

FILE="/tmp/benchmark_randomdata_${SUFFIX}"

# Generate 100MiB data.
if [ ! -f "$FILE" ]; then
    echo "Generating $FILE ..."
    cat /dev/urandom | ${BASE64_CMD} |
        dd of="$FILE" bs=1048576 count=100 iflag=fullblock
fi

echo "Benchmark Result ($SUFFIX):"
{ time dd if=$FILE bs=10240; }
