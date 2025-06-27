# Introducão ao Git e Github

### O que é o Git?

O Git é um sistema de controle de versão que permite que você acompanhe mudanças feitas em arquivos ao longo do tempo, podendo colaborar com outras pessoas e voltar a versões anteriores do seu projeto, caso necessário.

### O que é o Github?

É uma plataforma online que hospeda os repositórios Git. Ele facilita o compartilhamento, a colaboração e a contribuição em projetos com outras pessoas pela internet.

### Comandos Básicos do Git

- git init - Inicializa um novo repositório Git.
- git [URL] - Faz uma cópia de um repositório remoto.
- git add [arquivo] - Adiciona arquivos ao índice para serem commitados.
- git commit -m "mensagem"** - Salva as alterações no histórico do repositório.
- git status - Verifica o estado arquivos no repositório.
- git log - Exibe o histórico de commits.
- git branch - Lista, cria ou exclui branches.
- git checkout [branch] - Alterna entre branches ou restaura arquivos.
- git merge [branch] - Mescla branches.
- git pull - Atualiza o repositório local com alterações do remoto.
- git push - Envia mudanças do repositório local para o remoto.

## Convenção dos commits
A covenção dos commits é uma forma padronizada de mensagens de commit que facilita a leitura por humanos e ferramentas automatizadas.
- feat: adiciona um novo recurso (corresponde a uma versão minor)
- fix: corrige um bug (corresponde a uma versão patch)
- docs: mudanças na documentação
- style: mudanças de formatação (espaços, ponto e vírgula etc.)
- refactor: refatoração de código sem alterar comportamento
- test: adição ou modificação de testes
- build: mudanças em arquivos de build ou dependências
- ci: alterações em configurações de integração contínua
- chore: tarefas diversas que não afetam o código de produção
- perf: melhorias de performance
