.. _api:

=======
API
=======

Endpoints RESTful para operações com ações:

.. http:get:: /api/stock-info/<int:stock_id>/
   :synopsis: Obtém dados detalhados de uma ação
   
   **View**: :py:func:`core.views.stock_info`
   
   :param stock_id: ID da ação no sistema
   :returns: JSON com:
      - price: Preço atual
      - change: Variação absoluta
      - change_percent: Variação percentual
      - volume: Volume negociado
      - history: Array com histórico de preços

Exemplo de resposta:

.. code-block:: json

   {
    "price": 32.45,
    "change": 1.23,
    "change_percent": 3.94,
    "volume": 1500000,
    "history": [["2023-10-01T10:00:00", 31.50]]
    }
