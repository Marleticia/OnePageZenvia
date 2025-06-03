import streamlit as st

# Cores Personalizadas (AJUSTADO PARA BRANCO NOS TEXTOS E CONTRASTE NAS SEÇÕES)
BACKGROUND_COLOR = "#993399" # Roxão principal
HIGHLIGHT_COLOR = "#007AFF" # Azul vibrante (para destaques como títulos, links)
TEXT_COLOR = "#FFFFFF" # Branco (para textos no fundo roxo)
SECTION_BG_COLOR = "#FFFFFF" # Fundo das seções internas (Problema, Solução, Agendamento)
SECTION_HIGHLIGHT_TEXT_COLOR = "#333333" # Cor dos textos dentro das seções internas (para contraste no fundo branco)
LIGHT_BACKGROUND_HIGHLIGHT = "#B366B3" # Um roxo mais claro (se precisar de uma seção com fundo roxo mais claro)

st.set_page_config(
    page_title="Zenvia: Sua Próxima Conversa com o Crescimento!",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def set_custom_style():
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Open+Sans:wght@400;600&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {{
            font-family: 'Montserrat', sans-serif;
            color: {TEXT_COLOR}; /* Texto principal em branco */
            background-color: {BACKGROUND_COLOR}; /* Fundo roxo */
            line-height: 1.6;
            font-size: 14px; /* Tamanho base dos textos, levemente menor */
        }}
        
        /* Remove paddings e margens padrão do Streamlit para maior controle */
        .st-emotion-cache-1wvwm0x, .st-emotion-cache-z5fcl4, .st-emotion-cache-uf99v8 {{
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }}

        .css-vk325g {{ display: none !important; }}
        header[data-testid="stHeader"] {{ display: none !important; }}
        
        .zen-header {{
            background-color: {BACKGROUND_COLOR};
            padding: 5px 15px; /* Bem pequeno para o logo */
            text-align: left;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            display: flex;
            align-items: center;
            justify-content: flex-start;
        }}
        .zen-logo {{
            max-width: 60px; /* Logo miniatura */
            height: auto;
            margin-left: 0; /* Cola na borda esquerda */
        }}
        
        .zen-hero {{
            background-color: {HIGHLIGHT_COLOR};
            color: {TEXT_COLOR};
            padding: 50px 20px; /* Padding reduzido da hero */
            text-align: center;
            background-image: linear-gradient(to right, {HIGHLIGHT_COLOR}, #0056b3);
            border-radius: 0 0 15px 15px;
            margin-bottom: 30px;
        }}
        .zen-hero h1 {{
            font-size: 2.0em; /* Relativo à base de 14px -> 28px */
            margin-bottom: 10px;
            font-weight: 700;
            line-height: 1.2;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
            color: {TEXT_COLOR};
        }}
        .zen-hero p {{
            font-size: 1em; /* 14px */
            margin-bottom: 25px;
            font-weight: 400;
            opacity: 0.9;
            color: {TEXT_COLOR};
        }}
        .zen-btn-schedule {{
            display: inline-block;
            background-color: {HIGHLIGHT_COLOR};
            color: {TEXT_COLOR}; /* Texto do botão em branco */
            padding: 12px 25px; /* Ajusta padding para texto menor */
            border-radius: 50px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1em; /* 14px */
            transition: background-color 0.3s ease, transform 0.2s ease;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }}
        .zen-btn-schedule:hover {{
            background-color: #00c853; /* Um verde para hover do botão */
            transform: translateY(-3px);
        }}
        
        .zen-section {{
            padding: 35px 30px; /* Reduz padding das seções */
            background-color: {SECTION_BG_COLOR};
            margin: 20px auto;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            max-width: 900px;
            color: {SECTION_HIGHLIGHT_TEXT_COLOR}; /* Texto das seções internas em tom escuro para contraste */
        }}
        .zen-section.bg-light {{ /* Para seções com fundo roxo claro, se existirem */
            background-color: {LIGHT_BACKGROUND_HIGHLIGHT};
            color: {TEXT_COLOR}; /* Texto em branco */
        }}
        h2 {{
            font-size: 1.6em; /* 1.6 * 14px = 22.4px */
            color: {HIGHLIGHT_COLOR};
            text-align: center;
            margin-bottom: 25px;
            font-weight: 700;
            position: relative;
        }}
        h2::after {{
            content: '';
            display: block;
            width: 50px; /* Linha abaixo H2 menor */
            height: 2px;
            background-color: {HIGHLIGHT_COLOR};
            margin: 8px auto 0;
            border-radius: 1px;
        }}
        h3 {{ /* Para a nova seção "Solução Integrada" */
            font-size: 1.4em; /* 1.4 * 14px = 19.6px */
            color: {HIGHLIGHT_COLOR};
            margin-bottom: 15px;
            text-align: center;
            font-weight: 700;
        }}
        
        /* Ajuste para parágrafos e listas dentro das seções */
        .zen-section p, .zen-section ul, .zen-section li {{
            font-size: 1em; /* 14px */
            color: {SECTION_HIGHLIGHT_TEXT_COLOR}; /* Garante texto escuro nas seções brancas */
        }}
        .zen-section ul li {{
            margin-bottom: 8px; /* Reduz espaçamento entre itens da lista */
        }}
        .zen-section ul li span {{ /* Ajusta cor dos bullets */
            color: {HIGHLIGHT_COLOR};
        }}

        .zen-footer {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR}; /* Texto do footer em branco */
            text-align: center;
            padding: 25px 20px; /* Reduz padding do footer */
            font-size: 0.9em; /* Levemente menor que o base -> 12.6px */
            margin-top: 30px;
        }}
        .zen-footer a {{
            color: {HIGHLIGHT_COLOR};
            text-decoration: none;
        }}
        .zen-footer a:hover {{
            text-decoration: underline;
        }}
        
        .st-markdown a {{
            color: {HIGHLIGHT_COLOR};
            text-decoration: none;
            font-weight: 600;
        }}
        .st-markdown a:hover {{
            text-decoration: underline;
        }}

        /* Para o texto de contato direto no agendamento */
        .contact-text {{
            font-size: 1em; /* 14px */
            color: {SECTION_HIGHLIGHT_TEXT_COLOR}; /* Texto escuro na seção branca */
        }}
        .contact-links a {{
            font-size: 1.1em; /* Um pouco maior para links de contato */
            color: {HIGHLIGHT_COLOR};
        }}


        html {{ scroll-behavior: smooth; }}

        .calendly-inline-widget {{
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin: 25px auto; /* Reduz margin do calendly */
        }}
        @media (max-width: 768px) {{
            .zen-hero h1 {{ font-size: 1.6em; }} /* 1.6 * 14px = 22.4px */
            .zen-hero p {{ font-size: 0.9em; }} /* 0.9 * 14px = 12.6px */
            h2 {{ font-size: 1.3em; }} /* 1.3 * 14px = 18.2px */
            .zen-btn-schedule {{ padding: 10px 20px; font-size: 0.9em; }}
            .zen-section {{ padding: 20px 15px; }}
            .zen-logo {{ max-width: 50px; }} /* Logo ainda menor em mobile */
            .zen-footer {{ font-size: 0.8em; }} /* Footer menor em mobile */
        }}
    </style>
    """, unsafe_allow_html=True)
set_custom_style()

# --- Placeholder para os dados do Diretor e da Empresa ---
diretor_nome = "Michael Bruno de Lima"
empresa_dele = "Zenvia Tech"
segmento_empresa = "Marketing e Customer Success"
seu_linkedin_url = "https://www.linkedin.com/in/maria-let%C3%ADcia-sousa-335bb9154/"
seu_email = "maarinnolasco@gmail.com"
seu_nome = "Maria Leticia Sousa"

# --- Layout da One Page ---

# Header com o novo logo e posicionamento
st.markdown(f"""
<div class="zen-header">
    <img src="https://mir-s3-cdn-cf.behance.net/projects/404/4e9f4f212905251.Y3JvcCw4MDgsNjMyLDAsMA.png" alt="Logo da Empresa" class="zen-logo">
