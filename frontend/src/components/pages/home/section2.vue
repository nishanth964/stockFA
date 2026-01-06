<script setup>

</script>

<template>

    <div class="page-container">
        <!-- Card -->
        <div class="search-card">
            <!-- Search input -->
            <div class="coolinput">
                <label class="text">Ticker symbol</label>
                <input type="text" placeholder="AAPL, MSFT..." class="input" />
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
    <button>
    <div class="svg-wrapper-1">
      <div class="svg-wrapper">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          width="24"
          height="24"
        >
          <path fill="none" d="M0 0h24v24H0z"></path>
          <path
            fill="currentColor"
            d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"
          ></path>
        </svg>
      </div>
    </div>
    <span>Send</span>
  </button>
</template>


<style scoped>
/* Card */
.search-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 28px 28px;
    width: 500px;
    box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
}

/* Input */
.coolinput {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
}

.coolinput label.text {
    font-size: 0.9rem;
    font-weight: 600;
    color: #373f51;
    margin-bottom: 6px;
}

.coolinput .input {
    padding: 12px;
    font-size: 1rem;
    border: 2px solid #373f51;
    border-radius: 10px;
}

.coolinput .input:focus {
    outline: none;
    border-color: #6366f1;
}

/* Checkboxes */
.checkbox-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.checkbox-group label {
    font-size: 0.95rem;
    color: #373f51;
    display: flex;
    gap: 8px;
    align-items: center;
}

button {
    font-family: inherit;
    font-size: 20px;
    background: royalblue;
    color: white;
    padding: 0.7em 1em;
    padding-left: 0.9em;
    display: flex;
    align-items: center;
    border: none;
    border-radius: 16px;
    overflow: hidden;
    transition: all 0.2s;
    cursor: pointer;
  }

  button span {
    display: block;
    margin-left: 0.3em;
    transition: all 0.3s ease-in-out;
  }

  button svg {
    display: block;
    transform-origin: center center;
    transition: transform 0.3s ease-in-out;
  }

  button:hover .svg-wrapper {
    animation: fly-1 0.6s ease-in-out infinite alternate;
  }

  button:hover svg {
    transform: translateX(1.2em) rotate(45deg) scale(1.1);
  }

  button:hover span {
    transform: translateX(5em);
  }

  button:active {
    transform: scale(0.95);
  }

  @keyframes fly-1 {
    from {
      transform: translateY(0.1em);
    }

    to {
      transform: translateY(-0.1em);
    }
  }
</style>