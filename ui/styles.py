import streamlit as st


def inject_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap');

        :root {
            --bg-1: #f5f3ff;
            --bg-2: #ecfeff;
            --bg-3: #fdf2f8;
            --surface: rgba(255, 255, 255, 0.65);
            --surface-strong: rgba(255, 255, 255, 0.85);
            --border: rgba(15, 23, 42, 0.08);
            --border-strong: rgba(15, 23, 42, 0.14);
            --text-hi: #0f172a;
            --text-md: #475569;
            --text-lo: #94a3b8;
            --accent: #8b5cf6;
            --accent-soft: rgba(139, 92, 246, 0.12);
            --accent-border: rgba(139, 92, 246, 0.28);
            --accent-2: #10b981;
            --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.04);
            --shadow-md: 0 4px 16px rgba(15, 23, 42, 0.06);
            --shadow-lg: 0 8px 32px rgba(15, 23, 42, 0.08);
            --radius: 14px;
            --radius-sm: 10px;
        }

        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            color: var(--text-md);
        }

        .stApp {
            background:
                radial-gradient(1200px 600px at 10% -10%, var(--bg-1) 0%, transparent 60%),
                radial-gradient(1000px 500px at 110% 10%, var(--bg-2) 0%, transparent 60%),
                radial-gradient(900px 700px at 50% 110%, var(--bg-3) 0%, transparent 55%),
                #fafafa;
        }

        #MainMenu, footer, header { visibility: hidden; }
        .stDeployButton { display: none !important; }

        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 8rem !important;
            max-width: 920px !important;
        }

        h1, h2, h3 { color: var(--text-hi); font-weight: 600; letter-spacing: -0.01em; }

        /* ─── Sidebar ───────────────────────────────────────────────────── */
        [data-testid="stSidebar"] {
            background: var(--surface);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-right: 1px solid var(--border);
        }
        [data-testid="stSidebar"] > div:first-child { padding-top: 1.5rem; }

        .sidebar-brand {
            padding: 0.25rem 1.25rem 1.25rem;
            border-bottom: 1px solid var(--border);
            margin-bottom: 1.25rem;
        }
        .sidebar-brand .wordmark {
            font-family: 'Instrument Serif', Georgia, serif;
            font-size: 1.75rem;
            font-weight: 400;
            color: var(--text-hi);
            line-height: 1.1;
            letter-spacing: -0.01em;
        }
        .sidebar-brand .wordmark em {
            font-style: italic;
            color: var(--accent);
        }
        .sidebar-brand .tagline {
            font-size: 0.72rem;
            color: var(--text-lo);
            margin-top: 0.25rem;
            font-weight: 500;
        }

        .stat-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.5rem;
            padding: 0 1.25rem;
            margin-bottom: 1rem;
        }
        .stat-card {
            background: var(--surface-strong);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 0.75rem 0.85rem;
            box-shadow: var(--shadow-sm);
        }
        .stat-card .stat-value {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--text-hi);
            line-height: 1.1;
        }
        .stat-card .stat-label {
            font-size: 0.65rem;
            font-weight: 500;
            color: var(--text-lo);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-top: 0.15rem;
        }

        .sidebar-section-label {
            font-size: 0.65rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--text-lo);
            padding: 0 1.25rem;
            margin: 1rem 0 0.5rem;
        }
        .sidebar-footer {
            padding: 1rem 1.25rem;
            font-size: 0.7rem;
            color: var(--text-lo);
            border-top: 1px solid var(--border);
            margin-top: 1.5rem;
        }

        /* ─── Context bar ───────────────────────────────────────────────── */
        .context-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 1.1rem;
            background: var(--surface-strong);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            box-shadow: var(--shadow-sm);
            margin-bottom: 1.5rem;
        }
        .cb-model {
            font-size: 0.78rem;
            font-weight: 500;
            color: var(--text-md);
        }
        .cb-right {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.78rem;
        }
        .cb-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--text-lo);
        }
        .cb-dot.active {
            background: var(--accent-2);
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.18);
        }
        .cb-status { color: var(--text-md); }

        /* ─── Empty state ───────────────────────────────────────────────── */
        .empty-state {
            padding: 4rem 1.5rem;
            text-align: center;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            box-shadow: var(--shadow-md);
        }
        .empty-state .label {
            display: inline-block;
            padding: 0.25rem 0.7rem;
            border-radius: 999px;
            background: var(--accent-soft);
            color: var(--accent);
            font-size: 0.65rem;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }
        .empty-state h2 {
            font-family: 'Instrument Serif', Georgia, serif;
            font-style: italic;
            font-weight: 400;
            font-size: 2rem;
            color: var(--text-hi);
            margin: 0 0 0.75rem;
        }
        .empty-state p {
            color: var(--text-md);
            font-size: 0.92rem;
            line-height: 1.6;
            max-width: 460px;
            margin: 0 auto;
        }
        .empty-state .hint {
            margin-top: 1.5rem;
            font-size: 0.78rem;
            color: var(--text-lo);
        }

        /* ─── Buttons (light touch — let Streamlit handle most) ───────── */
        .stButton > button {
            border-radius: var(--radius-sm);
            font-weight: 500;
            border: 1px solid var(--border-strong);
            transition: all 0.15s ease;
        }
        .stButton > button[kind="primary"] {
            background: var(--accent);
            border-color: var(--accent);
            color: white;
        }
        .stButton > button[kind="primary"]:hover {
            background: #7c3aed;
            border-color: #7c3aed;
            box-shadow: 0 4px 14px rgba(139, 92, 246, 0.35);
        }

        /* ─── Chat messages ─────────────────────────────────────────────── */
        [data-testid="stChatMessage"] {
            background: var(--surface-strong);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1rem 1.25rem !important;
            margin-bottom: 0.75rem;
            box-shadow: var(--shadow-sm);
        }

        /* ─── Query badge ───────────────────────────────────────────────── */
        .query-badge {
            display: inline-block;
            padding: 0.2rem 0.65rem;
            border-radius: 999px;
            font-size: 0.65rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.75rem;
        }
        .badge-factual    { background: rgba(59, 130, 246, 0.12); color: #2563eb; }
        .badge-summary    { background: rgba(16, 185, 129, 0.12); color: #059669; }
        .badge-comparison { background: rgba(245, 158, 11, 0.12); color: #d97706; }
        .badge-other      { background: rgba(100, 116, 139, 0.12); color: #475569; }

        /* ─── Sources ───────────────────────────────────────────────────── */
        .sources-header {
            font-size: 0.7rem;
            font-weight: 600;
            color: var(--text-lo);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin: 1.25rem 0 0.5rem;
        }
        [data-testid="stExpander"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm) !important;
            margin-bottom: 0.4rem;
            box-shadow: var(--shadow-sm);
        }
        .source-body {
            font-size: 0.85rem;
            line-height: 1.6;
            color: var(--text-md);
        }

        /* ─── Chat input ────────────────────────────────────────────────── */
        [data-testid="stBottom"] {
            background: transparent !important;
        }
        [data-testid="stChatInput"] textarea {
            border-radius: var(--radius);
            border: 1px solid var(--border-strong);
            background: var(--surface-strong);
            font-size: 0.95rem;
        }
        [data-testid="stChatInput"] textarea:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px var(--accent-soft);
        }

        /* ─── File uploader ─────────────────────────────────────────────── */
        [data-testid="stFileUploader"] section {
            background: var(--surface);
            border: 1.5px dashed var(--border-strong);
            border-radius: var(--radius-sm);
        }
        [data-testid="stFileUploader"] section:hover {
            border-color: var(--accent);
            background: var(--accent-soft);
        }

        /* ─── Alerts ────────────────────────────────────────────────────── */
        [data-testid="stAlert"] {
            border-radius: var(--radius-sm);
        }

        /* ─── Progress ──────────────────────────────────────────────────── */
        [data-testid="stProgress"] > div > div {
            background: var(--accent);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
