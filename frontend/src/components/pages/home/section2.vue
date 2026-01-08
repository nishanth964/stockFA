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
          Income Statement
        </label>

        <label>
          <input type="checkbox" />
          Balance Sheet
        </label>

        <label>
          <input type="checkbox" />
          Cash Flow
        </label>
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

/* Input wrapper */
.coolinput {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.input {
  text-transform: uppercase;
}

.coolinput .text {
  font-size: 14px;
  font-weight: 500;
  color: #555;
}

.coolinput .input {
  height: 42px;
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
  flex-direction: column;
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
  width: 18px;
  height: 18px;
  accent-color: #4f46e5;
}

 </style>