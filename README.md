# Unni｜企業公式サイト（ポートフォリオ）

実在する企業のニーズに基づき、公式ウェブサイトとして設計・実装しました。  
Flask によるフォーム処理や、生成AIのAPI連携などを含むフルスタック構成で構築されており、Webエンジニア／AI活用ポジションへの応募用ポートフォリオとして公開しています。

---

## 🛠️ 使用技術

- フロントエンド: HTML / Tailwind CSS / Flowbite / JavaScript
- バックエンド: Python / Flask
- メール送信: Flask-Mail
- API連携: Hugging Face Chatbot API
- セキュリティ対策: `.env` による機密情報の管理

## 🔑 主な機能

- レスポンシブ対応の企業紹介ページ
- お問い合わせフォーム（バリデーションあり、メール送信対応）
- `.env` による機密情報のセキュアな管理
- Hugging Face API による生成AI の導入（POST通信）

---

## 📁 プロジェクト構成

.
├── app.py
├── requirements.txt
├── .env.example
├── routes/
│ ├── main.py
│ ├── contact.py
│ ├── factory.py
│ ├── profile.py
│ ├── product.py
│ └── services.py
├── static/
│ ├── css/
│ ├── images/
│ ├── js/
│ └── products.json
└── templates/
├── base.html
├── header.html
├── footer.html
├── index.html
├── contact.html
├── factory.html
├── profile.html
├── product.html
└── services.html

## 🚀 セットアップ方法

```bash
git clone https://github.com/irin1996/unni_website.git
cd backend
python -m venv venv
source venv/bin/activate  # Windows の場合: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # .env に環境変数を設定
python app.py
