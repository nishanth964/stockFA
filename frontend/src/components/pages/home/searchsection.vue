<script setup></script>

<template>
  <div class="page-container">
    <div class="coolinput">
        <label for="input" class="text">Ticker symbol:</label>
        <input type="text" placeholder="Write here..." name="input" class="input">
    </div>
  </div>  
</template>

<style scoped>
  .page-container {
    display: flex;
    justify-content: center; 
    align-items: center;     
    min-height: 100vh;       
    width: 100%;
    background-color: #f0f2f5; 
  }

  .coolinput {
    display: flex;
    flex-direction: column;
    width: fit-content;
    position: relative;
    max-width: 240px;
  }

  .coolinput label.text {
    font-size: 0.75rem;
    color: #818CF8;
    font-weight: 700;
    position: relative;
    top: 0.5rem;
    margin: 0 0 0 7px;
    padding: 0 3px;
    background: #e8e8e8;
    width: fit-content;
    z-index: 1;
  }

  .coolinput input[type=text].input {
    padding: 11px 10px;
    font-size: 0.75rem;
    border: 2px #818CF8 solid;
    border-radius: 5px;
    background: transparent;
  }

  .coolinput input[type=text].input:focus {
    outline: none;
    border-color: #6366F1;
  }
</style>
