odoo.define('demo_tour.sale_tour', function(require) {
    "use strict";

    const {_t} = require('web.core');
    const {Markup} = require('web.utils');
    var tour = require('web_tour.tour');

    const { markup } = owl;

    const steps =  [tour.stepUtils.showAppsMenuItem(), {
        trigger: ".o_menuitem[data-menu-xmlid='sale.sale_menu_root']",
        content: _t("Open Sales app to send your first quotation in a few clicks."),
        position: "bottom",
        edition: "enterprise"
    }, {
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
            actions.text("[E-COM11] Cabinet with Doors", $input.length === 0 ? this.$anchor : $input);
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
        trigger: "a:contains('[E-COM11] Cabinet with Doors')",
        auto: true,
    }, {
        trigger: ".o_field_widget[name='price_unit'] ",
        extra_trigger: ".fa-arrow-right",  // Wait for product creation
        content: Markup(_t("<b>Set a price</b>.")),
        position: "right",
        run: "text 10.0"
    }, {
        trigger: "button[name='action_confirm']",
        content: _t("step 3"),
        position: "bottom",
        edition: "enterprise",
        run: "click"
    },
]
    tour.register("adhoc_tour_sale", {
        url: "/web",
        rainbowMan: true,
        sequence: 20,
    }, steps);
});

