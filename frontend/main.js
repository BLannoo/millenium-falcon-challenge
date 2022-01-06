var app = new Vue({
    el: '#app',
    data: {
        oddsOfSuccess: 0.0
    },
    methods: {
        importCommunication: function () {
            const files = document.getElementById('selectFiles').files;
            if (files.length <= 0) {
                return false;
            }

            const fr = new FileReader();

            fr.onload = e => {
                const result = JSON.parse(e.target.result);

                const requestOptions = {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(result, null, 2)
                };
                fetch("/odds-of-success/", requestOptions)
                    .then(response => response.json())
                    .then(data => (this.oddsOfSuccess = data.odds_of_success));
            }
            fr.readAsText(files.item(0));
        }
    }
})
