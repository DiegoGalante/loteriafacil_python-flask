_bgcolorGray = "bg-gray";
_bgcolorInfo11_12 = "bg-info";
_bgcolorWarning13 = "bg-warning";
_bgcolorSuccess14 = "bg-success";
_bgcolorDanger15 = "bg-danger";

_colorGray = "#ced4da";
_colorInfo11_12 = "#17a2b8";
_colorWarning13 = "#ffc107";
_colorSuccess14 = "#28a745";
_colorDanger15 = "#dc3545";

_objPrincipal = new Object();
var _lotoChart = null;

$(document).ready(function () {
  carregaPagina();

  $("#concurseSearch").click(function () {
    carregaPagina($("#txtConcurse").val());
  });

  $("#btn-checkOnline").click(function () {
    divCarregando(true);
    num_concurse = 0
    try {
      num_concurse = parseInt($("#txtConcurse").val());
    } catch (error) {
      num_concurse = 0;
    }

    checkOnline(num_concurse);
  });

  $("#btn-email").click(function () {

    if (_objPrincipal != null && _objPrincipal.configuration != null && _objPrincipal.configuration.person > 0) {
      divCarregando(true);
      sendEmail();
    }

  });

  $(":input").keyup(function (event) {
    if (event.which == 13) {
      carregaPagina($("#txtConcurse").val());
    }
  });

  //CARREGA O GRAFICO
  //FIM - GRAFICO

  $('[data-toggle="popover"]').popover();
});

Number.prototype.toFixedDown = function (digits) {
  var n = this - Math.pow(10, -digits) / 2;
  n += n / Math.pow(2, 53); // added 1360765523: 17.56.toFixedDown(2) === "17.56"
  return n.toFixed(digits);
}

function calcPorcentagem(dezenas) {
  // campo.attr('style', "width: " + ();
  // campo.attr('title', ((dezenas * 100) / 15).toFixedDown(2) + "% de acerto.");
  return ((dezenas * 100) / 15);
}


//FUNÇÕES
function carregaPagina(concurse = 0) {
  $('#gamePerson').text("");
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    async: true,
    url: parseInt(concurse) === 0 ? '/load' : '/load/' + parseInt(concurse),
    success: (function (data) {
      _objPrincipal = data;

      if (!parseInt(concurse)) {
        $("#txtConcurse").val('');
      } else {
        $("#txtConcurse").val(data.concurse.concurse);
      }

      $("#concurseHeader").text("Concurso " + data.concurse.concurse + " - " + data.concurse.dtConcurse)
      $("#concurseHeader").attr('title', data.concurse.dtExtense);

      atualizaPontos(15, data.concurse.hit15, data.concurse.shared15, data.concurse.percent15);
      atualizaPontos(14, data.concurse.hit14, data.concurse.shared14, data.concurse.percent14);
      atualizaPontos(13, data.concurse.hit13, data.concurse.shared13, data.concurse.percent13);
      atualizaPontos(12, data.concurse.hit12, data.concurse.shared12, data.concurse.percent12);
      atualizaPontos(11, data.concurse.hit11, data.concurse.shared11, data.concurse.percent11);

      montaGrafico(data.concurse.game, []);

      loadGames();
    }),
    error: (function (erro) {
      console.log(erro);
    })
  });
}

function checkOnline(check_game = 0) {
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    async: true,
    url: '/checkOnline/' + check_game,
    data: JSON.stringify(_objPrincipal),
    success: (function (data) {
      divCarregando(false);
      if (data.return) {
        carregaPagina();
      }
      else {
        // console.log(data.msg);
      }

    }),
    error: (function (erro) {
      divCarregando(false);
      console.log(erro);
    })
  });
}

function loadGames() {
  divListaJogosCarregando(true);
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    async: true,
    url: '/loadGames',
    data: JSON.stringify(_objPrincipal),
    success: (function (data) {
      divListaJogosCarregando(false);
      if (data.return) {
      }
      else {
        // console.log(data.msg);
      }
      if (data.personGame.length == undefined)
        data.personGame = []

      // console.log(data)
      _objPrincipal.personGame = data.personGame;
      _objPrincipal.concurse.amount_tickets = data.amount_tickets;

      // console.log(_objPrincipal.personGame)

      // data.concurse.amount_tickets = 1000000;
      $("#amount_ticket").prop('style', 'font-size: 25px;');
      if (_objPrincipal.concurse.amount_tickets > 0) {
        $("#amount_ticket").addClass("text-success")

        $("#amount_ticket").text("R$ " + formatNumber(_objPrincipal.concurse.amount_tickets) + " ")
        $("#amount_ticket").append("<i class='fa fa-thumbs-o-up' title='Parabéns ;)'></i>");
      } else {
        $("#amount_ticket").removeClass("text-success");
        $("#amount_ticket").text("R$ " + formatNumber(_objPrincipal.concurse.amount_tickets))
      }

      listaJogos(_objPrincipal.personGame);
      montaGrafico(_objPrincipal.concurse.game, _objPrincipal.personGame);

    }),
    error: (function (erro) {
      divListaJogosCarregando(false);
      console.log(erro);
    })
  });
}

