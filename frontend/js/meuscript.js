$(function() { // quando o documento estiver pronto/carregado
    
    function exibir_cliente(){
    $.ajax({
        url: 'http://localhost:5000/listar_clientes',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (clientes) {
        // percorrer a lista de pessoas retornadas; 
        $('#corpoTabelaClientes').empty();
        mostrar_conteudo("tabelaClientes")
        for (var i in clientes) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
              '<td>' + clientes[i].username + '</td>' + 
              '<td>' + clientes[i].password + '</td>' + 
              '<td>' + clientes[i].name + '</td>' + 
              '<td>' + clientes[i].email + '</td>' + 
              '<td>' + clientes[i].cpf + '</td>' + 
              '<td>' + clientes[i].rg + '</td>' + 
              '<td>' + clientes[i].celular + '</td>' + 
              '<td>' + clientes[i].endereco + '</td>' +           

              '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaClientes').append(lin);
        }
    }

}

// função que mostra um conteúdo e esconde os outros
    function mostrar_conteudo(identificador) {
    // esconde todos os conteúdos
    $("#tabelaClientes").addClass('invisible');
    $("#conteudoInicial").addClass('invisible');
    // torna o conteúdo escolhido visível
    $("#"+identificador).removeClass('invisible');      
}

// código para mapear o click do link Listar
$(document).on("click", "#linkListarClientes", function() {
    exibir_clientes();
});

// código para mapear click do link Inicio
$(document).on("click", "#linkInicio", function() {
    mostrar_conteudo("conteudoInicial");
});

// código para mapear click do botão incluir pessoa
$(document).on("click", "#btIncluirCliente", function() {
    //pegar dados da tela
    nome_de_usuario = $("#campoUsername").val();
    senha = $("#campoPassword").val();
    nome = $("#campoName").val();
    email = $("#campoEmail").val();
    cpf = $("#campoCpf").val();
    rg = $("#campoRg").val();
    celular = $("#campoCelular").val();
    endereco = $("#campoEndereco").val();


    // preparar dados no formato json
    var dados = JSON.stringify({ nome_de_usuario: username, senha: senha, nome: name, email: email, cpf: cpf, rg: rg, celular: celular, endereco: endereco });
    // fazer requisição para o back-end
    $.ajax({
        url: 'http://localhost:5000/incluir_cliente',
        type: 'POST',
        dataType: 'json', // os dados são recebidos no formato json
        contentType: 'application/json', // tipo dos dados enviados
        data: dados, // estes são os dados enviados
        success: clienteIncluido, // chama a função listar para processar o resultado
        error: erroAoIncluir
    });
    function clienteIncluido (retorno) {
        if (retorno.resultado == "ok") { // a operação deu certo?
            // informar resultado de sucesso
            alert("Cliente incluído com sucesso!");
            // limpar os campos
            
            $("#campoUsername").val("");
            $("#campoPassword").val("");
            $("#campoName").val("");
            $("#campoEmail").val("");
            $("#campoCpf").val("");
            $("#campoRg").val("");
            $("#campoCelular").val("");
            $("#campoEndereco").val("");
        } else {
            // informar mensagem de erro
            alert(retorno.resultado + ":" + retorno.detalhes);
        }            
    }
    function erroAoIncluir (retorno) {
        // informar mensagem de erro
        alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
    }
});

// código a ser executado quando a janela de inclusão de pessoas for fechada
$('#modalIncluirClienta').on('hide.bs.modal', function (e) {
    // se a página de listagem não estiver invisível
    if (! $("#tabelaClientes").hasClass('invisible')) {
        // atualizar a página de listagem
        exibir_clientes();
    }
});

// a função abaixo é executada quando a página abre
mostrar_conteudo("conteudoInicial");
});
