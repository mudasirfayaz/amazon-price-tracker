# 📉 Amazon Price Tracker

A simple Python project that tracks the price of a product on Amazon and sends an email alert when the price drops below a predefined threshold.

This project demonstrates **web scraping, automation, and email notifications** in a compact end-to-end solution.

<br/>

## 🚀 Features

- Scrapes product price and title from Amazon using **BeautifulSoup**.
- Compares live price against a user-defined **target threshold**.
- Sends automated **email alerts** to multiple recipients when price drops.
- Credentials and configuration are securely handled using **`.env` variables**.

<br/>

## 🛠 Tech Stack

- **Python**
- **Requests** – for fetching HTML
- **BeautifulSoup** – for parsing product data
- **smtplib** – for email alerts
- **dotenv** – for environment variable management

<br/>

## ⚙️ Setup & Installation

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/amazon-price-tracker.git
cd amazon-price-tracker
```

<br/>

**2. Install required dependencies:**

```bash
pip install -r requirements.txt
```

<br/>

**3. Create a .env file in the root directory:**

```bash
SMTP_SERVER=smtp.gmail.com
MY_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
```

<br/>

**4. Add recipient emails in a file named recipients.txt (one per line).**

**5. Open `main.py` and set:**

- Your Amazon product URL
- Your TARGET_PRICE

<br/>

## ▶️ Usage

Run the script:

```bash
python main.py
```

If the product price is below the threshold, an email alert will be sent to all recipients.

<br/>

## 📌 Example Email Alert

```bash
Subject: Amazon Price Alert!

Sale Sale Sale!

Samsung Galaxy S24 Ultra is on sale for ₹95,499

https://www.amazon.in/example-product-url
```

<br/>

## ⚠️ Disclaimer

- This is a proof-of-concept project and not production-ready.
- Amazon frequently changes its site structure and may block scraping attempts.
- For production use, consider Amazon’s Product Advertising API.

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Python Developer | Automation Engineer | Aspiring AI/ML Specialist<br/>
_Building fun and useful Python tools_

<br/>

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

<br/>