</div>
""", unsafe_allow_html=True)

# Hero Section (Título personalizado e chamada vibrante)
st.markdown(f"""
<div class="zen-hero">
    <h1>Zenvia Tech | Comunicação que gera resultado</h1>
    <p>Soluções multicanal para escalar o relacionamento com leads e clientes sem perder agilidade, personalização e performance.</p>
    <a href="#agendamento" class="zen-btn-schedule">SEU MELHOR HORÁRIO PARA UM BATE-PAPO</a>
</div>
""", unsafe_allow_html=True)

# 🧠 2. Problema
st.markdown(f"""
<section class="zen-section">
    <h2><span style="color: {HIGHLIGHT_COLOR};">🧠</span> Problema: Você já deve ter vivido isso...</h2>
    <div style="font-size: 1em; max-width: 800px; margin: 0 auto 30px auto; color: {SECTION_HIGHLIGHT_TEXT_COLOR};">
        <ul style="list-style: none; padding: 0; text-align: left;">
            <li style="margin-bottom: 10px;"><span style="color: {HIGHLIGHT_COLOR}; font-weight: 700; margin-right: 10px;">•</span> Volume crescente de leads, mas conversão travada.</li>
            <li style="margin-bottom: 10px;"><span style="color: {HIGHLIGHT_COLOR}; font-weight: 700; margin-right: 10px;">•</span> Equipes sobrecarregadas, processos manuais e pouco escaláveis.</li>
            <li style="margin-bottom: 10px;"><span style="color: {HIGHLIGHT_COLOR}; font-weight: 700; margin-right: 10px;">•</span> Comunicação fragmentada entre marketing, vendas e atendimento.</li>
            <li style="margin-bottom: 10px;"><span style="color: {HIGHLIGHT_COLOR}; font-weight:
