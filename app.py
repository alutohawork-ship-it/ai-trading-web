# Let's inspect what we need to produce or generate. 
# The user wants:
# 1. UI style: Premium & Mewah (Luxury, elegant styling, high contrast so text is clearly visible/tidak terlihat gelap/tulisan terlihat jelas).
# 2. TP Parameters: Take Profit dibuat berjenjang (TP1 1:1, TP2 1:2, TP3 1:3).
# Let's create a rich, beautifully styled PDF cheat sheet / trading plan document (or dashboard UI design / visual template) incorporating these exact updates!

from weasyprint import HTML

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Trading Plan & Signal Dashboard - Premium Edition</title>
    <style>
        @page {
            size: A4;
            margin: 12mm 10mm;
            background-color: #0f141d; /* Elegant deep luxury navy background */
        }
        
        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background-color: #0f141d;
            color: #f0f4f8; /* Ultra clear high contrast light text */
            margin: 0;
            padding: 0;
            font-size: 10pt;
            line-height: 1.5;
        }

        /* Header luxury styling */
        .header {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid #334155;
            border-left: 5px solid #d97706; /* Golden amber accent */
            border-radius: 8px;
            padding: 16px 20px;
            margin-bottom: 18px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }

        .header table {
            width: 100%;
            border-collapse: collapse;
        }

        .brand-title {
            font-size: 18pt;
            font-weight: 800;
            color: #fbbf24; /* Warm Gold */
            letter-spacing: 1px;
            text-transform: uppercase;
            margin: 0;
        }

        .brand-subtitle {
            font-size: 9.5pt;
            color: #94a3b8;
            margin-top: 4px;
            font-weight: 500;
        }

        .badge-premium {
            background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
            color: #ffffff;
            font-size: 8.5pt;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
            text-align: right;
            display: inline-block;
            letter-spacing: 0.5px;
        }

        /* Card Container */
        .card {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
        }

        .card-title {
            font-size: 12pt;
            font-weight: 700;
            color: #38bdf8; /* Bright Sky Blue for headers */
            border-bottom: 2px solid #334155;
            padding-bottom: 8px;
            margin-top: 0;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Grid layout using table for print compatibility */
        .layout-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 12px;
            margin: -12px;
            margin-bottom: 6px;
        }

        .layout-cell {
            vertical-align: top;
            width: 50%;
        }

        /* Signal Box */
        .signal-box {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid #059669;
            border-radius: 8px;
            padding: 14px;
            text-align: center;
        }

        .signal-type {
            font-size: 16pt;
            font-weight: 900;
            color: #34d399; /* Emerald Green */
            letter-spacing: 1.5px;
        }

        .pair-name {
            font-size: 13pt;
            font-weight: 700;
            color: #f8fafc;
            margin-top: 4px;
        }

        /* Setup Tables */
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 6px;
        }

        .data-table th {
            background-color: #334155;
            color: #f1f5f9;
            font-size: 9pt;
            font-weight: 700;
            text-align: left;
            padding: 8px 10px;
            border-bottom: 2px solid #475569;
        }

        .data-table td {
            padding: 8px 10px;
            font-size: 9.5pt;
            border-bottom: 1px solid #334155;
            color: #f8fafc;
        }

        .tp-row-1 { background-color: rgba(16, 185, 129, 0.08); }
        .tp-row-2 { background-color: rgba(16, 185, 129, 0.15); }
        .tp-row-3 { background-color: rgba(16, 185, 129, 0.22); }

        .tp-tag {
            font-weight: 800;
            color: #34d399;
            display: inline-block;
            padding: 2px 6px;
            background: rgba(52, 211, 153, 0.15);
            border-radius: 4px;
            border: 1px solid rgba(52, 211, 153, 0.3);
        }

        .sl-tag {
            font-weight: 800;
            color: #f87171;
            display: inline-block;
            padding: 2px 6px;
            background: rgba(248, 113, 113, 0.15);
            border-radius: 4px;
            border: 1px solid rgba(248, 113, 113, 0.3);
        }

        .ratio-badge {
            font-size: 8.5pt;
            font-weight: 700;
            color: #fbbf24;
            background: rgba(251, 191, 36, 0.15);
            padding: 2px 8px;
            border-radius: 12px;
            border: 1px solid rgba(251, 191, 36, 0.3);
        }

        /* Checklists & Points */
        .checklist-item {
            padding: 6px 0;
            border-bottom: 1px solid #334155;
            color: #e2e8f0;
            font-size: 9pt;
        }

        .checklist-item:last-child {
            border-bottom: none;
        }

        .check-icon {
            color: #38bdf8;
            font-weight: bold;
            margin-right: 6px;
        }

        .footer-note {
            text-align: center;
            font-size: 8.5pt;
            color: #64748b;
            margin-top: 15px;
            border-top: 1px solid #334155;
            padding-top: 10px;
        }

    </style>
