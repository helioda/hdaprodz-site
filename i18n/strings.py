# Translations for the generated pages. Keys are the exact French texts in
# index.html / projet.html. Edit a French text there, then update its key here.

PAGES = {
    "index.html": {
        "out": {"en": "index.html", "pt": "index.html", "es": "index.html"},
        "must_not_remain": ["Votre expertise", "Parlons de", "Aller au contenu", "Éditeur", "Retour en haut",
                            "Découvrir", "copropriété.", "Notre assistant", "Comment démarrer", "Références", "16 ans chez", "parcours Copilot", "soumis à"],
    },
    "projet.html": {
        "out": {"en": "project.html", "pt": "projeto.html", "es": "proyecto.html"},
        "must_not_remain": ["Demande de projet", "Nom et prénom", "Envoyer ma demande", "Choisir…",
                            "Notice de confidentialité", "Vos droits", "obligatoire", "Retour à l’accueil"],
    },
}

def T(en, pt, es):
    return {"en": en, "pt": pt, "es": es}

TEXT = {
"index.html": {
 "HDA Solutions — Agents IA et automatisation": T(
  "HDA Solutions — AI agents and automation",
  "HDA Solutions — Agentes de IA e automação",
  "HDA Solutions — Agentes de IA y automatización"),
 "HDA Solutions développe des assistants IA, copilotes et automatisations sur les technologies Microsoft, pour les professionnels et les organisations.": T(
  "HDA Solutions builds AI assistants, copilots and automations on Microsoft technologies for professionals and organisations.",
  "A HDA Solutions desenvolve assistentes de IA, copilotos e automações com tecnologias Microsoft para profissionais e organizações.",
  "HDA Solutions desarrolla asistentes de IA, copilotos y automatizaciones con tecnologías Microsoft para profesionales y organizaciones."),
 "Aller au contenu": T("Skip to content", "Ir para o conteúdo", "Ir al contenido"),
 "Navigation principale": T("Main navigation", "Navegação principal", "Navegación principal"),
 "Solutions": T("Solutions", "Soluções", "Soluciones"),
 "Applications": T("Use cases", "Aplicações", "Aplicaciones"),
 "Parlons de votre projet ↗": T("Let’s talk about your project ↗", "Vamos falar do seu projeto ↗", "Hablemos de su proyecto ↗"),
 "Votre expertise.": T("Your expertise.", "Sua expertise.", "Su experiencia."),
 "Amplifiée par": T("Amplified by", "Amplificada por", "Amplificada por"),
 "des agents IA.": T("AI agents.", "agentes de IA.", "agentes de IA."),
 "Des agents IA, des copilotes et des automatisations pour retrouver l’information, simplifier vos processus et avancer dans votre travail.": T(
  "AI agents, copilots and automations to find information, simplify your processes and move your work forward.",
  "Agentes de IA, copilotos e automações para encontrar informações, simplificar seus processos e avançar no seu trabalho.",
  "Agentes de IA, copilotos y automatizaciones para encontrar la información, simplificar sus procesos y avanzar en su trabajo."),
 "Discuter de mon besoin ↗": T("Discuss my needs ↗", "Falar sobre minha necessidade ↗", "Hablar de mi necesidad ↗"),
 "Découvrir les solutions": T("Explore the solutions", "Conhecer as soluções", "Descubrir las soluciones"),
 "Aperçu de CoproSens : le tableau de bord du conseil syndical et une réponse de l’assistant avec sa source.": T(
  "CoproSens preview: the board dashboard and an assistant answer with its source.",
  "Prévia do CoproSens: o painel do conselho e uma resposta do assistente com sua fonte.",
  "Vista previa de CoproSens: el panel del consejo y una respuesta del asistente con su fuente."),
 "Assistant CoproSens": T("CoproSens assistant", "Assistente CoproSens", "Asistente CoproSens"),
 "Quels lots sont en retard de paiement ?": T("Which units are behind on payments?", "Quais unidades estão com pagamento atrasado?", "¿Qué lotes van atrasados en sus pagos?"),
 "3 lots en retard, <b>16 729,60 €</b> au total, hors pénalités.": T(
  "3 units behind, <b>$16,729.60</b> in total, excluding penalties.",
  "3 unidades atrasadas, <b>16 729,60 €</b> no total, sem multas.",
  "3 lotes atrasados, <b>16 729,60 €</b> en total, sin penalizaciones."),
 "Source : tableau de bord du conseil syndical, 8 octobre 2026": T(
  "Source: board dashboard, 8 October 2026", "Fonte: painel do conselho, 8 de outubro de 2026", "Fuente: panel del consejo, 8 de octubre de 2026"),
 "Réponse sourcée": T("Sourced answer", "Resposta com fonte", "Respuesta con fuente"),
 "Pour chaque acteur de la copropriété": T("For everyone in the building", "Para cada ator do condomínio", "Para cada actor de la comunidad"),
 "Syndics": T("Property managers", "Administradoras", "Administradores de fincas"),
 "Retrouver une décision d’AG ou un devis en quelques secondes, préparer les appels de fonds et les documents d’AG.": T(
  "Find a general-meeting decision or a quote in seconds; prepare service-charge calls and meeting documents.",
  "Encontrar uma decisão de assembleia ou um orçamento em segundos; preparar chamadas de cotas e documentos de assembleia.",
  "Encontrar un acuerdo de junta o un presupuesto en segundos; preparar cuotas y documentos de junta."),
 "Conseils syndicaux": T("Owners’ boards", "Conselhos do condomínio", "Juntas de propietarios"),
 "Suivre les impayés, les travaux et l’exécution des décisions d’AG.": T(
  "Track unpaid charges, works and how meeting decisions are carried out.",
  "Acompanhar inadimplências, obras e a execução das decisões de assembleia.",
  "Seguir impagos, obras y la ejecución de los acuerdos de junta."),
 "Copropriétaires": T("Owners", "Condôminos", "Propietarios"),
 "Des réponses claires sur leurs appels de fonds et les travaux votés, à toute heure.": T(
  "Clear answers about their charges and approved works, at any time.",
  "Respostas claras sobre suas cotas e as obras aprovadas, a qualquer hora.",
  "Respuestas claras sobre sus derramas y las obras aprobadas, a cualquier hora."),
 "Assistants & agents IA": T("AI assistants & agents", "Assistentes e agentes de IA", "Asistentes y agentes de IA"),
 "Solutions sur mesure, où que vous soyez": T("Tailor-made solutions, wherever you are", "Soluções sob medida, onde quer que esteja", "Soluciones a medida, dondequiera que esté"),
 "Ce que nous développons": T("What we build", "O que desenvolvemos", "Lo que desarrollamos"),
 "L’IA au service": T("AI at the service", "A IA a serviço", "La IA al servicio"),
 "du travail réel.": T("of real work.", "do trabalho real.", "del trabajo real."),
 "Nous partons d’un besoin concret et de vos outils existants pour construire une solution adaptée à votre organisation.": T(
  "We start from a concrete need and your existing tools to build a solution suited to your organisation.",
  "Partimos de uma necessidade concreta e das suas ferramentas atuais para construir uma solução adaptada à sua organização.",
  "Partimos de una necesidad concreta y de sus herramientas actuales para construir una solución adaptada a su organización."),
 "01 / ASSISTER": T("01 / ASSIST", "01 / ASSISTIR", "01 / ASISTIR"),
 "Assistants et copilotes": T("Assistants and copilots", "Assistentes e copilotos", "Asistentes y copilotos"),
 "Des interfaces conversationnelles pour guider les utilisateurs, préparer des contenus et accompagner les tâches quotidiennes.": T(
  "Conversational interfaces to guide users, prepare content and support everyday tasks.",
  "Interfaces conversacionais para orientar os usuários, preparar conteúdos e apoiar as tarefas do dia a dia.",
  "Interfaces conversacionales para guiar a los usuarios, preparar contenidos y acompañar las tareas diarias."),
 "Agents IA": T("AI agents", "Agentes de IA", "Agentes de IA"),
 "02 / CONNECTER": T("02 / CONNECT", "02 / CONECTAR", "02 / CONECTAR"),
 "Connaissance accessible": T("Accessible knowledge", "Conhecimento acessível", "Conocimiento accesible"),
 "Relier les documents utiles à un assistant, structurer l’information et faciliter la recherche dans le respect des accès définis.": T(
  "Connect the right documents to an assistant, structure information and make searching easier while respecting defined access rights.",
  "Conectar os documentos úteis a um assistente, estruturar a informação e facilitar a busca, respeitando os acessos definidos.",
  "Conectar los documentos útiles a un asistente, estructurar la información y facilitar la búsqueda respetando los accesos definidos."),
 "03 / AUTOMATISER": T("03 / AUTOMATE", "03 / AUTOMATIZAR", "03 / AUTOMATIZAR"),
 "Processus simplifiés": T("Simpler processes", "Processos simplificados", "Procesos simplificados"),
 "Préparer des réponses, organiser des demandes et connecter les étapes répétitives, avec les contrôles adaptés à chaque usage.": T(
  "Prepare answers, organise requests and connect repetitive steps, with the right controls for each use.",
  "Preparar respostas, organizar solicitações e conectar etapas repetitivas, com os controles adequados a cada uso.",
  "Preparar respuestas, organizar solicitudes y conectar los pasos repetitivos, con los controles adecuados a cada uso."),
 "Applications métier": T("Business apps", "Aplicativos de negócio", "Aplicaciones de negocio"),
 "💶 Tarifs": T("💶 Pricing", "💶 Preços", "💶 Precios"),
 "Essayer la démo ↗": T("Try the demo ↗", "Experimentar a demo ↗", "Probar la demo ↗"),
 "Démarrer un pilote": T("Start a pilot", "Iniciar um piloto", "Iniciar un piloto"),
 "Sur vos propres documents, dans votre Microsoft 365": T("On your own documents, in your Microsoft 365", "Com os seus próprios documentos, no seu Microsoft 365", "Con sus propios documentos, en su Microsoft 365"),
 "Posez vos questions à l’assistant": T("Ask the assistant your questions", "Faça suas perguntas ao assistente", "Haga sus preguntas al asistente"),
 "Estimer le coût": T("Estimate the cost", "Estimar o custo", "Estimar el coste"),
 "Prix par lot et par mois, en direct": T("Price per unit per month, live (in euros)", "Preço por unidade e por mês, em euros", "Precio por unidad y por mes, en euros"),
 "Tableau de bord ↗": T("Dashboard ↗", "Painel ↗", "Panel ↗"),
 "Le suivi du conseil syndical": T("The owners’ council overview", "O acompanhamento do conselho", "El seguimiento del consejo"),
 "Outils du syndic ↗": T("Manager tools ↗", "Ferramentas da administradora ↗", "Herramientas del administrador ↗"),
 "Appels de fonds et documents d’AG": T("Service charges and meeting documents", "Cotas e documentos de assembleia", "Cuotas y documentos de junta"),
 "Nous contacter": T("Contact us", "Fale conosco", "Contáctenos"),
 "Réponse personnalisée, sans engagement": T("Personal reply, no commitment", "Resposta personalizada, sem compromisso", "Respuesta personalizada, sin compromiso"),
 "Copropriété fictive, données de démonstration · réponses générées par IA": T(
  "Fictional condominium, demo data · AI-generated answers",
  "Condomínio fictício, dados de demonstração · respostas geradas por IA",
  "Comunidad ficticia, datos de demostración · respuestas generadas por IA"),
 "Cas concret": T("Case study", "Caso concreto", "Caso concreto"),
 "Un assistant conçu": T("An assistant built", "Um assistente criado", "Un asistente diseñado"),
 "pour un vrai métier.": T("for a real profession.", "para uma profissão real.", "para un oficio real."),
 "Notre premier assistant, développé pour la gestion de copropriété. La même démarche s’adapte à d’autres métiers.": T(
  "Our first assistant, developed for condominium management. The same approach adapts to other professions.",
  "Nosso primeiro assistente, desenvolvido para a gestão de condomínios. A mesma abordagem se adapta a outras profissões.",
  "Nuestro primer asistente, desarrollado para la gestión de comunidades de propietarios. El mismo enfoque se adapta a otros oficios."),
 "Volet musical : HDA Productions ↗": T("Music side: HDA Productions ↗", "Lado musical: HDA Productions ↗", "Faceta musical: HDA Productions ↗"),
 "Immobilier & copropriété": T("Real estate & co-ownership", "Imóveis e condomínios", "Inmobiliaria y comunidades de propietarios"),
 "Notre assistant IA pour la gestion de copropriété : documents, appels de fonds et assemblées générales.": T(
  "Our AI assistant for co-ownership management: documents, service-charge calls and general meetings.",
  "Nosso assistente de IA para a gestão de condomínios: documentos, chamadas de cotas e assembleias gerais.",
  "Nuestro asistente de IA para la gestión de comunidades: documentos, derramas y cuotas, y juntas generales."),
 "Retrouver une information dans les documents de la copropriété, avec sa source.": T(
  "Find information in the building’s documents, with its source.",
  "Encontrar uma informação nos documentos do condomínio, com a fonte.",
  "Encontrar información en los documentos de la comunidad, con su fuente."),
 "Calculer les appels de fonds de chaque lot : tantièmes, charges spéciales et consommations individuelles d’eau et de chauffage.": T(
  "Calculate each unit’s service-charge call: ownership shares, special charges and individual water and heating consumption.",
  "Calcular a chamada de cotas de cada unidade: frações ideais, encargos especiais e consumos individuais de água e aquecimento.",
  "Calcular la cuota de cada vivienda: coeficientes, gastos especiales y consumos individuales de agua y calefacción."),
 "Préparer l’ordre du jour, la convocation, le formulaire de vote par correspondance et le procès-verbal d’AG, validés par le syndic avant envoi.": T(
  "Draft the agenda, the notice of meeting, the postal-vote form and the general-meeting minutes, approved by the property manager before sending.",
  "Preparar a ordem do dia, a convocação, o formulário de voto por correspondência e a ata da assembleia, validados pela administradora antes do envio.",
  "Preparar el orden del día, la convocatoria, el formulario de voto por correo y el acta de la junta, validados por el administrador antes del envío."),
 "Présentation de CoproSens": T(
  "CoproSens presentation",
  "Apresentação do CoproSens",
  "Presentación de CoproSens"),
 "– l’assistant documentaire de votre copropriété": T(
  "– the document assistant for your condominium",
  "– o assistente de documentos do seu condomínio",
  "– el asistente documental de su comunidad de propietarios"),
 "Votre navigateur ne permet pas de lire cette vidéo.": T(
  "Your browser can’t play this video.", "Seu navegador não consegue reproduzir este vídeo.", "Su navegador no puede reproducir este vídeo."),
 "Télécharger la présentation": T("Download the presentation", "Baixar a apresentação", "Descargar la presentación"),
 "CoproSens en 1 min 18 s": T(
  "CoproSens in 1 min 22 s",
  "CoproSens em 1 min 32 s",
  "CoproSens en 1 min 31 s"),
 "Références": T("Credentials", "Referências", "Referencias"),
 "Membre du Microsoft AI Cloud Partner Program": T(
  "Member of the Microsoft AI Cloud Partner Program", "Membro do Microsoft AI Cloud Partner Program", "Miembro del Microsoft AI Cloud Partner Program"),
 "Founderz : Agent Commander (105 h) · Agent Maker · Agent Explorer": T(
  "Founderz: Agent Commander (105 h) · Agent Maker · Agent Explorer",
  "Founderz: Agent Commander (105 h) · Agent Maker · Agent Explorer",
  "Founderz: Agent Commander (105 h) · Agent Maker · Agent Explorer"),
 "16 ans chez Microsoft (cloud) · MCT Alumni": T(
  "16 years at Microsoft (cloud) · MCT Alumni", "16 anos na Microsoft (nuvem) · MCT Alumni", "16 años en Microsoft (nube) · MCT Alumni"),
 "Microsoft Learn : parcours Copilot Studio (2025) · Microsoft Specialist : Azure Infrastructure Solutions.": T(
  "Microsoft Learn: Copilot Studio learning paths (2025) · Microsoft Specialist: Azure Infrastructure Solutions.",
  "Microsoft Learn: trilhas Copilot Studio (2025) · Microsoft Specialist: Azure Infrastructure Solutions.",
  "Microsoft Learn: rutas de Copilot Studio (2025) · Microsoft Specialist: Azure Infrastructure Solutions."),
 "Fiche partenaire Microsoft Marketplace ↗": T("Microsoft Marketplace partner listing ↗", "Perfil de parceiro no Microsoft Marketplace ↗", "Ficha de partner en Microsoft Marketplace ↗"),
 "Badges vérifiables (Credly) ↗": T("Verifiable badges (Credly) ↗", "Badges verificáveis (Credly) ↗", "Insignias verificables (Credly) ↗"),
 "Profil LinkedIn ↗": T("LinkedIn profile ↗", "Perfil no LinkedIn ↗", "Perfil de LinkedIn ↗"),
 "Comment démarrer": T("How to start", "Como começar", "Cómo empezar"),
 "Commencer petit. Construire utile.": T("Start small. Build what’s useful.", "Começar pequeno. Construir o que é útil.", "Empezar poco a poco. Construir algo útil."),
 "Choisir un besoin": T("Choose a need", "Escolher uma necessidade", "Elegir una necesidad"),
 "Identifier une tâche, les utilisateurs concernés et le résultat attendu.": T(
  "Identify a task, the users involved and the expected result.",
  "Identificar uma tarefa, os usuários envolvidos e o resultado esperado.",
  "Identificar una tarea, los usuarios implicados y el resultado esperado."),
 "Tester une solution": T("Test a solution", "Testar uma solução", "Probar una solución"),
 "Définir le périmètre, connecter les sources nécessaires et évaluer un premier fonctionnement, avec un point d’avancement chaque semaine.": T(
  "Define the scope, connect the necessary sources and evaluate a first version, with a progress update every week.",
  "Definir o escopo, conectar as fontes necessárias e avaliar um primeiro funcionamento, com um status de andamento toda semana.",
  "Definir el alcance, conectar las fuentes necesarias y evaluar un primer funcionamiento, con un seguimiento cada semana."),
 "Ajuster et déployer": T("Adjust and deploy", "Ajustar e implantar", "Ajustar y desplegar"),
 "Vérifier les réponses, les permissions et les validations avant de généraliser l’usage.": T(
  "Check answers, permissions and approvals before rolling it out more widely.",
  "Verificar as respostas, as permissões e as validações antes de ampliar o uso.",
  "Verificar las respuestas, los permisos y las validaciones antes de generalizar su uso."),
 "Parlons de votre projet": T("Let’s talk about your project", "Vamos falar do seu projeto", "Hablemos de su proyecto"),
 "Quel travail aimeriez-vous simplifier ?": T("What work would you like to simplify?", "Que trabalho você gostaria de simplificar?", "¿Qué trabajo le gustaría simplificar?"),
 "Décrivez votre besoin, vos outils actuels et les tâches qui vous prennent du temps. Nous pourrons définir ensemble une première étape.": T(
  "Describe your need, your current tools and the tasks that take up your time. Together we can define a first step.",
  "Descreva sua necessidade, suas ferramentas atuais e as tarefas que tomam seu tempo. Juntos, podemos definir um primeiro passo.",
  "Describa su necesidad, sus herramientas actuales y las tareas que le quitan tiempo. Juntos podremos definir un primer paso."),
 "Décrire mon projet ↗": T("Describe my project ↗", "Descrever meu projeto ↗", "Describir mi proyecto ↗"),
 "ou écrire à contact@hdaprodz.com": T("or write to contact@hdaprodz.com", "ou escrever para contact@hdaprodz.com", "o escribir a contact@hdaprodz.com"),
 "Retour en haut ↑": T("Back to top ↑", "Voltar ao topo ↑", "Volver arriba ↑"),
 "Éditeur et confidentialité": T("Publisher and privacy", "Editor e privacidade", "Editor y privacidad"),
 "Éditeur :": T("Publisher:", "Editor:", "Editor:"),
 "Hélio Abreu de Andrade, entrepreneur individuel, nom commercial HDA PRODZ. 10 rue Jean Rostand, 91300 Massy, France. SIREN 910 349 968. Contact :": T(
  "Hélio Abreu de Andrade, sole proprietor (entrepreneur individuel), trading as HDA PRODZ. 10 rue Jean Rostand, 91300 Massy, France. SIREN 910 349 968. Contact:",
  "Hélio Abreu de Andrade, empresário individual (entrepreneur individuel), nome comercial HDA PRODZ. 10 rue Jean Rostand, 91300 Massy, França. SIREN 910 349 968. Contato:",
  "Hélio Abreu de Andrade, empresario individual (entrepreneur individuel), nombre comercial HDA PRODZ. 10 rue Jean Rostand, 91300 Massy, Francia. SIREN 910 349 968. Contacto:"),
 ". Responsable de publication : Hélio Abreu de Andrade.": T(
  ". Publication director: Hélio Abreu de Andrade.", ". Responsável pela publicação: Hélio Abreu de Andrade.", ". Director de la publicación: Hélio Abreu de Andrade."),
 "Ce site ne contient aucun traceur publicitaire ni outil d’analyse d’audience. Les informations transmises par courriel ou via le": T(
  "This site contains no advertising trackers or audience analytics. Information sent by e-mail or through the",
  "Este site não contém rastreadores publicitários nem ferramentas de análise de audiência. As informações enviadas por e-mail ou pelo",
  "Este sitio no contiene rastreadores publicitarios ni herramientas de análisis de audiencia. La información enviada por correo electrónico o mediante el"),
 "formulaire de demande de projet": T("project request form", "formulário de solicitação de projeto", "formulario de solicitud de proyecto"),
 "servent à traiter votre demande et à assurer le suivi de nos échanges (détails dans la": T(
  "is used to handle your request and follow up on our exchanges (details in the",
  "servem para tratar sua solicitação e acompanhar nossas conversas (detalhes no",
  "sirve para tramitar su solicitud y hacer el seguimiento de nuestros intercambios (detalles en el"),
 "notice de confidentialité": T("privacy notice", "aviso de privacidade", "aviso de privacidad"),
 "). Le site est hébergé par Cloudflare. L’assistant IA (bouton « Une question ? ») n’est chargé que si vous l’ouvrez ; vos messages sont alors traités par Microsoft Copilot Studio (": T(
  "). The site is hosted by Cloudflare. The AI assistant (the “Questions?” button) only loads if you open it; your messages are then processed by Microsoft Copilot Studio (",
  "). O site é hospedado pela Cloudflare. O assistente de IA (botão “Dúvidas?”) só é carregado se você o abrir; suas mensagens são então processadas pelo Microsoft Copilot Studio (",
  "). El sitio está alojado por Cloudflare. El asistente de IA (botón «¿Preguntas?») solo se carga si usted lo abre; sus mensajes son entonces tratados por Microsoft Copilot Studio ("),
 "détails": T("details", "detalhes", "detalles"),
 "). Vous pouvez demander l’accès, la rectification ou la suppression de vos données à l’adresse ci-dessus. Vous pouvez également adresser une réclamation à la CNIL.": T(
  "). You can request access to, correction or deletion of your data at the address above. You can also lodge a complaint with the CNIL (French data protection authority).",
  "). Você pode solicitar o acesso, a retificação ou a exclusão dos seus dados pelo endereço acima. Também pode apresentar uma reclamação à CNIL (autoridade francesa de proteção de dados).",
  "). Puede solicitar el acceso, la rectificación o la supresión de sus datos en la dirección indicada. También puede presentar una reclamación ante la CNIL (autoridad francesa de protección de datos)."),
},
"projet.html": {
 "Demande de projet — HDA Solutions": T("Project request — HDA Solutions", "Solicitação de projeto — HDA Solutions", "Solicitud de proyecto — HDA Solutions"),
 "Décrivez votre projet d’agent IA, de copilote ou d’automatisation : objectifs, délais et budget indicatif. Réponse personnalisée de HDA Solutions.": T(
  "Describe your AI agent, copilot or automation project: goals, timing and indicative budget. A personal reply from HDA Solutions.",
  "Descreva seu projeto de agente de IA, copiloto ou automação: objetivos, prazos e orçamento indicativo. Resposta personalizada da HDA Solutions.",
  "Describa su proyecto de agente de IA, copiloto o automatización: objetivos, plazos y presupuesto orientativo. Respuesta personalizada de HDA Solutions."),
 "Aller au formulaire": T("Skip to the form", "Ir para o formulário", "Ir al formulario"),
 "Navigation principale": T("Main navigation", "Navegação principal", "Navegación principal"),
 "Solutions": T("Solutions", "Soluções", "Soluciones"),
 "Applications": T("Use cases", "Aplicações", "Aplicaciones"),
 "Décrire mon projet ↗": T("Describe my project ↗", "Descrever meu projeto ↗", "Describir mi proyecto ↗"),
 "Demande de projet": T("Project request", "Solicitação de projeto", "Solicitud de proyecto"),
 "Parlez-nous de": T("Tell us about", "Fale-nos do", "Háblenos de"),
 "votre projet.": T("your project.", "seu projeto.", "su proyecto."),
 "Quelques informations suffisent pour préparer un premier échange utile : votre besoin, vos outils actuels, le délai et un ordre de budget. Vous recevez une réponse personnalisée, sans engagement.": T(
  "A few details are enough to prepare a useful first conversation: your need, your current tools, the timing and a rough budget. You’ll receive a personal reply, with no commitment.",
  "Algumas informações bastam para preparar uma primeira conversa útil: sua necessidade, suas ferramentas atuais, o prazo e uma ordem de orçamento. Você recebe uma resposta personalizada, sem compromisso.",
  "Unos pocos datos bastan para preparar una primera conversación útil: su necesidad, sus herramientas actuales, el plazo y un orden de presupuesto. Recibirá una respuesta personalizada, sin compromiso."),
 "Vous": T("You", "Você", "Usted"),
 "Nom et prénom": T("Full name", "Nome completo", "Nombre y apellidos"),
 "obligatoire": T("required", "obrigatório", "obligatorio"),
 "Entreprise ou organisation": T("Company or organisation", "Empresa ou organização", "Empresa u organización"),
 "E-mail": T("E-mail", "E-mail", "Correo electrónico"),
 "Téléphone": T("Phone", "Telefone", "Teléfono"),
 "Votre projet": T("Your project", "Seu projeto", "Su proyecto"),
 "Type de projet": T("Project type", "Tipo de projeto", "Tipo de proyecto"),
 "Choisir…": T("Choose…", "Escolher…", "Elegir…"),
 "Agent ou copilote IA": T("AI agent or copilot", "Agente ou copiloto de IA", "Agente o copiloto de IA"),
 "Automatisation de processus": T("Process automation", "Automação de processos", "Automatización de procesos"),
 "Accès aux documents et à la connaissance": T("Access to documents and knowledge", "Acesso a documentos e ao conhecimento", "Acceso a documentos y al conocimiento"),
 "Pilote CoproSens sur vos documents": T("CoproSens pilot on your documents", "Piloto do CoproSens com os seus documentos", "Piloto de CoproSens con sus documentos"),
 "Autre": T("Other", "Outro", "Otro"),
 "Description": T("Description", "Descrição", "Descripción"),
 "Le besoin, les utilisateurs concernés, les outils actuels (Microsoft 365, SharePoint…) et le résultat attendu.": T(
  "The need, the users involved, your current tools (Microsoft 365, SharePoint…) and the expected result.",
  "A necessidade, os usuários envolvidos, as ferramentas atuais (Microsoft 365, SharePoint…) e o resultado esperado.",
  "La necesidad, los usuarios implicados, las herramientas actuales (Microsoft 365, SharePoint…) y el resultado esperado."),
 "Délai souhaité": T("Preferred timing", "Prazo desejado", "Plazo deseado"),
 "Dès que possible": T("As soon as possible", "O quanto antes", "Lo antes posible"),
 "Dans 1 à 3 mois": T("Within 1 to 3 months", "Em 1 a 3 meses", "En 1 a 3 meses"),
 "Dans 3 à 6 mois": T("Within 3 to 6 months", "Em 3 a 6 meses", "En 3 a 6 meses"),
 "Plus tard / à définir": T("Later / to be defined", "Mais tarde / a definir", "Más adelante / por definir"),
 "Budget indicatif": T("Indicative budget", "Orçamento indicativo", "Presupuesto orientativo"),
 "Moins de 2 000 €": T("Under €2,000", "Menos de 2.000 €", "Menos de 2.000 €"),
 "2 000 – 5 000 €": T("€2,000 – €5,000", "2.000 – 5.000 €", "2.000 – 5.000 €"),
 "5 000 – 15 000 €": T("€5,000 – €15,000", "5.000 – 15.000 €", "5.000 – 15.000 €"),
 "Plus de 15 000 €": T("Over €15,000", "Mais de 15.000 €", "Más de 15.000 €"),
 "À définir ensemble": T("To be defined together", "A definir juntos", "Por definir juntos"),
 "Comment nous avez-vous connus ?": T("How did you hear about us?", "Como nos conheceu?", "¿Cómo nos ha conocido?"),
 "Ne pas remplir": T("Leave empty", "Não preencher", "No rellenar"),
 "J’accepte que mes informations soient utilisées pour traiter ma demande et me recontacter, conformément à la": T(
  "I agree that my information may be used to handle my request and contact me, in accordance with the",
  "Concordo que minhas informações sejam usadas para tratar minha solicitação e entrar em contato comigo, conforme o",
  "Acepto que mis datos se utilicen para tramitar mi solicitud y volver a contactarme, de acuerdo con el"),
 "notice de confidentialité": T("privacy notice", "aviso de privacidade", "aviso de privacidad"),
 "Envoyer ma demande ↗": T("Send my request ↗", "Enviar minha solicitação ↗", "Enviar mi solicitud ↗"),
 "* champs obligatoires": T("* required fields", "* campos obrigatórios", "* campos obligatorios"),
 "Le formulaire nécessite JavaScript. Vous pouvez aussi écrire à": T(
  "The form requires JavaScript. You can also write to", "O formulário requer JavaScript. Você também pode escrever para", "El formulario requiere JavaScript. También puede escribir a"),
 "CE QUI SE PASSE ENSUITE": T("WHAT HAPPENS NEXT", "O QUE ACONTECE DEPOIS", "QUÉ PASA DESPUÉS"),
 "Lecture de votre demande": T("We read your request", "Leitura da sua solicitação", "Lectura de su solicitud"),
 "et premières questions si nécessaire.": T("and ask first questions if needed.", "e primeiras perguntas, se necessário.", "y primeras preguntas si es necesario."),
 "Un échange": T("A conversation", "Uma conversa", "Una conversación"),
 "pour préciser le besoin, les outils et les contraintes.": T(
  "to clarify the need, the tools and the constraints.", "para detalhar a necessidade, as ferramentas e as restrições.", "para precisar la necesidad, las herramientas y las limitaciones."),
 "Une proposition": T("A proposal", "Uma proposta", "Una propuesta"),
 "de première étape, avec périmètre et estimation.": T(
  "for a first step, with scope and estimate.", "de primeira etapa, com escopo e estimativa.", "de primera etapa, con alcance y estimación."),
 "PRÉFÉREZ L’E-MAIL ?": T("PREFER E-MAIL?", "PREFERE E-MAIL?", "¿PREFIERE EL CORREO?"),
 "Écrivez directement à": T("Write directly to", "Escreva diretamente para", "Escriba directamente a"),
 "Notice de confidentialité": T("Privacy notice", "Aviso de privacidade", "Aviso de privacidad"),
 "Responsable du traitement :": T("Data controller:", "Responsável pelo tratamento:", "Responsable del tratamiento:"),
 "Hélio Abreu de Andrade, entrepreneur individuel (HDA PRODZ), 10 rue Jean Rostand, 91300 Massy, France. Contact :": T(
  "Hélio Abreu de Andrade, sole proprietor (HDA PRODZ), 10 rue Jean Rostand, 91300 Massy, France. Contact:",
  "Hélio Abreu de Andrade, empresário individual (HDA PRODZ), 10 rue Jean Rostand, 91300 Massy, França. Contato:",
  "Hélio Abreu de Andrade, empresario individual (HDA PRODZ), 10 rue Jean Rostand, 91300 Massy, Francia. Contacto:"),
 "Données et finalité :": T("Data and purpose:", "Dados e finalidade:", "Datos y finalidad:"),
 "les informations saisies servent uniquement à traiter votre demande, à vous recontacter et à préparer une éventuelle proposition (base légale : mesures précontractuelles prises à votre demande). Elles ne sont ni vendues ni utilisées à des fins publicitaires.": T(
  "the information you enter is used only to handle your request, contact you and prepare a possible proposal (legal basis: pre-contractual steps taken at your request). It is never sold or used for advertising.",
  "as informações fornecidas servem apenas para tratar sua solicitação, entrar em contato com você e preparar uma eventual proposta (base legal: medidas pré-contratuais tomadas a seu pedido). Elas não são vendidas nem usadas para fins publicitários.",
  "los datos introducidos sirven únicamente para tramitar su solicitud, volver a contactarle y preparar una posible propuesta (base jurídica: medidas precontractuales adoptadas a petición suya). No se venden ni se utilizan con fines publicitarios."),
 "Destinataires et sous-traitants :": T("Recipients and processors:", "Destinatários e subcontratados:", "Destinatarios y encargados del tratamiento:"),
 "la demande est transmise par e-mail à la messagerie professionnelle Microsoft 365 de HDA PRODZ. Le site est hébergé par Cloudflare, qui fournit aussi Turnstile, une vérification anti-robot qui traite des données techniques de connexion.": T(
  "your request is sent by e-mail to HDA PRODZ’s Microsoft 365 business mailbox. The site is hosted by Cloudflare, which also provides Turnstile, an anti-bot check that processes technical connection data.",
  "a solicitação é enviada por e-mail para a caixa de correio profissional Microsoft 365 da HDA PRODZ. O site é hospedado pela Cloudflare, que também fornece o Turnstile, uma verificação anti-robô que trata dados técnicos de conexão.",
  "la solicitud se envía por correo electrónico al buzón profesional Microsoft 365 de HDA PRODZ. El sitio está alojado por Cloudflare, que también proporciona Turnstile, una verificación antirrobot que trata datos técnicos de conexión."),
 "Assistant IA :": T("AI assistant:", "Assistente de IA:", "Asistente de IA:"),
 "l’assistant du site (bouton « Une question ? ») n’est chargé que si vous l’ouvrez. Vos messages sont alors traités par Microsoft (Copilot Studio) pour générer les réponses, à partir du contenu public de ce site, et les conversations sont enregistrées dans notre environnement Microsoft hébergé en Suisse, pays reconnu par l’Union européenne comme offrant un niveau de protection adéquat. Elles servent uniquement à améliorer l’assistant et sont supprimées après 30 jours. Les réponses sont générées par IA et peuvent contenir des erreurs ; elles ne constituent ni un devis ni un engagement. Ne partagez pas de données sensibles dans l’assistant.": T(
  "the site’s assistant (the “Questions?” button) only loads if you open it. Your messages are then processed by Microsoft (Copilot Studio) to generate answers from this site’s public content, and conversations are stored in our Microsoft environment hosted in Switzerland, a country recognised by the European Union as providing an adequate level of protection. They are used only to improve the assistant and are deleted after 30 days. Answers are AI-generated and may contain errors; they are neither a quote nor a commitment. Please don’t share sensitive data with the assistant.",
  "o assistente do site (botão “Dúvidas?”) só é carregado se você o abrir. Suas mensagens são então processadas pela Microsoft (Copilot Studio) para gerar as respostas a partir do conteúdo público deste site, e as conversas são registradas no nosso ambiente Microsoft hospedado na Suíça, país reconhecido pela União Europeia como oferecendo um nível de proteção adequado. Elas servem apenas para melhorar o assistente e são excluídas após 30 dias. As respostas são geradas por IA e podem conter erros; não constituem orçamento nem compromisso. Não compartilhe dados sensíveis no assistente.",
  "el asistente del sitio (botón «¿Preguntas?») solo se carga si usted lo abre. Sus mensajes son entonces tratados por Microsoft (Copilot Studio) para generar las respuestas a partir del contenido público de este sitio, y las conversaciones se guardan en nuestro entorno Microsoft alojado en Suiza, país reconocido por la Unión Europea como garante de un nivel de protección adecuado. Solo sirven para mejorar el asistente y se eliminan a los 30 días. Las respuestas se generan con IA y pueden contener errores; no constituyen un presupuesto ni un compromiso. No comparta datos sensibles en el asistente."),
 "Durée de conservation :": T("Retention:", "Prazo de conservação:", "Plazo de conservación:"),
 "3 ans à compter du dernier contact, sauf relation contractuelle ultérieure.": T(
  "3 years from the last contact, unless a contract follows.", "3 anos a partir do último contato, salvo relação contratual posterior.", "3 años desde el último contacto, salvo relación contractual posterior."),
 "Vos droits :": T("Your rights:", "Seus direitos:", "Sus derechos:"),
 "accès, rectification, effacement, limitation et opposition, en écrivant à l’adresse ci-dessus. Vous pouvez également adresser une réclamation à la CNIL (www.cnil.fr).": T(
  "access, correction, erasure, restriction and objection, by writing to the address above. You can also lodge a complaint with the CNIL, the French data protection authority (www.cnil.fr).",
  "acesso, retificação, exclusão, limitação e oposição, escrevendo para o endereço acima. Também pode apresentar uma reclamação à CNIL, autoridade francesa de proteção de dados (www.cnil.fr).",
  "acceso, rectificación, supresión, limitación y oposición, escribiendo a la dirección indicada. También puede presentar una reclamación ante la CNIL, autoridad francesa de protección de datos (www.cnil.fr)."),
 "Retour à l’accueil": T("Back to home", "Voltar à página inicial", "Volver al inicio"),
},
}

