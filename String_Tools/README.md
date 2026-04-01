# String_Tools

文字列を簡単に操作するための小さなツール群です。

- `revstr/`: 文字列をリバースするツール
- `rndgen/`: ランダム文字列ジェネレータ（`revstr` 連携オプションあり）

## Quick Start

```bash
cd String_Tools/revstr
python src/reverse.py "Reverse me!"

cd ../rndgen
python src/rndgen.py 16
python src/rndgen.py 16 --revstr
```

## テスト

```bash
cd String_Tools
python -m pytest
```

