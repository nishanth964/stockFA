<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    const ticker = ref('');
    const qualitative = ref(false);
    const quantitative = ref(false);
    const valuation = ref(false);

    const startResearch = () => {
      const options = {
        qualitative: qualitative.value,
        quantitative: quantitative.value,
        valuation: valuation.value,
      };
      router.push({ path: '/results', query: { ticker: ticker.value, ...options } });
    };

    return {
      ticker,
      qualitative,
      quantitative,
      valuation,
      startResearch,
    };
  },
};
</script>

<template>
  <section>
    <div class="content">
      <!--Background pattern-->
      <div class="container"></div>
      <!--Logo -->
      <header id="header">
        <div class="logo-container">
          <img src="/homepagelogo.png" alt="STOCKFA Logo" class="logo" />
        </div>
      </header>

      <!-- GitHub Button -->
      <a
        href="https://github.com/nishanth964/stockFA"
        target="_blank"
        rel="noopener noreferrer"
        class="btn-github"
      >
        <svg width="24" height="24" viewBox="0 0 16 16" fill="none">
          <path
            d="M7.99992 1.33331C7.12444 1.33331 6.25753 1.50575 5.4487 1.84078C4.63986 2.17581 3.90493 2.66688 3.28587 3.28593C2.03563 4.53618 1.33325 6.23187 1.33325 7.99998C1.33325 10.9466 3.24659 13.4466 5.89325 14.3333C6.22659 14.3866 6.33325 14.18 6.33325 14C6.33325 13.8466 6.33325 13.4266 6.33325 12.8733C4.48659 13.2733 4.09325 11.98 4.09325 11.98C3.78659 11.2066 3.35325 11 3.35325 11C2.74659 10.5866 3.39992 10.6 3.39992 10.6C4.06659 10.6466 4.41992 11.2866 4.41992 11.2866C4.99992 12.3 5.97992 12 6.35992 11.84C6.41992 11.4066 6.59325 11.1133 6.77992 10.9466C5.29992 10.78 3.74659 10.2066 3.74659 7.66665C3.74659 6.92665 3.99992 6.33331 4.43325 5.85998C4.36659 5.69331 4.13325 4.99998 4.49992 4.09998C4.49992 4.09998 5.05992 3.91998 6.33325 4.77998C6.85992 4.63331 7.43325 4.55998 7.99992 4.55998C8.56659 4.55998 9.13992 4.63331 9.66659 4.77998C10.9399 3.91998 11.4999 4.09998 11.4999 4.09998C11.8666 4.99998 11.6333 5.69331 11.5666 5.85998C11.9999 6.33331 12.2533 6.92665 12.2533 7.66665C12.2533 10.2133 10.6933 10.7733 9.20659 10.94C9.44659 11.1466 9.66659 11.5533 9.66659 12.1733C9.66659 13.0666 9.66659 13.7866 9.66659 14C9.66659 14.18 9.77325 14.3933 10.1133 14.3333C12.7599 13.44 14.6666 10.9466 14.6666 7.99998C14.6666 7.1245 14.4941 6.25759 14.1591 5.44876C13.8241 4.63992 13.333 3.90499 12.714 3.28593C12.0949 2.66688 11.36 2.17581 10.5511 1.84078C9.7423 1.50575 8.8754 1.33331 7.99992 1.33331V1.33331Z"
            fill="currentcolor"
          ></path>
        </svg>
        <span>View on Github</span>
      </a>

      <!-- Dark Theme Button -->
      <div class="dark-theme-toggle">
        <input id="darkmode-toggle" type="checkbox" />
        <label for="darkmode-toggle">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            class="sun"
          >
            <g transform="translate(0 512) scale(.1 -.1)">
              <path
                d="m2513 5105c-59-25-63-46-63-320 0-266 4-288 54-315 33-17 79-17 112 0 50 27 54 49 54 315 0 275-4 295-65 321-42 17-51 17-92-1z"
              ></path>
              <path
                d="m754 4366c-28-28-34-41-34-77 0-42 3-45 188-231l187-188h47c39 0 52 5 77 31 26 25 31 38 31 77v47l-188 187c-186 185-189 188-231 188-36 0-49-6-77-34z"
              ></path>
              <path
                d="m4058 4212-188-187v-47c0-39 5-52 31-77 25-26 38-31 77-31h46l188 188c186 186 188 188 188 231 0 36-6 49-34 77s-41 34-77 34c-42 0-45-3-231-188z"
              ></path>
              <path
                d="m2440 4224c-453-50-760-192-1056-488-264-264-419-570-475-936-17-109-17-371 0-480 56-366 211-672 475-936s570-419 936-475c109-17 371-17 480 0 366 56 672 211 936 475 225 225 358 455 438 758 38 143 50 249 50 418 0 219-30 388-104 590-137 372-450 719-813 901-143 72-315 128-474 154-89 15-329 26-393 19zm335-235c305-46 582-186 805-409 567-567 567-1473 0-2040s-1473-567-2040 0-567 1473 0 2040c328 328 777 476 1235 409z"
              ></path>
              <path
                d="m54 2651c-20-12-37-34-44-55-16-49 2-101 44-127 28-17 52-19 279-19 268 0 289 4 317 54 17 33 17 79 0 112-28 50-49 54-317 54-227 0-251-2-279-19z"
              ></path>
              <path
                d="m4512 2657c-73-41-73-155 0-193 21-11 81-14 275-14 227 0 251 2 279 19 42 26 60 78 44 127-7 21-24 43-44 55-28 17-52 19-281 19-181-1-256-4-273-13z"
              ></path>
              <path
                d="m908 1062c-185-186-188-189-188-231 0-36 6-49 34-77s41-34 77-34c43 0 45 2 231 188l188 188v46c0 39-5 52-31 77-25 26-38 31-77 31h-47l-187-188z"
              ></path>
              <path
                d="m3901 1219c-26-25-31-38-31-77v-47l188-187c186-185 189-188 231-188 36 0 49 6 77 34s34 41 34 77c0 43-2 45-188 231l-188 188h-46c-39 0-52-5-77-31z"
              ></path>
              <path
                d="m2540 663c-87-28-90-37-90-330 0-227 2-251 19-279 40-66 142-66 182 0 17 28 19 52 19 279 0 266-4 291-52 314-32 16-60 22-78 16z"
              ></path>
            </g>
          </svg>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            class="moon"
          >
            <g transform="translate(0 512) scale(.1 -.1)">
              <path
                d="m2090 5105c-248-51-443-118-659-226-514-256-909-652-1161-1163-94-191-139-311-185-490-127-500-110-999 51-1468 133-389 331-706 624-998 403-404 875-642 1460-736 147-24 529-24 693 0 539 78 981 283 1390 644 362 319 647 793 766 1270 46 186 56 256 42 299-22 71-80 116-151 117-73 1-104-19-181-116-307-390-733-627-1233-689-119-14-385-7-501 15-582 106-1066 469-1321 991-120 246-171 452-181 731-21 586 230 1126 695 1493 96 75 117 107 117 177 0 85-67 155-153 160-26 1-76-3-112-11zm110-149c0-2-26-23-57-47-81-60-254-230-325-318-213-264-353-573-415-916-22-126-25-508-5-625 62-346 195-651 395-910 72-93 228-250 327-329 266-213 571-349 930-413 117-20 499-17 625 5 343 62 652 202 916 415 88 71 258 244 318 325 24 32 46 56 48 54s-8-60-23-128c-127-606-501-1155-1027-1505-780-521-1798-535-2602-36-295 183-594 482-777 777-335 539-445 1180-308 1795 138 621 515 1158 1060 1511 136 88 374 201 530 253 148 49 390 106 390 92z"
              ></path>
            </g>
          </svg>
        </label>
      </div>
      <div class="page-container">
        <!-- Card -->
        <div class="search-card">
          <!-- Search input -->
          <div class="coolinput">
            <label class="text">Ticker symbol</label>
            <input
              type="text"
              placeholder="eg: RELIANCE,TCS ..."
              v-model="ticker"
              @keyup.enter="startResearch"
              class="input"/>
          </div>
          <!-- Checkboxes -->
          <div class="checkbox-group">
            <label>
              <input type="checkbox" v-model="qualitative" />
              Qualitative Data
            </label>

            <label>
              <input type="checkbox" v-model="quantitative" />
              Quantitative Data
            </label>

            <label>
              <input type="checkbox" v-model="valuation" />
              Valuation Models
            </label>
          </div>
          <!-- button -->
          <div>
            <button id="bottone5" @click="startResearch">Start Research</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Global font and reset */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

