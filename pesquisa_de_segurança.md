## Escrever um texto explicativo simples e teórico definindo as principais vulnerabilidades de segurança de sistemas (padrão OWASP Top 10) aplicáveis ao mercado, e como as leis da LGPD exigem que os dados de login e CPFs dos funcionários sejam armazenados de forma protegida.

# OWASP Top 10:

# 1.Contole de acesso quebrado
o que e: e quando um sistema não consegue impedir que pessoas mal intecionadas acessendo coisas que não deveria ter acesso isso pode causar ricos de motificação ou destuição de informaçães do sistema

Ex no mercado: como um funcionário do caixa consegue abrir o relatório de salário dos outros colaboradores.

Por que é perigoso: qualquer pessoa pode pular as travas e acessando dados sensívis do sistema.

LGPG e dados de funcionarios: O art.46 da LGPD exige que a empresa adote medidas técnicas e administrativas para proteger dados pessoais contra acesso não autorizados. isso segnifica que qualquer empresa garantir que o sistema apenas de acesso apenas a funcionários autorizado.

# 2.Falhas Criptográficas
o que e: São dados sensíveis que se movem entre sevidores ou são quardados sem criptografia inadequadas e fracas.

Ex no mercado: Senhas de logins de funcionários salvos em texto puro no banco de dados. CPFs trasfegando sem HTTPS entre o sistema do caixa e o servidor

Por que é perigoso: Se algum invasor interceptar a comunicação entre os servidores o invasor pode invadir a qualquer mesangem tento acesso a todo os dados sensíveis das mesangem ou compartilhamento de arquivos.

LGPD e dados de funcionários: No art.46 em quias de pesquisa e recomendato criptografia em trânsito TLS e em amezenados para dados 
