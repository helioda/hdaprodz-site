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
 "Principe d’une solution : relier vos connaissances à un assistant IA pour préparer des réponses et actions, avec validation humaine.": T(
  "How a solution works: connect your knowledge to an AI assistant to prepare answers and actions, with human validation.",
  "Princípio de uma solução: conectar seu conhecimento a um assistente de IA para preparar respostas e ações, com validação humana.",
  "Principio de una solución: conectar su conocimiento a un asistente de IA para preparar respuestas y acciones, con validación humana."),
 "VOTRE TRAVAIL, CONNECTÉ": T("YOUR WORK, CONNECTED", "SEU TRABALHO, CONECTADO", "SU TRABAJO, CONECTADO"),
 "01 / LA CONNAISSANCE": T("01 / KNOWLEDGE", "01 / O CONHECIMENTO", "01 / EL CONOCIMIENTO"),
 "Vos documents et vos outils": T("Your documents and tools", "Seus documentos e ferramentas", "Sus documentos y herramientas"),
 "02 / L’ASSISTANT": T("02 / THE ASSISTANT", "02 / O ASSISTENTE", "02 / EL ASISTENTE"),
 "Comprendre. Retrouver. Préparer.": T("Understand. Find. Prepare.", "Entender. Encontrar. Preparar.", "Entender. Encontrar. Preparar."),
 "03 / VOTRE DÉCISION": T("03 / YOUR DECISION", "03 / SUA DECISÃO", "03 / SU DECISIÓN"),
 "Une prochaine étape plus claire": T("A clearer next step", "Um próximo passo mais claro", "Un siguiente paso más claro"),
 "Une illustration de notre approche · validation humaine des actions sensibles.": T(
  "An illustration of our approach · human validation of sensitive actions.",
  "Uma ilustração da nossa abordagem · validação humana das ações sensíveis.",
  "Una ilustración de nuestro enfoque · validación humana de las acciones sensibles."),
 "Assistants & agents IA": T("AI assistants & agents", "Assistentes e agentes de IA", "Asistentes y agentes de IA"),
 "France · Solutions sur mesure": T("France · Tailor-made solutions", "França · Soluções sob medida", "Francia · Soluciones a medida"),
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
 "Essayer la démo ↗": T("Try the demo ↗", "Experimentar a demo ↗", "Probar la demo ↗"),
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
 "Notre assistant IA pour faciliter la gestion de copropriété et l’accès aux documents.": T(
  "Our AI assistant to simplify co-ownership (condominium) management and access to documents.",
  "Nosso assistente de IA para facilitar a gestão de condomínios e o acesso aos documentos.",
  "Nuestro asistente de IA para facilitar la gestión de comunidades de propietarios y el acceso a los documentos."),
 "Retrouver une information dans les documents de la copropriété.": T(
  "Find information in the building’s documents.",
  "Encontrar uma informação nos documentos do condomínio.",
  "Encontrar información en los documentos de la comunidad."),
 "Préparer des communications et organiser les demandes.": T(
  "Prepare communications and organise requests.",
  "Preparar comunicados e organizar as solicitações.",
  "Preparar comunicaciones y organizar las solicitudes."),
 "Aider à suivre les actions et les échéances.": T(
  "Help track actions and deadlines.",
  "Ajudar a acompanhar as ações e os prazos.",
  "Ayudar a seguir las acciones y los plazos."),
 "Présentation de Syndic Assist – CoproPilot AI": T(
  "Syndic Assist – CoproPilot AI presentation",
  "Apresentação do Syndic Assist – CoproPilot AI",
  "Presentación de Syndic Assist – CoproPilot AI"),
 "Votre navigateur ne permet pas de lire cette vidéo.": T(
  "Your browser can’t play this video.", "Seu navegador não consegue reproduzir este vídeo.", "Su navegador no puede reproducir este vídeo."),
 "Télécharger la présentation": T("Download the presentation", "Baixar a apresentação", "Descargar la presentación"),
 "Syndic Assist – CoproPilot AI · Projet soumis à l’Agent-a-thon Microsoft × Founderz · Présentation en anglais · 2 min 49 s": T(
  "Syndic Assist – CoproPilot AI · Project submitted to the Microsoft × Founderz Agent-a-thon · Presentation in English · 2 min 49 s",
  "Syndic Assist – CoproPilot AI · Projeto submetido ao Agent-a-thon Microsoft × Founderz · Apresentação em inglês · 2 min 49 s",
  "Syndic Assist – CoproPilot AI · Proyecto presentado al Agent-a-thon Microsoft × Founderz · Presentación en inglés · 2 min 49 s"),
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
 "ou écrire à h@hdaprodz.com": T("or write to h@hdaprodz.com", "ou escrever para h@hdaprodz.com", "o escribir a h@hdaprodz.com"),
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