function sendEmail() {
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    async: true,
    url: '/sendEmail',
    data: JSON.stringify(_objPrincipal),
    success: (function (data) {
      divCarregando(false);
      // console.log(data)
      if (data.return) {
        var divEmail = $("#divEmail");
        var btnEmail = $("#btn-email");


        btnEmail.addClass("hide");
        divEmail.fadeIn(1000);
        divEmail.val(data.msg)
        divEmail.removeClass("hide");

        setInterval(function () {
          divEmail.hide(1250, function () {
            divEmail.addClass("hide");
            divEmail.get(0).style.display = '';
            // btnEmail.removeClass("hide");
          });
        }, 3100);
      }
      else {
        console.log(data.msg);
      }

    }),
    error: (function (erro) {
      divCarregando(false);
      console.log(erro);
    })
  });
}


function divCarregando(mostrar = false) {
  if (mostrar) {
    $("#divCarregando").removeClass("hide");
  }
  else {
    $("#divCarregando").addClass("hide");
  }
}

function divListaJogosCarregando(mostrar = false) {
  if (mostrar) {
    $("#divCarregandoJogos").removeClass("hide");
  }
  else {
    $("#divCarregandoJogos").addClass("hide");
  }
}

function listaJogos(jogadores) {

  $('#gamePerson').text("");
  $("#pontuationStats").removeClass("hide");
  if (jogadores.length == 0) {
    $("#hasGame").addClass("hide");
    $("#noGame").removeClass("hide");
  }
  else {

    _colorGame = "";

    html = "";

    divGroup = "<div class='progress-group'>";
    fechaDiv = "</div>";
    divProgress = "<div class='progress progress-sm active'>";

    for (i = 0; i < jogadores.length; i++) {
      html = "";
      switch (jogadores[i].hits) {
        case 15:
          _colorGame = _bgcolorDanger15;
          break;
        case 14:
          _colorGame = _bgcolorSuccess14;
          break;
        case 13:
          _colorGame = _bgcolorWarning13;
          break;
        case 12:
        case 11:
          _colorGame = _bgcolorInfo11_12;
          break;
        default:
          _colorGame = _bgcolorGray;
          break;
      }
      html += divGroup;

      if (jogadores[i].hits > 10) {
        popoverGroup = "<a href='#' title='Autor' data-toggle='popover' data-trigger='hover' data-placement='left' data-content='" + jogadores[i].name + " - R$ " + formatNumber(jogadores[i].amount) + "'>Jogo  #" + jogadores[i].id + "</a> - <strong>" + jogadores[i].hits + "</strong> dezenas sorteadas!";
      }
      else {
        popoverGroup = "<a title='Autor' data-toggle='popover' data-trigger='hover' data-placement='left' data-content='" + jogadores[i].name + "'>Jogo  #" + jogadores[i].id + "</a> - " + jogadores[i].hits + " dezenas sorteadas!";
      }

      html += popoverGroup;
      spanGroup = "<span class='float-right'><b><span class='badge " + _colorGame + "'>" + jogadores[i].hits + "</span></b> / <span class='badge bg-danger'>15</span></span>";
      html += spanGroup;
      html += divProgress;
      progressBar = "<div class='progress-bar " + _colorGame + " progress-bar-striped' role='progressbar' aria-valuenow='11' aria-valuemin='0' aria-valuemax='15' title='" + calcPorcentagem(jogadores[i].hits) + "% de acerto!'  style='width: " + calcPorcentagem(jogadores[i].hits) + "%;' id='progressBar" + jogadores[i].id + "'>";
      html += progressBar;
      html += fechaDiv;
      html += fechaDiv;
      html += fechaDiv;
      $('#gamePerson').append(html);
      $('[data-toggle="popover"]').popover();
    }

    $("#noGame").addClass("hide");
    $("#divCarregandoJogos").addClass("hide");
    $("#hasGame").removeClass("hide");
  }
  // $("#pontuationStats").removeClass("hide");
  divListaJogosCarregando()
}

function formatNumber(num) {
  return num
    .toFixed(2) // always two decimal digits
    .replace(".", ",") // replace decimal point character with ,
    .replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.") // use . as a separator
}

