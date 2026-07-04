#!/usr/bin/env bash
# Checks only lines 101..200 of urls.txt (the additions in v2).
# Outputs pipe-delimited to results_new.tsv: num|domain|dns(ok/fail)|final_code|final_url
set -u
INPUT="urls.txt"
OUT="results_new.tsv"
: > "$OUT"

awk -F'|' 'NR>=101 && NR<=200 {print}' "$INPUT" | \
while IFS='|' read -r num domain desc; do
  [ -z "$num" ] && continue
  url="https://$domain"
  host_only="${domain%%/*}"
  if host "$host_only" >/dev/null 2>&1; then dns="ok"; else dns="fail"; fi

  if [ "$dns" = "fail" ]; then
    echo "${num}|${domain}|fail|000|DNS_FAIL" >> "$OUT"
    echo "${num} ${domain} -> DNS_FAIL"
    continue
  fi

  read -r code finalurl < <(curl -sS -L --max-time 25 --retry 2 \
    -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15" \
    -o /dev/null \
    -w "%{http_code} %{url_effective}\n" \
    "$url" 2>/dev/null)
  code="${code:-000}"
  finalurl="${finalurl:-TIMEOUT}"
  echo "${num}|${domain}|${dns}|${code}|${finalurl}" >> "$OUT"
  echo "${num} ${domain} -> ${code} ${finalurl}"
done
echo "DONE"
