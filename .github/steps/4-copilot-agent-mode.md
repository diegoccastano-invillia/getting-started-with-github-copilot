## Passo 4: Ative o Hiperdrive - Copilot Agent Mode 🚀

### 📖 Teoria: O que é o Copilot Agent Mode?

O [Agent Mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) do Copilot é a próxima evolução na codificação assistida por IA. Atuando como um programador parceiro autônomo, ele executa tarefas de codificação em múltiplos passos ao seu comando.

O Copilot Agent Mode responde a erros de compilação e lint, monitora a saída do terminal e de testes, e auto-corrige em um loop até que a tarefa seja concluída.

#### Edit Mode vs Agent Mode (em resumo)

| Aspecto                  | ✏️ Edit Mode                              | 👩‍🚀 Agent Mode                                                                        |
| ------------------------ | ----------------------------------------- | ------------------------------------------------------------------------------------- |
| Escopo de contexto       | Apenas os arquivos que você adiciona      | Pode ler/adicionar arquivos e recursos adicionais conforme necessário                 |
| Auto-revisão             | Mínima (você conduz a iteração)           | Loop de feedback e retry integrado em erros/falhas                                    |
| Escopo de mudanças       | Altamente focado e cirúrgico              | Mais amplo; pode tocar camadas relacionadas para consistência                         |
| Quando escolher          | Você sabe exatamente o que mudar          | Objetivo é mais amplo ou incerto; requer exploração                                   |
| Chamada de ferramentas   | Nenhuma (você executa comandos manualmente) | Pode invocar ferramentas (ler/editar arquivos, executar comandos, inspecionar terminal e saída de testes) |

#### 🧰 Ferramentas do Agent Mode

O Agent Mode usa ferramentas para realizar tarefas especializadas enquanto processa uma solicitação do usuário. Exemplos de tais tarefas são:

- Encontrar arquivos relevantes para completar seu prompt
- Buscar conteúdo de uma página web
- Executar testes ou comandos de terminal

> [!TIP]
> Enquanto o VS Code fornece muitas ferramentas integradas, você também pode dar ao Agent Mode poderes mais específicos de domínio através de **MCP tools**.
>
> Leia mais sobre [MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) e [GitHub MCP Server](https://github.com/github/github-mcp-server)

Agora, vamos experimentar o **Agent Mode**! 👩‍🚀

### :keyboard: Atividade: Use o Agent Mode para adicionar botões funcionais de "cancelar inscrição"

Vamos experimentar algumas solicitações mais abertas que adicionarão mais funcionalidades à nossa aplicação web.

Se você não obtiver os resultados desejados, pode tentar outros modelos ou fornecer feedback de acompanhamento para refinar os resultados.

1. Abra o painel do **Copilot** Chat e use o menu dropdown para mudar para o modo **Agent**.

   <img width="250" alt="agent mode" src="https://github.com/user-attachments/assets/9bb85530-77a1-4d47-86b2-99769ce197db" />

1. Clique no ícone de **Tools** e explore todas as ferramentas atualmente disponíveis para o Copilot Agent Mode.

   <img width="250"  alt="ícone de tools" src="https://github.com/user-attachments/assets/8f73400a-2647-4b28-b52b-721b8cf348d8" />


1. Hora do nosso teste! Vamos pedir ao Copilot para adicionar funcionalidade para remover participantes.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Por favor, adicione um ícone de deletar ao lado de cada participante e esconda os marcadores de lista.
   > Quando clicado, ele vai cancelar a inscrição daquele participante da atividade.
   > ```

   A ferramenta `#codebase` é usada pelo Copilot para encontrar arquivos relevantes e trechos de código que são relevantes para a tarefa em questão.

   > 🪧 **Nota:** Neste laboratório incluímos explicitamente a ferramenta `#codebase` para obter os resultados mais repetíveis.
   > Sinta-se à vontade para tentar o prompt **sem** `#codebase` e observar se o Agent Mode decide coletar contexto mais amplo do projeto por conta própria.

1. Quando o Copilot terminar, reinicie o debugger e inspecione os resultados. Se você gostar dos resultados, pressione o botão **Keep**. Se não, tente fornecer ao Copilot algum feedback para refinar os resultados.

1. Peça ao Copilot para corrigir um bug de registro.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Eu notei que parece haver um bug.
   > Quando um participante é registrado, a página precisa ser atualizada para ver a mudança na atividade.
   > ```

1. Quando o Copilot terminar, inspecione os resultados. Se você gostar dos resultados, pressione o botão **Keep**. Se não, tente fornecer ao Copilot algum feedback.

### :keyboard: Atividade: Use o Agent Mode para obter cobertura de testes 🧑‍🚀

Seu backend agora está rico em funcionalidades — mas ainda tem zero cobertura de testes. Use o **Agent Mode** do Copilot para adicionar dependências de teste, criar a estrutura inicial de testes e executá-los.

1. Peça ao Copilot no **Agent Mode** para configurar e executar testes para seu backend.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-placeholder?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Adicione testes do FastAPI usando pytest em um novo diretório tests e execute-os.
   > Certifique-se de adicionar quaisquer novas dependências ao requirements.txt
   > ```

1. Enquanto o Copilot trabalha no seu prompt, diferentes ferramentas podem precisar da sua aprovação.

   **🎯 Objetivo: Fazer todos os testes passarem (verde) — mire em uma execução limpa! ✅**

   > 🪧 **Nota:** O Copilot pode resolver isso de uma vez com o prompt inicial ou precisar de mais orientação sua.

1. Assim que os testes estiverem passando - faça o **commit** e **push** de todas as mudanças para seu branch `accelerate-with-copilot` para avançar para o último passo! Quase lá!
