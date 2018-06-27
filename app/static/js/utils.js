var enumConfiguracao = {
    CalcularDezenasSemPontuacao: 1,
    EmailManual: 2,
    ValorMinimoParaEnviarEmail: 3,
    EmailAutomatico: 4,
    VerificaJogoOnline: 5
}

var enumValoresJogos = {
    _15Dezenas: 2.0,
    _16Dezenas: 32.0,
    _17Dezenas: 272.0,
    _18Dezenas: 1632.0
}

function formatNumber(num) {
    return num
        .toFixed(2) // always two decimal digits
        .replace(".", ",") // replace decimal point character with ,
        .replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.") // use . as a separator
}