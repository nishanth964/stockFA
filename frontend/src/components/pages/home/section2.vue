<script setup>

</script>

<template>
    <div class="page-container">
        <div class="coolinput">
            <label for="input" class="text">Ticker symbol:</label>
            <input type="text" placeholder="Type here..." name="input" class="input">
        </div>
    </div>
</template>

<style scoped>
.page-container{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;

}

.coolinput {
    display: flex;
    flex-direction: column;
    width: fit-content;
    position: relative;
    max-width: 240px;
}

.coolinput label.text {
    font-size: 1rem;
    color: #373F51;
    font-weight: 700;
    position: relative;
    top: 0.5rem;
    margin: 0 0 0 7px;
    padding: 0 3px;
    background: #ffffff;
    width: fit-content;
    z-index: 1;
}

.coolinput input[type=text].input {
    padding: 11px 10px;
    font-size: 1rem;
    border: 2px #373F51 solid;
    border-radius: 10px;
    background: transparent;
}

.coolinput input[type=text].input:focus {
    outline: none;
    border-color: #6366F1;
}
</style>