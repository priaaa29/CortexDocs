import streamlit as st


def inject_css() -> None:
    st.markdown(
        """
        <style>
        /* ═══════════════════════════════════════════════════════════════════════
           FONTS — Instrument Serif (brand) + JetBrains Mono (everything)
           This is a document intelligence tool. Mono IS the personality.
        ═══════════════════════════════════════════════════════════════════════ */
        @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@300;400;500;600;700&display=swap');

        /* ═══════════════════════════════════════════════════════════════════════
           DESIGN TOKENS
           Mood: Soviet scientific instrument manual × Bloomberg terminal
           Dense, ruled, precise. Amber is the only warmth.
        ═══════════════════════════════════════════════════════════════════════ */
        :root {
            /* Surfaces */
            --bg:            hsl(215, 22%, 4%);
            --bg-raised:     hsl(215, 20%, 6%);
            --bg-panel:      hsl(215, 18%, 8%);
            --bg-hover:      hsl(215, 16%, 11%);

            /* Rules & structure */
            --rule:          hsl(215, 14%, 14%);
            --rule-strong:   hsl(215, 12%, 20%);
            --rule-accent:   hsl(38, 98%, 50%);   /* amber rule — used sparingly */

            /* Accent — hot amber, no compromise */
            --amber:         hsl(38, 98%, 50%);
            --amber-bright:  hsl(42, 100%, 62%);
            --amber-dim:     hsla(38, 98%, 50%, 0.08);
            --amber-glow:    hsla(38, 98%, 50%, 0.18);
            --amber-border:  hsla(38, 98%, 50%, 0.28);

            /* Cyan — live/active states only */
            --cyan:          hsl(185, 75%, 48%);
            --cyan-dim:      hsla(185, 75%, 48%, 0.10);

            /* Red — destructive */
            --red:           hsl(4, 78%, 58%);
            --red-dim:       hsla(4, 78%, 58%, 0.09);

            /* Text — high contrast, no muddy grays */
            --text-hi:       hsl(215, 15%, 90%);   /* headings, values */
            --text-md:       hsl(215, 10%, 65%);   /* body, labels */
            --text-lo:       hsl(215, 8%, 40%);    /* muted, hints */
            --text-ghost:    hsl(215, 6%, 25%);    /* disabled, rules */

            /* Typography scale */
            --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
            --font-serif: 'Instrument Serif', Georgia, serif;

            /* Spacing rhythm — 4px base unit */
            --u1: 4px; --u2: 8px; --u3: 12px; --u4: 16px;
            --u5: 20px; --u6: 24px; --u8: 32px; --u10: 40px;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           RESET & BASE
        ═══════════════════════════════════════════════════════════════════════ */
        *, *::before, *::after {
            box-sizing: border-box;
        }

        html, body, [class*="css"] {
            font-family: var(--font-mono) !important;
            color: var(--text-md) !important;
            -webkit-font-smoothing: antialiased;
            font-feature-settings: "liga" 0, "calt" 0; /* kill mono ligatures in UI */
        }

        .stApp {
            background: var(--bg) !important;
            /* Subtle dot-grid background — the "ledger paper" texture */
            background-image: radial-gradient(
                circle,
                hsl(215, 14%, 12%) 1px,
                transparent 1px
            ) !important;
            background-size: 24px 24px !important;
        }

        /* Kill Streamlit chrome */
        #MainMenu, footer, header { visibility: hidden !important; }
        .stDeployButton { display: none !important; }

        /* ═══════════════════════════════════════════════════════════════════════
           GLOBAL TEXT OVERRIDES
           Steamlit injects color on everything. We reclaim it all.
        ═══════════════════════════════════════════════════════════════════════ */
        p, span, li, td, th, div, label, small, strong, em {
            font-family: var(--font-mono) !important;
        }

        /* Markdown prose */
        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li,
        [data-testid="stMarkdownContainer"] td,
        [data-testid="stMarkdownContainer"] strong,
        [data-testid="stMarkdownContainer"] em,
        .stMarkdown p, .stMarkdown li {
            color: var(--text-md) !important;
            font-size: 0.82rem !important;
            line-height: 1.8 !important;
        }

        [data-testid="stMarkdownContainer"] h1,
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3,
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            font-family: var(--font-serif) !important;
            color: var(--text-hi) !important;
            font-weight: 400 !important;
            letter-spacing: -0.01em !important;
        }

        /* Widget labels — ALL CAPS MONO, consistent everywhere */
        label,
        [data-testid="stWidgetLabel"] p,
        .stFileUploader label,
        .stSelectbox label,
        .stMultiSelect label,
        .stTextInput label,
        .stTextArea label {
            font-family: var(--font-mono) !important;
            font-size: 0.62rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.12em !important;
            text-transform: uppercase !important;
            color: var(--text-lo) !important;
        }

        .stCaption,
        [data-testid="stCaptionContainer"] p,
        small {
            font-family: var(--font-mono) !important;
            font-size: 0.65rem !important;
            color: var(--text-ghost) !important;
        }

        [data-testid="stSpinner"] p {
            font-family: var(--font-mono) !important;
            font-size: 0.68rem !important;
            color: var(--text-lo) !important;
        }

        /* Sidebar text */
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span {
            color: var(--text-md) !important;
        }

        /* Alert text */
        [data-testid="stAlert"] p { color: inherit !important; }

        /* ═══════════════════════════════════════════════════════════════════════
           LAYOUT
        ═══════════════════════════════════════════════════════════════════════ */
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 6rem !important;
            max-width: 100% !important;
        }

        /* Horizontal rules — the spine of the ledger aesthetic */
        hr {
            border: none !important;
            border-top: 1px solid var(--rule) !important;
            margin: var(--u4) 0 !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           SIDEBAR — The instrument panel
        ═══════════════════════════════════════════════════════════════════════ */
        [data-testid="stSidebar"] {
            background: var(--bg-raised) !important;
            border-right: 1px solid var(--rule-strong) !important;
            /* Amber pinstripe at top */
            box-shadow: inset 0 3px 0 0 var(--amber) !important;
        }
        [data-testid="stSidebar"] > div:first-child {
            padding: 0 !important;
        }
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] .stFileUploader,
        [data-testid="stSidebar"] .stButton,
        [data-testid="stSidebar"] .stMultiSelect {
            padding-left: var(--u5) !important;
            padding-right: var(--u5) !important;
        }

        /* ── Brand / Wordmark ─────────────────────────────────────────────── */
        .sidebar-brand {
            padding: var(--u6) var(--u5) var(--u5);
            border-bottom: 1px solid var(--rule-strong);
            position: relative;
            overflow: hidden;
            animation: fadeIn 0.5s ease both;
        }
        /* Large ghosted serif watermark behind the brand */
        .sidebar-brand::before {
            content: 'CX';
            font-family: var(--font-serif);
            font-size: 7rem;
            font-weight: 400;
            font-style: italic;
            color: var(--rule-strong);
            position: absolute;
            right: -12px;
            top: -18px;
            line-height: 1;
            pointer-events: none;
            user-select: none;
        }
        .sidebar-brand .wordmark {
            font-family: var(--font-mono);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--text-hi);
            line-height: 1;
            position: relative;
        }
        .sidebar-brand .wordmark em {
            color: var(--amber);
            font-style: normal;
        }
        .sidebar-brand .tagline {
            font-family: var(--font-mono);
            font-size: 0.56rem;
            color: var(--text-ghost);
            letter-spacing: 0.14em;
            text-transform: uppercase;
            margin-top: var(--u2);
            position: relative;
        }

        /* ── Stats — ledger row style ─────────────────────────────────────── */
        .stat-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            border-bottom: 1px solid var(--rule-strong);
        }
        .stat-card {
            padding: var(--u4) var(--u5) var(--u3);
            border-right: 1px solid var(--rule);
            transition: background 0.12s ease;
            position: relative;
        }
        .stat-card:last-child { border-right: none; }
        .stat-card:hover { background: var(--bg-hover); }
        /* Amber top rule on hover */
        .stat-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 2px;
            background: var(--amber);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.2s ease;
        }
        .stat-card:hover::before { transform: scaleX(1); }

        .stat-card .stat-value {
            font-family: var(--font-serif);
            font-style: italic;
            font-size: 2.4rem;
            color: var(--amber);
            line-height: 1;
            letter-spacing: -0.02em;
        }
        .stat-card .stat-label {
            font-family: var(--font-mono);
            font-size: 0.55rem;
            font-weight: 600;
            color: var(--text-ghost);
            margin-top: var(--u1);
            text-transform: uppercase;
            letter-spacing: 0.14em;
        }

        /* ── Sidebar section dividers ─────────────────────────────────────── */
        .sidebar-section-label {
            font-family: var(--font-mono);
            font-size: 0.55rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            color: var(--text-ghost);
            margin: var(--u5) 0 var(--u3);
            padding: 0 var(--u5);
            display: flex;
            align-items: center;
            gap: var(--u3);
        }
        .sidebar-section-label::after {
            content: '';
            flex: 1;
            height: 1px;
            background: var(--rule);
        }

        /* ── Sidebar footer ───────────────────────────────────────────────── */
        .sidebar-footer {
            padding: var(--u4) var(--u5);
            font-family: var(--font-mono);
            font-size: 0.54rem;
            font-weight: 400;
            color: var(--text-ghost);
            letter-spacing: 0.08em;
            border-top: 1px solid var(--rule);
        }

        /* ═══════════════════════════════════════════════════════════════════════
           CONTEXT BAR — top strip of main panel
        ═══════════════════════════════════════════════════════════════════════ */
        .context-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: var(--u3) 0 var(--u3);
            margin-bottom: var(--u6);
            border-bottom: 1px solid var(--rule-strong);
            animation: fadeIn 0.4s ease both;
            /* Top amber pinstripe — mirrors sidebar */
            border-top: 3px solid var(--amber);
        }
        .cb-model {
            font-family: var(--font-mono);
            font-size: 0.62rem;
            font-weight: 500;
            color: var(--text-lo);
            letter-spacing: 0.06em;
        }
        .cb-right {
            display: flex;
            align-items: center;
            gap: var(--u3);
        }
        .cb-pill {
            display: inline-flex;
            align-items: center;
            gap: var(--u2);
            font-family: var(--font-mono);
            font-size: 0.58rem;
            font-weight: 600;
            letter-spacing: 0.10em;
            text-transform: uppercase;
            color: var(--text-lo);
            padding: 2px var(--u3);
            border: 1px solid var(--rule-strong);
        }
        .cb-pill.live {
            color: var(--cyan);
            border-color: hsla(185, 75%, 48%, 0.3);
            background: var(--cyan-dim);
        }
        .cb-dot {
            width: 5px; height: 5px;
            border-radius: 50%;
            background: var(--rule-strong);
            flex-shrink: 0;
        }
        .cb-dot.live {
            background: var(--cyan);
            box-shadow: 0 0 6px var(--cyan);
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; box-shadow: 0 0 6px var(--cyan); }
            50%       { opacity: 0.6; box-shadow: 0 0 3px var(--cyan); }
        }

        /* ═══════════════════════════════════════════════════════════════════════
           FILE UPLOADER
        ═══════════════════════════════════════════════════════════════════════ */
        [data-testid="stFileUploader"] section,
        [data-testid="stFileUploader"] section > div,
        [data-testid="stFileUploaderDropzone"],
        [data-testid="stFileUploaderDropzoneInstructions"] {
            background: var(--bg-panel) !important;
            background-color: var(--bg-panel) !important;
        }
        [data-testid="stFileUploader"] section {
            border: 1px dashed var(--rule-strong) !important;
            border-radius: 0 !important;
            transition: border-color 0.15s ease, background 0.15s ease !important;
        }
        [data-testid="stFileUploader"] section:hover {
            border-color: var(--amber) !important;
            background: var(--amber-dim) !important;
        }
        [data-testid="stFileUploader"] small,
        [data-testid="stFileUploader"] p,
        [data-testid="stFileUploader"] span {
            font-family: var(--font-mono) !important;
            font-size: 0.68rem !important;
            color: var(--text-lo) !important;
        }
        /* Browse files button */
        [data-testid="stFileUploader"] button,
        [data-testid="stFileUploaderDropzone"] button {
            background: transparent !important;
            border: 1px solid var(--rule-strong) !important;
            border-radius: 0 !important;
            color: var(--text-lo) !important;
            font-family: var(--font-mono) !important;
            font-size: 0.65rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.10em !important;
            text-transform: uppercase !important;
            padding: var(--u2) var(--u4) !important;
            transition: border-color 0.12s ease, color 0.12s ease, background 0.12s ease !important;
        }
        [data-testid="stFileUploader"] button:hover,
        [data-testid="stFileUploaderDropzone"] button:hover {
            border-color: var(--amber) !important;
            color: var(--amber) !important;
            background: var(--amber-dim) !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           MULTISELECT
        ═══════════════════════════════════════════════════════════════════════ */
        [data-testid="stMultiSelect"] > div,
        [data-testid="stMultiSelect"] [data-baseweb="select"] > div,
        [data-baseweb="select"] > div,
        [data-baseweb="popover"] {
            background: var(--bg-panel) !important;
            background-color: var(--bg-panel) !important;
            border: 1px solid var(--rule-strong) !important;
            border-radius: 0 !important;
            color: var(--text-md) !important;
        }
        [data-testid="stMultiSelect"] input {
            background: transparent !important;
            color: var(--text-md) !important;
            font-family: var(--font-mono) !important;
            font-size: 0.75rem !important;
        }
        [data-testid="stMultiSelect"] [data-baseweb="tag"] {
            background: var(--amber-dim) !important;
            border: 1px solid var(--amber-border) !important;
            border-radius: 0 !important;
        }
        [data-testid="stMultiSelect"] [data-baseweb="tag"] span {
            font-family: var(--font-mono) !important;
            font-size: 0.65rem !important;
            font-weight: 600 !important;
            color: var(--amber) !important;
        }
        [data-baseweb="menu"],
        [data-baseweb="popover"] > div {
            background: var(--bg-panel) !important;
            border: 1px solid var(--rule-strong) !important;
            border-radius: 0 !important;
        }
        [data-baseweb="menu"] li {
            background: var(--bg-panel) !important;
            color: var(--text-md) !important;
            font-family: var(--font-mono) !important;
            font-size: 0.75rem !important;
            border-bottom: 1px solid var(--rule) !important;
        }
        [data-baseweb="menu"] li:hover {
            background: var(--amber-dim) !important;
            color: var(--amber) !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           BUTTONS
        ═══════════════════════════════════════════════════════════════════════ */
        .stButton > button {
            font-family: var(--font-mono) !important;
            font-size: 0.68rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.12em !important;
            text-transform: uppercase !important;
            border-radius: 0 !important;
            height: 36px !important;
            transition: background 0.12s ease, color 0.12s ease, box-shadow 0.12s ease !important;
        }
        /* Primary — solid amber, black text */
        .stButton > button[kind="primary"] {
            background: var(--amber) !important;
            color: hsl(215, 22%, 4%) !important;
            border: 1px solid var(--amber) !important;
        }
        .stButton > button[kind="primary"]:hover {
            background: var(--amber-bright) !important;
            border-color: var(--amber-bright) !important;
            box-shadow: 0 0 0 3px var(--amber-glow) !important;
        }
        .stButton > button[kind="primary"]:active {
            transform: translateY(1px) !important;
        }
        /* Secondary — ghost */
        .stButton > button:not([kind="primary"]) {
            background: transparent !important;
            border: 1px solid var(--rule-strong) !important;
            color: var(--text-lo) !important;
        }
        .stButton > button:not([kind="primary"]):hover {
            border-color: var(--red) !important;
            color: var(--red) !important;
            background: var(--red-dim) !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           PROGRESS BAR — 1px amber line, no border radius
        ═══════════════════════════════════════════════════════════════════════ */
        [data-testid="stProgress"] > div {
            background: var(--rule) !important;
            border-radius: 0 !important;
            height: 1px !important;
        }
        [data-testid="stProgress"] > div > div {
            background: var(--amber) !important;
            border-radius: 0 !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           ALERTS
        ═══════════════════════════════════════════════════════════════════════ */
        [data-testid="stAlert"] {
            border-radius: 0 !important;
            border: none !important;
            border-left: 2px solid !important;
            font-family: var(--font-mono) !important;
            font-size: 0.75rem !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           CHAT MESSAGES
        ═══════════════════════════════════════════════════════════════════════ */
        [data-testid="stChatMessage"] {
            background: transparent !important;
            border: none !important;
            border-bottom: 1px solid var(--rule) !important;
            padding: var(--u5) 0 !important;
            border-radius: 0 !important;
            animation: slideIn 0.25s ease both;
        }
        [data-testid="stChatMessage"]:nth-child(1) { animation-delay: 0.05s; }
        [data-testid="stChatMessage"]:nth-child(2) { animation-delay: 0.10s; }
        [data-testid="stChatMessage"]:nth-child(3) { animation-delay: 0.15s; }
        [data-testid="stChatMessage"]:nth-child(4) { animation-delay: 0.20s; }

        [data-testid="stChatMessage"] .stMarkdown p {
            color: var(--text-md) !important;
            line-height: 1.8 !important;
        }

        [data-testid="chatAvatarIcon-user"] {
            background: var(--amber-dim) !important;
            color: var(--amber) !important;
            border: 1px solid var(--amber-border) !important;
            border-radius: 0 !important;
            font-family: var(--font-mono) !important;
            font-size: 0.6rem !important;
        }
        [data-testid="chatAvatarIcon-assistant"] {
            background: var(--bg-panel) !important;
            color: var(--text-lo) !important;
            border: 1px solid var(--rule-strong) !important;
            border-radius: 0 !important;
            font-family: var(--font-mono) !important;
            font-size: 0.6rem !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           QUERY TYPE BADGE
        ═══════════════════════════════════════════════════════════════════════ */
        .query-badge {
            display: inline-flex;
            align-items: center;
            gap: var(--u2);
            padding: 1px var(--u3);
            font-family: var(--font-mono);
            font-size: 0.58rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: var(--u4);
            border-radius: 0;
        }
        .badge-factual    { background: hsla(210,80%,65%,0.08); color: hsl(210,80%,65%); border: 1px solid hsla(210,80%,65%,0.2); }
        .badge-summary    { background: var(--cyan-dim);        color: var(--cyan);       border: 1px solid hsla(185,75%,48%,0.2); }
        .badge-comparison { background: var(--amber-dim);       color: var(--amber);      border: 1px solid var(--amber-border); }
        .badge-other      { background: transparent;            color: var(--text-lo);    border: 1px solid var(--rule-strong); }

        /* ═══════════════════════════════════════════════════════════════════════
           SOURCE EXPANDERS
        ═══════════════════════════════════════════════════════════════════════ */
        .sources-header {
            font-family: var(--font-mono);
            font-size: 0.58rem;
            font-weight: 700;
            color: var(--text-ghost);
            text-transform: uppercase;
            letter-spacing: 0.14em;
            margin: var(--u6) 0 var(--u3);
            display: flex;
            align-items: center;
            gap: var(--u4);
        }
        .sources-header::after {
            content: '';
            flex: 1;
            height: 1px;
            background: var(--rule);
        }

        [data-testid="stExpander"] {
            background: var(--bg-panel) !important;
            border: 1px solid var(--rule) !important;
            border-left: 2px solid var(--amber) !important;
            border-radius: 0 !important;
            margin-bottom: 2px !important;
        }
        [data-testid="stExpander"] summary {
            color: var(--text-lo) !important;
            font-family: var(--font-mono) !important;
            font-size: 0.68rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.04em !important;
            transition: color 0.12s ease !important;
        }
        [data-testid="stExpander"] summary:hover {
            color: var(--amber) !important;
        }
        .source-body {
            font-family: var(--font-mono) !important;
            font-size: 0.75rem;
            line-height: 1.75;
            color: var(--text-lo) !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           CHAT INPUT BOTTOM BAR
           Nuclear option: every layer gets the bg color + shadow nuked.
        ═══════════════════════════════════════════════════════════════════════ */
        [data-testid="stBottom"],
        [data-testid="stBottom"] > div,
        [data-testid="stBottom"] > div > div,
        [data-testid="stBottom"] > div > div > div,
        [data-testid="stBottom"] > div > div > div > div {
            background: var(--bg) !important;
            background-color: var(--bg) !important;
            box-shadow: none !important;
        }
        [data-testid="stBottom"] {
            border-top: 1px solid var(--rule-strong) !important;
        }
        [data-testid="stChatInput"],
        [data-testid="stChatInputContainer"],
        [data-testid="stChatInput"] > div {
            background: var(--bg) !important;
            background-color: var(--bg) !important;
            box-shadow: none !important;
            border: none !important;
        }
        [data-testid="stChatInput"] textarea {
            background: var(--bg-panel) !important;
            background-color: var(--bg-panel) !important;
            border: 1px solid var(--rule-strong) !important;
            border-radius: 0 !important;
            color: var(--text-hi) !important;
            font-family: var(--font-mono) !important;
            font-size: 0.82rem !important;
            font-weight: 400 !important;
            caret-color: var(--amber) !important;
            transition: border-color 0.12s ease !important;
        }
        [data-testid="stChatInput"] textarea:focus {
            border-color: var(--amber) !important;
            box-shadow: 0 0 0 1px var(--amber-glow),
                        inset 0 0 0 1px var(--amber-glow) !important;
            outline: none !important;
        }
        [data-testid="stChatInput"] textarea::placeholder {
            color: var(--text-ghost) !important;
            font-style: italic;
            font-size: 0.78rem !important;
        }
        /* Send button */
        [data-testid="stChatInput"] button {
            background: var(--amber) !important;
            color: var(--bg) !important;
            border-radius: 0 !important;
            border: none !important;
            transition: background 0.12s ease !important;
        }
        [data-testid="stChatInput"] button:hover {
            background: var(--amber-bright) !important;
        }
        [data-testid="stChatInput"] button svg path {
            fill: var(--bg) !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           SPINNER
        ═══════════════════════════════════════════════════════════════════════ */
        .stSpinner > div {
            border-top-color: var(--amber) !important;
            border-right-color: transparent !important;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           EMPTY STATE
        ═══════════════════════════════════════════════════════════════════════ */
        .empty-state {
            padding: var(--u10) 0 var(--u8);
            animation: fadeIn 0.6s 0.2s ease both;
            border-top: 3px solid var(--amber);
        }
        .empty-state .label {
            font-family: var(--font-mono);
            font-size: 0.58rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            color: var(--text-ghost);
            margin-bottom: var(--u4);
        }
        .empty-state h2 {
            font-family: var(--font-serif);
            font-style: italic;
            font-weight: 400;
            font-size: clamp(1.8rem, 3vw, 2.6rem);
            letter-spacing: -0.02em;
            color: var(--text-hi);
            margin: 0 0 var(--u4);
            line-height: 1.15;
        }
        .empty-state p {
            font-family: var(--font-mono);
            font-size: 0.78rem;
            color: var(--text-lo);
            line-height: 1.8;
            max-width: 480px;
            margin: 0;
        }
        .empty-state .hint {
            margin-top: var(--u6);
            display: flex;
            align-items: center;
            gap: var(--u3);
            font-family: var(--font-mono);
            font-size: 0.60rem;
            color: var(--text-ghost);
            letter-spacing: 0.08em;
        }
        .empty-state .hint::before {
            content: '→';
            color: var(--amber);
            font-size: 0.75rem;
        }

        /* ═══════════════════════════════════════════════════════════════════════
           SCROLLBAR — ultra-thin amber thumb
        ═══════════════════════════════════════════════════════════════════════ */
        ::-webkit-scrollbar { width: 2px; height: 2px; }
        ::-webkit-scrollbar-track { background: var(--bg); }
        ::-webkit-scrollbar-thumb {
            background: var(--amber);
            opacity: 0.4;
        }
        ::-webkit-scrollbar-thumb:hover { background: var(--amber-bright); }

        /* ═══════════════════════════════════════════════════════════════════════
           ANIMATIONS
        ═══════════════════════════════════════════════════════════════════════ */
        @keyframes fadeIn {
            from { opacity: 0; }
            to   { opacity: 1; }
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-6px); }
            to   { opacity: 1; transform: translateX(0); }
        }
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(8px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        /* ═══════════════════════════════════════════════════════════════════════
           RESPONSIVE
        ═══════════════════════════════════════════════════════════════════════ */
        @media (max-width: 768px) {
            .stat-row { grid-template-columns: 1fr; }
            .context-bar { flex-direction: column; align-items: flex-start; gap: var(--u2); }
            .sidebar-brand::before { font-size: 4rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )