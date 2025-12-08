## Passo 5: Usando o GitHub Copilot em um pull request

Parabéns! Você terminou a codificação deste exercício (e o VS Code). Agora é hora de fazer o merge do nosso trabalho. :tada: Para finalizar, vamos aprender sobre dois recursos do Copilot com acesso limitado que podem acelerar nossos pull requests!

### 📖 Teoria: GitHub Copilot para pull requests

#### Copilot pull request summaries

Normalmente, você revisaria suas anotações e mensagens de commit e as resumiria para a descrição do seu pull request. Isso pode levar algum tempo, especialmente se as mensagens de commit forem inconsistentes ou o código não estiver bem documentado. Felizmente, o Copilot pode considerar todas as mudanças no pull request e fornecer os destaques importantes, e com referências também!

#### Copilot code review

Mais olhos no nosso trabalho é sempre útil, então vamos pedir ao Copilot para fazer uma primeira passagem antes de fazermos o processo normal de revisão por pares. O Copilot é ótimo em detectar erros comuns que são corrigidos com ajustes simples, mas lembre-se de usá-lo de forma responsável.

> [!NOTE]
> Esses recursos estão disponíveis apenas nos planos pagos do **GitHub Copilot**. [[docs]](https://docs.github.com/en/copilot/get-started/plans)

### :keyboard: Atividade: Resumir e revisar um PR com o Copilot

Tanto o **Copilot pull request summaries** quanto o **Copilot code review** têm acesso limitado, então esta atividade é principalmente opcional. Se você não tiver acesso, pule os passos opcionais desta atividade.

1. Em um navegador web, abra outra aba e navegue até seu repositório do exercício.

1. Você pode notar um **banner de notificação** sugerindo criar um novo pull request. Clique nele ou use a aba **Pull Requests** no topo para **criar um novo pull request**. Por favor, use os seguintes detalhes:

   - **base:** `main`
   - **compare:** `accelerate-with-copilot`
   - **title:** `Improve student activity registration system`

1. (Opcional) Na barra de ferramentas da descrição do PR, clique no ícone do **Copilot** e na ação **Summary**. Após um momento, o Copilot adicionará uma descrição baseada nas suas mudanças. :memo:

   <img alt="Botão de resumo do Copilot" width="450px" src="https://github.com/user-attachments/assets/7a712d8b-484d-41df-9353-bc2b397fc1e0">

1. (Opcional) No painel de informações do lado direito, no topo, localize a seção **Reviewers** e clique no botão **Request** ao lado do **ícone do Copilot**. Aguarde um momento para o Copilot adicionar um comentário de revisão ao seu pull request!

   <img alt="Botão de review do Copilot" width="300px" src="https://github.com/user-attachments/assets/39b15002-a235-4c25-b09d-6a8097e27b62">

   > 💡 **Dica:** Note uma entrada de log informando que o Copilot foi solicitado para uma revisão.

1. Na parte inferior, pressione o botão **Merge pull request**. Ótimo trabalho! Você terminou! :tada:

1. Aguarde um momento para a Mona verificar seu trabalho, fornecer feedback e postar uma revisão final deste exercício!
