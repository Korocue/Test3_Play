# rndgen Usage

`rndgen` はランダム文字列を生成する CLI ツールです。

- 既定では暗号学的に安全な乱数（`secrets.SystemRandom`）で生成します
- `--seed` を指定した場合は再現性のため `random.Random(seed)` を使います（セキュリティ用途には不向き）
- `--revstr` を指定すると、`String_Tools/revstr/src/reverse.py` の `reverse_string()` を import してリバースします

## 基本

```bash
cd String_Tools/rndgen
python src/rndgen.py 16
python src/rndgen.py 32 --count 3
```

## 文字種（`--preset`）

プリセットで文字集合を選べます（`--alphabet` を指定すると `--preset` は無視されます）。

- `alnum`: 英大小 + 数字（既定）
- `letters`: 英大小
- `lower`: 英小
- `upper`: 英大
- `digits`: 数字
- `hex`: 0-9 + a-f
- `base64url`: 英大小 + 数字 + `-` + `_`
- `printable`: 空白類を除いた printable

例:

```bash
cd String_Tools/rndgen
python src/rndgen.py 24 --preset digits
python src/rndgen.py 32 --preset hex
python src/rndgen.py 22 --preset base64url
```

## 曖昧文字の除外（`--no-ambiguous`）

`0/O` や `1/l/I` を除外します（プリセット利用時に有効）。

```bash
cd String_Tools/rndgen
python src/rndgen.py 20 --no-ambiguous
python src/rndgen.py 20 --preset base64url --no-ambiguous
```

## カスタム文字集合（`--alphabet`）

任意の文字集合から生成できます（この場合 `--preset` は無視されます）。

```bash
cd String_Tools/rndgen
python src/rndgen.py 16 --alphabet "abc123"
python src/rndgen.py 12 --alphabet "@#$%&*"
```

## 再現性（`--seed`）

同じ引数なら同じ出力にできます（テストやデバッグ用）。

```bash
cd String_Tools/rndgen
python src/rndgen.py 16 --seed 1
python src/rndgen.py 16 --seed 1
```

## リバース

### 生成後にローカルでリバース（`--reverse`）

```bash
cd String_Tools/rndgen
python src/rndgen.py 16 --seed 1 --reverse
```

### `revstr` 連携でリバース（`--revstr`）

`revstr` の実装を使ってリバースします（連携を想定したオプション）。

```bash
cd String_Tools/rndgen
python src/rndgen.py 16 --seed 1 --revstr
```

### `--reverse` と `--revstr` の併用

両方指定すると「ローカルでリバース → revstr でもう一度リバース」なので、結果的に元に戻ります（同じ関数を 2 回当てるのと同等）。

```bash
cd String_Tools/rndgen
python src/rndgen.py 16 --seed 1 --reverse --revstr
```

## 出力の扱い（ファイル/パイプ）

```bash
cd String_Tools/rndgen
python src/rndgen.py 16 --count 10 > out.txt
python src/rndgen.py 32 --count 5 | Select-Object -First 1
```

## Python から利用（ライブラリとして）

`src/rndgen.py` には生成関数があります。

```python
from rndgen import build_alphabet, generate_random_string

alphabet = build_alphabet("base64url", no_ambiguous=True)
token = generate_random_string(24, alphabet)
print(token)
```
