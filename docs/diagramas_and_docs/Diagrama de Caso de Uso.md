
## 🛠️ Guia para DCU - Controlasso

### 1. Defina os Atores do Sistema

* **Usuário Comum**: cadastra conta, transfere dinheiro, negocia ações, visualiza dashboards.
* **Administrador (ADM)**: gerencia ações, usuários, acessa relatórios.
* **Sistema Externo**: serviço de cotação de ações (por exemplo, `yfinance`).

---

### 2. Liste os Casos de Uso

1. **Cadastrar-se**: criar conta com dados iniciais.
2. **Login / Logout**: autenticar usuário no sistema.
3. **Visualizar Dashboard**: ver saldo, histórico, carteira de ações.
4. **Transferir Valores**: enviar dinheiro entre contas.
5. **Comprar Ação**: selecionar ação, quantidade e confirmar compra.
6. **Vender Ação**: selecionar ação da carteira e confirmar venda.
7. **Marcar Ação como Favorita**: adicionar à lista pessoal.
8. **Desmarcar Favorita**: remover da lista favorita.
9. **Visualizar Histórico de Transações**: ver entradas e saídas.
10. **Visualizar Histórico de Ações**: acompanhar histórico individual.
11. **Cadastrar/Editar/Remover Ação**: realizado pelo ADM.
12. **Gerenciar Usuários**: ADM cria, edita ou exclui usuários.
13. **Atualizar Preço das Ações**: via agente automático ou manual, usando dados externos.

---

### 3. Relacione Atores e Casos de Uso

| Caso de Uso                   | Usuário Comum | ADM | Sistema Externo |
| ----------------------------- | :-----------: | :-: | :-------------: |
| Cadastrar-se                  |       ✔       |     |                 |
| Login / Logout                |       ✔       |  ✔  |                 |
| Visualizar Dashboard          |       ✔       |  ✔  |                 |
| Transferir Valores            |       ✔       |     |                 |
| Comprar / Vender Ação         |       ✔       |     |                 |
| Marcar/Desmarcar Favorita     |       ✔       |     |                 |
| Visualizar Históricos         |       ✔       |  ✔  |                 |
| Cadastrar/Editar/Remover Ação |               |  ✔  |                 |
| Gerenciar Usuários            |               |  ✔  |                 |
| Atualizar Preço das Ações     |               |     |        ✔        |

---

### 4. Organização Visual no DCU

* Atores posicionados externamente.
* No lado esquerdo: **Usuário Comum** (laço circundando seus casos).
* No lado direito: **Administrador**, com casos ADMIN específicos.
* **Sistema externo** no topo.
* Use flechas ou linhas conectando atores aos casos.

---

### 5. Detalhe (Opcional) – Notas por Caso de Uso

Exemplo:
**Comprar Ação**

* **Pré-condições:** usuário logado e saldo suficiente.
* **Fluxo principal:**

  1. Seleciona ação
  2. Define quantidade
  3. Confirma operação
  4. Sistema debita saldo e adiciona ação na carteira
* **Fluxo alternativo:** saldo insuficiente → exibe mensagem de erro.

Repita esse nível de detalhe para casos críticos.

---

### 6. Ferramentas sugeridas

* **draw\.io** ou **diagrams.net**
* **Lucidchart**
* **Astah Community**
* **Visual Paradigm**

---

### 7. Entrega

✅ Inclua o diagrama exportado (PNG ou PDF) em `docs/casos_de_uso/`.
✅ Documente os fluxos (pré-condições, exceções e pós-condições) de pelo menos os casos principais.

---

Se quiser, posso criar um diagrama visual com base nessas instruções ou gerar os fluxos detalhados com descrição para cada caso de uso. Só falar! 🚀