* {
  box-sizing: border-box;
}

body {
  font-family: 'Inter', sans-serif;
  margin: 0;
  padding: 0;
}

/* Background pattern */
.container {
  position: fixed;
  top: 0;
  left: 0;
  min-height: 100vh;
  width: 100%;
  height: 100%;
  --color: #e1e1e1;
  background-color: #f3f3f3;
  background-image: linear-gradient(
      0deg,
      transparent 24%,
      var(--color) 25%,
      var(--color) 26%,
      transparent 27%,
      transparent 74%,
      var(--color) 75%,
      var(--color) 76%,
      transparent 77%,
      transparent
    ),
    linear-gradient(
      90deg,
      transparent 24%,
      var(--color) 25%,
      var(--color) 26%,
      transparent 27%,
      transparent 74%,
      var(--color) 75%,
      var(--color) 76%,
      transparent 77%,
      transparent
    );
  background-size: 60px 60px;
  z-index: -1;
  transition: background-color 0.3s ease;
}

/* Dark mode background */
.dark-mode .container {
  --color: #444;
  background-color: #1a1a1a;
}

/* Logo */
#header {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px 0;
  height: 300px;
}

.logo {
  height: 750px; /* Increased from 80px for bigger logo */
  filter: drop-shadow(5px 5px 5px rgba(0.5, 0.5, 0.5, 0.5));
  transition: transform 0.3s ease;
}

