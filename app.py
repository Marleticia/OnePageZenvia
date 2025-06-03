import streamlit as st

# Cores Personalizadas (AJUSTADAS CONFORME SUAS ÚLTIMAS INSTRUÇÕES)
BACKGROUND_COLOR = "#1A2D40" # Novo Azul Noite/Escuro (padrão Zenvia)
HIGHLIGHT_COLOR = "#007AFF" # Azul vibrante (para ícones, links, sublinhados)
TEXT_COLOR = "#FFFFFF" # Branco (PARA TODOS OS TEXTOS)
SECTION_BG_COLOR = "#2C3E50" # Novo Fundo das seções internas (Cinza/Azul Escuro para contraste com texto branco)
BUTTON_COLOR = "#993399" # Roxo para o botão de agendamento (o roxo original)

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
            color: {TEXT_COLOR}; /* TODOS OS TEXTOS PADRÃO EM BRANCO */
            background-color: {BACKGROUND_COLOR}; /* Fundo azul noite */
            line-height: 1.6;
            font-size: 14px; /* Tamanho base dos textos */
        }}
        
        /* Remove paddings e margens padrão do Streamlit para maior controle */
        .st-emotion-cache-1wvwm0x, .st-emotion-cache-z5fcl4, .st-emotion-cache-uf99v8 {{
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }}

        .css-vk325g {{ display: none !important; }}
        header[data-testid="stHeader"] {{ display: none !important; }}
        
        /* Estilo para o logo "capa horizontal" */
        .zen-header {{
            background-color: {BACKGROUND_COLOR}; /* Cor de fundo do header */
            padding: 0; /* Zero padding para o logo preencher */
            width: 100%;
            height: auto;
            overflow: hidden; /* Garante que nada vaze */
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            min-height: 80px; /* Altura mínima para o logo aparecer bem */
        }}
        .zen-header img {{
            width: 100%; /* Logo cobrindo toda a largura */
            max-height: 150px; /* Limita a altura do logo para não ficar gigante */
            display: block; /* Remove espaços extras */
            object-fit: cover; /* Faz a imagem cobrir o espaço, cortando se necessário */
            object-position: center; /* Centraliza a imagem no espaço */
        }}
        
        .zen-hero {{
            background-color: {HIGHLIGHT_COLOR}; /* Fundo azul vibrante para a hero */
            color: {TEXT_COLOR};
            padding: 50px 20px;
            text-align: center;
            background-image: linear-gradient(to right, {HIGHLIGHT_COLOR}, #0056b3);
            border-radius: 0 0 15px 15px;
            margin-bottom: 30px;
        }}
        .zen-hero h1 {{
            font-size: 2.0em; /* 2.0 * 14px = 28px */
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
            background-color: {BUTTON_COLOR}; /* Botão na cor roxa */
            color: {TEXT_COLOR}; /* Texto do botão em branco */
            padding: 12px 25px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1em; /* 14px */
            transition: background-color 0.3s ease, transform 0.2s ease;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }}
        .zen-btn-schedule:hover {{
            background-color: #7A2E7A; /* Roxo mais escuro no hover */
            transform: translateY(-3px);
        }}
        
        .zen-section {{
            padding: 35px 30px;
            background-color: {SECTION_BG_COLOR}; /* Fundo das seções internas agora é escuro */
            margin: 20px auto;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            max-width: 900px;
            color: {TEXT_COLOR}; /* Texto das seções internas em branco */
        }}
        .zen-section h2, .zen-section h3 {{ /* Títulos dentro das seções internas */
            color: {TEXT_COLOR}; /* Títulos em branco */
        }}
        .zen-section h2 span, .zen-section h3 span {{ /* Ícones dentro dos títulos (Problema, Solução) */
            color: {HIGHLIGHT_COLOR}; /* Ícones em azul vibrante */
        }}

        h2 {{
            font-size: 1.6em; /* 1.6 * 14px = 22.4px */
            text-align: center;
            margin-bottom: 25px;
            font-weight: 700;
            position: relative;
        }}
        h2::after {{
            content: '';
            display: block;
            width: 50px;
            height: 2px;
            background-color: {HIGHLIGHT_COLOR}; /* Linha em azul vibrante */
            margin: 8px auto 0;
            border-radius: 1px;
        }}
        h3 {{ /* Para a nova seção "Solução Integrada" */
            font-size: 1.4em; /* 1.4 * 14px = 19.6px */
            text-align: center;
            margin-bottom: 15px;
            font-weight: 700;
        }}
        
        /* Ajuste para parágrafos e listas dentro das seções */
        .zen-section p, .zen-section ul, .zen-section li {{
            font-size: 1em; /* 14px */
            color: {TEXT_COLOR}; /* Garante texto branco nas seções escuras */
        }}
        .zen-section ul li {{
            margin-bottom: 8px;
        }}
        .zen-section ul li span {{ /* Estilo para os ícones de checkmark/bullets */
            color: {HIGHLIGHT_COLOR}; /* Ícones em azul vibrante */
        }}

        .zen-footer {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR}; /* Texto do footer em branco */
            text-align: center;
            padding: 25px 20px;
            font-size: 0.9em; /* 0.9 * 14px = 12.6px */
            margin-top: 30px;
        }}
        .zen-footer a {{
            color: {HIGHLIGHT_COLOR}; /* Links do footer em azul vibrante */
            text-decoration: none;
        }}
        .zen-footer a:hover {{
            text-decoration: underline;
        }}
        
        /* Links em geral, Streamlit markdown pode aplicar isso */
        .st-markdown a {{
            color: {HIGHLIGHT_COLOR}; /* Links em azul vibrante */
            text-decoration: none;
            font-weight: 600;
        }}
        .st-markdown a:hover {{
            text-decoration: underline;
        }}

        /* Para o texto de contato direto no agendamento */
        .contact-text {{
            font-size: 1em; /* 14px */
            color: {TEXT_COLOR}; /* Texto branco na seção escura */
        }}
        .contact-links a {{
            font-size: 1.1em; /* Um pouco maior para links de contato */
            color: {HIGHLIGHT_COLOR}; /* Links de contato em azul vibrante */
        }}

        html {{ scroll-behavior: smooth; }}

        /* Estilo para o container do iframe do Calendly */
        .calendly-container {{
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin: 25px auto;
            width: 100%; /* Ocupa a largura total da seção */
            max-width: 800px; /* Limita a largura para telas maiores */
        }}
        .calendly-container iframe {{
            width: 100%;
            height: 700px; /* Altura do Calendly */
            border: none;
            background-color: white; /* Garante que o iframe tenha um fundo branco para o Calendly */
        }}

        @media (max-width: 768px) {{
            .zen-hero h1 {{ font-size: 1.6em; }}
            .zen-hero p {{ font-size: 0.9em; }}
            h2 {{ font-size: 1.3em; }}
            .zen-btn-schedule {{ padding: 10px 20px; font-size: 0.9em; }}
            .zen-section {{ padding: 20px 15px; }}
            .zen-header img {{ max-width: 100%; height: auto; }}
            .zen-footer {{ font-size: 0.8em; }}
            .calendly-container {{ margin: 15px auto; }}
            .calendly-container iframe {{ height: 600px; }}
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

# Header com o logo "capa horizontal"
st.markdown(f"""
<div class="zen-header">
    <img src="https://mir-s3-cdn-cf.behance.net/projects/404/4e9f4f212905251.Y3JvcCw4MDgsNjMyLDAsMA.png" alt="Logo da Empresa">
</div>
""", unsafe_allow_html=True)

# Hero Section (Título personalizado e chamada vibrante)
st.markdown(f"""
<div class="zen-hero">
    <h1>Zenvia Tech | Comunicação que gera resultado</h1>
    <p>Soluções multicanal para escalar o relacionamento com leads e clientes sem perder agilidade, personalização e performance.</p>
    <a href="#agendamento" class="zen-btn-schedule">SEU MELHOR HORÁRIO PARA UM BATE-PAPO</a>
</div>
