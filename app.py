import streamlit as st

# Cores Personalizadas (AJUSTADO COM AS NOVAS CORES)
# Cor principal de fundo
BACKGROUND_COLOR = "#993399" # Roxão agora!
# Cor de destaque para títulos, botões e elementos
HIGHLIGHT_COLOR = "#007AFF" # Azul vibrante
# Cor dos textos
TEXT_COLOR = "#FFFFFF" # Branco para contrastar com o roxo
# Cor do fundo das seções (se ainda tiver seções brancas/claras)
SECTION_BG_COLOR = "#FFFFFF" # Mantém branco para seções internas se for o caso
# Cor para subtítulos ou elementos secundários (opcional, mas bom ter um tom mais claro do roxo)
LIGHT_BACKGROUND_HIGHLIGHT = "#B366B3" # Um roxo mais claro

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
            background-color: {BACKGROUND_COLOR}; /* Mantém a cor de fundo do site */
            padding: 20px;
            text-align: left; /* Alinha o logo à esquerda */
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            display: flex;
            align-items: center;
            justify-content: flex-start; /* Alinha o conteúdo à esquerda */
        }}
        .zen-logo {{
            max-width: 180px; /* Ajustado para um logo horizontal, se necessário */
            height: auto;
            margin-left: 20px; /* Espaçamento da borda */
        }}
        
        .zen-hero {{
            background-color: {HIGHLIGHT_COLOR}; /* Fundo da hero em destaque azul */
            color: #fff;
            padding: 80px 20px;
            text-align: center;
            background-image: linear-gradient(to right, {HIGHLIGHT_COLOR}, #0056b3); /* Gradiente do destaque */
            border-radius: 0 0 15px 15px;
            margin-bottom: 30px;
        }}
        .zen-hero h1 {{
            font-size: 3.2em;
            margin-bottom: 20px;
            font-weight: 700;
            line-height: 1.2;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
            color: {TEXT_COLOR}; /* Título da hero em branco */
        }}
        .zen-hero p {{
            font-size: 1.4em;
            margin-bottom: 40px;
            font-weight: 400;
            opacity: 0.9;
            color: {TEXT_COLOR}; /* Texto da hero em branco */
        }}
        .zen-btn-schedule {{
            display: inline-block;
            background-color: {HIGHLIGHT_COLOR}; /* Botão em destaque azul */
            color: #fff;
            padding: 18px 35px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.3em;
            transition: background-color 0.3s ease, transform 0.2s ease;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }}
        .zen-btn-schedule:hover {{
            background-color: #00c853; /* Um verde para hover do botão, mantendo contraste */
            transform: translateY(-3px);
        }}
        
        .zen-section {{
            padding: 60px 40px;
            background-color: {SECTION_BG_COLOR}; /* Seções internas em branco */
            margin: 20px auto;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            max-width: 900px;
            color: {BACKGROUND_COLOR}; /* Texto das seções internas na cor principal */
        }}
        .zen-section.bg-light {{ background-color: {LIGHT_BACKGROUND_HIGHLIGHT}; /* Uma cor mais clara para o fundo */
                                   color: {TEXT_COLOR}; /* Texto em branco para seções claras */
                                }}
        h2 {{
            font-size: 2.5em;
            color: {HIGHLIGHT_COLOR}; /* Títulos H2 em destaque azul */
            text-align: center;
            margin-bottom: 50px;
            font-weight: 700;
            position: relative;
        }}
        h2::after {{
            content: '';
            display: block;
            width: 80px;
            height: 4px;
            background-color: {HIGHLIGHT_COLOR}; /* Linha abaixo H2 em destaque azul */
            margin: 15px auto 0;
            border-radius: 2px;
        }}
        h3 {{
            font-size: 2em;
            color: {HIGHLIGHT_COLOR}; /* Títulos H3 em destaque azul */
            margin-bottom: 25px;
            text-align: center;
            font-weight: 700;
        }}
        
        .zen-footer {{
            background-color: {BACKGROUND_COLOR}; /* Footer na cor principal */
            color: {TEXT_COLOR}; /* Texto do footer em branco */
            text-align: center;
            padding: 40px 20px;
            font-size: 1em;
            margin-top: 30px;
        }}
        .zen-footer a {{
            color: {HIGHLIGHT_COLOR}; /* Links do footer em destaque azul */
            text-decoration: none;
        }}
        .zen-footer a:hover {{
            text-decoration: underline;
        }}
        
        .st-markdown a {{
            color: {HIGHLIGHT_COLOR}; /* Links gerais em destaque azul */
            text-decoration: none;
            font-weight: 600;
        }}
        .st-markdown a:hover {{
            text-decoration: underline;
        }}

        html {{ scroll-behavior: smooth; }}

        .calendly-inline-widget {{
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin: 40px auto;
        }}
        @media (max-width: 768px) {{
            .zen-hero h1 {{ font-size: 2em; }}
            .zen-hero p {{ font-size: 1em; }}
            h2 {{ font-size: 1.8em; }}
            .zen-btn-schedule {{ padding: 12px 25px; font-size: 1em; }}
            .zen-section {{ padding: 40px 15px; }}
        }}
    </style>
    """, unsafe_allow_html=True)
set_custom_style() # Chame a função de estilo customizado

# --- Placeholder para os dados do Diretor e da Empresa ---
diretor_nome = "Michael Bruno de Lima"
empresa_dele = "Zenvia Tech"
segmento_empresa = "Marketing e Customer Success"
seu_linkedin_url = "https://www.linkedin.com/in/maria-let%C3%ADcia-sousa-335bb9154/" # Seu perfil do LinkedIn
seu_email = "maarinnolasco@gmail.com" # Seu e-mail de contato
seu_nome = "Maria Leticia Sousa" # Para o footer

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
    <div style="font-size: 1.2em; max-width: 800px; margin: 0 auto 40px auto; color: {BACKGROUND_COLOR};">
        <ul style="list-style: none; padding: 0; text-align: left;">
            <li style="margin-bottom: 15px;"><span style="color: {HIGHLIGHT_COLOR};
