<template>
    <div>
        <img alt="Vue logo" src="../assets/never-tell-me-the-odds.gif">
        <br/>
        <input type="file" id="selectFiles" value="Import"/>
        <br/>
        <button id="import" v-on:click="importCommunication">Upload the empires communication!</button>
        <div v-if="oddsOfSuccess != -1.0">
            <br/>
            Your odds of success are: {{ oddsOfSuccess * 100 }}%
        </div>
    </div>
</template>

<script>
export default {
    name: 'GiveMeTheOdds',
    data: function () {
        return {
            oddsOfSuccess: -1.0
        }
    },
    methods: {
        importCommunication: function () {
            const files = document.getElementById('selectFiles').files;
            if (files.length <= 0) {
                return false;
            }

            const fr = new FileReader();
            fr.onload = this.requestOddsOfSuccess
            fr.readAsText(files.item(0));
        },
        requestOddsOfSuccess: function (file) {
            const result = JSON.parse(file.target.result);

            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(result, null, 2)
            };
            fetch("http://localhost:5000/api/odds-of-success/", requestOptions)
                .then(response => response.json())
                .then(data => (this.oddsOfSuccess = data.odds_of_success));
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
