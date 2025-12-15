# Test3_Play

このリポジトリは、Codex（CLI/IDE）に指示して試行回数を回すための練習場です（PR練習にも利用可）。

## 収録物

- `Number_Game/`: 数当てゲーム（Python）
- `String_Tools/`: 文字列を扱うためのツール（リバース機能）

## 必要環境

- Python 3.10+（目安）

## Quick Start（Number_Game）

```bash
cd Number_Game
python src/game.py
```

※ `python -m src.game` は `Number_Game/` 配下で実行する場合に利用できます。

## テスト（Number_Game）

```bash
cd Number_Game
python -m pytest
```

## Quick Start（String_Tools）

```bash
cd String_Tools
python src/reverse.py "Reverse me!"
```

## テスト（String_Tools）

```bash
cd String_Tools
python -m pytest
```

## ディレクトリ構成

```text
./
  README.md
  PROMPT.md
  ACCEPTANCE.md
  Number_Game/
    src/
      game.py
    tests/
      test_game.py
```

## Codex運用ルール（おすすめ）

- 変更範囲を固定する（例: 今回は `Number_Game/` 配下のみ）
- Codexに投げた指示は `PROMPT.md` に残す
- 合格条件・チェック観点は `ACCEPTANCE.md` に残す

