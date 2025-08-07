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
        html, body, [class*="css"] { font-family: var(--font-mono) !important; color: var(--text-md) !important; }
        .stApp { background: var(--bg) !important; }
        #MainMenu, footer, header { visibility: hidden !important; }
        .block-container { padding-top: 0 !important; padding-bottom: 6rem !important; max-width: 100% !important; }

        /* SIDEBAR */
        [data-testid="stSidebar"] {
            background: var(--bg-raised) !important;
            border-right: 1px solid var(--rule-strong) !important;
            box-shadow: inset 0 3px 0 0 var(--amber) !important;
        }
        [data-testid="stSidebar"] > div:first-child { padding: 0 !important; }
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] .stFileUploader,
        [data-testid="stSidebar"] .stButton,
        [data-testid="stSidebar"] .stMultiSelect {
            padding-left: var(--u5) !important;
            padding-right: var(--u5) !important;
        }

        .sidebar-brand {
            padding: var(--u6) var(--u5) var(--u5);
            border-bottom: 1px solid var(--rule-strong);
            position: relative; overflow: hidden;
        }
        .sidebar-brand::before {
            content: 'CX'; font-family: var(--font-serif); font-size: 7rem;
            color: var(--rule-strong); position: absolute; right: -12px; top: -18px;
            line-height: 1; pointer-events: none; user-select: none;
        }
        .sidebar-brand .wordmark {
            font-family: var(--font-mono); font-size: 0.72rem; font-weight: 700;
            letter-spacing: 0.16em; text-transform: uppercase; color: var(--text-hi);
        }
        .sidebar-brand .wordmark em { color: var(--amber); font-style: normal; }
        .sidebar-brand .tagline {
            font-size: 0.56rem; color: var(--text-ghost); letter-spacing: 0.14em;
            text-transform: uppercase; margin-top: var(--u2);
        }

        .stat-row { display: grid; grid-template-columns: 1fr 1fr; border-bottom: 1px solid var(--rule-strong); }
        .stat-card { padding: var(--u4) var(--u5) var(--u3); border-right: 1px solid var(--rule); }
        .stat-card:last-child { border-right: none; }
        .stat-card .stat-value { font-family: var(--font-serif); font-style: italic; font-size: 2.4rem; color: var(--amber); line-height: 1; }
        .stat-card .stat-label { font-size: 0.55rem; font-weight: 600; color: var(--text-ghost); text-transform: uppercase; letter-spacing: 0.14em; }

        .sidebar-section-label {
            font-size: 0.55rem; font-weight: 700; text-transform: uppercase;
            letter-spacing: 0.16em; color: var(--text-ghost);
            margin: var(--u5) 0 var(--u3); padding: 0 var(--u5);
            display: flex; align-items: center; gap: var(--u3);
        }
        .sidebar-section-label::after { content: ''; flex: 1; height: 1px; background: var(--rule); }

        .sidebar-footer {
            padding: var(--u4) var(--u5); font-size: 0.54rem;
            color: var(--text-ghost); letter-spacing: 0.08em; border-top: 1px solid var(--rule);
        }
        </style>
        ''',
        unsafe_allow_html=True,
    )
