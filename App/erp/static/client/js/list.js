var tablClient;

function getData() {
    tablClient = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "names"},
            {"data": "surnames"},
            {"data": "dni"},
            {"data": "date_birthday"},
            {"data": "gender"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {

    getData(); //se debe llamar al inicio, sino no aparece el modal

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add'); //significa que al hacer click en el input hidden action (será automático), su valor cambiará a add.
        //$('form')[0].reset(); //se utiliza para limpiar el formulario. el [0] pensando en q limpie los datos del último formulario llenado.
        //se comenta $('form')[0].reset(); para usar el evento shown.bs.modal q hace lo mismo, ambos métodos sirven
        $('#myModalClient').modal('show');
    });

    $('#myModalClient').on('shown.bs.modal', function () {
        $('form')[0].reset();
    });

    
    $('form').on('submit', function (e) {
        e.preventDefault(); //corta la secuencia por defecto, en este caso evitará que se guarde el nuevo registro categoría

        var parameters = new FormData(this);

        submit_with_ajax (window.location.pathname, 'Notificación', '¿Estás seguro de agregar este registro?',parameters, function (){
            //location.reload(); para refrescar sólo la tabla y no toda la página se usará la función creada getData
            $('#myModalClient').modal('hide'); //es para cerrar el modal con evento hide
            //getData(); se comenta para usar el método de datatable ajax.reload()
            tablClient.ajax.reload();

        });

    });
});