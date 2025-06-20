// URLs base da API
const apiContas = 'http://localhost:8000/api/contas/';
const apiTransferencias = 'http://localhost:8000/api/transferencias/';
const apiAcoes = 'http://localhost:8000/api/acoes/';
const apiCompraVenda = 'http://localhost:8000/api/compras-vendas/';
const apiFavoritas = 'http://localhost:8000/api/favoritas/';

/* ======= CONTAS ======= */
async function listarContas() {
    const response = await fetch(apiContas);
    const contas = await response.json();

    const lista = document.getElementById('contas-list');
    if (!lista) return;

    lista.innerHTML = '';
    contas.forEach(conta => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>Conta:</strong> ${conta.numero_conta} | 
            <strong>Saldo:</strong> R$${conta.saldo} | 
            <strong>Usuário ID:</strong> ${conta.usuario} 
            <button onclick="excluirConta(${conta.id})">Excluir</button>
        `;
        lista.appendChild(li);
    });
}

async function adicionarConta() {
    const numeroConta = document.getElementById('numero_conta')?.value;
    const saldo = document.getElementById('saldo')?.value;
    const usuarioId = document.getElementById('usuario_id')?.value;

    if (!numeroConta || !saldo || !usuarioId) {
        alert('Preencha todos os campos para criar uma conta.');
        return;
    }

    const dados = { numero_conta: numeroConta, saldo: saldo, usuario: usuarioId };

    const response = await fetch(apiContas, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });

    if (response.ok) {
        alert('Conta criada com sucesso!');
        listarContas();
    } else {
        alert('Erro ao criar conta. Verifique os dados.');
    }
}

async function excluirConta(id) {
    const response = await fetch(apiContas + id + '/', { method: 'DELETE' });
    if (response.ok) {
        alert('Conta excluída!');
        listarContas();
    } else {
        alert('Erro ao excluir conta.');
    }
}

/* ======= TRANSFERÊNCIAS ======= */
async function listarTransferencias() {
    const response = await fetch(apiTransferencias);
    const transferencias = await response.json();

    const lista = document.getElementById('transferencias-list');
    if (!lista) return;

    lista.innerHTML = '';
    transferencias.forEach(t => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>Remetente:</strong> ${t.remetente} | 
            <strong>Destinatário:</strong> ${t.destinatario} | 
            <strong>Valor:</strong> R$${t.valor} | 
            <strong>Data:</strong> ${new Date(t.data).toLocaleString()}
        `;
        lista.appendChild(li);
    });
}

async function adicionarTransferencia() {
    const remetente = document.getElementById('remetente')?.value;
    const destinatario = document.getElementById('destinatario')?.value;
    const valor = document.getElementById('valor_transferencia')?.value;

    if (!remetente || !destinatario || !valor) {
        alert('Preencha todos os campos para fazer transferência.');
        return;
    }

    const dados = { remetente: remetente, destinatario: destinatario, valor: valor };

    const response = await fetch(apiTransferencias, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });

    if (response.ok) {
        alert('Transferência realizada com sucesso!');
        listarTransferencias();
    } else {
        alert('Erro ao realizar transferência.');
    }
}

/* ======= AÇÕES ======= */
async function listarAcoes() {
    const response = await fetch(apiAcoes);
    const acoes = await response.json();

    const lista = document.getElementById('acoes-list');
    if (!lista) return;

    lista.innerHTML = '';
    acoes.forEach(acao => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>Nome:</strong> ${acao.nome} | 
            <strong>Código:</strong> ${acao.codigo} | 
            <strong>Preço Atual:</strong> R$${acao.preco_atual} | 
            <strong>Atualizado em:</strong> ${new Date(acao.data_atualizacao).toLocaleString()}
        `;
        lista.appendChild(li);
    });
}

/* ======= COMPRA / VENDA DE AÇÕES ======= */
async function listarOperacoes() {
    const response = await fetch(apiCompraVenda);
    const operacoes = await response.json();

    const lista = document.getElementById('operacoes-list');
    if (!lista) return;

    lista.innerHTML = '';
    operacoes.forEach(op => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>Ação ID:</strong> ${op.acao} | 
            <strong>Quantidade:</strong> ${op.quantidade} | 
            <strong>Tipo:</strong> ${op.tipo} | 
            <strong>Data:</strong> ${new Date(op.data).toLocaleString()}
        `;
        lista.appendChild(li);
    });
}

async function adicionarOperacao() {
    const usuario = document.getElementById('usuario_operacao')?.value;
    const acao = document.getElementById('acao_operacao')?.value;
    const quantidade = document.getElementById('quantidade_operacao')?.value;
    const tipo = document.getElementById('tipo_operacao')?.value;

    if (!usuario || !acao || !quantidade || !tipo) {
        alert('Preencha todos os campos para registrar operação.');
        return;
    }

    const dados = { usuario, acao, quantidade, tipo };

    const response = await fetch(apiCompraVenda, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });

    if (response.ok) {
        alert('Operação registrada com sucesso!');
        listarOperacoes();
    } else {
        alert('Erro ao registrar operação.');
    }
}

/* ======= FAVORITAS ======= */
async function listarFavoritas() {
    const response = await fetch(apiFavoritas);
    const favoritas = await response.json();

    const lista = document.getElementById('favoritas-list');
    if (!lista) return;

    lista.innerHTML = '';
    favoritas.forEach(fav => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>Usuário ID:</strong> ${fav.usuario} | 
            <strong>Ação ID:</strong> ${fav.acao}
            <button onclick="removerFavorita(${fav.id})">Remover</button>
        `;
        lista.appendChild(li);
    });
}

async function adicionarFavorita() {
    const usuario = document.getElementById('usuario_favorita')?.value;
    const acao = document.getElementById('acao_favorita')?.value;

    if (!usuario || !acao) {
        alert('Preencha todos os campos para favoritar uma ação.');
        return;
    }

    const dados = { usuario, acao };

    const response = await fetch(apiFavoritas, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });

    if (response.ok) {
        alert('Favorita adicionada!');
        listarFavoritas();
    } else {
        alert('Erro ao adicionar favorita.');
    }
}

async function removerFavorita(id) {
    const response = await fetch(apiFavoritas + id + '/', { method: 'DELETE' });
    if (response.ok) {
        alert('Favorita removida!');
        listarFavoritas();
    } else {
        alert('Erro ao remover favorita.');
    }
}

/* ======= FUNÇÃO PARA INICIALIZAR TODAS LISTAGENS AO CARREGAR A PÁGINA ======= */
function inicializar() {
    listarContas();
    listarTransferencias();
    listarAcoes();
    listarOperacoes();
    listarFavoritas();
}

// Chama inicializar ao carregar a página, se quiser pode chamar isso diretamente no script do HTML também
window.onload = inicializar;
