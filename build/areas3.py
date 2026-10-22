# Terceiro nível: páginas específicas dentro de cada área (executado ao final de build.py)
T = ' | Quartieri & Maldonado Advogados Associados'

# ---------------- Defesa Criminal › Retirada de antecedentes ----------------
page_area('retirada-antecedentes',
 'Retirada de Antecedentes Criminais' + T,
 'Registros como inquéritos arquivados, absolvições ou processos encerrados nem sempre podem continuar prejudicando sua vida profissional.',
 'Retirada de antecedentes',
 'Antecedente criminal no seu nome? Saiba quando é possível retirar ou restringir legalmente',
 'Registros como inquéritos arquivados, absolvições ou processos encerrados não podem continuar prejudicando sua vida profissional e participação em concursos.',
 'Solicitar avaliação jurídica', 'documentos', 'Ilustração de uma pasta com documentos.', 'matheus', [
 b_statement('A manutenção de registros superados pode gerar efeitos indevidos', 'A manutenção de registros em folhas de antecedentes criminais, mesmo após o encerramento de investigações ou processos, impacta diretamente a vida de muitos cidadãos. Inquéritos arquivados, absolvições e penas já cumpridas, embora juridicamente superados, podem continuar gerando efeitos práticos negativos, especialmente em concursos públicos, oportunidades de emprego e análise de vida pregressa. O ordenamento jurídico brasileiro estabelece limites quanto à exposição dessas informações, para evitar que fatos sem relevância atual continuem produzindo consequências indevidas.'),
 b_checks('Situações que podem gerar registro indevido', '', ['Inquérito arquivado','Absolvição','Processo encerrado','Extinção da punibilidade','Pena já cumprida','Registros de transação penal','Apontamentos indevidos em certidões'], warn=True),
 b_band('O que esses registros podem impactar', '', [
   {'t':'Concursos públicos','p':'Especialmente na fase de investigação social.','href':'../direito-publico/investigacao-social.html','more':'Ver investigação social'},
   {'t':'Oportunidades profissionais','p':'Restrições em processos seletivos e análise de perfil.'},
   {'t':'Análise de vida pregressa','p':'Avaliações que consideram registros sem relevância jurídica atual.'}]),
 b_statement('O que a lei garante', 'A Constituição Federal assegura a inviolabilidade da intimidade, da honra e da imagem. No plano infraconstitucional, o Código de Processo Penal restringe a menção de condenações após reabilitação, a Lei de Execução Penal garante o sigilo dos registros após o cumprimento da pena, e a Lei 9.099/1995 limita os efeitos de registros de transação penal. A jurisprudência do Superior Tribunal de Justiça reforça que registros sem relevância atual não devem restringir direitos.'),
 b_details('Benefícios práticos da regularização', '', [
   {'t':'Acesso a concursos públicos','p':'Evita prejuízos indevidos em fases como investigação social.'},
   {'t':'Proteção da imagem e reputação','p':'Impede que fatos já superados continuem gerando estigmatização.'},
   {'t':'Igualdade de oportunidades','p':'Garante que o indivíduo seja avaliado por sua condição atual.'},
   {'t':'Segurança da informação','p':'Restringe o acesso indevido a dados sensíveis em sistemas administrativos.'}]),
 b_statement('Retirada não significa apagar o passado', 'O procedimento jurídico não tem como finalidade eliminar o registro histórico do Estado. O objetivo é retirar ou restringir a exposição do dado, desvincular o nome do cidadão em certidões e consultas administrativas e limitar o acesso às informações a hipóteses legalmente autorizadas. Os dados permanecem arquivados para fins judiciais, mas deixam de produzir efeitos negativos na esfera civil e administrativa.'),
 b_statement('Negativa administrativa e possibilidade judicial', 'Mesmo quando há fundamento jurídico para a retirada ou restrição do registro, a Administração pode manter os apontamentos por ausência de atualização ou interpretação restritiva. Nesses casos, é possível requerer a correção na via administrativa e, em caso de negativa ou omissão, buscar a tutela judicial para assegurar a efetividade dos direitos fundamentais, especialmente a dignidade, a imagem e o acesso a oportunidades profissionais.'),
 b_faq('Dúvidas frequentes', '', [
   ('Quem foi absolvido pode ter o nome retirado dos antecedentes?','Sim. A manutenção desse tipo de registro pode ser indevida em determinadas consultas.'),
   ('Inquérito arquivado pode continuar aparecendo?','Em regra, não deve gerar prejuízo ao cidadão, podendo ser objeto de correção.'),
   ('Antecedentes podem prejudicar concurso público?','Sim. Por isso, a regularização dos registros é relevante para evitar restrições indevidas.'),
   ('É necessário ingressar com ação judicial?','Nem sempre. Contudo, em caso de negativa administrativa, é cabível a via judicial para garantir o direito ao sigilo e à proteção da imagem.')]),
 b_statement('A análise depende do tipo de registro e da situação jurídica atual', 'A natureza do registro, a situação jurídica atual, a documentação disponível e o impacto prático na vida do interessado são elementos que determinam a viabilidade e o meio adequado para efetivação do pedido.', 'quiet'),
 lambda link: b_cta('Possui registros no seu nome e quer entender o que pode ser feito?', 'Uma análise técnica do caso pode identificar a viabilidade jurídica e o caminho mais adequado para a regularização.', 'Solicitar avaliação jurídica', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre retirada de antecedentes criminais.', parent=('penal','Defesa Criminal'))

# ---------------- Direito Público › Administrativo Sancionador ----------------
page_area('administrativo-sancionador',
 'Direito Administrativo Sancionador' + T,
 'Defesa técnica em Processo Administrativo Disciplinar e Sindicância diante de procedimentos que podem resultar em sanções funcionais.',
 'Administrativo Sancionador',
 'Foi notificado para responder a Processo Administrativo Disciplinar ou Sindicância?',
 'A forma como você se defende desde o início pode impactar diretamente sua carreira. Procedimentos que podem resultar em sanções funcionais exigem análise técnica desde a primeira notificação.',
 'Solicitar análise do caso', 'fotos/administrativo-sancionador.jpg', 'Mão folheando uma pilha de documentos presos com clipes, sobre uma mesa escura.', 'matheus', [
 b_statement('Receber uma notificação de instauração gera insegurança e incerteza quanto aos próximos passos', 'O servidor pode não saber exatamente do que está sendo acusado, subestimar a gravidade do procedimento, prestar esclarecimentos sem orientação técnica ou acreditar que a situação será resolvida administrativamente. Contudo, esses procedimentos podem resultar em advertência, suspensão, perda de função ou demissão.'),
 b_details('Sindicância e PAD: o que são', '', [
   {'t':'Sindicância Administrativa','p':'Procedimento investigatório que busca apurar fatos e responsabilidades, podendo ou não resultar em aplicação de penalidade.'},
   {'t':'Processo Administrativo Disciplinar (PAD)','p':'Procedimento formal voltado à apuração de infração funcional, com possibilidade de aplicação de sanções administrativas.'}]),
 b_statement('O momento inicial é decisivo', 'Desde a primeira notificação, o servidor já está inserido em um procedimento que exige atenção técnica. Manifestações iniciais podem influenciar toda a apuração, provas começam a ser produzidas e versões dos fatos são registradas oficialmente. Uma atuação sem orientação pode comprometer a defesa ao longo de todo o processo.'),
 b_band('Direitos do servidor no processo administrativo', 'O servidor possui garantias fundamentais que devem ser observadas em todo o procedimento.', ['Direito ao contraditório e à ampla defesa','Direito de acesso integral aos autos','Direito de produzir provas','Direito de ser assistido por advogado']),
 b_checks('Erros comuns que podem prejudicar a defesa', '', ['Apresentar defesa sem análise técnica dos autos','Prestar declarações sem estratégia definida','Não impugnar irregularidades do procedimento','Perder prazos ou oportunidades de manifestação'], warn=True),
 b_checks('O que a análise técnica do procedimento permite', '', ['Compreender a real extensão da acusação','Identificar nulidades ou irregularidades','Definir estratégia de defesa adequada','Acompanhar atos como oitivas e interrogatórios','Atuar na dosimetria de eventual penalidade']),
 b_statement('Possibilidade de revisão e controle judicial', 'Caso haja decisão administrativa desfavorável ou irregularidades no procedimento, é possível interpor recursos administrativos, requerer a revisão do ato e, quando cabível, buscar o controle judicial. A via judicial tem como finalidade assegurar o respeito às garantias legais e constitucionais do servidor.'),
 b_faq('Dúvidas frequentes', '', [
   ('Sindicância pode gerar punição?','Sim, dependendo da modalidade e da apuração realizada.'),
   ('Preciso de advogado no PAD?','Não é obrigatório, mas é recomendável diante da complexidade e dos riscos envolvidos.'),
   ('Posso me defender sozinho?','Pode, mas a ausência de orientação técnica pode comprometer a estratégia de defesa.'),
   ('Se houver irregularidade, o que pode ser feito?','É possível questionar administrativamente e, se necessário, judicialmente.')]),
 b_statement('A atuação preventiva é determinante para a proteção da carreira do servidor', 'Se você foi notificado para responder a sindicância ou processo administrativo disciplinar, é recomendável compreender, desde o início, os aspectos jurídicos envolvidos e as possíveis implicações para sua carreira.', 'quiet'),
 lambda link: b_cta('Converse com o escritório antes de tomar qualquer decisão no procedimento', 'Um primeiro contato permite esclarecer o cenário, identificar riscos e definir a resposta técnica cabível.', 'Solicitar análise do caso', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre PAD ou sindicância.', parent=('direito-publico','Direito Público'))

# ---------------- Direito Público › Investigação social ----------------
page_area('investigacao-social',
 'Investigação Social em Concurso Público' + T,
 'Antecedentes criminais podem comprometer sua aprovação? Inquéritos arquivados, absolvições e ocorrências antigas nem sempre podem ser usados contra o candidato.',
 'Investigação social',
 'Investigação social em concurso público: antecedentes criminais podem comprometer sua aprovação?',
 'Registros como inquéritos arquivados, absolvições ou ocorrências antigas nem sempre podem ser utilizados para prejudicar sua vida funcional. Em alguns casos, também é possível corrigi-los.',
 'Solicitar avaliação do caso', 'concurso', 'Ilustração de livros de estudo empilhados.', None, [
 b_statement('A investigação social é uma das etapas mais sensíveis dos concursos públicos', 'É nesse momento que muitos candidatos, mesmo aprovados nas demais fases, se deparam com problemas decorrentes de registros antigos, muitas vezes sem relevância jurídica atual. Inquéritos arquivados, processos com absolvição, registros sem condenação e ocorrências antigas já superadas podem gerar insegurança e risco de eliminação, ainda que não exista fundamento legal para tanto.'),
 b_statement('O que a lei e a jurisprudência dizem', 'A análise da vida pregressa deve respeitar princípios constitucionais como a presunção de inocência, a dignidade da pessoa humana e a razoabilidade. O entendimento do Superior Tribunal de Justiça e do Supremo Tribunal Federal é no sentido de que a mera existência de inquérito arquivado ou processo sem condenação não pode, por si só, justificar a eliminação do candidato, e que registros sem relevância jurídica atual não devem ser utilizados para restringir direitos.'),
 b_checks('O que pode ser questionado juridicamente', 'Nem toda informação constante nos sistemas pode ser utilizada de forma automática pela Administração.', ['Utilização de registros sem condenação','Ausência de fundamentação específica','Decisão baseada apenas em histórico sem análise concreta','Manutenção indevida de registros já superados']),
 b_checks('Registros que mais geram dificuldades em concursos', '', ['Inquérito policial arquivado','Processo com absolvição','Termo circunstanciado antigo','Transação penal já superada','Registros administrativos desatualizados','Apontamentos indevidos em sistemas policiais'], warn=True),
 b_statement('Regularização prévia pode evitar problemas antes mesmo da investigação social', 'Em muitos casos, é possível antecipar riscos mediante análise da folha de antecedentes, verificação de registros ativos, identificação de inconsistências e adoção de medidas para regularização. Essa etapa pode ser determinante para evitar prejuízos futuros no certame.'),
 b_band('Eliminação na investigação social: possibilidade de reversão', 'Caso o candidato seja eliminado, é possível:', ['Apresentar defesa administrativa','Interpor recurso','Buscar continuidade no certame via judicial','Requerer anulação de eliminações indevidas']),
 b_faq('Dúvidas frequentes', '', [
   ('Posso ser eliminado por ter um inquérito arquivado?','Em regra, não. A jurisprudência entende que a ausência de condenação impede a utilização isolada desse registro para eliminação.'),
   ('Absolvição pode prejudicar no concurso?','Não deve. A absolvição afasta a responsabilidade penal, sendo indevida sua utilização para restringir direitos.'),
   ('Vale a pena verificar isso antes da investigação social?','Sim. A análise prévia pode evitar riscos e permitir a correção de eventuais inconsistências.'),
   ('Preciso entrar na Justiça?','Nem sempre. Muitos casos são resolvidos administrativamente. Contudo, em caso de eliminação ou negativa indevida, é cabível a via judicial.')]),
 b_statement('A avaliação depende do registro, do edital e do concurso', 'O tipo de registro existente, a natureza do concurso, as exigências do edital e a jurisprudência aplicável definem a medida cabível. A análise pode influenciar diretamente a preservação do direito de permanência no certame.', 'quiet'),
 lambda link: b_cta('Vai participar de concurso ou já enfrenta questionamentos na investigação social?', 'A análise técnica do caso pode identificar riscos, verificar a viabilidade de questionamento e indicar as medidas mais adequadas.', 'Solicitar avaliação do caso', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre investigação social em concurso.', parent=('direito-publico','Direito Público'))

# ---------------- Direito Público › Remoção de servidor ----------------
page_area('remocao-servidor-publico',
 'Remoção de Servidor Público' + T,
 'Orientação jurídica para pedidos de remoção de servidor público e contestação de negativas, conforme as regras da carreira e os documentos do pedido.',
 'Remoção de servidor público',
 'Remoção de servidor público',
 'A distância da família ou a necessidade de tratamento de saúde podem motivar um pedido de mudança de lotação. Atuamos na preparação do requerimento e na contestação de negativas administrativas, conforme as regras da sua carreira e os documentos do caso.',
 'Conversar sobre minha remoção', 'remocao', 'Ilustração de um mapa com marcador de localização.', 'jackson', [
 b_statement('Seu pedido de remoção foi negado', 'A negativa administrativa deve ser examinada em conjunto com o pedido apresentado, os documentos e a legislação aplicável. A atuação jurídica busca identificar os fundamentos da decisão e verificar a possibilidade de reconsideração, recurso ou medida judicial.'),
 b_details('Situações que podem fundamentar um pedido', 'As hipóteses e os requisitos de remoção variam conforme o vínculo e o regime jurídico do servidor.', [
   {'t':'Tratamento de saúde','p':'Pedidos relacionados à saúde do servidor ou de familiares abrangidos pelo regime da carreira exigem atenção à prova médica e às condições de tratamento na lotação atual.'},
   {'t':'Vida familiar','p':'O deslocamento do cônjuge ou companheiro e outras situações familiares podem ter tratamento específico na legislação. O vínculo, a origem da mudança e as regras da instituição precisam ser examinados.'},
   {'t':'Concurso de remoção e permuta','p':'Editais, classificação, vagas e pedidos de permuta seguem critérios próprios. A orientação jurídica pode abranger a participação no procedimento e a revisão das decisões administrativas.'}]),
 b_statement('Policiais penais do Rio Grande do Sul', 'Os pedidos de remoção na Polícia Penal do RS (SUSEPE) seguem normas estaduais próprias. Conheça as particularidades dos pedidos de saúde, unidade familiar, permuta e concurso de remoções.', link=('remocao-policiais-penais-rs.html','Ver a página sobre remoção na Polícia Penal do RS')),
 b_statement('Atuação desde o requerimento até a resposta administrativa', 'A Quartieri & Maldonado atua na defesa de servidores e no controle de atos administrativos. Examinamos a situação funcional, organizamos os fundamentos e os documentos do pedido e acompanhamos sua tramitação. Se já houver uma negativa, verificamos a medida adequada para contestá-la, inclusive pela via judicial quando cabível.'),
 b_band('Documentos que ajudam a compreender o pedido', 'O requerimento, a resposta recebida e as informações sobre seu cargo e lotação permitem iniciar a leitura do caso.', [
   {'t':'Pedido e decisão','p':'Requerimento protocolado, documentos apresentados, resposta da Administração e data em que você tomou ciência da decisão.'},
   {'t':'Situação funcional','p':'Cargo, instituição, lotação atual e pretendida, tempo de exercício e informações sobre o estágio probatório, se houver.'},
   {'t':'Fundamento da mudança','p':'Conforme o motivo do pedido, podem ser relevantes laudos, exames, comprovantes familiares, dados sobre o cônjuge ou o edital do concurso de remoção.'}]),
 b_faq('Dúvidas sobre remoção de servidor público', '', [
   ('Toda solicitação de remoção precisa ser autorizada?','As regras variam conforme a carreira e o fundamento do pedido. Algumas hipóteses dependem da avaliação administrativa, enquanto outras têm requisitos legais específicos que precisam ser verificados.'),
   ('Posso contestar uma negativa?','É possível examinar os fundamentos da decisão e verificar quais medidas administrativas ou judiciais são cabíveis. O requerimento, os documentos apresentados e a data da resposta são relevantes para essa avaliação.'),
   ('O estágio probatório impede a remoção?','A resposta depende do regime aplicável. Algumas carreiras admitem exceções à restrição durante o estágio probatório em hipóteses previstas na legislação. É necessário verificar o fundamento do pedido e os requisitos da sua instituição.'),
   ('Preciso ter o pedido pronto para buscar orientação?','A atuação pode começar antes do protocolo, com a definição do fundamento e a organização dos documentos, ou após a resposta administrativa, para examinar a decisão e os próximos passos.')]),
 lambda link: b_cta('Converse sobre o seu pedido de remoção', 'Informe seu cargo, a lotação atual, o destino pretendido e o motivo da mudança. Se o pedido já foi negado, tenha a decisão disponível para a primeira conversa.', 'Conversar sobre minha remoção', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre remoção de servidor público.', parent=('direito-publico','Direito Público'))

# ---------------- Trabalhista › Rescisão indireta ----------------
page_area('rescisao-indireta',
 'Rescisão Indireta' + T,
 'Atraso de salários ou falta de FGTS podem dar direito à rescisão indireta para trabalhadores do Rio Grande do Sul.',
 'Rescisão indireta',
 'Quando o empregador comete faltas graves, o trabalhador pode ter direito à rescisão indireta',
 'Se você está recebendo salário em atraso ou a empresa não está depositando o FGTS, pode ter direito a encerrar o vínculo de emprego e receber todas as verbas rescisórias. É a chamada justa causa do empregador.',
 'Falar com o escritório', 'contrato', 'Ilustração de um contrato de trabalho com caneta.', 'jackson', [
 b_statement('O que é rescisão indireta?', 'A rescisão indireta ocorre quando a empresa torna inviável a continuidade do vínculo de emprego por descumprir deveres essenciais da relação de trabalho, como realizar o pagamento de salário em atraso e não depositar o FGTS. Nesses casos, o trabalhador pode buscar judicialmente o encerramento do contrato com recebimento das verbas rescisórias normalmente devidas em uma dispensa sem justa causa.'),
 b_checks('Situações que podem justificar rescisão indireta', 'Exemplos frequentes analisados pelo escritório.', ['Atraso reiterado de salários','Falta de depósito de FGTS','Assédio moral e humilhações','Ambiente de trabalho inadequado ou degradante','Risco à saúde ou segurança do trabalhador'], warn=True),
 b_statement('A viabilidade depende dos documentos e da prova disponível', 'Nem todo problema autoriza pedido imediato de rescisão indireta. A medida correta depende de documentos, provas disponíveis e forma de condução do caso. Por isso, a avaliação jurídica prévia costuma ser necessária.'),
 b_band('O que pode servir como prova', '', ['Contracheques assinados após o quinto dia útil','Comprovantes de pagamento de salário em atraso','Extratos do FGTS comprovando a ausência de depósitos','Conversas por WhatsApp ou e-mail','Testemunhas']),
 b_faq('Dúvidas frequentes', '', [
   ('Nunca conferi meu FGTS. Vale verificar?','Sim. A ausência de depósitos é uma das causas frequentemente discutidas.'),
   ('Posso continuar trabalhando enquanto analiso o caso?','Em muitos casos, sim. A estratégia depende da gravidade da situação e da prova existente.'),
   ('Como funciona o primeiro contato?','Você relata a situação, apresenta os documentos disponíveis e recebe orientação objetiva sobre viabilidade e próximos passos.')]),
 b_statement('Antes de pedir demissão, avalie a possibilidade de rescisão indireta', 'Em alguns casos, o pedido de demissão pode significar perda de verbas que poderiam ser discutidas judicialmente. Uma análise correta pode mudar completamente o resultado.', 'quiet'),
 lambda link: b_cta('Converse com o escritório para avaliar sua situação', 'O primeiro contato serve para compreender o caso, analisar os documentos disponíveis e indicar os próximos passos com objetividade.', 'Entrar em contato agora', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre rescisão indireta.', parent=('trabalhista','Direito Trabalhista'))

# ---------------- Trabalhista › Empresas ----------------
page_area('empresas',
 'Assessoria Trabalhista para Empregador' + T,
 'Atuação técnica nas relações de trabalho, no contencioso, no consultivo e em compliance trabalhista.',
 'Para empresas',
 'Atuação técnica nas relações de trabalho e na defesa do negócio',
 'Empresas lidam diariamente com contratações, jornada, desligamentos, gestão de equipe e cumprimento de obrigações legais. Decisões mal conduzidas podem gerar passivos relevantes e demandas judiciais evitáveis.',
 'Falar com o escritório', 'fotos/empresas.jpg', 'Equipe unindo as mãos sobre uma mesa de trabalho com notebooks e documentos.', 'jackson', [
 b_statement('Prevenir riscos costuma ser mais eficiente do que remediar passivos', 'Por isso é importante ter uma assessoria jurídica de confiança para auxiliar na condução das relações de trabalho, com foco em organização interna, redução de contingências e respostas juridicamente seguras para situações sensíveis do dia a dia empresarial. O escritório também atua na defesa judicial e administrativa em reclamações trabalhistas, autos de infração e conflitos envolvendo empregados e ex-empregados.'),
 b_band('Os principais pedidos de uma ação trabalhista', 'Demandas que exigem defesa técnica e estratégica.', ['Cobrança de horas extras e adicionais','Alegações de vínculo de emprego','Rescisão indireta proposta por empregado','Acidente de trabalho e indenizações','Assédio moral e danos extrapatrimoniais']),
 b_checks('A atuação vai muito além da defesa judicial', 'Outras medidas podem salvar sua empresa de ter um passivo trabalhista.', ['Consultoria trabalhista empresarial','Suporte preventivo para decisões do dia a dia','Admissões e modelos de contratação','Aplicação de advertências e suspensões','Desligamentos e rescisões sensíveis','Gestão de jornada e banco de horas','Cargos de confiança e enquadramentos','Políticas internas e regulamentos','Remuneração variável, comissões e premiações','Orientação em casos disciplinares','Compliance trabalhista','Estruturação interna para reduzir passivos e melhorar governança','Revisão de contratos de trabalho']),
 b_statement('Contencioso e consultiva caminham juntos', 'Uma empresa pode precisar de defesa pontual sem abrir mão da organização contratual, da jornada e dos desligamentos — sempre com segurança jurídica no dia a dia.'),
 b_faq('Dúvidas frequentes', '', [
   ('Vale buscar assessoria mesmo sem processo em andamento?','Sim. A atuação preventiva costuma reduzir custos, riscos e litígios futuros.'),
   ('Pequenas empresas também precisam de suporte trabalhista?','Sim. Empresas de qualquer porte estão sujeitas a passivos relevantes quando não há orientação adequada.'),
   ('É possível revisar rotinas internas já existentes?','Sim. O escritório pode analisar procedimentos atuais e apontar ajustes necessários.'),
   ('O escritório atua apenas em ações judiciais?','Não. Além do contencioso, há suporte consultivo recorrente e projetos de compliance trabalhista.'),
   ('Como funciona o primeiro contato?','É realizada compreensão inicial da empresa, do problema apresentado ou da rotina existente, com indicação objetiva dos próximos passos.')]),
 b_statement('Decisões trabalhistas seguras impactam diretamente o resultado da empresa', 'Uma orientação jurídica adequada pode evitar passivos, fortalecer processos internos e proteger a operação.', 'quiet'),
 lambda link: b_cta('Converse com o escritório para avaliar a situação da sua empresa', 'O primeiro contato serve para compreender o cenário, identificar riscos e indicar os próximos passos com objetividade.', 'Entrar em contato', link),
 ], 'Olá! Vim pelo site e gostaria de falar sobre assessoria trabalhista para a minha empresa.', parent=('trabalhista','Direito Trabalhista'))

# ---------------- Assistência funcional › Brigadianos / Bombeiros / Policiais penais ----------------
ENFRENTAR = [
 {'t':'Investigações Preliminares','p':'Apurações iniciais que podem evoluir para procedimentos de maior gravidade.'},
 {'t':'Sindicâncias','p':'Procedimentos que investigam fatos e condutas no âmbito institucional.'},
 {'t':'Processos Administrativos Disciplinares','p':'PADs com potencial de impacto direto na carreira e no vínculo funcional.'},
 {'t':'Corregedoria','p':'Instância de controle interno que exige postura técnica desde o primeiro ato.'},
 {'t':'Procedimentos na PGE','p':'Demandas conduzidas pela Procuradoria-Geral do Estado com repercussão funcional.'},
 {'t':'Questionamentos funcionais','p':'Situações que colocam em xeque decisões tomadas no exercício da função.'},
 {'t':'Responsabilizações injustas','p':'Imputações sem suporte nos fatos que exigem defesa estruturada e imediata.'}]
CONQUISTA = [
 {'t':'Preservação da sua história profissional','p':'Sua trajetória protegida de registros injustos e consequências duradouras.'},
 {'t':'Respeito à sua dignidade funcional','p':'Defesa que reconhece o peso da função e o valor do vínculo institucional.'},
 {'t':'Respaldo jurídico técnico','p':'Representação técnica em todas as fases do procedimento.'},
 {'t':'Proteção diante de injustiças','p':'Defesa estruturada quando a responsabilização não tem amparo nos fatos.'},
 {'t':'Orientação para momentos críticos','p':'Atendimento jurídico quando o procedimento exige resposta rápida.'}]
MILITAR_COBERTURA = [
 {'t':'Sindicâncias','p':'Acompanhamento técnico desde a instauração até o encerramento do procedimento.'},
 {'t':'Processos Administrativos Disciplinares','p':'Defesa estruturada em PADs, com análise criteriosa de cada fase.'},
 {'t':'Conselhos de Disciplina','p':'Atuação técnica nos conselhos que apuram infrações de natureza grave.'},
 {'t':'IPM: Inquérito Policial Militar','p':'Assessoria e defesa nos inquéritos conduzidos no âmbito militar.'},
 {'t':'Justiça Militar Estadual','p':'Representação e defesa perante a Justiça Militar do Estado do Rio Grande do Sul.'}]
PENAL_COBERTURA = [
 {'t':'Sindicâncias investigativas','p':'Acompanhamento técnico desde a instauração até o encerramento do procedimento.'},
 {'t':'PAD na SUSEPE','p':'Defesa estruturada em processos administrativos disciplinares no âmbito da SUSEPE-RS.'},
 {'t':'Procedimentos na Corregedoria','p':'Atuação técnica nos procedimentos conduzidos pela Corregedoria.'},
 {'t':'PAD na PGE','p':'Defesa em processos administrativos disciplinares conduzidos pela Procuradoria-Geral do Estado.'},
 {'t':'Requerimentos funcionais administrativos','p':'Atuação em demandas administrativas relacionadas ao vínculo e ao exercício da função.'}]

def funcional_page(slug, meta_title, meta_desc, crumb, h1, quem, quem_beneficio, tecnica, cobertura_titulo, cobertura, art, art_alt, wa_msg):
    page_area(slug, meta_title + T, meta_desc, crumb, h1,
     'Proteção jurídica contínua para quem atua na linha de frente da segurança pública.',
     'Falar com o escritório', art, art_alt, None, [
     b_statement('Por que a assistência jurídica existe', f'A carreira na segurança pública é marcada por alto grau de risco, elevada responsabilidade e forte escrutínio institucional. {quem} pode ser alvo de apurações e sindicâncias mesmo quando age corretamente. Quando isso acontece, não existe tempo para procurar advogado, negociar valores e improvisar defesa. Tempo, técnica e documentação passam a ser decisivos.'),
     b_details('O que você pode enfrentar', 'Procedimentos que exigem defesa técnica imediata.', ENFRENTAR),
     b_band('O que é a Assistência Jurídica', 'Proteção jurídica contínua, construída sobre três pilares.', [
       {'t':'Proteção','p':'Atendimento jurídico quando houver investigação, sindicância ou PAD.'},
       {'t':'Técnica','p':tecnica},
       {'t':'Prontidão','p':'Atuação imediata quando necessário. No mundo real, cada minuto conta.'}]),
     b_statement('Como um seguro de vida para a sua carreira', 'Você não contrata porque espera usar. Contrata porque um procedimento funcional pode surgir sem aviso. Assim como o seguro de vida atua nos momentos críticos, a assistência jurídica permite defesa técnica imediata e evita contratação emergencial com custos elevados.'),
     b_details('Benefícios ao associado', '', [
       {'t':'Acompanhamento jurídico permanente','p':'Amparo profissional sempre que a função exigir.'},
       {'t':'Defesa técnica','p':f'Advocacia técnica voltada à realidade funcional {quem_beneficio}.'},
       {'t':'Previsibilidade','p':'Sem sustos, sem desespero, sem improviso.'},
       {'t':'Resposta em momentos críticos','p':'Você sabe a quem recorrer quando houver procedimento funcional.'}]),
     b_statement('Não espere o PAD chegar', 'Um primeiro contato pode esclarecer sua situação e indicar o próximo passo com mais segurança.', 'quiet'),
     b_details(cobertura_titulo, '', cobertura),
     b_details('O que você realmente conquista', '', CONQUISTA),
     b_statement('Instrumento jurídico sério e responsável', 'Esta assistência não é promessa de resultado, não é instrumento de impunidade, não é mercantilização da advocacia e não é propaganda agressiva. É atuação funcional guiada por técnica, ética, lealdade e respeito às instituições, voltada à preservação da história profissional e da dignidade funcional.', 'quiet'),
     lambda link: b_cta('Converse com o escritório antes que a situação avance', 'Um primeiro contato pode esclarecer sua situação e indicar o próximo passo com mais segurança.', 'Entrar em contato', link),
     ], wa_msg, parent=('mensalista-funcional','Assistência funcional'))

funcional_page('brigadianos', 'Assistência Jurídica para Brigadianos',
 'Assistência jurídica contínua para brigadianos do Rio Grande do Sul, com foco em defesa técnica.',
 'Brigada Militar', 'Assistência Jurídica para Brigadianos do Rio Grande do Sul',
 'O brigadiano', 'do Brigadiano', 'Defesa elaborada por escritório com experiência real no ambiente militar.',
 'O que está incluído para Brigadianos', MILITAR_COBERTURA, 'fotos/brigadianos.jpg', 'Policiais militares de costas, com a inscrição Polícia Militar no colete.',
 'Olá! Vim pelo site e gostaria de saber mais sobre a assistência jurídica para brigadianos.')
funcional_page('bombeiros-militares', 'Assistência Jurídica para Bombeiros Militares',
 'Assistência jurídica contínua para bombeiros militares do Rio Grande do Sul, com foco em defesa técnica.',
 'Bombeiros Militares', 'Assistência Jurídica para Bombeiros Militares do Rio Grande do Sul',
 'O militar', 'do bombeiro militar', 'Defesa elaborada por escritório com experiência real no ambiente militar.',
 'O que está incluído para Bombeiros Militares', MILITAR_COBERTURA, 'fotos/bombeiros-militares.jpg', 'Bombeiro militar de capacete e equipamento de respiração, com outros bombeiros ao fundo.',
 'Olá! Vim pelo site e gostaria de saber mais sobre a assistência jurídica para bombeiros militares.')
funcional_page('policiais-penais', 'Assistência Jurídica para Policiais Penais',
 'Assistência jurídica contínua para policiais penais do Rio Grande do Sul, com foco em defesa técnica.',
 'SUSEPE', 'Assistência Jurídica para Policiais Penais do Rio Grande do Sul',
 'O policial penal', 'do policial penal', 'Defesa elaborada por escritório com experiência real no ambiente institucional da segurança pública.',
 'O que está incluído para Policiais Penais', PENAL_COBERTURA, 'fotos/policiais-penais.jpg', 'Policiais penais uniformizados em formação, com a inscrição Polícia Penal no colete.',
 'Olá! Vim pelo site e gostaria de saber mais sobre a assistência jurídica para policiais penais.')
