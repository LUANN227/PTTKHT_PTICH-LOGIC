#!/bin/sh
# Xuất mọi .drawio trong thư mục (đệ quy) thành .svg và .png cùng tên.
# Dùng: sh render_all.sh <thư mục>   (cần Node và Playwright Chromium)
D=$(cd "$(dirname "$0")" && pwd)
find "$1" -name '*.drawio' | while read f; do
  b="${f%.drawio}"
  node "$D/render.mjs" "$f" "$b.svg" "$b.png" 1.6 || echo "LỖI: $f"
done
