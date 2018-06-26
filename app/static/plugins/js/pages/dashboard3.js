$(function () {
  'use strict'

  var ticksStyle = {
    fontColor: '#495057',
    fontStyle: 'bold'
  }

  var mode      = 'index'
  var intersect = true

  var $visitorsChart = $('#visitors-chart')
  var visitorsChart  = new Chart($visitorsChart, {
    data   : {
      labels  : ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
      datasets: [{
        type                : 'line',
        data                : [100, 120, 170, 167, 180, 177, 160],
        backgroundColor     : 'transparent',
        borderColor         : '#007bff',
        pointBorderColor    : '#007bff',
        pointBackgroundColor: '#007bff',
        fill                : false
        // pointHoverBackgroundColor: '#007bff',
        // pointHoverBorderColor    : '#007bff'
      },
        {
          type                : 'line',
          data                : [60, 80, 70, 67, 80, 77, 100],
          backgroundColor     : 'tansparent',
          borderColor         : '#ced4da',
          pointBorderColor    : '#ced4da',
          pointBackgroundColor: '#ced4da',
          fill                : false
          // pointHoverBackgroundColor: '#ced4da',
          // pointHoverBorderColor    : '#ced4da'
        }]
    },
    options: {
      maintainAspectRatio: false,
      tooltips           : {
        mode     : mode,
        intersect: intersect
      },
      hover              : {
        mode     : mode,
        intersect: intersect
      },
      legend             : {
        display: false
      },
      scales             : {
        yAxes: [{
          // display: false,
          gridLines: {
            display      : true,
            lineWidth    : '4px',
            color        : 'rgba(0, 0, 0, .2)',
            zeroLineColor: 'transparent'
          },
          ticks    : $.extend({
            beginAtZero : true,
            suggestedMax: 200
          }, ticksStyle)
        }],
        xAxes: [{
          display  : true,
          gridLines: {
            display: true
          },
          ticks    : ticksStyle
        }]
      }
    }
  })

  var $fasterChart = $('#faster-chart')
  var fasterChart  = new Chart($fasterChart, {
    data   : {
      labels  : ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
      datasets: [{
        type                : 'line',
        data                : [100, 70, 170, 60, 180, 77, 35],
        backgroundColor     : 'transparent',
        borderColor         : '#dc3545',
        pointBorderColor    : '#dc3545',
        pointBackgroundColor: '#dc3545',
        fill                : false
        // pointHoverBackgroundColor: '#007bff',
        // pointHoverBorderColor    : '#007bff'
      },
        {
          type                : 'line',
          data                : [60, 80, 70, 67, 80, 77, 100],
          backgroundColor     : 'tansparent',
          borderColor         : '#ced4da',
          pointBorderColor    : '#ced4da',
          pointBackgroundColor: '#ced4da',
          fill                : false,
          pointHoverBackgroundColor: '#6c757d',
           //pointHoverBorderColor    : '#6c757d'
        }]
    },
    options: {
      maintainAspectRatio: false,
      tooltips           : {
        mode     : mode,
        intersect: intersect
      },
      hover              : {
        mode     : mode,
        intersect: intersect
      },
      legend             : {
        display: false
      },
      scales             : {
        yAxes: [{
          // display: false,
          gridLines: {
            display      : true,
            lineWidth    : '4px',
            color        : 'rgba(0, 0, 0, .2)',
            zeroLineColor: 'transparent'
          },
          ticks    : $.extend({
            beginAtZero : true,
            suggestedMax: 200
          }, ticksStyle)
        }],
        xAxes: [{
          display  : true,
          gridLines: {
            display: true
          },
          ticks    : ticksStyle
        }]
      }
    }
  })

  var $errosChart = $('#erros-chart')
  var errosChart  = new Chart($errosChart, {
    data   : {
      labels  : ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
      datasets: [{
        type                : 'line',
        data                : [0, 0, 0, 0, 0, 1, 0],
        backgroundColor     : 'transparent',
        borderColor         : '#dc3545',
        pointBorderColor    : '#dc3545',
        pointBackgroundColor: '#dc3545',
        fill                : false
        // pointHoverBackgroundColor: '#007bff',
        // pointHoverBorderColor    : '#007bff'
      },
        {
          type                : 'line',
          data                : [0, 0, 0, 0, 0, 0, 0],
          backgroundColor     : 'tansparent',
          borderColor         : '#ced4da',
          pointBorderColor    : '#ced4da',
          pointBackgroundColor: '#ced4da',
          fill                : false,
          pointHoverBackgroundColor: '#6c757d',
           //pointHoverBorderColor    : '#6c757d'
        }]
    },
    options: {
      maintainAspectRatio: false,
      tooltips           : {
        mode     : mode,
        intersect: intersect
      },
      hover              : {
        mode     : mode,
        intersect: intersect
      },
      legend             : {
        display: false
      },
      scales             : {
        yAxes: [{
          // display: false,
          gridLines: {
            display      : true,
            lineWidth    : '4px',
            color        : 'rgba(0, 0, 0, .2)',
            zeroLineColor: 'transparent'
          },
          ticks    : $.extend({
            beginAtZero : true,
            suggestedMax: 1
          }, ticksStyle)
        }],
        xAxes: [{
          display  : true,
          gridLines: {
            display: true
          },
          ticks    : ticksStyle
        }]
      }
    }
  })


   var $lotoChart = $('#loto-chart')
  var lotoChart  = new Chart($lotoChart, {
    data   : {
      labels  : ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '!3', '14', '15'],
      datasets: [
         {
          type                : 'line',
          data                : [1,2,3,5,6,8,9,10,12,15,16,17,21,22,25],
          backgroundColor: '#17a2b8',
          borderColor         : '#17a2b8',
          pointBorderColor    : '#17a2b8',
          pointBackgroundColor: '#17a2b8',
          fill                : false,
          label               : "Jogo 99",
          
          // pointHoverBackgroundColor: '#ced4da',
          // pointHoverBorderColor    : '#ced4da'
        },

        {
          type                : 'line',
          data                : [1,2,3,5,8,9,10,11,14,15,16,19,23,24,25],
          backgroundColor     : '#ced4da',
          borderColor         : '#ced4da',
          pointBorderColor    : '#ced4da',
          pointBackgroundColor: '#ced4da',
          fill                : false,
          label               : "Jogo 75",
          // pointHoverBackgroundColor: '#ced4da',
          // pointHoverBorderColor    : '#ced4da'
        },

        {
          type                : 'line',
          data                : [1,2,3,5,8,9,10,11,14,15,17,19,22,23,25],
          backgroundColor     : '#ced4da',
          borderColor         : '#ced4da',
          pointBorderColor    : '#ced4da',
          pointBackgroundColor: '#ced4da',
          fill                : false,
          label               : "Jogo 76",
          // pointHoverBackgroundColor: '#ced4da',
          // pointHoverBorderColor    : '#ced4da'
        },

        {
          type                : 'line',
          data                : [1,2,3,5,6,8,9,10,12,15,19,21,22,23,25],
          backgroundColor     : '#ced4da',
          borderColor         : '#ced4da',
          pointBorderColor    : '#ced4da',
          pointBackgroundColor: '#ced4da',
          fill                : false,
          label               : "Jogo 77",
          // pointHoverBackgroundColor: '#ced4da',
          // pointHoverBorderColor    : '#ced4da'
        },{
        type                : 'line',
        data                : [1,2,3,5,6,7,9,11,12,13,16,17,21,22,23],
        backgroundColor     : '#dc3545',
        borderColor         : '#dc3545',
        pointBorderColor    : '#dc3545',
        pointBackgroundColor: '#dc3545',
        fill                : false,
        label               : "Lotofacil",
        // pointHoverBackgroundColor: '#007bff',
        // pointHoverBorderColor    : '#007bff'
      }
     
        ]
    },
    options: {
      maintainAspectRatio: false,
      tooltips           : {
        mode     : mode,
        intersect: intersect
      },
      hover              : {
        mode     : mode,
        intersect: intersect
      },
      legend             : {
        display: true
      },
      scales             : {
        yAxes: [{
          // display: false,
          gridLines: {
            display      : true,
            lineWidth    : '4px',
            color        : 'rgba(0, 0, 0, .2)',
            zeroLineColor: 'transparent'
          },
          ticks    : $.extend({
            beginAtZero : true,
            suggestedMax: 25
          }, ticksStyle)
        }],
        xAxes: [{
          display  : true,
          gridLines: {
            display: true
          },
          ticks    : ticksStyle
        }]
      }
    }
  })
})
