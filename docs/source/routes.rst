.. _rotas:

=========
Endpoints
=========

.. http:get:: /login/
   :synopsis: Tela de login
   
   **View**: :py:class:`django.contrib.auth.views.LoginView`

.. http:get:: /register/
   :synopsis: Tela de registro
   
   **View**: :py:func:`core.views.register`

.. http:get:: /transfer/
   :synopsis: Tela de transferência
   
   **View**: :py:func:`core.views.make_transfer`

.. http:get:: /api/stock-info/<int:stock_id>/
   :synopsis: Dados em tempo real de uma ação via API
   
   **View**: :py:func:`core.views.stock_info`
   
   :param stock_id: ID da ação
   :returns: JSON com preço, variação e histórico

.. http:get:: /trade/
   :synopsis: Lista de ações disponíveis
   
   **View**: :py:func:`core.views.stock_list`

.. http:get:: /trade/<int:stock_id>/
   :synopsis: Página de negociação de ação
   
   **View**: :py:func:`core.views.operate_stock`
   
   :param stock_id: ID da ação

.. http:post:: /trade/<int:stock_id>/
   :synopsis: Executa compra/venda de ação
   
   **View**: :py:func:`core.views.operate_stock`

.. http:get:: /api/stock-info/<int:stock_id>/
   :synopsis: Endpoint de API para dados da ação
   
   **View**: :py:func:`core.views.stock_info`

.. http:get:: /trades/history/
   :synopsis: Histórico de trades do usuário
   
   **View**: :py:func:`core.views.trade_history`

.. http:post:: /favorite/<int:stock_id>/
   :synopsis: Adiciona/remove favorito
   
   **View**: :py:func:`core.views.toggle_favorite_stock`

.. http:post:: /favorite-list/<int:stock_id>/
   :synopsis: Alterna favorito na lista
   
   **View**: :py:func:`core.views.toggle_favorite_stock_list`

.. http:post:: /toggle-theme/
   :synopsis: Alterna tema claro/escuro
   
   **View**: :py:func:`core.views.toggle_theme`

.. http:get:: /
   :synopsis: Dashboard principal
   
   **View**: :py:func:`core.views.dashboard`