# Video poster (SVG image) texts.
POSTER = {
 "en": [("L’IA au service de la gestion de copropriété.", "AI for co-ownership (condominium) management."),
        ("Présentation · 2 min 49 s · English", "Presentation · 2 min 49 s · English")],
 "pt": [("L’IA au service de la gestion de copropriété.", "IA a serviço da gestão de condomínios."),
        ("Présentation · 2 min 49 s · English", "Apresentação · 2 min 49 s · em inglês")],
 "es": [("L’IA au service de la gestion de copropriété.", "La IA al servicio de la gestión de comunidades."),
        ("Présentation · 2 min 49 s · English", "Presentación · 2 min 49 s · en inglés")],
}

# ---------------------------------------------------------------------------
# Standalone pages: syndic tools demo (/outils/) and price estimator (/tarifs/).
# Their JavaScript texts live in outils/l10n.js and tarifs/l10n.js.
# Prices stay in euros in every language; only the number format follows the locale.
PAGES["outils/index.html"] = {
    "out": {"en": "tools/index.html", "pt": "ferramentas/index.html", "es": "herramientas/index.html"},
    "must_not_remain": ["Outils du syndic", "Appels de fonds", "Ordre du jour", "Procès-verbal", "Budget prévisionnel",
                        "Télécharger", "Imprimer", "Retour à l’accueil", "tantièmes", "copropriétaires", "Tableau de bord", "Parlons de"],
}
PAGES["tarifs/index.html"] = {
    "out": {"en": "pricing/index.html", "pt": "precos/index.html", "es": "precios/index.html"},
    "must_not_remain": ["Votre copropriété", "Demander", "Imprimer", " lots", "Estimation indicative", "par mois",
                        "Retour à l’accueil", "conseil syndical", "Tableau de bord", "Outils du syndic", "TVA"],
}

