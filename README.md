# Unni 公式サイト（作品集）

これは実際の企業用に制作したウェブサイトです。Flask によるフォーム処理や、生成AIのAPI接続を想定した構成など、フルスタック開発のスキルを示す目的で公開しています。

## 🛠️ 使用技術

- フロントエンド: HTML / Tailwind CSS / Flowbite
- バックエンド: Python / Flask
- メール送信: Flask-Mail
- デプロイ環境: [Render / GitHub Pages]

## 🔑 主な機能

- レスポンシブデザインによる企業紹介ページ
- お問い合わせフォーム（バリデーション付き）
- メール送信機能（SMTP経由）
- .envによる機密情報の管理
- Hugging FaceのChatbot API連携

## 📁 プロジェクト構成

（可以贴上 tree 命令结果）

## 🔧 セットアップ方法

```bash
git clone https://github.com/yourname/unni-portfolio.git
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # ここに環境変数を設定
python app.py

## 🔐 環境変数設定（.envファイル）

本プロジェクトでは、メール送信機能にGmailのSMTPを利用しています。  
セキュリティ保護のため、メールアカウントとパスワードは `.env` に設定してください。

### 1. `.env` ファイルをプロジェクトルートに作成

以下のように `.env` を作成してください（ファイルはアップロードしないでください）：

```env
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_generated_app_password
