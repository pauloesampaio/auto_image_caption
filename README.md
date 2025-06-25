# 🧾 AI Product Description Generator

Generate tailored product descriptions from images using Google Gemini.

This project leverages a multimodal large language model (LLM) to automatically generate **high-quality product descriptions** from a single image input — optimized for **SEO**, **Millennials**, and **Gen-Z** audiences.

It’s ideal for e-commerce teams looking to **scale A/B testing**, **personalize listings**, or **automate long-tail product copy**.

---

## 🎯 Use Case

Writing unique, audience-tailored product descriptions for hundreds or thousands of items is time-consuming. With this tool, you can:

- 🧠 Automatically generate three versions of a description from one image
- 🎯 Target different user groups (SEO bots, Millennials, Gen-Z)
- ⚡ Scale fast while keeping human-level creativity
- 💼 Free up marketing teams to focus on high-impact products

---

## 🧩 Features

- 🖼 Upload a product image (e.g. dress, sneaker, bag)
- ✨ Google **Gemini Pro Vision** for multimodal understanding
- 📝 Generates three copy variants:
  - SEO-optimized (keyword-rich)
  - Millennial-friendly (emotional/lifestyle tone)
  - Gen-Z-friendly (slang, emojis, playful style)
- 🧪 Built-in Streamlit UI for experimentation
- 📥 Export descriptions in CSV or JSON format

---

## 💡 Technologies

- **Google Gemini Pro Vision** – Image-to-text via Gemini API
- **Python** – Core backend and logic
- **Streamlit** – Interactive web interface
- **Pandas / JSON** – Output formatting and export
- _(Optional: FAISS)_ – Used in related style-based product search module

---

## 🚀 Quick Start

This code requires access to Google Gemini 2.0 flash (set up credentials as .env variables accordingly, as on the .env_example)

### 1. Clone the repo

```bash
git clone https://github.com/pauloesampaio/auto_image_caption.git
cd product-caption-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run app

```bash
streamlit run app.py
```

### 3. Run app

```bash
streamlit run app.py
```
