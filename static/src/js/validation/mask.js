$(document).ready(function () {
    var $cpf = $("#CPF");
    $cpf.mask('000.000.000-00', {reverse: true});
    var $zip_code = $("#CEP");
    $zip_code.mask('99.999-999', {reverse: true});
  });
