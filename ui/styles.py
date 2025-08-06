import streamlit as st


def inject_css() -> None:
    st.markdown(
        '''
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@300;400;500;600;700&display=swap');

        :root {
            --bg:            hsl(215, 22%, 4%);
            --bg-raised:     hsl(215, 20%, 6%);
            --bg-panel:      hsl(215, 18%, 8%);
            --bg-hover:      hsl(215, 16%, 11%);
            --rule:          hsl(215, 14%, 14%);
            --rule-strong:   hsl(215, 12%, 20%);
            --rule-accent:   hsl(38, 98%, 50%);
            --amber:         hsl(38, 98%, 50%);
            --amber-bright:  hsl(42, 100%, 62%);
            --amber-dim:     hsla(38, 98%, 50%, 0.08);
            --amber-glow:    hsla(38, 98%, 50%, 0.18);
            --amber-border:  hsla(38, 98%, 50%, 0.28);
            --cyan:          hsl(185, 75%, 48%);
            --cyan-dim:      hsla(185, 75%, 48%, 0.10);
            --red:           hsl(4, 78%, 58%);
            --red-dim:       hsla(4, 78%, 58%, 0.09);
            --text-hi:       hsl(215, 15%, 90%);
            --text-md:       hsl(215, 10%, 65%);
            --text-lo:       hsl(215, 8%, 40%);
            --text-ghost:    hsl(215, 6%, 25%);
            --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
            --font-serif: 'Instrument Serif', Georgia, serif;
            --u1: 4px; --u2: 8px; --u3: 12px; --u4: 16px;
            --u5: 20px; --u6: 24px; --u8: 32px; --u10: 40px;
        }

        *, *::before, *::after { box-sizing: border-box; }

        html, body, [class*="css"] {
            font-family: var(--font-mono) !important;
            color: var(--text-md) !important;
            -webkit-font-smoothing: antialiased;
        }

        .stApp {
            background: var(--bg) !important;
            background-image: radial-gradient(circle, hsl(215, 14%, 12%) 1px, transparent 1px) !important;
            background-size: 24px 24px !important;
        }

        #MainMenu, footer, header { visibility: hidden !important; }
        .stDeployButton { display: none !important; }

        .block-container {
            padding-top: 0 !important;
            padding-bottom: 6rem !important;
            max-width: 100% !important;
        }

        hr {
            border: none !important;
            border-top: 1px solid var(--rule) !important;
            margin: var(--u4) 0 !important;
        }
        </style>
        ''',
        unsafe_allow_html=True,
    )
