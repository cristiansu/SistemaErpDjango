var tablClient;
var modal_title;

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
            {"data": "gender.name"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {

    modal_title = $('.modal-title'); //se usa para dar título al modal

    getData(); //se debe llamar al inicio, sino no aparece el modal

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add'); //significa que al hacer click en el input hidden action (será automático), su valor cambiará a add.
        modal_title.find('span').html('Crear Cliente');
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset(); //se utiliza para limpiar el formulario. el [0] pensando en q limpie los datos del último formulario llenado.
        //se comenta $('form')[0].reset(); para usar el evento shown.bs.modal q hace lo mismo, ambos métodos sirven
        $('#myModalClient').modal('show');
    });

    //significa en id=tabla componente tbody al evento click, componente a ejecutar función
    $('#data tbody').on('click', 'a[rel="edit"]', function() { //al boton editar se le agregó el atributo rel=edit. ver function getData
            modal_title.find('span').html('Editar Cliente');
            modal_title.find('i').removeClass().addClass('fas fa-edit');
            var tr = tablClient.cell($(this).closest('td, li')).index();
            var data = tablClient.row(tr.row).data(); //la función closest es similar a parents significa q traerá todos los datos del componente antipasado tr
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="names"]').val(data.names);
            $('input[name="surnames"]').val(data.surnames);
            $('input[name="dni"]').val(data.dni);
            $('input[name="date_birthday"]').val(data.date_birthday);
            $('input[name="address"]').val(data.address);
            $('select[name="gender"]').val(data.gender.id);
            $('#myModalClient').modal('show');
    })
    $('#data tbody').on('click', 'a[rel="delete"]', function() { 
            var tr = tablClient.cell($(this).closest('td, li')).index();
            var data = tablClient.row(tr.row).data();

            var parameters = new FormData(); //no se usará this pero se pasarán los datos con iteración
            parameters.append('action', 'delete');
            parameters.append('id', data.id);

            submit_with_ajax (window.location.pathname, 'Notificación', '¿Estás seguro de eliminar este registro?',parameters, function (){
                tablClient.ajax.reload();
            });

    });    

    $('#myModalClient').on('shown.bs.modal', function () {
        //$('form')[0].reset();  //se comenta pq se limpia formulario en evento de  .btnAdd
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