
document.addEventListener("DOMContentLoaded", function () {

    const tripOptions = document.querySelectorAll(
        'input[name="trip_type"]'
    );

    const returnDateGroup = document.getElementById(
        "return-date-group"
    );

    const departureDate = document.getElementById(
        "departure-date"
    );

    const returnDate = document.getElementById(
        "return-date"
    );

    // Set today's date as the earliest departure date
    const today = new Date();
    const todayString = [
        today.getFullYear(),
        String(today.getMonth() + 1).padStart(2, "0"),
        String(today.getDate()).padStart(2, "0")
    ].join("-");

    departureDate.min = todayString;

    function updateTripType() {

        const selectedTrip = document.querySelector(
            'input[name="trip_type"]:checked'
        );

        if (selectedTrip.value === "round_trip") {

            returnDateGroup.hidden = false;
            returnDate.disabled = false;
            returnDate.required = true;

            updateReturnDateMinimum();

        } else {

            returnDateGroup.hidden = true;
            returnDate.disabled = true;
            returnDate.required = false;
            returnDate.value = "";

        }
    }

    function updateReturnDateMinimum() {

        if (departureDate.value) {

            returnDate.min = departureDate.value;

            if (
                returnDate.value &&
                returnDate.value < departureDate.value
            ) {
                returnDate.value = "";
            }

        }
    }

    // Listen for One Way / Round Trip selection
    tripOptions.forEach(function (option) {

        option.addEventListener("change", updateTripType);

    });

    // Update return date restrictions when departure changes
    departureDate.addEventListener(
        "change",
        updateReturnDateMinimum
    );

    // Set the initial form state
    updateTripType();

});
