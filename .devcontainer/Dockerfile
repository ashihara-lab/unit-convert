FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /workspace

# Pythonの基本的なツールをインストール
RUN pip install --upgrade pip

# よく使用されるPython開発ツールをインストール
RUN pip install pytest pytest-cov black flake8 mypy

# ユーザーを作成（セキュリティのため）
RUN useradd -m -s /bin/bash vscode
USER vscode

# 作業ディレクトリの権限を設定
USER root
RUN chown -R vscode:vscode /workspace
USER vscode 