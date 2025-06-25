flowchart TD
    Inicio([Início])
    Validacao{Valida login?}
    Registro[→ Registro]
    Login[→ Login]
    isStaff{is_staff?}
    Dashboard[Dashboard padrão]
    DashboardADM[Dashboard administrativo]

    Operacao{Escolhe operação}
    Transferir[Transferência]
    Comprar[Comprar ação]
    Vender[Vender ação]

    TemSaldoT{Tem saldo para transferir?}
    TemSaldoC{Tem saldo para comprar?}
    TemAcoesV{Tem ações para vender?}

    ExecutaT[Executa transferência]
    ExecutaC[Executa compra]
    ExecutaV[Executa venda]
    
    Falha[Exibe erro]
    Sucesso[Exibe sucesso]

    GerenciarAcoes[Gerenciar ações]
    GerenciarUsuarios[Gerenciar usuários]
    ValidacaoADM[Validação de campos]
    Salvar[Salvar no banco]

    Inicio --> Validacao
    Validacao -- Não --> Registro
    Validacao -- Sim --> Login
    Login --> isStaff
    isStaff -- Sim --> DashboardADM
    isStaff -- Não --> Dashboard

    Dashboard --> Operacao
    Operacao --> Transferir --> TemSaldoT
    Operacao --> Comprar --> TemSaldoC
    Operacao --> Vender --> TemAcoesV

    TemSaldoT -- Sim --> ExecutaT --> Sucesso
    TemSaldoT -- Não --> Falha

    TemSaldoC -- Sim --> ExecutaC --> Sucesso
    TemSaldoC -- Não --> Falha

    TemAcoesV -- Sim --> ExecutaV --> Sucesso
    TemAcoesV -- Não --> Falha

    DashboardADM --> GerenciarUsuarios --> ValidacaoADM --> Salvar
