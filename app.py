import streamlit as st

# Cores da Zenvia (confirmadas visualmente no site)
ZEN_BLUE_PRIMARY = "#007AFF" # Azul principal vibrante da Zenvia
ZEN_GREEN_CTA = "#00E676"   # Verde do CTA
ZEN_TEXT_COLOR = "#2C2C2C"  # Texto escuro, mas não preto puro
ZEN_LIGHT_BG = "#F8F8F8"    # Fundo quase branco
ZEN_LIGHT_BLUE_BG = "#E8F0FE" # Um azul super claro para seções de destaque

st.set_page_config(
    page_title="Zenvia Tech | Comunicação que gera resultado",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def set_zenvia_style():
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Open+Sans:wght@400;600&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {{
            font-family: 'Montserrat', sans-serif;
            color: {ZEN_TEXT_COLOR};
            background-color: {ZEN_LIGHT_BG};
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
            background-color: #fff;
            padding: 20px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }}
        .zen-logo {{ max-width: 150px; }}
        
        .zen-hero {{
            background-color: {ZEN_BLUE_PRIMARY};
            color: #fff;
            padding: 80px 20px;
            text-align: center;
            background-image: linear-gradient(to right, {ZEN_BLUE_PRIMARY}, #0056b3);
            border-radius: 0 0 15px 15px;
            margin-bottom: 30px;
        }}
        .zen-hero h1 {{
            font-size: 3.2em;
            margin-bottom: 20px;
            font-weight: 700;
            line-height: 1.2;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }}
        .zen-hero p {{
            font-size: 1.4em;
            margin-bottom: 40px;
            font-weight: 400;
            opacity: 0.9;
        }}
        .zen-btn-schedule {{
            display: inline-block;
            background-color: {ZEN_GREEN_CTA};
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
            background-color: #00c853;
            transform: translateY(-3px);
        }}
        
        .zen-section {{
            padding: 60px 40px;
            background-color: #fff;
            margin: 20px auto;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            max-width: 900px;
        }}
        .zen-section.bg-light {{ background-color: {ZEN_LIGHT_BLUE_BG}; }}
        h2 {{
            font-size: 2.5em;
            color: {ZEN_BLUE_PRIMARY};
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
            background-color: {ZEN_GREEN_CTA};
            margin: 15px auto 0;
            border-radius: 2px;
        }}
        h3 {{
            font-size: 2em;
            color: {ZEN_BLUE_PRIMARY};
            margin-bottom: 25px;
            text-align: center;
            font-weight: 700;
        }}
        .zen-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 40px;
            margin-top: 40px;
        }}
        .zen-item {{
            text-align: center;
            padding: 35px;
            border-radius: 10px;
            background-color: #fff;
            box-shadow: 0 3px 10px rgba(0,0,0,0.07);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .zen-item:hover {{
            transform: translateY(-7px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        }}
        .zen-item img {{
            max-width: 90px;
            margin-bottom: 25px;
        }}
        .zen-item h4 {{
            font-size: 1.6em;
            color: {ZEN_TEXT_COLOR};
            margin-bottom: 15px;
            font-weight: 600;
        }}
        .zen-item p {{
            font-size: 1.15em;
            color: #555;
        }}
        .zen-logo-cliente {{
            max-width: 140px;
            margin-bottom: 20px;
        }}
        .zen-resultado {{
            font-size: 2.0em;
            font-weight: 700;
            color: {ZEN_GREEN_CTA};
            margin-top: 20px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }}
        .personalized-solution {{
            padding: 50px;
            background-color: #e6f0ff;
            border-left: 6px solid {ZEN_BLUE_PRIMARY};
            border-radius: 12px;
            margin-top: 40px;
        }}
        .personalized-solution h3 {{
            font-size: 2.2em;
            color: {ZEN_BLUE_PRIMARY};
            margin-bottom: 20px;
            text-align: center;
            font-weight: 700;
        }}
        .personalized-solution p, .personalized-solution li {{
            font-size: 1.2em;
            color: #444;
            line-height: 1.7;
        }}
        .personalized-solution ul {{
            list-style: none;
            padding: 0;
            margin-top: 30px;
        }}
        .personalized-solution ul li {{
            margin-bottom: 15px;
        }}
        .personalized-solution ul li strong {{
            color: {ZEN_BLUE_PRIMARY};
        }}
        
        .zen-footer {{
            background-color: {ZEN_TEXT_COLOR};
            color: #fff;
            text-align: center;
            padding: 40px 20px;
            font-size: 1em;
            margin-top: 30px;
        }}
        .zen-footer a {{
            color: {ZEN_GREEN_CTA};
            text-decoration: none;
        }}
        .zen-footer a:hover {{
            text-decoration: underline;
        }}
        
        .st-markdown a {{
            color: {ZEN_BLUE_PRIMARY};
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
set_zenvia_style()

# --- Placeholder para os dados do Diretor e da Empresa ---
# AJUSTADO COM OS DADOS QUE VOCÊ FORNECEU
diretor_nome = "Michael Bruno de Lima"
empresa_dele = "Zenvia Tech"
segmento_empresa = "Marketing e Customer Success"
seu_linkedin_url = "https://www.linkedin.com/in/maria-let%C3%ADcia-sousa-335bb9154/" # Seu perfil do LinkedIn
seu_email = "maarinnolasco@gmail.com" # Seu e-mail de contato
seu_nome = "Maria Leticia Sousa" # Para o footer

# --- Layout da One Page ---

# Header
st.markdown(f"""
<div class="zen-header">
    <img src="https://www.zenvia.com/wp-content/uploads/2023/11/logo-zenvia.svg" alt="Logo Zenvia" class="zen-logo">
</div>
""", unsafe_allow_html=True)

# Hero Section (Título personalizado e chamada vibrante)
st.markdown(f"""
<div class="zen-hero">
    <h1>{diretor_nome}, e se a {empresa_dele} tivesse superpoderes de comunicação?</h1>
    <p>A gente sabe que o futuro das vendas e do marketing está nas conversas que engajam. E a Zenvia tem o mapa da mina para você escalar isso, sem complicação.</p>
    <a href="#agendamento" class="zen-btn-schedule">Agendar um Bate-Papo Transformador</a>
</div>
""", unsafe_allow_html=True)

# A Dor (Humanizado e com a sua voz)
st.markdown(f"""
<section class="zen-section">
    <h2>{diretor_nome}, a gente sabe que desafios te tiram o sono...</h2>
    <p style="text-align: center; font-size: 1.2em; max-width: 800px; margin: 0 auto 40px auto; color: #555;">No ritmo alucinante do mercado de hoje, engajar e encantar clientes é uma arte (e uma ciência!). Se você está buscando soluções para:</p>
    <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; text-align: left; font-size: 1.15em; color: #444; margin: 0 auto; max-width: 800px;">
        <li><span style="color: {ZEN_BLUE_PRIMARY}; font-weight: 700; margin-right: 10px;">•</span> Dar um chega pra lá na baixa conversão de leads?</li>
        <li><span style="color: {ZEN_BLUE_PRIMARY}; font-weight: 700; margin-right: 10px;">•</span> Acabar com os gargalos no atendimento ao cliente?</li>
        <li><span style="color: {ZEN_BLUE_PRIMARY}; font-weight: 700; margin-right: 10px;">•</span> Personalizar a comunicação em escala, mas sem perder o toque humano?</li>
        <li><span style="color: {ZEN_BLUE_PRIMARY}; font-weight: 700; margin-right: 10px;">•</span> Transformar o marketing e vendas da {empresa_dele} em uma máquina de resultados?</li>
    </ul>
    <p style="text-align: center; font-size: 1.2em; max-width: 800px; margin: 50px auto 0 auto; color: #555;">Se a resposta é sim para alguma delas, a gente tem uma conversa que vai te interessar.</p>
</section>
""", unsafe_allow_html=True)

# A Solução Zenvia (Com a pegada do PDF Drivin nos "poderes" mas focada na Zenvia)
st.markdown(f"""
<section class="zen-section bg-light">
    <h2>Como a Zenvia empodera a {empresa_dele} a crescer?</h2>
    <p style="text-align: center; font-size: 1.2em; max-width: 800px; margin: 0 auto 50px auto; color: #555;">Com a gente, a <strong>{empresa_dele}</strong> vai conseguir:</p>

    <div class="zen-grid">
        <div class="zen-item">
            <img src="https://img.icons8.com/ios-filled/100/007AFF/bot.png" alt="Chatbot Icon">
            <h4>Atendimento que nunca dorme (e resolve!)</h4>
            <p>Seus clientes atendidos 24/7 por chatbots inteligentes, liberando sua equipe para focar no que realmente faz a diferença. <br>É **agilidade** na veia!</p>
        </div>
        <div class="zen-item">
            <img src="https://img.icons8.com/ios-filled/100/007AFF/speech-bubble.png" alt="Speech Bubble Icon">
            <h4>Conversas que vendem e fidelizam</h4>
            <p>Comunicação super personalizada via WhatsApp, SMS, e-mail e voz, criando experiências que os clientes amam (e compram de novo!). <br>É **engajamento** de verdade!</p>
        </div>
        <div class="zen-item">
            <img src="https://img.icons8.com/ios-filled/100/007AFF/target.png" alt="Target Icon">
            <h4>Leads quentes na sua mão (e em escala!)</h4>
            <p>Automatize a qualificação de leads, entregando oportunidades "no ponto" para o seu time de vendas. <br>É **eficiência** máxima!</p>
        </div>
        <div class="zen-item">
            <img src="https://img.icons8.com/ios-filled/100/007AFF/flow-chart.png" alt="Flow Chart Icon">
            <h4>Visão 360º para decisões certeiras</h4>
            <p>Integre todos os seus canais e tenha uma visão completa do cliente para tomar decisões estratégicas que impulsionam o crescimento. <br>É **controle total**!</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Cases de Sucesso (mantive os dados, mas com a linguagem mais leve)
st.markdown(f"""
<section class="zen-section">
    <h2>Quem já está virando o jogo com a Zenvia?</h2>
    <div class="zen-grid">
        <div class="zen-item">
            <img src="https://via.placeholder.com/120x60?text=LOGO+CLIENTE+1" alt="Logo Cliente 1" class="zen-logo-cliente">
            <h4>Gigante do Varejo</h4>
            <p><strong>O desafio:</strong> Milhões de clientes e dificuldade em dar atenção individualizada.</p>
            <p><strong>A virada:</strong> Implementamos chatbots no WhatsApp para atendimento e campanhas de SMS ultra-segmentadas.</p>
            <p class="zen-resultado">🚀 +40% Leads Qualificados</p>
            <p class="zen-resultado">💰 -30% Custo no Atendimento</p>
        </div>
        <div class="zen-item">
            <img src="https://via.placeholder.com/120x60?text=LOGO+CLIENTE+2" alt="Logo Cliente 2" class="zen-logo-cliente">
            <h4>Líder em Serviços</h4>
            <p><strong>O desafio:</strong> Leads esfriando no funil de vendas e processos manuais demais.</p>
            <p><strong>A virada:</strong> Automação completa do fluxo de nutrição de leads e integração com CRM existente.</p>
            <p class="zen-resultado">📈 +25% Taxa de Conversão</p>
            <p class="zen-resultado">⏱️ -20% Tempo de Vendas</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Solução Personalizada (o Coração da Prospecção - foco na empresa DELE)
st.markdown(f"""
<section class="zen-section personalized-solution">
    <h3>{diretor_nome}, uma solução que a {empresa_dele} vai amar (e sentir no bolso)!</h3>
    <p style="text-align: center; font-size: 1.2em; max-width: 800px; margin: 0 auto 30px auto; color: #444;">Pesquisamos a fundo o universo da <strong>{empresa_dele}</strong> e os desafios do setor de <strong>{segmento_empresa}</strong>. Com a Zenvia, a gente pode, juntos:</p>
    <ul style="list-style: none; padding: 0; margin-top: 30px; text-align: left; font-size: 1.2em; color: #333; max-width: 700px; margin: 0 auto;">
        <li><span style="color: {ZEN_BLUE_PRIMARY}; font-weight: 700; margin-right: 10px;">✅</span> <strong>Multiplicar a captação de leads</strong>, focando em oportunidades que realmente se convertem nos seus produtos/serviços de SaaS e Comunicações Digitais.</li>
        <li><span style="color: {ZEN_BLUE_PRIMARY}; font-weight: 700; margin-right: 10px;">✅</span> <strong>Blindar seu funil de vendas</strong>, garantindo que nenhum cliente em potencial se perca, otimizando cada etapa da jornada.</li>
        <li><span style="color: {ZEN_BLUE_PRIMARY}; font-weight: 700; margin-right: 10px;">✅</span> <strong>Transformar clientes em fãs</strong> com experiências de comunicação pós-venda que geram lealdade e recompra (e depoimentos 5 estrelas!).</li>
        <li><span style="color: {ZEN_BLUE_PRIMARY}; font-weight: 700; margin-right: 10px;">✅</span> **[Ponto Super Personalizado Aqui]:** Otimizar a jornada do cliente da {empresa_dele} desde o primeiro contato, garantindo que as ferramentas de marketing e vendas trabalhem em perfeita sintonia, aumentando a satisfação e o churn.</li>
    </ul>
    <p style="margin-top: 40px; text-align: center; font-size: 1.2em; color: #444;">Não é mágica, é inteligência Zenvia. Estamos prontos para mostrar como tudo isso se traduz em resultados reais para a <strong>{empresa_dele}</strong>.</p>
</section>
""", unsafe_allow_html=True)

# Seção de Agendamento (Com Widget Integrado e CTA amigável)
st.markdown('<section id="agendamento" class="zen-section agenda-section">', unsafe_allow_html=True)
st.markdown(f"""
    <h2>{diretor_nome}, vamos bater um papo sem compromisso?</h2>
    <p style="font-size: 1.2em; margin-bottom: 30px; color: #555;">Seu tempo é ouro, e o nosso bate-papo de 15 minutinhos será recheado de insights e focado nos seus desafios. Escolha o melhor horário:</p>
""", unsafe_allow_html=True)

# --- Opção 1: Embedar Calendly/HubSpot Meetings (Recomendado para o teste da Zenvia) ---
# SUBSTITUA PELO SEU CÓDIGO EMBED DO CALENDLY/HUBSPOT MEETINGS!
# É CRUCIAL que você configure seu link de agendamento lá e cole aqui.
# Por exemplo, se seu link Calendly for https://calendly.com/minhamaria/15min
calendly_embed_code = f"""
<div class="calendly-inline-widget" data-url="https://calendly.com/SEU_USUARIO/15min" style="min-width:320px;height:700px; border-radius: 12px; overflow: hidden;"></div>
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
"""
# Substitua a linha acima com o seu código de embed do Calendly ou HubSpot Meetings.
# Exemplo (se você tiver o seu link do Calendly):
# calendly_embed_code = f"""
# <div class="calendly-inline-widget" data-url="https://calendly.com/SEU_USUARIO_DO_CALENDLY/15min-conversa" style="min-width:320px;height:700px; border-radius: 12px; overflow: hidden;"></div>
# <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
# """

st.markdown(calendly_embed_code, unsafe_allow_html=True)


st.markdown(f"""
    <p style="margin-top: 50px; font-size: 1.1em; color: #555;">Prefere um contato mais direto, sem enrolação? Me chama no LinkedIn ou manda um e-mail:</p>
    <p style="font-size: 1.2em; font-weight: 600; margin-top: 15px;">
        <a href="{seu_linkedin_url}" target="_blank" style="color: {ZEN_BLUE_PRIMARY}; text-decoration: none;">Meu LinkedIn</a> | <a href="mailto:{seu_email}" style="color: {ZEN_BLUE_PRIMARY}; text-decoration: none;">{seu_email}</a>
    </p>
""", unsafe_allow_html=True)

st.markdown('</section>', unsafe_allow_html=True)


# Footer
st.markdown(f"""
<div class="zen-footer">
    <p>Criado com paixão e inteligência por {seu_nome}. 😉</p>
    <p>&copy; 2025 Zenvia. Todos os direitos reservados. | Este conteúdo é parte de um desafio de prospecção.</p>
</div>
""", unsafe_allow_html=True)
