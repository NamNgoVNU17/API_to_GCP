# 🇺🇸 USD Exchange Rates to Vietnam's Top 10 Export Markets

This project collects and visualizes historical USD exchange rates to the top 10 countries importing the most from Vietnam, leveraging Google Cloud Platform (GCP) services for scalable data processing and storage. It enables analysts and decision-makers to better understand currency fluctuations that may impact international trade.

## 📊 Dashboard

View the interactive Looker Studio dashboard:  
🔗 [USD Exchange Rates Dashboard](https://lookerstudio.google.com/reporting/d6b2ba5d-4000-444d-b544-bb8fabe525f0)

## 🌍 Target Countries and Currencies

The following countries are the top destinations for Vietnamese exports, based on recent trade data. This project tracks USD exchange rates to their respective currencies.

| No. | Country         | Currency Code | Currency Name           |
|-----|------------------|----------------|--------------------------|
| 1   | United States    | USD            | US Dollar               |
| 2   | China            | CNY            | Chinese Yuan            |
| 3   | Japan            | JPY            | Japanese Yen            |
| 4   | South Korea      | KRW            | South Korean Won        |
| 5   | Hong Kong        | HKD            | Hong Kong Dollar        |
| 6   | India            | INR            | Indian Rupee            |
| 7   | United Kingdom   | GBP            | British Pound Sterling  |
| 8   | Germany          | EUR            | Euro                    |
| 9   | Netherlands      | EUR            | Euro                    |
| 10  | Australia        | AUD            | Australian Dollar       |

> Note: Both Germany and the Netherlands use the Euro (EUR).

## 📦 Data Source

- 📡 **API**: [exchangerate.host](https://exchangerate.host/)
- Supports historical and real-time exchange rates
- Free 100 request / monthly (API key required)

Example endpoint for historical rates:
```bash
https://api.exchangerate.host/timeframe?source=USD&currencies=CNY,JPY,KRW,HKD,INR,GBP,EUR,AUD&start_date=2015-01-01&end_date=2025/07/07
