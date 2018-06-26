_objConfiguration = new Object();
_objSaveConfiguration = new Object();
_valor_antigo = 0;

var imported = document.createElement('script');
imported.src = '/static/js/utils.js';
document.head.appendChild(imported);

$(document).ready(function () {
    carregaConfiguracao();
});

function carregaConfiguracao() {
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        async: true,
        url: '/loadConfiguration',
        success: (function (data) {
            _objConfiguration = data.configuracao
            _valor_antigo = _objConfiguration.min_amount_to_send_email
            // console.log(_objConfiguration);

            $('#CalcularDezenasSemPontuacao').prop('checked', false);
            $('#VerificaJogoOnline').prop('checked', false);
            $('#EmailAutomatico').prop('checked', false);
            $('#EmailManual').prop('checked', false);
            $('#minAmountToSentEmail').val('')

            if (_objConfiguration.calculate_tens_without_success === true) {
                $('#CalcularDezenasSemPontuacao').prop('checked', true);
            }

            if (_objConfiguration.check_game_online === true) {
                $('#VerificaJogoOnline').prop('checked', true);
            }

            if (_objConfiguration.send_email_automatically === true) {
                $('#EmailAutomatico').prop('checked', true);
            }

            if (_objConfiguration.send_email_manually === true) {
                $('#EmailManual').prop('checked', true);
            }

            if (_objConfiguration.min_amount_to_send_email > 0) {
                novo_valor = Number(parseFloat(_objConfiguration.min_amount_to_send_email)).toFixed(2);
                $("#minAmountToSentEmail").val(novo_valor);
            }

            validateConfiguration();
        }),
        error: (function (erro) {
            console.log(erro)
        })
    });
}

function validateConfiguration() {
    try {
        if (_objConfiguration.check_game_online === true) {
            $('#btn-checkOnline').removeClass('hide');
        }
        else {
            $('#btn-checkOnline').addClass('hide');
        }

        if (_objConfiguration.send_email_manually === true) {
            $('#btn-email').removeClass('hide');
        }
        else {
            $('#btn-email').addClass('hide');
        }
    } catch (error) {

    }


}

function saveConfig(new_config) {
    console.log(JSON.stringify(new_config));
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        async: true,
        url: '/saveConfiguration',
        data: JSON.stringify(new_config),
        success: (function (obj) {
            if (obj.result) {
                limpaObjetoNovaCofiguracao();
            }
            carregaConfiguracao();
        }),
        error: (function (erro) {
            console.log(erro)
            // TrataErroAjax(erro);
        })
    });
}

function limpaObjetoNovaCofiguracao() {
    _objSaveConfiguration.config_id = 0;
    _objSaveConfiguration.pes_id = 0;
    _objSaveConfiguration.valor_campo = 0;
    _objSaveConfiguration.enum_config = 0;
}


$("#minAmountToSentEmail").keydown(function (e) {

    if (e.currentTarget.value.length >= 2 && e.currentTarget.value[0] == 0) {
        console.log(e.currentTarget.value)
        e.currentTarget.value = e.currentTarget.value.slice(1, e.currentTarget.value.length)
        $("#minAmountToSentEmail").val(e.currentTarget.value);
    }
    // Allow: backspace, delete, tab, escape, enter and .
    if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
        // Allow: Ctrl/cmd+A
        (e.keyCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
        // Allow: Ctrl/cmd+C
        (e.keyCode == 67 && (e.ctrlKey === true || e.metaKey === true)) ||
        // Allow: Ctrl/cmd+X
        (e.keyCode == 88 && (e.ctrlKey === true || e.metaKey === true)) ||
        // Allow: home, end, left, right
        (e.keyCode >= 35 && e.keyCode <= 39)) {
        // let it happen, don't do anything
        return;
    }
    // Ensure that it is a number and stop the keypress
    if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
        e.preventDefault();
    }
});

$("#minAmountToSentEmail").blur(function () {

    novo_valor = Number(parseFloat($("#minAmountToSentEmail").val())).toFixed(2);

    $("#minAmountToSentEmail").val(novo_valor);

    _objSaveConfiguration.config_id = _objConfiguration.id
    _objSaveConfiguration.pes_id = _objConfiguration.person
    _objSaveConfiguration.valor_campo = parseFloat(novo_valor);
    _objSaveConfiguration.valor_antigo = _valor_antigo;
    _objSaveConfiguration.enum_config = enumConfiguracao.ValorMinimoParaEnviarEmail;

    console.log(_objSaveConfiguration)
    saveConfig(_objSaveConfiguration);
});

$('#CalcularDezenasSemPontuacao').click(function () {
    _objSaveConfiguration.config_id = _objConfiguration.id
    _objSaveConfiguration.pes_id = _objConfiguration.person
    _objSaveConfiguration.valor_campo = $('#CalcularDezenasSemPontuacao')[0].checked;
    _objSaveConfiguration.enum_config = enumConfiguracao.CalcularDezenasSemPontuacao;

    console.log(_objSaveConfiguration)
    saveConfig(_objSaveConfiguration);
});

$('#VerificaJogoOnline').click(function () {
    _objSaveConfiguration.config_id = _objConfiguration.id
    _objSaveConfiguration.pes_id = _objConfiguration.person
    _objSaveConfiguration.valor_campo = $('#VerificaJogoOnline')[0].checked;
    _objSaveConfiguration.enum_config = enumConfiguracao.VerificaJogoOnline;

    console.log(_objSaveConfiguration)
    saveConfig(_objSaveConfiguration);
});

$('#EmailAutomatico').click(function () {
    _objSaveConfiguration.config_id = _objConfiguration.id
    _objSaveConfiguration.pes_id = _objConfiguration.person
    _objSaveConfiguration.valor_campo = $('#EmailAutomatico')[0].checked;
    _objSaveConfiguration.enum_config = enumConfiguracao.EmailAutomatico;

    saveConfig(_objSaveConfiguration);
});

$('#EmailManual').click(function () {
    _objSaveConfiguration.config_id = _objConfiguration.id
    _objSaveConfiguration.pes_id = _objConfiguration.person
    _objSaveConfiguration.valor_campo = $('#EmailManual')[0].checked;
    _objSaveConfiguration.enum_config = enumConfiguracao.EmailManual;

    saveConfig(_objSaveConfiguration);
});




