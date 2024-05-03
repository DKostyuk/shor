// order_admin.js
(function ($) {
    $(document).ready(function () {
        console.log('order admin started');
        var cosmetologField = $('#id_cosmetolog');
        var bonusAccountCosmetologField = $('#id_cosmetolog_bonus');

        // Unbind the change event to prevent multiple bindings
        cosmetologField.off('change');

        // Function to update the BonusAccountCosmetolog options based on the selected Cosmetolog
        function updateBonusAccountCosmetologOptions() {
            var selectedCosmetolog = cosmetologField.val();

            bonusAccountCosmetologField.empty();
            var orderNumberElement = document.querySelector('.fieldBox.field-order_number .readonly');
            if (orderNumberElement) {
                var orderNumber = orderNumberElement.textContent;
                console.log('Order number:', orderNumber);
            }
            $.ajax({
                url: '/get_bonus_account_cosmetolog_options/',
                data: {
                    'cosmetolog_id': selectedCosmetolog,
                    'order_id': orderNumber,
                },
                dataType: 'json',
                success: function (data) {
                    console.log('SUPER AJAX SUCCESS');
                    bonusAccountCosmetologField.empty();

                    $.each(data.options, function (id, option) {
                        var optionElement = $('<option>', {
                            value: id,
                            text: option.text
                        });

                        // Check the 'selected' flag and set the option as selected
                        if (option.selected) {
                            optionElement.attr('selected', 'selected');
                        }

                        bonusAccountCosmetologField.append(optionElement);
                    });

                    // Add a default option if needed

                    bonusAccountCosmetologField.prepend($('<option>', {
                        value: '',
                        text: 'Select option 145'
                    }));

                }
            });
        }

        // Bind the change event after unbinding to avoid multiple bindings
        cosmetologField.on('change', function () {
            updateBonusAccountCosmetologOptions();
        });

        // Initial update on page load
        updateBonusAccountCosmetologOptions();
    });
})(django.jQuery);