TEXT["outils/index.html"] = {
 "Outils du syndic – CoproSens (démonstration)": T(
  "Property manager tools – CoproSens (demo)",
  "Ferramentas da administradora – CoproSens (demonstração)",
  "Herramientas del administrador de fincas – CoproSens (demostración)"),
 "Démonstration CoproSens : répartition des charges et appels de fonds, ordre du jour, convocation et procès-verbal d’assemblée générale.": T(
  "CoproSens demo: charge allocation and service-charge calls, agenda, notice of meeting and general meeting minutes.",
  "Demonstração do CoproSens: rateio de despesas e cotas, ordem do dia, convocação e ata de assembleia geral.",
  "Demostración de CoproSens: reparto de gastos y cuotas, orden del día, convocatoria y acta de la junta general."),
 "Navigation principale": T("Main navigation", "Navegação principal", "Navegación principal"),
 "Tableau de bord": T("Dashboard", "Painel", "Panel"),
 "Parlons de votre projet ↗": T("Let’s talk about your project ↗", "Vamos falar do seu projeto ↗", "Hablemos de su proyecto ↗"),
 "CoproSens · démonstration": T("CoproSens · demo", "CoproSens · demonstração", "CoproSens · demostración"),
 "Les outils du syndic, sans ressaisie.": T(
  "Property manager tools, with no re-keying.",
  "As ferramentas da administradora, sem redigitação.",
  "Las herramientas del administrador, sin volver a teclear nada."),
 "Répartition des charges au centime près, appels de fonds par lot, et documents d’assemblée générale prêts à relire. Exemple sur la copropriété fictive": T(
  "Charges split to the cent, service-charge calls per unit, and general meeting documents ready to review. Example based on the fictional building",
  "Rateio das despesas ao centavo, cotas por unidade e documentos de assembleia geral prontos para revisar. Exemplo com o condomínio fictício",
  "Reparto de gastos al céntimo, cuotas por vivienda y documentos de junta general listos para revisar. Ejemplo con la comunidad ficticia"),
 "(42 lots, 10 000 tantièmes).": T("(42 units, 10,000 ownership shares).", "(42 unidades, 10.000 frações ideais).", "(42 viviendas, coeficientes sobre 10.000)."),
 "Appels de fonds": T("Service-charge calls", "Cotas condominiais", "Cuotas por vivienda"),
 "Documents d’assemblée générale": T("General meeting documents", "Documentos da assembleia geral", "Documentos de la junta general"),
 "Budget prévisionnel": T("Annual budget", "Previsão orçamentária", "Presupuesto anual"),
 "Charges générales (tantièmes généraux)": T("General charges (general shares)", "Despesas gerais (frações ideais gerais)", "Gastos generales (coeficientes generales)"),
 "Ascenseur (lots en étage uniquement)": T("Lift (upper-floor units only)", "Elevador (somente unidades nos andares)", "Ascensor (solo viviendas en plantas superiores)"),
 "Eau froide (compteurs individuels)": T("Cold water (individual meters)", "Água fria (medidores individuais)", "Agua fría (contadores individuales)"),
 "Chauffage collectif": T("Communal heating", "Aquecimento coletivo", "Calefacción central"),
 "Part consommation du chauffage (%)": T("Heating: usage-based share (%)", "Aquecimento: parcela por consumo (%)", "Calefacción: parte según consumo (%)"),
 "Fonds de travaux (% du budget)": T("Reserve fund (% of budget)", "Fundo de reserva (% do orçamento)", "Fondo de reserva (% del presupuesto)"),
 "Chauffage : part variable selon les répartiteurs de chaque lot, part fixe selon les tantièmes. Fonds de travaux : au moins 5 % du budget prévisionnel.": T(
  "Heating: variable share based on each unit’s heat cost allocators, fixed share based on ownership shares. Reserve fund: at least 5% of the annual budget (French rule).",
  "Aquecimento: parcela variável conforme os medidores de calor de cada unidade, parcela fixa conforme as frações ideais. Fundo de reserva: no mínimo 5% da previsão orçamentária (regra francesa).",
  "Calefacción: parte variable según los repartidores de costes de cada vivienda, parte fija según los coeficientes. Fondo de reserva: al menos el 5 % del presupuesto (norma francesa)."),
 "Mode simple : tout répartir aux tantièmes généraux": T(
  "Simple mode: split everything by general shares",
  "Modo simples: ratear tudo pelas frações ideais gerais",
  "Modo simple: repartir todo según los coeficientes generales"),
 "Le mode simple est celui du": T("Simple mode is the one used in the", "O modo simples é o do", "El modo simple es el del"),
 "tableau de bord de démonstration": T("demo dashboard", "painel de demonstração", "panel de demostración"),
 "(lot 01 : 796,98 € par trimestre). Le mode détaillé applique l’ascenseur aux seuls lots en étage et les consommations réelles d’eau et de chauffage.": T(
  "(unit 01: €796.98 per quarter). Detailed mode charges the lift to upper-floor units only and uses actual water and heating consumption.",
  "(unidade 01: € 796,98 por trimestre). O modo detalhado cobra o elevador apenas das unidades nos andares e usa os consumos reais de água e aquecimento.",
  "(vivienda 01: 796,98 € por trimestre). El modo detallado imputa el ascensor solo a las viviendas de plantas superiores y aplica los consumos reales de agua y calefacción."),
 "Fonds de travaux": T("Reserve fund", "Fundo de reserva", "Fondo de reserva"),
 "Total à appeler sur l’année": T("Total to collect for the year", "Total a arrecadar no ano", "Total a recaudar en el año"),
 "Exporter (Excel, CSV)": T("Export (Excel, CSV)", "Exportar (Excel, CSV)", "Exportar (Excel, CSV)"),
 "Imprimer": T("Print", "Imprimir", "Imprimir"),
 "Calcul déterministe, sans IA : chaque montant est arrondi au centime et le total des lots est toujours égal au budget.": T(
  "Deterministic calculation, no AI: every amount is rounded to the cent and the units always add up exactly to the budget.",
  "Cálculo determinístico, sem IA: cada valor é arredondado ao centavo e a soma das unidades é sempre igual ao orçamento.",
  "Cálculo determinista, sin IA: cada importe se redondea al céntimo y la suma de las viviendas coincide siempre con el presupuesto."),
 "Répartition annuelle et appel trimestriel par lot": T("Annual split and quarterly call per unit", "Rateio anual e cota trimestral por unidade", "Reparto anual y cuota trimestral por vivienda"),
 "Lot": T("Unit", "Unidade", "Vivienda"),
 "Tantièmes": T("Shares", "Fração", "Coeficiente"),
 "Charges générales": T("General charges", "Despesas gerais", "Gastos generales"),
 "Ascenseur": T("Lift", "Elevador", "Ascensor"),
 "Eau": T("Water", "Água", "Agua"),
 "Chauffage": T("Heating", "Aquecimento", "Calefacción"),
 "Total annuel": T("Annual total", "Total anual", "Total anual"),
 "Appel trimestriel": T("Quarterly call", "Cota trimestral", "Cuota trimestral"),
 "Préparer l’assemblée": T("Prepare the meeting", "Preparar a assembleia", "Preparar la junta"),
 "Date de l’assemblée": T("Meeting date", "Data da assembleia", "Fecha de la junta"),
 "Heure": T("Time", "Horário", "Hora"),
 "Lieu": T("Venue", "Local", "Lugar"),
 "Date d’envoi de la convocation": T("Date the notice is sent", "Data de envio da convocação", "Fecha de envío de la convocatoria"),
 "Participation possible en visioconférence": T("Attendance by video conference possible", "Participação por videoconferência possível", "Posibilidad de asistir por videoconferencia"),
 "Ordre du jour": T("Agenda", "Ordem do dia", "Orden del día"),
 "Ajouter une résolution": T("Add a resolution", "Adicionar uma resolução", "Añadir una propuesta"),
 "Résultats des votes (pour le procès-verbal)": T("Voting results (for the minutes)", "Resultados das votações (para a ata)", "Resultados de las votaciones (para el acta)"),
 "Lots absents et non représentés": T("Units absent and not represented", "Unidades ausentes e não representadas", "Viviendas ausentes y no representadas"),
 "Document": T("Document", "Documento", "Documento"),
 "Convocation": T("Notice of meeting", "Convocação", "Convocatoria"),
 "Vote par correspondance": T("Postal vote", "Voto por correspondência", "Voto por correo"),
 "Procès-verbal": T("Minutes", "Ata", "Acta"),
 "Télécharger (Word)": T("Download (Word)", "Baixar (Word)", "Descargar (Word)"),
 "Imprimer / PDF": T("Print / PDF", "Imprimir / PDF", "Imprimir / PDF"),
 "Envoyer aux copropriétaires": T("Send to owners", "Enviar aos condôminos", "Enviar a los propietarios"),
 "En démonstration, rien n’est envoyé. Chez vous, l’envoi part de votre messagerie Microsoft 365 ou de votre prestataire de lettre recommandée électronique, uniquement après validation du document par le syndic.": T(
  "Nothing is sent in this demo. In your organisation, documents go out from your Microsoft 365 mailbox or your electronic registered mail provider, only after the property manager has approved them.",
  "Nada é enviado nesta demonstração. Na sua empresa, o envio sai da sua caixa de e-mail Microsoft 365 ou do seu provedor de carta registrada eletrônica, somente após a validação do documento pela administradora.",
  "En esta demostración no se envía nada. En su despacho, el envío sale de su buzón de Microsoft 365 o de su proveedor de correo certificado electrónico, solo después de que el administrador haya validado el documento."),
 "Démonstration sur données fictives. Les modèles de documents reprennent les mentions usuelles de la loi du 10 juillet 1965 et du décret du 17 mars 1967 ; ils doivent être relus et validés par le syndic et ne constituent pas un conseil juridique.": T(
  "Demo with fictional data. The document templates follow the standard wording of the French law of 10 July 1965 and decree of 17 March 1967; they must be reviewed and approved by the property manager and are not legal advice. During a pilot, they are adapted to your country and legal framework.",
  "Demonstração com dados fictícios. Os modelos de documentos seguem as menções usuais da lei francesa de 10 de julho de 1965 e do decreto de 17 de março de 1967; devem ser revisados e validados pela administradora e não constituem aconselhamento jurídico. Durante um piloto, são adaptados ao seu país e ao seu marco legal.",
  "Demostración con datos ficticios. Los modelos de documentos recogen las menciones habituales de la ley francesa de 10 de julio de 1965 y del decreto de 17 de marzo de 1967; deben ser revisados y validados por el administrador y no constituyen asesoramiento jurídico. Durante un piloto, se adaptan a su país y a su marco legal."),
 "Retour à l’accueil": T("Back to home", "Voltar à página inicial", "Volver al inicio"),
}

