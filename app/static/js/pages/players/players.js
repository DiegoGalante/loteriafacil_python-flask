_objPerson = new Object();


$(document).ready(function () {
    limpaObjeto();
    carregaPlayers();


    window.actionEvents = {
        'click .edit': function (e, value, row, index) {
            // alert('You click edit icon, row: ' + JSON.stringify(row));
            // // console.log(value, row, index);
            _objPerson = row;
            buttonsVisible(true);
            alteraDados(row)

            $('#tbPlayers').bootstrapTable('remove', {
                field: 'id',
                values: [row.id]
            });
        },
        'click .remove': function (e, value, row, index) {
            alert('You click remove icon, row: ' + JSON.stringify(row));
            console.log(value, row, index);
        }
    };

    // var $table = $('#tbPlayers');
    // $('#toolbar').find('select').change(function () {
    //     $table.bootstrapTable('refreshOptions', {
    //         exportDataType: $(this).val()
    //     });
    // });

    $('#btnCancel').click(function () {

        if ($('#txtName').val() != '' || $('#txtEmail').val() != '') {
            $('#txtName').val('');
            $('#txtEmail').val('');
            $('#chkActive').prop('checked', false);
            _objPerson = null;
            carregaPlayers();
            buttonsVisible(false);
        }


    });

    $('#btnSave').click(function () {

        if (_objPerson != null && $('#txtName').val() != '' && $('#txtEmail').val() != '') {
            _objPerson.name = $('#txtName').val();
            _objPerson.email = $('#txtEmail').val();
            _objPerson.dtCadastro = dataAtualFormatada(_objPerson.dtCadastro);
            _objPerson.active = $('#chkActive')[0].checked;
            console.log(_objPerson);
            savePlayer(_objPerson);

            $('#txtName').val('');
            $('#txtEmail').val('');
            $('#chkActive').prop('checked', false);
        }

        buttonsVisible(false);
    });


});

$(":input").keyup(function (event) {
    buttonsVisible(true);
  });

function limpaObjeto() {
    _objPerson.id = 0;
    _objPerson.name = "";
    _objPerson.email = "";
    _objPerson.dtCadastro = "";
    // _objPerson.dtCadastro = dataAtualFormatada(new Date());
    _objPerson.active = false;
}

function carregaPlayers(player = 0) {
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        async: true,
        url: parseInt(player) === 0 ? '/players' : '/players/' + parseInt(player),
        success: (function (data) {
            $('#tbPlayers').bootstrapTable('load', data.players);
        }),
        error: (function (erro) {
            console.log(erro);
        })
    });
}

function savePlayer(player) {
    console.log(JSON.stringify(player));
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        async: true,
        url: '/savePlayer',
        data: JSON.stringify(player),
        success: (function (obj) {
            limpaObjeto();
            console.log(obj)
            carregaPlayers();
        }),
        error: (function (erro) {
            console.log(erro)
            // console.log(erro);
        })
    });
}


function alteraDados(dados) {
    $('#txtName').val(dados.name);
    $('#txtEmail').val(dados.email);

    $('#chkActive').prop('checked', false);
    if (dados.active === true) {
        $('#chkActive').prop('checked', true);
    }

}

function buttonsVisible(ok = false) {
    if (!ok) {
        $('#btns').addClass("hide");
    }
    else {
        $('#btns').removeClass("hide");
    }
}

function actionFormatter(value, row, index) {
    return [
        '<div style="text-align:center;">',
        '<span class="edit text-info" style="cursor: pointer; margin:10px;" title="Edit">',
        '<i class="fa fa-edit"></i>',
        '</span>',
        // '<span class="remove text-danger" style="cursor: pointer; margin:10px;" title="Remove">',
        // '<i class="fa fa-trash-o"></i>',
        // '</span>',

        '</div>'
    ].join('');
}

function nameFormatter(value, row, index) {
    return [
        '<span id="nameEditable' + row.id + '" data-type="text" data-pk="1" data-name="name">',
        row.name,
        '</span>',
    ].join('');
}

function activeFormatter(value, row, index) {
    if (row.active === true) {
        return [
            '<span class="text-success" title="Ativo">',
            '<i class="fa fa-thumbs-o-up"></i>',
            '</span>',
        ].join('');

    }
    else {
        return [
            '<span class="text-danger" title="Inativo">',
            '<i class="fa fa-thumbs-o-down"></i>',
            '</span>',
        ].join('');
    }
}

function runningFormatter(value, row, index) {
    return index;
}

function formataData(value, row, index) {
    return dataAtualFormatada(row.dtCadastro);
}

function dataAtualFormatada(data) {
    var d = new Date(data);
    return d.toLocaleDateString();

    // var data = new Date(data);
    // var dia = data.getDate();

    // if (dia.toString().length == 1)
    //   dia = "0"+dia;
    // var mes = data.getMonth()+1;
    // if (mes.toString().length == 1)
    //   mes = "0"+mes;
    // var ano = data.getFullYear();  
    // return dia+"/"+mes+"/"+ano;
}


$(function () {
    var $result = $('#tbPlayers');

    $('#eventsTable').on('all.bs.table', function (e, name, args) {
        console.log('Event:', name, ', data:', args);
    })
        .on('click-row.bs.table', function (e, row, $element) {
            $result.text('Event: click-row.bs.table');
        })
        .on('dbl-click-row.bs.table', function (e, row, $element) {
            $result.text('Event: dbl-click-row.bs.table');
        })
        .on('sort.bs.table', function (e, name, order) {
            $result.text('Event: sort.bs.table');
        })
        .on('check.bs.table', function (e, row) {
            $result.text('Event: check.bs.table');
        })
        .on('uncheck.bs.table', function (e, row) {
            $result.text('Event: uncheck.bs.table');
        })
        .on('check-all.bs.table', function (e) {
            $result.text('Event: check-all.bs.table');
        })
        .on('uncheck-all.bs.table', function (e) {
            $result.text('Event: uncheck-all.bs.table');
        })
        .on('load-success.bs.table', function (e, data) {
            $result.text('Event: load-success.bs.table');
        })
        .on('load-error.bs.table', function (e, status) {
            $result.text('Event: load-error.bs.table');
        })
        .on('column-switch.bs.table', function (e, field, checked) {
            $result.text('Event: column-switch.bs.table');
        })
        .on('page-change.bs.table', function (e, number, size) {
            $result.text('Event: page-change.bs.table');
        })
        .on('search.bs.table', function (e, text) {
            $result.text('Event: search.bs.table');
        });
});

