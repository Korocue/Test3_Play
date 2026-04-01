# rndgen

ランダム文字列を生成する小さなツールです。単体で起動でき、`revstr` 連携（生成後に `revstr` の関数でリバース）も可能です。

より詳細な使用法・用例は `Usage.md` を参照してください。

## 使い方（単体）

```bash
cd String_Tools/rndgen
python src/rndgen.py 16
python src/rndgen.py 32 --count 3
python src/rndgen.py 24 --preset hex
python src/rndgen.py 20 --no-ambiguous
python src/rndgen.py 16 --alphabet "abc123"
```

## `revstr` 連携（リバース）

`--revstr` を付けると、`String_Tools/revstr/src/reverse.py` の `reverse_string()` を import してリバースします。

```bash
cd String_Tools/rndgen
python src/rndgen.py 16 --revstr
```

※ `--seed` は再現性のための機能で、セキュリティ用途には向きません。

## テスト

```bash
cd String_Tools
python -m pytest
```
