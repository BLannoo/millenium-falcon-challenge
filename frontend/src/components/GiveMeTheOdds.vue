<template>
    <div>
        <img src="../assets/never-tell-me-the-odds.gif">
        <div>
            <label for="selectFile">
                Select the empire communication
            </label>
            <input id="selectFile" type="file" accept="application/JSON"/>
            <button id="importCommunication" v-on:click="importCommunication">
                Upload the empires communication
            </button>
        </div>
        <div v-if="typeof(oddsOfSuccess) === 'number'">
            <p>Your odds of success are: {{ oddsOfSuccess * 100 }}%</p>
        </div>
        <p>{{ errorMessage }}</p>
    </div>
</template>

<script>
export default {
    name: 'GiveMeTheOdds',
    data: function () {
        return {
            oddsOfSuccess: undefined,
            errorMessage: ""
        }
    },
    methods: {
        importCommunication: function () {
            const files = document.getElementById('selectFile').files;
            if (files.length <= 0) {
                return false;
            }

            const fr = new FileReader();
            fr.onload = this.requestOddsOfSuccess
            fr.readAsText(files.item(0));
        },
        requestOddsOfSuccess: function (file) {
            this.oddsOfSuccess = undefined;
            this.errorMessage = "";

            const result = JSON.parse(file.target.result);

            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(result, null, 2)
            };
            fetch("http://localhost:5000/api/odds-of-success/", requestOptions)
                .then(function(response) {
                    if (!response.ok) {
                        throw Error(response.statusText)
                    }
                    return response
                })
                .then(response => response.json())
                .then(data => (this.oddsOfSuccess = data.odds_of_success))
                .catch(() => this.errorMessage = "Is this is a communication from the empire?");
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img {
    border-radius: 40%;
    margin: 50px;
}
label, button {
    background-color:#292354;
    border: none;
    color: white;
    padding: 15px 32px;
    margin: 5px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 1.5em;
    border-radius: 20px;
}
input {
    display: none;
}
p {
    color: white;
    font-size: 2.5em;
}
</style>
