# Test3_Play

このリポジトリは「Codexに指示 → 実装/修正 → 検証」を何度も回すための練習場です（PR練習も可）。

## 収録物

- `Number_Game/`: シンプルな数当てゲーム（Python）

## 必要環境

- Python 3.10+（目安）

## Number_Game

1〜100 の数字を、最大 8 回の試行で当てるゲームです。入力に応じて「もっと大きい/小さい」のヒントが出ます。

### 実行方法

プロジェクト直下から実行:

```bash
python Number_Game/src/game.py
```

`Number_Game/` に移動して実行:

```bash
cd Number_Game
python src/game.py
```

（環境によっては `python -m src.game` でも動きますが、動かない場合は上記の `python src/game.py` を使ってください）

### テスト

```bash
cd Number_Game
python -m pytest
```

## ディレクトリ構成

```text
./
  README.md
  Number_Game/
    src/
      game.py
    tests/
      test_game.py
```

## Codex運用ルール（おすすめ）

反復実験が散らからないように、毎回「変更範囲」と「合格条件」を固定します。

- 変更は対象フォルダ配下だけ（例: `Number_Game/` のみ）
- 指示はファイルに残す（例: `PROMPT.md`）
- 合格条件/チェック観点もファイルに残す（例: `ACCEPTANCE.md`）

必要になったら、実験フォルダを `plays/<experiment>/` のように増やしていく運用も検討してください。
