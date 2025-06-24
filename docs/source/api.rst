.. _api:

=======
API
=======

**Autenticação**
----------------

Todos os endpoints da API requerem que o usuário esteja **autenticado**. Utilize o processo de login padrão da aplicação para obter acesso. Requisições feitas sem autenticação ou com autenticação inválida serão rejeitadas.

---

Endpoints para operações com ações:

.. http:get:: /api/stock-info/<int:stock_id>/
   :synopsis: Obtém dados detalhados de uma ação

   **View**: :py:func:`core.views.stock_info`

   Obtém informações atualizadas de uma ação, incluindo preço atual, variação, volume e histórico intradiário.
   Os dados são obtidos da API do Yahoo Finance através da biblioteca Python `yfinance` (`https://pypi.org/project/yfinance/`) e são **armazenados em cache por 15 minutos** para otimizar o desempenho e reduzir chamadas externas.

   **Códigos de Status HTTP**:
      - **200 OK**: Dados da ação retornados com sucesso.
      - **401 Unauthorized**: Não autorizado (autenticação necessária).
      - **404 Not Found**: Ação com o ``stock_id`` fornecido não encontrada.
      - **500 Internal Server Error**: Erro interno do servidor ou falha ao buscar dados da API externa.

   :param stock_id: **(obrigatório)** ID da ação no sistema (ex: ``123``).
   :type stock_id: int
   :returns: Um objeto JSON contendo os dados da ação.
   :rtype: application/json

   **Dados de Retorno (JSON)**:
      - **price** (float): Preço atual da ação.
      - **change** (float): Variação absoluta do preço desde o último fechamento.
      - **change_percent** (float): Variação percentual do preço.
      - **volume** (int): Volume negociado da ação.
      - **history** (array de arrays): Histórico de preços intradiário. Cada sub-array contém:
         - **data** (string, formato ISO 8601): Data e hora do registro (ex: ``"2023-10-01T10:00:00"``).
         - **preço** (float): Preço da ação naquele momento.

   **Exemplo de Resposta Bem-Sucedida (HTTP 200 OK)**:

   .. code-block:: json

      {
       "price": 32.45,
       "change": 1.23,
       "change_percent": 3.94,
       "volume": 1500000,
       "history": [
           ["2023-10-01T10:00:00", 31.50],
           ["2023-10-01T10:05:00", 31.65]
       ]
      }

   **Possível Resposta de Erro (HTTP 404 Not Found)**:

   .. code-block:: json

      {
          "detail": "Não encontrado."
      }

---

.. http:get:: /api/stock-chart/<int:stock_id>/
   :synopsis: Obtém dados simplificados de uma ação para gráficos

   **View**: :py:func:`core.views.stock_info`

   Fornece dados de preço e variação percentual de uma ação, focando em um histórico recente (últimas 4 entradas) e a variação geral, ideal para exibição em gráficos. Os dados são obtidos da API do Yahoo Finance através da biblioteca Python `yfinance` (`https://pypi.org/project/yfinance/`) e são **armazenados em cache por 15 minutos**.

   **Códigos de Status HTTP**:
      - **200 OK**: Dados do gráfico retornados com sucesso.
      - **401 Unauthorized**: Não autorizado (autenticação necessária).
      - **404 Not Found**: Ação com o ``stock_id`` fornecido não encontrada.
      - **500 Internal Server Error**: Erro interno do servidor ou falha ao buscar dados da API externa.

   :param stock_id: **(obrigatório)** ID da ação no sistema (ex: ``123``).
   :type stock_id: int
   :returns: Um objeto JSON com dados para o gráfico.
   :rtype: application/json

   **Dados de Retorno (JSON)**:
      - **hist** (array de arrays): Histórico recente de preços para o gráfico (geralmente as últimas 4 entradas). Cada sub-array contém:
         - **data** (string, formato ISO 8601): Data e hora do registro (ex: ``"2023-10-01T14:00:00"``).
         - **preço** (float): Preço da ação naquele momento.
      - **change** (float): Variação percentual total da ação.

   **Exemplo de Resposta Bem-Sucedida (HTTP 200 OK)**:

   .. code-block:: json

      {
          "hist": [
              ["2023-10-01T14:00:00", 32.10],
              ["2023-10-01T15:00:00", 32.25],
              ["2023-10-01T16:00:00", 32.30],
              ["2023-10-01T17:00:00", 32.45]
          ],
          "change": 3.94
      }

   **Possível Resposta de Erro (HTTP 404 Not Found)**:

   .. code-block:: json

      {
          "detail": "Não encontrado."
      }