function atualizaPontos(pontuation, hit, shared, percent) {
  success = "text-success";
  danger = "text-danger";
  warning = "text-warning";
  up = "<i class='fa fa-caret-up'></i>";
  down = "<i class='fa fa-caret-down'></i>";
  same = "<i class='fa fa-caret-left'></i>";

  popoverContent = "";

  txtPercent = "";
  if (percent == 0) {
    $("#percent" + pontuation).addClass(warning);
    popoverContent = "Mesmo valor que concurso passado!";
    txtPercent = same;
  } else if (percent < 0) {
    $("#percent" + pontuation).addClass(danger);
    txtPercent = down;
    popoverContent = Math.abs(percent) + "% Menor que o concurso passado!";
  } else {
    $("#percent" + pontuation).addClass(success);
    txtPercent = up;
    popoverContent = Math.abs(percent) + "% Maior que o concurso passado!";
  }

  switch (hit) {
    case 0:
      $("#hit" + pontuation).text("Ninguém acertou")
      break;
    case 1:
      $("#hit" + pontuation).text(hit + " Ganhador")
      break;
    default:
      $("#hit" + pontuation).text(hit + " Ganhadores")
      break;
  }
  try {
    $("#shared" + pontuation).text("R$ " + formatNumber(shared));
    $("#percent" + pontuation).text(Math.abs(percent) + "% ");
    $("#percent" + pontuation).append(txtPercent);
    $("#percent" + pontuation)[0].dataset.content = popoverContent;
  } catch (error) {

  }

}

function montaGrafico(lot_game, personGame) {
  $("#divCarregandoGraph").addClass("hide")
  $("#chart").removeClass("hide")

  'use strict'

  var ticksStyle = {
    fontColor: '#495057',
    fontStyle: 'bold'
  }

  var mode = 'index'
  var intersect = true

  var dataSetPersonGameChart = [];

  var $lotoChart = "";
  $lotoChart = $('#loto-chart');
  for (i = 0; i < personGame.length; i++) {
    if (personGame.length > 0) {
      colorPersonGame = "";
      switch (personGame[i].hits) {
        case 15:
          colorPersonGame = _colorDanger15;
          break;
        case 14:
          colorPersonGame = _colorSuccess14;
          break;
        case 13:
          colorPersonGame = _colorWarning13;
          break;
        case 12:
        case 11:
          colorPersonGame = _colorInfo11_12;
          break;
        default:
          colorPersonGame = _colorGray;
          break;
      }
      dataSetPersonGameChart.push(
        {
          type: 'line',
          steppedLine: false,
          data: personGame[i].game.split('-'),
          backgroundColor: colorPersonGame,
          borderColor: colorPersonGame,
          pointBorderColor: colorPersonGame,
          pointBackgroundColor: colorPersonGame,
          fill: false,
          label: "Jogo #" + personGame[i].id,
          // borderDash: [5, 5],
        }
      );
    }
  }

  dataSetPersonGameChart.push(
    {
      type: 'line',
      steppedLine: false,
      data: lot_game.split('-'),
      backgroundColor: _colorDanger15,
      borderColor: _colorDanger15,
      pointBorderColor: _colorDanger15,
      pointBackgroundColor: _colorDanger15,
      fill: false,
      label: "Lotofacil",
      pointStyle: 'star',
      pointRadius: 15,
      // pointBorderColor: 'rgb(0, 0, 0)'
      // pointHoverBackgroundColor: '_colorDanger15',
      // pointHoverBorderColor    : '_colorDanger15'
    }
  )

  if (_lotoChart != null) {
    _lotoChart.destroy();
  }

  _lotoChart = new Chart($lotoChart, {
    data: {
      labels: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15'],

      datasets: dataSetPersonGameChart
    },
    options: {
      responsive: true,
      title: {
        display: true,
        text: String.format('{0} : {1}', 'Loto Fácil', _objPrincipal.concurse.game),
        fontSize: 18,
      },
      maintainAspectRatio: false,
      tooltips: {
        mode: mode,
        intersect: intersect,
        position: 'nearest',
      },
      hover: {
        mode: mode,
        intersect: intersect
      },
      legend: {
        display: true,
        position: 'bottom'
      },
      elements: {
        line: {
          // tension : 0.000001,
          tension: 0.4,
        }
      },
      scales: {
        yAxes: [{
          // display: false,
          gridLines: {
            display: true,
            lineWidth: '4px',
            color: 'rgba(0, 0, 0, .2)',
            zeroLineColor: 'transparent'
          },
          ticks: $.extend({
            beginAtZero: true,
            suggestedMax: 25
          }, ticksStyle)
        }],
        xAxes: [{
          display: true,
          gridLines: {
            display: true
          },
          ticks: ticksStyle
        }]
      }
    }
  })
}

if (!String.format) {
  String.format = function (format) {
    var args = Array.prototype.slice.call(arguments, 1);
    return format.replace(/{(\d+)}/g, function (match, number) {
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
        ;
    });
  };
}
//FIM FUNÇÕES

// $('#myButton').on('click', function () {
//   var $btn = $(this).button('loading')
//   // business logic...
//   $btn.button('reset')
// })


{/* <div class="col-md-8 pull-right" style="
    text-align: right;
">
    <i class="fa fa-gears"></i> Configurações

</div> */}

jQuery("#loto-chart").attr("tabindex", -1).focus();