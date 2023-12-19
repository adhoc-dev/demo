odoo.define('demo_tour.multicompany', function(require) {
    "use strict";

    const {_t} = require('web.core');
    const {Markup} = require('web.utils');
    var tour = require('web_tour.tour');
    var tourStepUtils = require('web_tour.TourStepUtils');

    const { markup } = owl;

    const steps =  [tour.stepUtils.showAppsMenuItem(),
        // {
            // trigger: ".o_switch_company_menu > .dropdown-toggle",
            // content: _t("Paso 1: Abrir desplegable"),
            // position: "bottom",
            // edition: "enterprise",
            // run: function (actions) {
            //         location.reload();
            // },
            // async run() {
            //     location.reload();
            //     await new Promise((r) => setTimeout(r, 10000));
            // }
        // },
        // {
        //     trigger: "div[title='Switch to Muebleria SRL']",
        //     content: _t("Paso 2: Seleccionamos compañía muebleria srl"),
        //     position: "bottom",
        //     edition: "enterprise",
        //     run: "click"
        // },
        // {
        //     trigger: ".o_switch_company_menu > .dropdown-toggle",
        //     content: _t("Paso 3: Abrir desplegable"),
        //     position: "bottom",
        //     edition: "enterprise",
        //     run: "click"
        // },
        // {
        //     trigger: ".fa-square-o:before",
        //     content: _t("Paso 4: incorporamos otra compania"),
        //     position: "bottom",
        //     edition: "enterprise",
        //     run: "click"
        // },

    // Paso 1: Seleccione la compania AR Inscripto y quedar ahi parado

    // TODO Probar si funciona y descomentar
    {
        trigger: "body > header > nav > div > div.o-dropdown.dropdown.o_switch_company_menu.d-none.d-md-block.o-dropdown--no-caret > button",
        content: _t("Paso 1: Open multicompany dropdown"),
        position: "bottom",
        edition: "enterprise"
   },
   {
       trigger: ".log_into[aria-label='Switch to (AR) Responsable Inscripto']",
       content: _t("Paso 2: Select (AR) Responsable Inscripto company"),
       position: "bottom",
       edition: "enterprise"
   },

   // Paso 2: Ver que esten seleccionados las otras companias en con la tilde

    // Paso 3: Crear una orden de venta a ADHOC
    {
        trigger: ".o_menuitem[data-menu-xmlid='sale.sale_menu_root']",
        content: _t("Open Sales app to send your first quotation in a few clicks."),
        position: "bottom",
        edition: "enterprise"
    },
    {
        trigger: "button.btn-primary.o_list_button_add",
        content: _t("step 2"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    }, {
        trigger: ".o_field_res_partner_many2one[name='partner_id']",
        extra_trigger: ".o_sale_order",
        content: _t("Write a company name to create one, or see suggestions."),
        position: "right",
        run: function (actions) {
            actions.text("Deco Addict", this.$anchor.find("input"));
        },
    }, {
        trigger: ".ui-menu-item > a:contains('Deco Addict')",
        auto: true,
        in_modal: false,
    }, {
        trigger: ".o_field_x2many_list_row_add > a",
        content: _t("Click here to add some products or services to your quotation."),
        position: "bottom",
    }, {
        trigger: ".o_field_widget[name='product_id'], .o_field_widget[name='product_template_id']",
        extra_trigger: ".o_sale_order",
        content: _t("Select a product, or create a new one on the fly."),
        position: "right",
        run: function (actions) {
            var $input = this.$anchor.find("input");
            actions.text("[FURN_8855] Drawer", $input.length === 0 ? this.$anchor : $input);
            // fake keydown to trigger search
            var keyDownEvent = jQuery.Event("keydown");
            keyDownEvent.which = 42;
            this.$anchor.trigger(keyDownEvent);
            var $descriptionElement = $(".o_form_editable textarea[name='name']");
            // when description changes, we know the product has been created
            $descriptionElement.change(function () {
                $descriptionElement.addClass("product_creation_success");
            });
        },
        id: "product_selection_step"
    }, {
        trigger: "a:contains('[FURN_8855] Drawer')",
        auto: true,
    }, {
        trigger: ".o_field_widget[name='price_unit'] ",
        extra_trigger: ".fa-arrow-right",  // Wait for product creation
        content: Markup(_t("<b>Set a price</b>.")),
        position: "right",
        run: "text 10.0"
    },
    // Paso 4: Validar y confirmar la orden de venta
    {
        trigger: "button[name='action_confirm']",
        content: _t("step 3"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    }, {
        trigger: "button[name='action_view_delivery']",
        content: _t("step 3"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    }, {
        trigger: "button[name='button_validate']",
        content: _t("step 3"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    }, {
        trigger: "button[name='process']",
        content: _t("step 3"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    },
    {
        content: "Breadcrumb back to Bank Reconciliation from INV/2019/00002",
        trigger: ".o_back_button a, .breadcrumb-item:not('.active'):last",
        run: "click"
    },
    // Paso 5: Crear una factura de cliente a partir de esta venta
    // Frenamos acá porque esperamos nuevo desarrollo de cambio de diario en facturas.
    {
        trigger: "button[id='create_invoice']",
        content: _t("step 3"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    },{
        trigger: "button[id='create_invoice_open']",
        content: _t("step 3"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    },
    // Paso 6: Ir y cambiar el diario y sleeccionar un diario de otra compania 
    {
        // trigger: 'button[data-menu-xmlid="account_multicompany_ux.action_account_change_company"]',
        trigger: "button[data-tooltip='Change Company']",
        content: _t("Selecciona lapiz"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    },
    // Paso 7: Guardar la factura.


    // Aqui iria lo del nuevo desarrollo relacionado al nuevo wizard para cambiar de diario 

    // Pasos que siguen:
    // {
    //     trigger: "button[name='action_post']",
    //     content: _t("step 3"),
    //     position: "bottom",
    //     edition: "enterprise",
    //     run: "click"
    // },
 ]
     tour.register("adhoc_tour_multicompany", {
         url: "/web",
         sequence: 20,
     }, steps);
});