TEXT["tarifs/index.html"] = {
 "Estimer le coût de CoproSens – HDA Solutions": T(
  "Estimate the cost of CoproSens – HDA Solutions",
  "Estime o custo do CoproSens – HDA Solutions",
  "Calcule el coste de CoproSens – HDA Solutions"),
 "Estimez en quelques secondes le coût de CoproSens pour votre copropriété : pilote, mise en place, licences Microsoft et coût par lot et par mois.": T(
  "Estimate in seconds what CoproSens costs for your building: pilot, setup, Microsoft licences and cost per unit per month, in euros.",
  "Estime em segundos o custo do CoproSens para o seu condomínio: piloto, implantação, licenças Microsoft e custo por unidade e por mês, em euros.",
  "Calcule en segundos el coste de CoproSens para su comunidad: piloto, implantación, licencias de Microsoft y coste por vivienda y mes, en euros."),
 "Navigation principale": T("Main navigation", "Navegação principal", "Navegación principal"),
 "Outils du syndic": T("Manager tools", "Ferramentas da administradora", "Herramientas del administrador"),
 "Tableau de bord": T("Dashboard", "Painel", "Panel"),
 "Demander un devis ↗": T("Request a quote ↗", "Solicitar orçamento ↗", "Solicitar presupuesto ↗"),
 "CoproSens · estimation en toute transparence": T("CoproSens · transparent estimate", "CoproSens · estimativa transparente", "CoproSens · estimación transparente"),
 "Combien coûte CoproSens pour votre copropriété&nbsp;?": T(
  "How much does CoproSens cost for your building?",
  "Quanto custa o CoproSens para o seu condomínio?",
  "¿Cuánto cuesta CoproSens para su comunidad?"),
 "Indiquez la taille de votre copropriété et les options souhaitées : vous obtenez une estimation immédiate, y compris le coût par lot et par mois. Nos prix dépendent de la complexité réelle du projet, pas d’un forfait unique.": T(
  "Enter the size of your building and the options you want: you get an instant estimate, including the cost per unit per month. All prices are in euros and reflect the real complexity of the project, not a one-size-fits-all package.",
  "Informe o tamanho do seu condomínio e as opções desejadas: você recebe uma estimativa imediata, incluindo o custo por unidade e por mês. Todos os valores estão em euros e dependem da complexidade real do projeto, não de um pacote único.",
  "Indique el tamaño de su comunidad y las opciones que desea: obtendrá una estimación inmediata, incluido el coste por vivienda y mes. Todos los importes están en euros y dependen de la complejidad real del proyecto, no de una tarifa única."),
 "Votre copropriété": T("Your building", "Seu condomínio", "Su comunidad"),
 "Nombre de lots principaux (logements, commerces, bureaux)": T(
  "Number of main units (homes, shops, offices)",
  "Número de unidades principais (apartamentos, lojas, salas comerciais)",
  "Número de viviendas y locales (viviendas, comercios, oficinas)"),
 "Sans compter les caves ni les parkings. Ce chiffre figure sur la fiche synthétique de votre copropriété.": T(
  "Not counting storage rooms or parking spaces. You will find this figure in your building’s records.",
  "Sem contar depósitos nem vagas de garagem. Esse número consta nos documentos do seu condomínio.",
  "Sin contar trasteros ni plazas de garaje. Esta cifra figura en la documentación de su comunidad."),
 "Membres du conseil syndical (comptes Microsoft 365)": T(
  "Owners’ council members (Microsoft 365 accounts)",
  "Membros do conselho (contas Microsoft 365)",
  "Miembros del consejo de propietarios (cuentas de Microsoft 365)"),
 "Jours supplémentaires (numérisation d’archives papier, historique très volumineux, séances de prise en main en plus)": T(
  "Extra days (digitising paper archives, very large history, additional onboarding sessions)",
  "Dias adicionais (digitalização de arquivos em papel, histórico muito volumoso, sessões extras de capacitação)",
  "Días adicionales (digitalización de archivos en papel, histórico muy voluminoso, sesiones de formación adicionales)"),
 "Options": T("Options", "Opções", "Opciones"),
 "Tableau de bord du conseil syndical (appels de fonds, travaux, décisions d’AG)": T(
  "Owners’ council dashboard (service-charge calls, works, general meeting decisions)",
  "Painel do conselho (cotas, obras, decisões de assembleia)",
  "Panel del consejo (cuotas, obras, acuerdos de la junta)"),
 "Contrat de maintenance après le pilote": T("Maintenance contract after the pilot", "Contrato de manutenção após o piloto", "Contrato de mantenimiento tras el piloto"),
 "Offre clients fondateurs (copropriétés jusqu’à 32 lots, jusqu’au 31/12/2026)": T(
  "Founding client offer (buildings up to 32 units, until 31 December 2026)",
  "Oferta clientes fundadores (condomínios com até 32 unidades, até 31/12/2026)",
  "Oferta clientes fundadores (comunidades de hasta 32 viviendas, hasta el 31/12/2026)"),
 "Pilote à tarif réduit et tableau de bord inclus, en échange d’un témoignage et d’une étude de cas.": T(
  "Discounted pilot with the dashboard included, in exchange for a testimonial and a case study.",
  "Piloto com preço reduzido e painel incluído, em troca de um depoimento e de um estudo de caso.",
  "Piloto a precio reducido con el panel incluido, a cambio de un testimonio y un caso de éxito."),
 "Pilote CoproSens (6 semaines)": T("CoproSens pilot (6 weeks)", "Piloto CoproSens (6 semanas)", "Piloto CoproSens (6 semanas)"),
 "Mise en place Microsoft 365 et prise en main": T("Microsoft 365 setup and onboarding", "Implantação no Microsoft 365 e capacitação", "Implantación en Microsoft 365 y formación"),
 "Licences Microsoft 365 (par an)": T("Microsoft 365 licences (per year)", "Licenças Microsoft 365 (por ano)", "Licencias de Microsoft 365 (por año)"),
 "Total première année": T("First-year total", "Total do primeiro ano", "Total del primer año"),
 "Par lot et par mois, la 1": T("Per unit per month, 1", "Por unidade e por mês, no 1", "Por vivienda y mes, el 1."),
 "re": T("st", "º", "er"),
 "année": T("year", "ano", "año"),
 "Par lot et par mois, les années suivantes": T("Per unit per month, following years", "Por unidade e por mês, nos anos seguintes", "Por vivienda y mes, años siguientes"),
 "Maintenance (par mois), soit par lot et par mois": T(
  "Maintenance (per month), i.e. per unit per month",
  "Manutenção (por mês), ou seja, por unidade e por mês",
  "Mantenimiento (al mes), es decir, por vivienda y mes"),
 "Au-delà de 200 lots, chaque projet est étudié sur mesure : nous vous adressons un devis détaillé.": T(
  "Above 200 units, each project is assessed individually: we send you a detailed quote.",
  "Acima de 200 unidades, cada projeto é estudado sob medida: enviamos um orçamento detalhado.",
  "Por encima de 200 viviendas, cada proyecto se estudia a medida: le enviamos un presupuesto detallado."),
 "Imprimer": T("Print", "Imprimir", "Imprimir"),
 "Demander un devis personnalisé": T("Request a tailored quote", "Solicitar um orçamento personalizado", "Solicitar un presupuesto personalizado"),
 "Notre grille, selon la taille de la copropriété": T("Our price grid, by building size", "Nossa tabela, conforme o tamanho do condomínio", "Nuestras tarifas, según el tamaño de la comunidad"),
 "Taille": T("Size", "Tamanho", "Tamaño"),
 "Pilote": T("Pilot", "Piloto", "Piloto"),
 "Mise en place et prise en main": T("Setup and onboarding", "Implantação e capacitação", "Implantación y formación"),
 "Maintenance (option)": T("Maintenance (optional)", "Manutenção (opcional)", "Mantenimiento (opcional)"),
 "Jusqu’à 32 lots": T("Up to 32 units", "Até 32 unidades", "Hasta 32 viviendas"),
 "2 500 € (1 750 € offre fondateurs)": T("€2,500 (€1,750 founding offer)", "€ 2.500 (€ 1.750 na oferta fundadores)", "2500 € (1750 € oferta fundadores)"),
 "3 jours, soit 1 650 €": T("3 days, i.e. €1,650", "3 dias, ou seja, € 1.650", "3 días, es decir, 1650 €"),
 "175 € / mois (2 h incluses)": T("€175 / month (2 h included)", "€ 175 / mês (2 h incluídas)", "175 € / mes (2 h incluidas)"),
 "33 à 100 lots": T("33 to 100 units", "33 a 100 unidades", "De 33 a 100 viviendas"),
 "2 500 €": T("€2,500", "€ 2.500", "2500 €"),
 "5 jours, soit 2 750 €": T("5 days, i.e. €2,750", "5 dias, ou seja, € 2.750", "5 días, es decir, 2750 €"),
 "350 € / mois (½ journée incluse)": T("€350 / month (½ day included)", "€ 350 / mês (½ dia incluído)", "350 € / mes (½ jornada incluida)"),
 "101 à 200 lots": T("101 to 200 units", "101 a 200 unidades", "De 101 a 200 viviendas"),
 "8 jours, soit 4 400 €": T("8 days, i.e. €4,400", "8 dias, ou seja, € 4.400", "8 días, es decir, 4400 €"),
 "550 € / mois (1 journée incluse)": T("€550 / month (1 day included)", "€ 550 / mês (1 dia incluído)", "550 € / mes (1 jornada incluida)"),
 "Plus de 200 lots": T("More than 200 units", "Mais de 200 unidades", "Más de 200 viviendas"),
 "Devis personnalisé, établi après étude de vos documents": T(
  "Tailored quote, prepared after reviewing your documents",
  "Orçamento personalizado, elaborado após análise dos seus documentos",
  "Presupuesto personalizado, elaborado tras estudiar sus documentos"),
 "Tableau de bord du conseil syndical : 750 € (inclus dans l’offre fondateurs). Jour supplémentaire : 550 €. Au-delà du temps inclus, la maintenance est facturée 550 € par jour. Licences Microsoft 365 refacturées à prix coûtant (base indicative 7,80 € TTC par membre et par mois). La consommation d’IA est facturée directement par Microsoft à la copropriété ; pendant le pilote, elle est déduite de notre facture.": T(
  "Owners’ council dashboard: €750 (included in the founding offer). Extra day: €550. Beyond the included time, maintenance is billed at €550 per day. Microsoft 365 licences re-invoiced at cost (indicative basis €7.80 per member per month, taxes included). AI consumption is billed directly by Microsoft to the building; during the pilot, it is deducted from our invoice.",
  "Painel do conselho: € 750 (incluído na oferta fundadores). Dia adicional: € 550. Além do tempo incluído, a manutenção é cobrada a € 550 por dia. Licenças Microsoft 365 repassadas a preço de custo (base indicativa de € 7,80 por membro e por mês, impostos incluídos). O consumo de IA é faturado diretamente pela Microsoft ao condomínio; durante o piloto, ele é descontado da nossa fatura.",
  "Panel del consejo: 750 € (incluido en la oferta fundadores). Día adicional: 550 €. Más allá del tiempo incluido, el mantenimiento se factura a 550 € por día. Licencias de Microsoft 365 refacturadas a precio de coste (base orientativa de 7,80 € por miembro y mes, impuestos incluidos). El consumo de IA lo factura Microsoft directamente a la comunidad; durante el piloto, se descuenta de nuestra factura."),
 "Estimation indicative, non contractuelle.": T("Indicative, non-binding estimate.", "Estimativa indicativa, sem valor contratual.", "Estimación orientativa, sin valor contractual."),
 "Ces montants servent à vous donner un ordre de grandeur. Le prix définitif est confirmé par un devis écrit, après un échange sur vos documents, vos besoins et vos contraintes. TVA non applicable, art. 293 B du CGI. Les prix des licences et de la consommation Microsoft peuvent évoluer.": T(
  "These amounts give you an order of magnitude. The final price is confirmed in a written quote, after we discuss your documents, needs and constraints. All prices are in euros. VAT not applicable (French micro-enterprise, art. 293 B of the French General Tax Code). Microsoft licence and consumption prices may change.",
  "Esses valores dão uma ordem de grandeza. O preço final é confirmado por um orçamento por escrito, após uma conversa sobre seus documentos, necessidades e restrições. Todos os valores estão em euros. Sem incidência de IVA francês (microempresa francesa, art. 293 B do Código Geral de Impostos da França). Os preços das licenças e do consumo Microsoft podem mudar.",
  "Estos importes le dan un orden de magnitud. El precio definitivo se confirma mediante un presupuesto por escrito, tras analizar sus documentos, necesidades y limitaciones. Todos los importes están en euros. IVA no aplicable (microempresa francesa, art. 293 B del Código General de Impuestos de Francia). Los precios de las licencias y del consumo de Microsoft pueden variar."),
 "Retour à l’accueil": T("Back to home", "Voltar à página inicial", "Volver al inicio"),
}
