$(document).ready(function () {
    // Função de envio de cadastro para o banco de dados
    $("#enviarComentario").click(function () {
        // Recuperando dados da página
        Nome = $("#inputNome").val();
        Email = $("#inputEmail").val();
        Telefone = $("#inputTelefone").val();
        Descricao = $("#inputDescricao").val();

        // transforma os dados em um arquivo json
        var dados = JSON.stringify({
            Nome: Nome, Email: Email, Telefone: Telefone, Descricao: Descricao
        });
        // Faz o envio por meio do método ajax
        $.ajax({
            url: 'http://localhost:5000/incluir_comentario', // Endereço do banco de dados
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
                alert("Comentário incluido com sucesso!!");
                // Redireciona para outra página
                location.href = "index.html";
            }
        }
        // Função de erro
        function deuErrado(retorno) {
            // informar mensagem de erro
            alert("ERRO: " + retorno.resultado + ": " + retorno.detalhes);
        }

    });
});