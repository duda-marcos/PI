$(document).ready(function () {
    // Retorno de dados dos agendamentos
    // Chamada do metodo ajax para consultar o back-end
    $.ajax({
        // Chamando o back-end
        url: 'http://localhost:5000/listar_comentarios',
        // Metodo Get para buscar dados
        method: 'GET',
        // Tipo de dados que receberá
        dataType: 'json',
        // Caso não tenha erros, executará a função listar_agendamentos
        success: listar_comentarios,
        // Em caso de erro, imprimirá a mensagem
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });
    // Função que será chamada caso o back-end seja chamado com sucesso
    // Função que coloca os dados em uma tabela
    function listar_comentarios(comentarios) {
        // Variável que armagenará os dados que serão impressos
        linhas = ''
        // For que lerá item por item da tabela agendamentos
        for (var i in comentarios) {
            // Criando a variavel auxiliar
            // Na variavel lin se controi o que seria um código html junto das variáveis vindas da tabela
            lin = '<div class="product-box">' +
                '<button type="button" class="btn btn-danger icon-del" onclick="deletar(' + comentarios[i].Id + ')">' +
                '<i class="bx bx-trash"></i>' +
                '</button>' +
                '<div class="product-details">' +
                '<p class="p-name">' + comentarios[i].Nome + '</p>' +
                '<span class="p-price">' + comentarios[i].Descricao + '</span>' +
                '</div>' +
                '</div>';

            // Adicionando a variavel lin a variavel que será impressa na tabela
            linhas = linhas + lin;
        };
        // Adicionando as informações na tabela
        $('#comentariosPostados').append(linhas);
    };
});

function deletar(key) {
    // transforma os dados em um arquivo json
    var dados = JSON.stringify({
        Id: key
    });
    // Faz o envio por meio do método ajax
    $.ajax({
        url: 'http://localhost:5000/deletar_comentario', // Endereço do banco de dados
        type: 'POST', // O tipo POST é o de envio, enquanto GET é o de recuperação de dados
        dataType: 'json', // Tipo de arquivo que será enviado
        contentType: 'application/json', // tipo dos dados enviados
        data: dados, // estes são os dados enviados
        success: deuCerto, // Mostra uma mensagem indicando o sucesso na operação e limpa o formulário
        error: deuErrado // Caso de erro, mostra uma mensagem indicando o tal
    });
    // Função de sucesso
    function deuCerto(retorno) {
        // Se o back-end retornar ok, procede com tais funções
        if (retorno.resultado == "ok") {
            // Alerta que teve sucesso
            alert("Comentário apagado com sucesso!!");
            // Redireciona para outra página
            location.reload();
        }
    }
    // Função de erro
    function deuErrado(retorno) {
        // informar mensagem de erro
        alert("ERRO: " + retorno.resultado + ": " + retorno.detalhes);
    }

};