</head>
<body>

    <!-- Header Section -->
    <div class="header">
        <table>
            <tr>
                <td>
                    <div class="brand-title">TRADING PLAN & UI SPECIFICATION</div>
                    <div class="brand-subtitle">Smart Money Concepts & ICT Logic System — Luxury Premium Mode</div>
                </td>
                <td style="text-align: right;">
                    <div class="badge-premium">PREMIUM GOLD UI</div>
                </td>
            </tr>
        </table>
    </div>

    <!-- Main Layout Grid -->
    <table class="layout-table">
        <tr>
            <!-- Left Column: Signal & Multi-Tier TP -->
            <td class="layout-cell">
                <div class="card">
                    <div class="card-title">1. Structure & Execution Setup</div>
                    
                    <div class="signal-box">
                        <div class="signal-type">BUY LIMIT / ENTRY ZONE</div>
                        <div class="pair-name">XAUUSD (GOLD)</div>
                    </div>

                    <table class="data-table" style="margin-top: 12px;">
                        <thead>
                            <tr>
                                <th>Parameter</th>
                                <th>Harga / Level</th>
                                <th>Keterangan</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Entry Zone</strong></td>
                                <td style="color: #38bdf8; font-weight: bold;">2645 - 2648</td>
                                <td>Fresh OB + FVG M5/M15</td>
                            </tr>
                            <tr>
                                <td><strong>Stop Loss (SL)</strong></td>
                                <td><span class="sl-tag">2638</span></td>
                                <td>Invalidation Low / Inducement</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="card">
                    <div class="card-title">2. Target Profit Berjenjang (Multi-TP)</div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Level Target</th>
                                <th>Target Price</th>
                                <th>Risk : Reward</th>
                                <th>Aksi Manajemen</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="tp-row-1">
                                <td><span class="tp-tag">TP 1</span></td>
                                <td style="font-weight: bold; color: #f8fafc;">2653</td>
                                <td><span class="ratio-badge">1 : 1</span></td>
                                <td>Set BEP / Ambil Partial 30%</td>
                            </tr>
                            <tr class="tp-row-2">
                                <td><span class="tp-tag">TP 2</span></td>
                                <td style="font-weight: bold; color: #f8fafc;">2660</td>
                                <td><span class="ratio-badge">1 : 2</span></td>
                                <td>Lock Profit / Ambil Partial 40%</td>
                            </tr>
                            <tr class="tp-row-3">
                                <td><span class="tp-tag">TP 3</span></td>
                                <td style="font-weight: bold; color: #f8fafc;">2667</td>
                                <td><span class="ratio-badge">1 : 3</span></td>
                                <td>Run Sisa Position ke HTF SNR</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </td>

            <!-- Right Column: UI & Analysis Rules -->
            <td class="layout-cell">
                <div class="card">
                    <div class="card-title">3. Peningkatan Visual UI (Kontras Tinggi)</div>
                    <div class="checklist-item"><span class="check-icon">✓</span> <strong>Background Deep Luxury Navy (#0f141d):</strong> Warna gelap yang tidak buram dan memberikan kesan premium.</div>
                    <div class="checklist-item"><span class="check-icon">✓</span> <strong>Teks High Contrast (#f0f4f8):</strong> Warna putih terang berkilau sehingga semua teks dan angka terbaca sangat jelas.</div>
                    <div class="checklist-item"><span class="check-icon">✓</span> <strong>Gold & Emerald Accent:</strong> Aksen emas (#fbbf24) dan hijau emerald (#34d399) untuk identifikasi zona penting secara instan.</div>
                    <div class="checklist-item"><span class="check-icon">✓</span> <strong>Border & Padding Presisi:</strong> Layout rapi berstruktur tanpa elemen berantakan.</div>
                </div>

                <div class="card">
                    <div class="card-title">4. Checklist Konfirmasi Analisa</div>
                    <div class="checklist-item"><span class="check-icon">✓</span> <strong>SMC / Kill Zone:</strong> Asia/London Session Inducement Sweep.</div>
                    <div class="checklist-item"><span class="check-icon">✓</span> <strong>Zona Premium/Discount:</strong> Entry berada di area Discount 61.8% - 78.6% Retracement Fibo.</div>
                    <div class="checklist-item"><span class="check-icon">✓</span> <strong>Liquidity Void / FVG:</strong> Imbalance terkonfirmasi terisi sebelum bounce.</div>
                    <div class="checklist-item"><span class="check-icon">✓</span> <strong>RRR Berjenjang:</strong> Terstruktur secara otomatis (1:1, 1:2, 1:3).</div>
                </div>
            </td>
        </tr>
    </table>

    <div class="footer-note">
        UI Spec & Trading Setup Generated Automatically • System Mode: LuxAlgo SMC + ICT Logic • Premium High-Contrast Theme
    </div>

</body>
</html>
"""

with open("trading_ui_plan.html", "w", encoding="utf-8") as f:
    f.write(html_content)

HTML("trading_ui_plan.html").write_pdf("Trading_Plan_UI_Premium.pdf")
print("PDF Generated successfully!")
