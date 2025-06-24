# Unni 公式サイト

これは実際の企業用に制作したウェブサイトです。Flask によるフォーム処理や、生成AIのAPI接続を想定した構成など、フルスタック開発のスキルを示す目的で公開しています。

## 🛠️ 使用技術

- フロントエンド: HTML / Tailwind CSS / Flowbite
- バックエンド: Python / Flask
- メール送信: Flask-Mail

## 🔑 主な機能

- レスポンシブデザインによる企業紹介ページ
- お問い合わせフォーム（バリデーション付き）
- メール送信機能（SMTP経由）
- .envによる機密情報の管理
- Hugging FaceのChatbot API連携

## 📁 プロジェクト構成

.
├── app.py
├── README.md
├── requirements.txt
├── routes
│   ├── contact.py
│   ├── factory.py
│   ├── main.py
│   ├── product.py
│   ├── profile.py
│   └── services.py
├── static
│   ├── css
│   ├── images
│   ├── js
│   └── products.json
└── templates
    ├── base.html
    ├── contact.html
    ├── factory.html
    ├── footer.html
    ├── header.html
    ├── index.html
    ├── product.html
    ├── profile.html
    └── services.html

7 directories, 19 files

## 🔧 セットアップ方法

```bash
git clone https://github.com/irin1996/unni_website.git
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # ここに環境変数を設定
python app.py


