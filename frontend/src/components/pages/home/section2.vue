<script setup>

</script>

<template>

  <div class="page-container">
    <!-- Card -->
    <div class="search-card">
      <!-- Search input -->
      <div class="coolinput">
        <label class="text">Ticker symbol</label>
        <input type="text" @input="ticker = ticker.toUpperCase()" placeholder="eg: RELIANCE,TCS ..." class="input" />
      </div>

      <!-- Checkboxes -->
      <div class="checkbox-group">
        <label>
          <input type="checkbox" />
          Qualitative Data
        </label>

        <label>
          <input type="checkbox" />
          Quantitative Data 
        </label>

        <label>
          <input type="checkbox" />
          ValuationModels
        </label>
      </div>
      <!-- button -->
      <div>
        <button id="bottone5">Start Research</button>
      </div>
    </div>
  </div>
</template>


<style scoped>
/* Full page center */
.page-container {
  min-height: 40vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Card */
.search-card {
  width: 420px;
  padding: 30px 32px;
  background: #ffffff;
  border-radius: 14px;
  box-shadow:
    0 10px 25px rgba(0, 0, 0, 0.08),
    0 4px 10px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.search-card > div:last-child {
  display: flex;
  justify-content: center;
  margin-top: auto;
}

/* Input wrapper */
.coolinput {
  display: flex;
  flex-direction: column;
  gap: px;
}

.input {
  text-transform: uppercase;
}

.coolinput .text {
  font-size: 16px;
  font-weight: 800;
  color: #555;
}

.coolinput .input {
  height: 40px;
  padding: 0 12px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 15px;
  outline: none;
  transition: border 0.2s, box-shadow 0.2s;
}

.coolinput .input:focus {
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
}

/* Checkbox group */
.checkbox-group {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 12px;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 15px;
  color: #333;
  cursor: pointer;
}

.checkbox-group input[type="checkbox"] {
  width: 15px;
  height: 15px;
  accent-color: #4f46e5;
}

/* Start research button */
  #bottone5 {
   align-items: center;
   background-color: #58A4B0;
   border: 1px solid rgba(0, 0, 0, 0);
   border-radius: .25rem;
   box-shadow: rgba(0, 0, 0, 0.3) 0 1px 3px 0;
   box-sizing: border-box;
   color: rgba(0, 0, 0, 1);
   cursor: pointer;
   display: inline-flex;
   font-family: system-ui,-apple-system,system-ui,"Helvetica Neue",Helvetica,Arial,sans-serif;
   font-size: 16px;
   font-weight: 600;
   justify-content: center;
   line-height: 1.25;
   min-height: 3rem;
   padding: calc(.875rem - 1px) calc(1.5rem - 1px);
   text-decoration: none;
   transition: all 250ms;
   user-select: none;
   -webkit-user-select: none;
   touch-action: manipulation;
   vertical-align: baseline;
   width: auto;
  }

  #bottone5:hover,
  #bottone5:focus {
   border-color: rgba(0, 0, 0, 0.15);
   box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
   color: rgba(0, 0, 0, 0.8);
  }

  #bottone5:hover {
   transform: translateY(-1px);
  }

  #bottone5:active {
   background-color: #F0F0F1;
   border-color: rgba(0, 0, 0, 0.15);
   box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
   color: rgba(0, 0, 0, 0.7);
   transform: translateY(0);
  }
 </style>