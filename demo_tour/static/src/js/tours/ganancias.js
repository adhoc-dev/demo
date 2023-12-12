odoo.define('demo_tour.sale_tour', function(require) {
    "use strict";

    const {_t} = require('web.core');
    const {Markup} = require('web.utils');
    var tour = require('web_tour.tour');

    const { markup } = owl;

    const steps =  [

        // 1. Dirigirse al menú “Pagos de Proveedor”
        // 2. Crear un nuevo pago de proveedor.
        // 3. Seleccionar el proveedor “ADHOC SA“.
        // 4. Verificar en el pago que se trae por defecto el número de régimen configurando en la data demo. Que seria el 21
        // 5. Congigurar store “Shared Store (No company)” (no es realmente necesario para el test, pero si nom nos deja continuar para guardar el pago)
        // 6. Ir a la pestana deudas, y limpiar el campo to_pay_move_line_ids
        // 7. Modificar capo auste avances y colocar monto 100.000
        // 8. Dar click en el boton Calular Retenciones
        // 9. Verificar que se agrego una linea de pago que se llama Retenciones de Gananias Aplicada
        // 10. Verificar dentro de la linea de retencion (pop up de la linea de pago)
        //     10.a Importe Base de Retención 100000
        //     10.b Importe a cuenta sujeto a retención 100000
        //     10.c Importe total 100000
        //     10.d Base no Imponible 7.870,00
        //     10.e Importe Base de Retención 92.130,00
        //     10.f Retención del periodo 5.527,80
        //     10.g Importe de retención calculado 5.527,80
        // 11. Regresar a la vista del grupo de pago y dar al boton Validar

        // 12. Ir al menu “Liq. de Impuestos”
        // 13. Ir a la tarjetita que dice “Liquidación SICORE Aplicado (ARS) (Muebleria SRL)”
        // 14. Dar click en “2 Líneas a liquidar”
        // 15. Seleciconamos todos los elementos de la vista lista
        // 16. Vamos al menu accion y damos click en la opcion “Liquidacion de Impuestos”
        // 17. Damos click en el boton CONFIRMAR
        // 18. Dar click en  el stat bottom que se llama "Descargar Archivo de Liquidación"
        // 19. Seleccionar “SICORE Aplicado.txt​​​”
        // 20. Dar click en “SICORE Aplicado.txt” para descargar el archivo
        // 21. EXTRA Ver que se genero o descargo el archivo (opcional)
        // 22. Salir de los los 2 pop up. Regresar al journal entry y dar click en publicar.

//     const steps =  [tour.stepUtils.showAppsMenuItem(), {
//         trigger: ".o_menuitem[data-menu-xmlid='sale.sale_menu_root']",
//         content: _t("Open Sales app to send your first quotation in a few clicks."),
//         position: "bottom",
//         edition: "enterprise"
//     }, {
//         trigger: "button.btn-primary.o_list_button_add",
//         content: _t("step 2"),
//         position: "bottom",
//         edition: "enterprise",
//         run: "click"
//     }, {
//         trigger: ".o_field_res_partner_many2one[name='partner_id']",
//         extra_trigger: ".o_sale_order",
//         content: _t("Write a company name to create one, or see suggestions."),
//         position: "right",
//         run: function (actions) {
//             actions.text("Deco Addict", this.$anchor.find("input"));
//         },
//     }, {
//         trigger: ".ui-menu-item > a:contains('Deco Addict')",
//         auto: true,
//         in_modal: false,
//     }, {
//         trigger: ".o_field_x2many_list_row_add > a",
//         content: _t("Click here to add some products or services to your quotation."),
//         position: "bottom",
//     }, {
//         trigger: ".o_field_widget[name='product_id'], .o_field_widget[name='product_template_id']",
//         extra_trigger: ".o_sale_order",
//         content: _t("Select a product, or create a new one on the fly."),
//         position: "right",
//         run: function (actions) {
//             var $input = this.$anchor.find("input");
//             actions.text("[E-COM11] Cabinet with Doors", $input.length === 0 ? this.$anchor : $input);
//             // fake keydown to trigger search
//             var keyDownEvent = jQuery.Event("keydown");
//             keyDownEvent.which = 42;
//             this.$anchor.trigger(keyDownEvent);
//             var $descriptionElement = $(".o_form_editable textarea[name='name']");
//             // when description changes, we know the product has been created
//             $descriptionElement.change(function () {
//                 $descriptionElement.addClass("product_creation_success");
//             });
//         },
//         id: "product_selection_step"
//     }, {
//         trigger: "a:contains('[E-COM11] Cabinet with Doors')",
//         auto: true,
//     }, {
//         trigger: ".o_field_widget[name='price_unit'] ",
//         extra_trigger: ".fa-arrow-right",  // Wait for product creation
//         content: Markup(_t("<b>Set a price</b>.")),
//         position: "right",
//         run: "text 10.0"
//     }, {
//         trigger: "button[name='action_confirm']",
//         content: _t("step 3"),
//         position: "bottom",
//         edition: "enterprise",
//         run: "click"
//     },
// ]

    tour.register("adhoc_tour_ganancias", {
        url: "/web",
        rainbowMan: true,
        sequence: 20,
    }, steps);
});

