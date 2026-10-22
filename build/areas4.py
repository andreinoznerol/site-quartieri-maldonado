# Páginas adicionais: Para trabalhadores, Remoção na Polícia Penal do RS, Política de Privacidade e Termos de Uso
T = ' | Quartieri & Maldonado Advogados Associados'

# ---------------- Trabalhista › Para trabalhadores ----------------
page_area('trabalhador',
 'Direito do Trabalhador' + T,
 'Análise jurídica séria para trabalhadores do Rio Grande do Sul. Atuação em atrasos salariais, horas extras, rescisões, acidentes de trabalho e demais violações trabalhistas.',
 'Para trabalhadores',
 'Seus direitos trabalhistas merecem análise séria e atuação firme',
 'Se houve atraso salarial, falta de FGTS, horas extras não pagas, irregularidades na rescisão, acidente de trabalho ou outras violações, o caso pode exigir providência jurídica adequada.',
 'Falar com o escritório', 'trabalhista', 'Ilustração de um capacete de trabalho e uma pasta.', 'jackson', [
 b_statement('Nem toda irregularidade aparece de imediato', 'Muitos trabalhadores encerram o contrato sem saber se receberam corretamente, suportam jornadas abusivas por longos períodos ou convivem com descumprimentos recorrentes sem conhecer as medidas cabíveis. A análise da relação de emprego, dos pagamentos realizados, da jornada praticada e dos documentos disponíveis indica a viabilidade jurídica e o caminho processual adequado.'),
 b_checks('Muitos trabalhadores sofrem diariamente com:', '', ['Atraso de salários','Falta de depósito de FGTS','Horas extras não pagas','Intervalos suprimidos e excesso de jornada','Insalubridade e periculosidade','Acidente de trabalho','Assédio moral e pressão abusiva','Demissão com verbas rescisórias incorretas'], warn=True),
 b_statement('Cada situação exige leitura técnica própria', 'A análise da relação de emprego, dos documentos disponíveis e das circunstâncias do caso permite indicar a viabilidade e a medida juridicamente cabível.', link=('rescisao-indireta.html','Salário atrasado ou FGTS sem depósito? Veja a rescisão indireta')),
 b_faq('Dúvidas frequentes', '', [
   ('Fui demitido e tenho dúvidas sobre os valores recebidos. Ainda vale analisar?','Sim. A conferência das verbas rescisórias costuma ser um dos motivos mais comuns de consulta.'),
   ('Ainda estou trabalhando. Posso buscar orientação?','Sim. Muitas situações devem ser avaliadas ainda durante o vínculo, inclusive para preservar provas e definir a melhor estratégia.'),
   ('Não tenho todos os documentos. Isso impede a análise?','Não. Outros elementos podem ser relevantes, como mensagens, extratos, recibos, registros de ponto e testemunhas.'),
   ('Quanto tempo posso esperar para buscar meus direitos?','Alguns direitos estão sujeitos a prazos legais. Quanto antes houver análise, melhor tende a ser a preservação da prova e da estratégia.'),
   ('Como funciona o primeiro contato?','Você apresenta a situação, os documentos disponíveis são avaliados e recebe orientação objetiva sobre viabilidade e próximos passos.')]),
 b_statement('Análise jurídica para esclarecer direitos e indicar as medidas cabíveis', 'Por isso, é muito importante buscar orientação antes que prazos se esgotem ou que provas se percam. Um primeiro contato já permite organizar os fatos e avaliar o que pode ser feito.', 'quiet'),
 lambda link: b_cta('Converse com o escritório para entender o que é possível no seu caso', 'O primeiro contato serve para compreender a situação, avaliar os documentos disponíveis e indicar os próximos passos com objetividade.', 'Entrar em contato', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre os meus direitos trabalhistas.', parent=('trabalhista','Direito Trabalhista'))

# ---------------- Direito Público › Remoção na Polícia Penal do RS ----------------
page_area('remocao-policiais-penais-rs',
 'Remoção de Policiais Penais do RS / SUSEPE' + T,
 'Atuação jurídica em pedidos de remoção e negativas na Polícia Penal do RS / SUSEPE: saúde, unidade familiar, permuta e concurso de remoções.',
 'Remoção na Polícia Penal do RS',
 'Remoção de policiais penais do RS',
 'Orientação jurídica para pedidos de mudança de lotação e negativas de remoção na Polícia Penal do Rio Grande do Sul / SUSEPE. Examinamos o motivo do pedido, a situação funcional e as normas estaduais para definir os próximos passos.',
 'Conversar sobre minha remoção', 'remocao', 'Ilustração de um mapa com marcador de localização.', 'jackson', [
 b_statement('Pedido negado ou ainda em preparação', 'A atuação pode começar na organização do requerimento ou após o indeferimento. O exame considera a modalidade de remoção, os documentos apresentados, os motivos informados pela instituição e as medidas disponíveis para o servidor.'),
 b_details('Hipóteses previstas nas normas estaduais', 'O regulamento de remoções prevê situações com requisitos próprios para os servidores da Polícia Penal do RS.', [
   {'t':'Saúde do servidor ou de familiares','p':'Abrange saúde própria, do cônjuge ou companheiro e de dependentes, com requisitos de comprovação médica e de impossibilidade de tratamento na localidade de lotação.'},
   {'t':'Manutenção da unidade familiar','p':'Há hipóteses relacionadas à lotação de cônjuges ou companheiros. O enquadramento considera a situação funcional e a avaliação administrativa prevista na norma.'},
   {'t':'Permuta e concurso de remoções','p':'A troca de lotação entre servidores e o preenchimento de vagas em concurso de remoções seguem critérios próprios. Edital e classificação integram a avaliação.'}]),
 b_statement('A razão do indeferimento precisa ser examinada', 'Uma resposta baseada em falta de efetivo ou interesse do serviço deve ser lida junto à modalidade de remoção, às normas aplicáveis e às provas apresentadas. O exame jurídico verifica como a instituição fundamentou a negativa e se há elementos para pedir sua revisão.'),
 b_band('O que examinamos no processo', '', [
   {'t':'Requerimento e resposta','p':'Fundamento do pedido, documentos anexados, razões do indeferimento e data de ciência da decisão administrativa.'},
   {'t':'Vínculo e lotação','p':'Ficha funcional, unidade atual e pretendida, tempo de exercício e eventual estágio probatório, além das informações familiares pertinentes ao pedido.'},
   {'t':'Provas e regras do procedimento','p':'Registros médicos e avaliação oficial nos pedidos de saúde; edital, vagas e classificação nos concursos; documentos funcionais nos pedidos de unidade familiar ou permuta.'}]),
 b_statement('Atuação administrativa e judicial', 'A Quartieri & Maldonado atua na defesa de servidores e no controle de atos administrativos. Organizamos os fundamentos e os documentos do pedido, acompanhamos a tramitação e avaliamos a contestação de decisões. A necessidade de uma ação judicial depende do fundamento da remoção e das provas disponíveis.'),
 b_faq('Dúvidas sobre remoção na Polícia Penal do RS', '', [
   ('Quem está em estágio probatório pode pedir remoção?','O regulamento restringe a remoção a pedido durante o estágio probatório, mas prevê exceções, como saúde, unidade familiar nas hipóteses regulamentadas e permuta. O enquadramento depende do motivo e dos requisitos do pedido.'),
   ('A falta de efetivo encerra a discussão?','A justificativa precisa ser examinada junto à modalidade de remoção e às regras aplicáveis. É necessário verificar como a instituição fundamentou a negativa e quais documentos sustentam o pedido para avaliar a possibilidade de contestação.'),
   ('Ter um laudo médico basta para obter a remoção?','O laudo é relevante, mas há outros requisitos e comprovação pelo serviço médico oficial. Os documentos precisam relacionar a condição de saúde à mudança de lotação pretendida.'),
   ('Posso pedir remoção para acompanhar meu cônjuge?','Há situações específicas de manutenção da unidade familiar. A instituição de origem do cônjuge, a lotação, a forma do deslocamento e o vínculo precisam ser examinados.'),
   ('A orientação também abrange pedido já negado?','Sim. O exame pode abranger a decisão de indeferimento e a possibilidade de reconsideração, recurso ou medida judicial, conforme os fundamentos e os documentos do processo.')]),
 b_statement('Remoção em outras carreiras públicas', 'Para servidores de outras instituições, o pedido precisa considerar o regime jurídico da respectiva carreira.', 'quiet', link=('remocao-servidor-publico.html','Ver remoção de servidor público')),
 lambda link: b_cta('Converse sobre sua mudança de lotação', 'Informe sua unidade atual, a lotação pretendida e o motivo da remoção. Se já recebeu uma negativa, tenha o requerimento e a resposta administrativa disponíveis.', 'Conversar sobre minha remoção', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre remoção na Polícia Penal do RS.', parent=('direito-publico','Direito Público'))

# ---------------- Páginas legais ----------------
import re as _re
def slugify(t):
    import unicodedata
    t = unicodedata.normalize('NFD', t).encode('ascii','ignore').decode()
    return _re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')

def legal_page(fname, title, lede, updated, sections, canon, desc):
    r = ''
    toc = ''.join(f'<li><a href="#{slugify(h)}">{E(h)}</a></li>' for h,_ in sections)
    body = ''
    for h, parts in sections:
        body += f'<h2 id="{slugify(h)}">{E(h)}</h2>'
        for kind, val in parts:
            if kind == 'p': body += f'<p>{val}</p>'
            elif kind == 'ul': body += '<ul>' + ''.join(f'<li>{x}</li>' for x in val) + '</ul>'
            elif kind == 'box': body += f'<div class="contact-box">{val}</div>'
            elif kind == 'table':
                head_, rows = val
                body += '<table><thead><tr>' + ''.join(f'<th scope="col">{x}</th>' for x in head_) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows) + '</tbody></table>'
    main = f'''<main>
<section class="legal-hero">
  <div class="wrap">
    <nav class="crumb" aria-label="Você está em"><a href="index.html">Início</a><span aria-hidden="true">/</span><span aria-current="page">{E(title)}</span></nav>
    <h1 class="display">{E(title)}</h1>
    <p>{E(lede)}</p>
    <div class="meta">Última atualização: {updated}</div>
  </div>
</section>
<article class="legal">
  <div class="wrap">
    <ol class="toc" aria-label="Nesta página">{toc}</ol>
    {body}
  </div>
</article>
</main>
'''
    doc = head(r, title + T, desc, canon) + header(r, WA_DEFAULT) + main + footer(r, WA_DEFAULT)
    open(f'{OUT}/{fname}', 'w', encoding='utf-8').write(doc)

QM = 'Quartieri &amp; Maldonado Advogados Associados'
DPO = '<a href="mailto:dpo@quartierimaldonado.com">dpo@quartierimaldonado.com</a>'

legal_page('termos-de-uso.html', 'Termos de Uso',
 'Regras básicas para acesso ao site, leitura de publicações e uso de conteúdo informativo.',
 '1º de julho de 2026', [
 ('1. Objetivo e aceitação', [('p',f'Estes Termos de Uso estabelecem as condições aplicáveis ao acesso e à utilização do site da {QM}.'),('p','A navegação no site pressupõe ciência e observância destes Termos. Caso não haja concordância com as condições apresentadas, a utilização deverá ser interrompida.')]),
 ('2. Natureza institucional e informativa', [('p','O site possui finalidade institucional e disponibiliza informações sobre a sociedade de advocacia, suas áreas de atuação e temas jurídicos de interesse geral.'),('p','Os conteúdos são apresentados em caráter informativo, com observância das normas legais e profissionais aplicáveis à advocacia. Não constituem oferta de resultado, indução ao litígio ou garantia de solução para situações concretas.'),('p','As informações disponibilizadas não constituem orientação jurídica e não substituem consulta individual. Também não devem ser interpretadas como parecer jurídico ou recomendação de conduta para determinado caso.'),('p','A adequada avaliação de uma situação jurídica depende de suas circunstâncias próprias, incluindo fatos, documentos, provas, prazos, relações envolvidas e legislação aplicável.'),('p','As normas e os entendimentos jurídicos poderão ser alterados após a publicação de um conteúdo. Por esse motivo, não deverá ser tomada decisão exclusivamente com base nas informações gerais disponíveis no site.')]),
 ('3. Relação profissional', [('p','O acesso ao site, a leitura de conteúdos ou a utilização dos canais de contato disponibilizados não estabelecem, por si só, relação advogado-cliente nem implicam aceitação de representação profissional.'),('p','A relação profissional somente será constituída após manifestação expressa de aceitação, verificação de eventuais conflitos de interesses, definição do escopo da atuação e formalização dos instrumentos aplicáveis.'),('p','O envio espontâneo de informações por canal externo não representa confirmação de atendimento, assunção de prazo ou responsabilidade por medida jurídica.')]),
 ('4. Uso adequado do site', [('p','O site deverá ser utilizado de forma lícita e compatível com sua finalidade institucional. Não são permitidas práticas que possam:'),('ul',['comprometer a segurança, a disponibilidade ou o funcionamento do site;','tentar obter acesso não autorizado a sistemas, áreas restritas ou informações;','introduzir código malicioso, executar testes abusivos ou explorar vulnerabilidades;','realizar extração automatizada massiva de conteúdo ou dados;','utilizar a identidade, a marca ou os conteúdos para finalidade enganosa, ilícita ou não autorizada; ou','violar direitos de terceiros ou a legislação aplicável.']),('p','Poderão ser adotadas medidas técnicas e jurídicas para prevenir, interromper ou apurar utilizações indevidas.')]),
 ('5. Propriedade intelectual', [('p',f'O conteúdo do site, incluindo textos, artigos, publicações, títulos, seleção e organização editorial, bem como marcas, imagens de titularidade própria, elementos gráficos, identidade visual, código e demais elementos próprios, constitui propriedade intelectual da {QM}.'),('p','Imagens e demais ativos licenciados de terceiros constituem propriedade intelectual de seus respectivos titulares e são utilizados de acordo com as licenças ou autorizações aplicáveis.'),('p',f'A utilização do site implica ciência e concordância quanto à titularidade da {QM} sobre seus elementos próprios. O acesso não implica cessão, licença ampla ou transferência de direitos sobre esses elementos.'),('p','É permitido compartilhar links públicos e realizar citações nos limites autorizados pela legislação, com indicação adequada da autoria e da origem.'),('p','Nas utilizações autorizadas por estes Termos, toda referência parcial ao conteúdo publicada na internet deverá conter a identificação da fonte e um link clicável para a página original correspondente. Esse link deverá permitir o rastreamento normal pelos mecanismos de busca, sem o atributo nofollow ou outra configuração equivalente que restrinja esse rastreamento.'),('p','A reprodução integral, modificação, exploração comercial, remoção de créditos ou utilização da marca dependerá de autorização prévia, salvo nas hipóteses expressamente permitidas por lei.')]),
 ('6. Links e serviços externos', [('p','O site poderá disponibilizar links para plataformas, aplicações e conteúdos mantidos por terceiros. A inclusão desses links possui finalidade informativa ou funcional e não representa controle, aprovação ou responsabilidade sobre os serviços externos.'),('p','O acesso a serviços de terceiros ficará sujeito aos respectivos termos de uso, políticas de privacidade, condições de disponibilidade e práticas de segurança.')]),
 ('7. Atualização dos conteúdos', [('p','Os conteúdos poderão ser corrigidos, atualizados, reorganizados ou removidos a qualquer momento, inclusive para refletir alterações legislativas, regulatórias, jurisprudenciais, institucionais ou editoriais.'),('p','Não há garantia de que toda informação permanecerá permanentemente disponível ou atualizada em relação a acontecimentos posteriores à sua publicação.')]),
 ('8. Disponibilidade e segurança', [('p','Poderão ocorrer interrupções temporárias em razão de manutenção, atualização, falha técnica, indisponibilidade de fornecedores ou eventos fora de controle razoável.'),('p','São adotadas medidas destinadas à manutenção da segurança e da estabilidade do site, sem garantia de funcionamento contínuo, ausência absoluta de falhas ou completa imunidade a riscos próprios do ambiente digital.')]),
 ('9. Responsabilidade', [('p','O conteúdo é elaborado com finalidade informativa e com o cuidado compatível com sua natureza. Ainda assim, sua aplicação a uma situação concreta exige análise jurídica própria.'),('p','Não haverá responsabilidade por decisões tomadas exclusivamente com base em conteúdo geral do site, sem a consideração das circunstâncias específicas do caso e sem orientação profissional adequada.'),('p','Estes Termos não excluem nem limitam responsabilidades que não possam ser afastadas pela legislação aplicável.')]),
 ('10. Privacidade e proteção de dados', [('p','O tratamento de dados pessoais relacionado à navegação é descrito na <a href="politica-de-privacidade.html">Política de Privacidade</a>, que integra estes Termos para fins de informação e transparência.')]),
 ('11. Legislação aplicável', [('p','O acesso e a utilização do site serão regidos pela legislação brasileira, sem prejuízo das normas profissionais aplicáveis ao exercício da advocacia.')]),
 ('12. Alterações destes Termos', [('p','Estes Termos poderão ser atualizados para refletir mudanças legais, regulatórias, tecnológicas, institucionais ou operacionais. A versão vigente será sempre aquela publicada nesta página, acompanhada da data de sua última atualização.')]),
 ], '/termos-de-uso', 'Termos de Uso do site Quartieri & Maldonado Advogados Associados.')

LI = 'Legítimo interesse'; OL = 'Cumprimento de obrigação legal ou regulatória'
legal_page('politica-de-privacidade.html', 'Política de Privacidade',
 'Como este site trata dados técnicos de navegação, analytics e mensuração.',
 '1º de julho de 2026', [
 ('1. Objetivo e abrangência', [('p',f'Esta Política de Privacidade apresenta, de forma objetiva e transparente, como são tratados os dados pessoais relacionados à navegação no site da {QM}.'),('p','O site possui finalidade institucional e informativa. Não são disponibilizadas contas de usuário, área de login, compras, newsletter ou formulários próprios de cadastro.'),('p','O tratamento de dados realizado no contexto de atendimento ou de prestação de serviços jurídicos poderá observar regras próprias, além dos deveres legais, regulatórios, contratuais e profissionais aplicáveis à advocacia.')]),
 ('2. Controlador e canal de privacidade', [('p','Para os tratamentos descritos nesta Política, a controladora dos dados pessoais é:'),('box',f'<p><strong>{QM}</strong></p>'),('p','Solicitações relacionadas à privacidade e à proteção de dados poderão ser encaminhadas para:'),('box',f'<p>{DPO}</p>')]),
 ('3. Dados que podem ser tratados', [('p','Durante a utilização do site, poderão ser tratados dados técnicos e informações relacionadas à navegação, tais como:'),('ul',['endereço IP e informações de rede;','tipo de navegador, dispositivo e sistema operacional;','data e horário de acesso;','páginas visitadas e tempo aproximado de navegação;','página ou endereço eletrônico de origem;','interações com links, botões e demais recursos do site;','informações técnicas relacionadas à segurança, disponibilidade e desempenho.']),('p','Essas informações poderão constituir dados pessoais quando permitirem a identificação direta ou indireta de uma pessoa natural.'),('p','O site não coleta, por meio de formulários próprios, nome, telefone, e-mail, CPF, endereço residencial, documentos ou conteúdo de comunicações.')]),
 ('4. Como os dados são obtidos', [('p','Os dados poderão ser obtidos automaticamente durante o acesso ao site, por meio da infraestrutura de hospedagem, de registros técnicos, de ferramentas de segurança e de serviços de mensuração.'),('p','Quando houver acesso a plataformas externas por meio de links disponibilizados no site, o tratamento realizado nessas plataformas ficará sujeito também aos respectivos termos e políticas de privacidade.')]),
 ('5. Finalidades e bases legais', [('p','Os dados relacionados à navegação poderão ser tratados para as seguintes finalidades:'),('table',(['Finalidade','Base legal aplicável'],[
    ['Disponibilizar as páginas e os recursos do site',LI],
    ['Manter a segurança, a estabilidade e a integridade do ambiente digital',LI],
    ['Produzir estatísticas de acesso e compreender o desempenho de páginas e conteúdos',LI],
    ['Avaliar, de forma agregada, o desempenho de comunicações e campanhas institucionais',LI],
    ['Prevenir abusos, falhas técnicas e acessos automatizados indevidos',LI],
    ['Cumprir obrigações legais, regulatórias ou determinações de autoridades competentes',OL],
    ['Atender solicitações relacionadas aos direitos dos titulares',OL]])),
    ('p','O legítimo interesse é adotado apenas quando o tratamento se mostra necessário e compatível com as legítimas expectativas dos titulares, consideradas a finalidade, a proporcionalidade e as medidas de proteção aplicáveis.')]),
 ('6. Cookies e tecnologias de mensuração', [('p','Na configuração atual, não são armazenados no dispositivo do visitante cookies de publicidade ou de análise. Também não é utilizado o Pixel da Meta/Facebook.'),('p','Serviços como Google Analytics e Google Ads poderão ser utilizados, em modo sem cookies, para produzir estatísticas gerais de navegação, avaliar o desempenho de conteúdos e campanhas e verificar o funcionamento de recursos do site.'),('p','Mesmo sem o armazenamento de cookies, poderão ser enviados aos provedores sinais técnicos relacionados à navegação, como página acessada, data e horário, endereço de origem, características gerais do navegador ou dispositivo e informações sobre a origem publicitária do acesso. Esses sinais poderão ser utilizados pelos provedores para gerar métricas e estimativas agregadas.'),('p','Essa medição não é utilizada para remarketing, criação de perfis individuais ou personalização de anúncios. Para essa finalidade, não são enviados pelo site dados como nome, telefone, e-mail ou conteúdo de comunicações.'),('p','Caso sejam adotadas novas tecnologias ou alteradas as finalidades de tratamento, esta Política e os mecanismos de privacidade aplicáveis deverão ser revistos.'),('p','Mais informações sobre o tratamento realizado pelo Google estão disponíveis na <a href="https://policies.google.com/privacy?hl=pt-BR" target="_blank" rel="noopener">Política de Privacidade do Google</a>, na página sobre <a href="https://support.google.com/analytics/answer/6004245?hl=pt-BR" target="_blank" rel="noopener">privacidade e proteção de dados no Google Analytics</a> e na explicação sobre o <a href="https://support.google.com/google-ads/answer/10000067?hl=pt-BR" target="_blank" rel="noopener">funcionamento do modo de consentimento</a>.')]),
 ('7. Compartilhamento e operadores', [('p','Os dados poderão ser tratados por fornecedores contratados para viabilizar a hospedagem, a segurança, o funcionamento e a mensuração do site, incluindo:'),('ul',['<strong>Netlify</strong>, responsável pela infraestrutura de hospedagem e entrega das páginas; e','<strong>Google</strong>, quando estiverem ativos os serviços de análise e mensuração.']),('p','O compartilhamento também poderá ocorrer quando necessário para o cumprimento de obrigação legal ou regulatória, atendimento de ordem judicial ou requisição válida de autoridade competente, bem como para o exercício regular de direitos.'),('p','Não são comercializados dados pessoais.')]),
 ('8. Transferência internacional', [('p','Alguns fornecedores de tecnologia poderão armazenar ou processar informações fora do Brasil. Nessas situações, deverão ser observados os requisitos aplicáveis à transferência internacional de dados e adotadas medidas compatíveis com a legislação de proteção de dados.')]),
 ('9. Armazenamento e eliminação', [('p','Os dados serão mantidos somente pelo período necessário ao atendimento das finalidades descritas nesta Política, ressalvadas as hipóteses de conservação autorizadas pela legislação, como o cumprimento de obrigações legais ou regulatórias e o exercício regular de direitos.'),('p','Os prazos e procedimentos aplicados diretamente pelos fornecedores de tecnologia também poderão observar suas respectivas políticas e configurações. Dados estatísticos efetivamente anonimizados poderão ser conservados por período superior, desde que não permitam a identificação do titular.')]),
 ('10. Segurança da informação', [('p','São adotadas medidas técnicas e administrativas compatíveis com a natureza dos dados tratados e com os riscos envolvidos, destinadas a proteger as informações contra acessos não autorizados, perda, alteração, divulgação ou destruição indevida.'),('p','Nenhum ambiente digital é integralmente isento de riscos. Eventuais incidentes serão avaliados e tratados conforme a legislação e os procedimentos aplicáveis.')]),
 ('11. Direitos dos titulares', [('p','Nos termos da Lei Geral de Proteção de Dados Pessoais, poderão ser exercidos, quando aplicáveis, os seguintes direitos:'),('ul',['confirmação da existência de tratamento;','acesso aos dados pessoais;','correção de dados incompletos, inexatos ou desatualizados;','anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade com a legislação;','portabilidade, observada a regulamentação aplicável;','informação sobre as entidades públicas e privadas com as quais ocorreu compartilhamento;','informação sobre a possibilidade de não fornecer consentimento e sobre as consequências da negativa, quando aplicável;','revogação do consentimento e eliminação dos dados tratados com essa base legal, ressalvadas as hipóteses de conservação previstas em lei;','oposição a tratamento realizado em desconformidade com a legislação; e','revisão de decisões tomadas unicamente com base em tratamento automatizado, quando aplicável.']),('p',f'As solicitações poderão ser encaminhadas para {DPO}. Poderão ser solicitadas informações necessárias à confirmação da identidade do requerente e à prevenção de fraude.')]),
 ('12. Links e serviços de terceiros', [('p','O site poderá conter links para serviços externos, como plataformas de mensagens, mapas, redes sociais e outros endereços eletrônicos. Esses serviços possuem regras próprias de tratamento de dados, que deverão ser consultadas diretamente pelo titular.')]),
 ('13. Alterações desta Política', [('p','Esta Política poderá ser atualizada para refletir mudanças legais, regulatórias, tecnológicas ou operacionais. A versão vigente será sempre aquela publicada nesta página, acompanhada da data de sua última atualização.')]),
 ], '/politica-de-privacidade', 'Política de Privacidade do site Quartieri & Maldonado Advogados Associados.')

# ---------------- Página 404 ----------------
r = '/'
nf = f'''<main>
<section class="legal-hero" style="min-height:60vh;display:flex;align-items:center">
  <div class="wrap">
    <h1 class="display">Página não encontrada</h1>
    <p>O endereço acessado não existe ou mudou de lugar. Volte ao início ou fale com o escritório.</p>
    <div class="hero__ctas"><a class="btn btn-solid" href="/">Voltar ao início</a><a class="btn btn-line" href="/#areas">Ver áreas de atuação</a></div>
  </div>
</section>
</main>
'''
open(f'{OUT}/404.html','w',encoding='utf-8').write(head(r,'Página não encontrada'+T,'Página não encontrada.','/404') + header(r, WA_DEFAULT) + nf + footer(r, WA_DEFAULT))
