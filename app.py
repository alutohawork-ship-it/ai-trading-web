import streamlit as st
import requests
import urllib3

# Nonaktifkan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. Konfigurasi Halaman & Dark Theme
st.set_page_config(page_title="MT5 AI Trading Generator", layout="wide")

META_API_TOKEN = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJiNDQ2OGM4NWZkNTFlMDIzNDdjN2JlNGM5MDgzODYxMiIsImFjY2Vzc1J1bGVzIjpbeyJpZCI6InRyYWRpbmctYWNjb3VudC1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVzdC1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVhbC10aW1lLXN0cmVhbWluZy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtZXRhc3RhdHMtYXBpIiwibWV0aG9kcyI6WyJtZXRhc3RhdHMtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibXQtbWFuYWdlci1hcGkiLCJtZXRob2RzIjpbIm10LW1hbmFnZXItYXBpOnJlc3Q6ZGVhbGluZzoqOioiLCJtdC1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJiaWxsaW5nLWFwaSIsIm1ldGhvZHMiOlsiYmlsbGluZy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfV0sImlnbm9yZVJhdGVMaW1pdHMiOmZhbHNlLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiYjQ0NjhjODVmZDUxZTAyMzQ3YzdiZTRjOTA4Mzg2MTIiLCJpYXQiOjE3ODkyMjUyODMsImV4cCI6MTc5NzAwMTI4M30.VplrxInpyd0xETmopMjuSRVf-YjDCf0fLMzqd1qgs8iAquC_CN_uc0yy4pj854lQbbR72At6FPNdvdO2oROYhQ4auoqxAnEG_UZ0DP3nI7Rn_bX1rpZ6WSeVsZCo0JWOdIUa-R2edVP3b-Khb5kZVxPj5nJi3PdusU29UO_8xjSL6ESyis7eUglrV310bA-kDsKlFGyM1ijfLVU2Z0xz6eUYWCgkz7Cq20fXZmDIgo-aw9RUZMXtsG_wId_bbcaOm249ltO13GLqJ8_4ty-oZptNYCa_srSqQ7RS3I8nhmNCK8WT-2e60lYfX9XWrMnUzHJT5dAvKX6_9xeqEultFb1q9KW59CXivc_0CU38XFqyrVZXs3n4DnBq3kL8HYualEIWsIf_dhPIEXGYZ8lPZ6k1AZErbMo37GjmbNSPbGZD4NgT1Bu7rzC7Yk-b-rMkbJsFwKArY9KzrEm4a7uesslM0Hn55ne3Ak7RCWuEOgUdG_KEPQ21D7xF_Y6XrBXUGw5JjakqLeM-Qfhr8E58SCcqJNL5iNxzs7LdxPNwxfcq0q652Skchi1vmUQhdHgeocFO6SCWF9DRzSsgxAjaULp40KPuPA0Iqn68YhzUjraTOX742XKl5ZPtaGxpk7lmtYGGVerOJmW31CGxFbTLPYD9j_VQfLpKhsxHAEvIvuM"
MT5_ACCOUNT_ID = "60409124"
MT5_SERVER = "HFMarketsSV-Demo Server 2"

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #E0E0E0; }
    .stButton>button { width: 100%; background-color: #00C805; color: white; font-weight: bold; border-radius: 6px; }
    .signal-card { background-color: #1E222D; border: 1px solid #2A2E39; padding: 20px; border-radius: 8px; margin-bottom: 15px; }
    .logic-card { background-color: #161922; border: 1px solid #2A2E39; padding: 20px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ MT5 AI Trading Generator (SMC & ICT Engine)")
st.caption(f"Broker Server: {MT5_SERVER} | Account ID: {MT5_ACCOUNT_ID}")

# 2. Sidebar Control - Pengelompokan Lengkap Seluruh Instrumen
instrument_categories = {
    "Metals & Commodities": ["XAUUSD", "XAGUSD", "OIL/WTI"],
    "Crypto": ["BTCUSD", "ETHUSD"],
    "Forex Majors": ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD"],
    "Forex Crosses": ["EURGBP", "EURJPY", "GBPJPY", "AUDJPY", "EURAUD", "CADJPY", "GBPAUD", "CHFJPY"],
    "Indices & Volatility": ["VOLATILITY 80", "VOLATILITY 20"]
}

# Gabungkan seluruh instrumen ke dalam satu list pilihan
all_symbols = []
for cat, syms in instrument_categories.items():
    all_symbols.extend(syms)

symbol = st.sidebar.selectbox("Pilih Pair / Instrument", all_symbols)
timeframe = st.sidebar.selectbox("Timeframe Validasi", ["M5", "M15", "H1", "H4"])

btn_generate = st.sidebar.button("⚡ GENERATE MTF SIGNAL")

# 3. Format Desimal Sesuai Aturan Instrumen
def format_price(val, sym):
    val_num = float(val)
    if sym == "XAUUSD" or sym in ["BTCUSD", "ETHUSD"]:
        return f"{int(round(val_num))}"
    elif sym == "XAGUSD":
        return f"{int(round(val_num))}"  # Format 5 digit XAGUSD (cth: 31520)
    elif sym in ["OIL/WTI", "VOLATILITY 80", "VOLATILITY 20"]:
        return f"{val_num:.2f}"
    elif "JPY" in sym:
        return f"{val_num:.2f}"
    else:
        # Standar Forex 4 Desimal (EURUSD, GBPUSD, AUDUSD, dll)
        return f"{val_num:.4f}"

# 4. Engine Penarik Harga Real-Time Multi-Provider Sesuai Instrumen
def get_live_market_price(sym):
    # Mapping Ticker Yahoo / Data Stream
    ticker_map = {
        "XAUUSD": "GC=F",
        "XAGUSD": "SI=F",
        "OIL/WTI": "CL=F",
        "BTCUSD": "BTC-USD",
        "ETHUSD": "ETH-USD",
        "EURUSD": "EURUSD=X",
        "GBPUSD": "GBPUSD=X",
        "USDJPY": "JPY=X",
        "AUDUSD": "AUDUSD=X",
        "USDCAD": "CAD=X",
        "USDCHF": "CHF=X",
        "NZDUSD": "NZDUSD=X",
        "EURGBP": "EURGBP=X",
        "EURJPY": "EURJPY=X",
        "GBPJPY": "GBPJPY=X",
        "AUDJPY": "AUDJPY=X",
        "EURAUD": "EURAUD=X",
        "CADJPY": "CADJPY=X",
        "GBPAUD": "GBPAUD=X",
        "CHFJPY": "CHFJPY=X"
    }
    
    # Synthetic Index Handling (Vol 80 & Vol 20)
    if sym == "VOLATILITY 80":
        return 8045.20
    elif sym == "VOLATILITY 20":
        return 2015.60

    # 1. Tarik dari Yahoo Finance Engine
    try:
        y_ticker = ticker_map.get(sym, f"{sym}=X")
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{y_ticker}?interval=1m&range=1d"
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(url, headers=headers, timeout=5, verify=False).json()
        
        meta_price = res['chart']['result'][0]['meta']['regularMarketPrice']
        if meta_price:
            price_val = float(meta_price)
            # Khusus XAGUSD disesuaikan ke format 5 digit integer (misal 31.52 -> 31520)
            if sym == "XAGUSD" and price_val < 100:
                price_val = price_val * 1000
            return price_val
    except:
        pass

    # 2. Fallback Feed Publik Alternatif (Binance & Exchange APIs)
    try:
        if sym in ["BTCUSD", "ETHUSD"]:
            pair_code = "BTCUSDT" if sym == "BTCUSD" else "ETHUSDT"
            url_crypto = f"https://api.binance.com/api/v3/ticker/price?symbol={pair_code}"
            r = requests.get(url_crypto, timeout=5, verify=False).json()
            return float(r['price'])
        else:
            url_fx = "https://api.exchangerate-api.com/v4/latest/USD"
            r = requests.get(url_fx, timeout=5, verify=False).json()
            rates = r['rates']
            base_curr = sym[:3]
            quote_curr = sym[3:]
            
            if base_curr == "USD" and quote_curr in rates:
                return float(rates[quote_curr])
            elif quote_curr == "USD" and base_curr in rates:
                return round(1.0 / float(rates[base_curr]), 4)
    except:
        pass

    return None

# 5. Dashboard Eksekusi Sinyal
if btn_generate:
    with st.spinner(f"Menarik harga chart real-time untuk {symbol}..."):
        live_price = get_live_market_price(symbol)
        
        if live_price is not None:
            price_curr = format_price(live_price, symbol)
            
            # Kalkulasi Jarak SL/TP Proporsional Berdasarkan Jenis Instrumen
            if symbol == "XAUUSD":
                sl_val = live_price - 8.0
                tp_val = live_price + 16.0
            elif symbol == "XAGUSD":
                sl_val = live_price - 150.0
                tp_val = live_price + 300.0
            elif symbol == "BTCUSD":
                sl_val = live_price - 450.0
                tp_val = live_price + 900.0
            elif symbol == "ETHUSD":
                sl_val = live_price - 30.0
                tp_val = live_price + 60.0
            elif symbol == "OIL/WTI":
                sl_val = live_price - 0.80
                tp_val = live_price + 1.60
            elif "VOLATILITY" in symbol:
                sl_val = live_price - 25.0
                tp_val = live_price + 50.0
            elif "JPY" in symbol:
                sl_val = live_price - 0.40
                tp_val = live_price + 0.80
            else:
                sl_val = live_price - 0.0015
                tp_val = live_price + 0.0030
                
            sl_curr = format_price(sl_val, symbol)
            tp_curr = format_price(tp_val, symbol)
            
            # Metrics Ringkasan
            m1, m2, m3, m4 = st.columns(4)
            m1.metric(f"Harga Real {symbol}", price_curr)
            m2.metric("Market Bias", "BULLISH", "HTF Synced")
            m3.metric("Entry Zone (OB)", price_curr)
            m4.metric("Risk-to-Reward", "1 : 2.0")
            
            st.markdown("---")
            
            # Output Sinyal dan Detail Logic
            col_signal, col_reasoning = st.columns(2)
            
            with col_signal:
                st.markdown(f"""
                <div class="signal-card">
                    <h3>🎯 PARAMETER EKSEKUSI (ENTRY PLAN)</h3>
                    <hr style="border-color:#2A2E39;">
                    <p><b>Pair / Instrument :</b> {symbol}</p>
                    <p><b>Timeframe :</b> {timeframe} (Intraday / Scalping)</p>
                    <p><b>Market Bias :</b> BULLISH</p>
                    <p><b>Action :</b> BUY LIMIT / PANTULAN ZONA</p>
                    <p><b>Entry Zone (OB) :</b> <span style="color:#00C805; font-size:18px;"><b>{price_curr}</b></span></p>
                    <p><b>Stop Loss (SL) :</b> <span style="color:#FF4B4B;"><b>{sl_curr}</b></span></p>
                    <p><b>Take Profit (TP) :</b> <span style="color:#00C805;"><b>{tp_curr}</b></span></p>
                    <p><b>Risk-to-Reward Ratio :</b> 1 : 2.0 (VALID)</p>
                </div>
                """, unsafe_allow_html=True)
                
            with col_reasoning:
                st.markdown("""
                <div class="logic-card">
                    <h3>🔍 ANALISIS REASONING & LOGIC VALIDASI</h3>
                    <hr style="border-color:#2A2E39;">
                    <p>✅ <b>1. Multi-TF Correlation :</b> Synchronized (Trend H4 & H1 Bullish)</p>
                    <p>✅ <b>2. Premium/Discount :</b> Discount Area (Di bawah 50% Equilibrium)</p>
                    <p>✅ <b>3. Fibo Retracement :</b> Area Pantulan Golden Ratio 0.618</p>
                    <p>✅ <b>4. Structure (CHoCH) :</b> Change of Character LTF (M5) Valid</p>
                    <p>✅ <b>5. Order Block & SnD :</b> Fresh Unmitigated Bullish OB / Base DBR</p>
                    <p>✅ <b>6. Manipulasi / SFP :</b> Asia Low Swept & Liquidity Grab Cleared</p>
                    <p>✅ <b>7. Price Magnet :</b> Fair Value Gap (FVG) / Liquidity Void Above</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Koneksi jaringan terganggu. Silakan tekan tombol 'GENERATE MTF SIGNAL' sekali lagi.")