/* GitHub Button */
.btn-github {
  position: fixed;
  filter: drop-shadow(5px 5px 5px rgba(1, 0.5, 0.5, 1));
  top: 20px;
  left: 20px;
  z-index: 1000;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  font-size: 0.825rem;
  font-weight: 800;
  color: #ffffff;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 100px;
  box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.04),
    inset 0 0 0 1px rgba(255, 255, 255, 0.04);
  transition: all 0.3s ease;
}

.btn-github:hover {
  background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
  box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.08),
    inset 0 0 1 1px rgba(252, 232, 3, 0.08);
  transform: translateY(-0.25rem);
}

/* Dark Theme Toggle */
.dark-theme-toggle {
  position: fixed;
  filter: drop-shadow(5px 5px 5px rgba(0.5, 0.5, 0.5, 0.5));
  top: 20px;
  right: 20px;
  z-index: 1000;
}

.dark-theme-toggle:hover {
  transform: translateY(-0.3rem);
}

.dark-theme-toggle input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.dark-theme-toggle label {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 46px;
  height: 46px;
  background: rgb(233, 227, 227);
  border: 1px solid #1a1818;
  border-radius: 10px;
  cursor: pointer;
  position: relative;
  transition: all 0.5s;
}

.dark-theme-toggle label:active {
  border-radius: 5px;
}

.dark-theme-toggle label svg {
  position: absolute;
  width: 20px;
  transition: opacity 0.3s;
  z-index: 1;
}

.dark-theme-toggle label .moon {
  fill: #000;
  opacity: 1;
}

.dark-theme-toggle label .sun {
  width: 24px;
  fill: #fff;
  opacity: 0;
}

.dark-theme-toggle input:checked + label {
  background: #4a6cf7;
}

.dark-theme-toggle input:checked + label .moon {
  opacity: 0;
}

.dark-theme-toggle input:checked + label .sun {
  opacity: 1;
}

/* Full page center */
.page-container {
  min-height: 40vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

/* Card */
.search-card {
  width: 100%;
  max-width: 600px;
  padding: 30px 32px;
  background: #ffffff;
  border-radius: 14px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08), 0 4px 10px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 24px;
  z-index: 1000;
  transition: transform 0.3s ease;
}

.search-card:hover {
  transform: translateY(-5px);
}

.search-card > div:last-child {
  display: flex;
  justify-content: center;
  margin-top: auto;
}

/* Dark mode card */
.dark-mode .search-card {
  background: #2a2a2a;
  color: #fff;
}

/* Input wrapper */
.coolinput {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input {
  text-transform: uppercase;
}

.coolinput .text {
  font-size: 16px;
  font-weight: 800;
  color: #555;
}

.dark-mode .coolinput .text {
  color: #ccc;
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
  flex-wrap: wrap;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 15px;
  color: #333;
  cursor: pointer;
  transition: color 0.2s ease;
}

.checkbox-group label:hover {
  color: #4f46e5;
}

.dark-mode .checkbox-group label {
  color: #ccc;
}

.checkbox-group input[type="checkbox"] {
  width: 15px;
  height: 15px;
  accent-color: #4f46e5;
}

/* Start research button */
#bottone5 {
  align-items: center;
  background: linear-gradient(135deg, #58a4b0 0%, #4a90e2 100%);
  border: 1px solid rgba(0, 0, 0, 0);
  border-radius: 0.25rem;
  box-shadow: rgba(0, 0, 0, 0.3) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 1);
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui, -apple-system, system-ui, "Helvetica Neue", Helvetica,
    Arial, sans-serif;
  font-size: 16px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  min-height: 3rem;
  padding: calc(0.875rem - 1px) calc(1.5rem - 1px);
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
  box-shadow: rgba(0, 0, 0, 0.5) 0 4px 12px;
  color: rgba(0, 0, 0, 0.8);
}

#bottone5:hover {
  transform: translateY(-1.5px);
}

#bottone5:active {
  background-color: #f0f0f1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.7);
  transform: translateY(0);
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  #header {
    height: 150px;
  }

  .logo {
    height: 90px; /* Increased from 60px for bigger logo on mobile */
  }

  .btn-github {
    top: 10px;
    left: 10px;
    padding: 0.5rem 0.75rem;
    font-size: 0.75rem;
  }

  .dark-theme-toggle {
    top: 10px;
    right: 10px;
  }

  .page-container {
    padding: 10px;
  }

  .search-card {
    padding: 20px 16px;
    gap: 16px;
  }

  .checkbox-group {
    flex-direction: column;
    gap: 8px;
  }

  .checkbox-group label {
    font-size: 14px;
  }

  #bottone5 {
    font-size: 14px;
    padding: calc(0.75rem - 1px) calc(1.25rem - 1px);
  }
}

/* Dark mode toggle script (add to script section if needed) */
/* Note: Implement dark mode toggle in Vue script to add/remove 'dark-mode' class on body or .content */
</style>
