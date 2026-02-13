<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const ticker = route.query.ticker || '';
const qualitative = route.query.qualitative === 'true';
const quantitative = route.query.quantitative === 'true';
const valuation = route.query.valuation === 'true';

const overviewRef = ref(null);
const qualitativeRef = ref(null);
const quantitativeRef = ref(null);
const valuationRef = ref(null);
const isOpen = ref(false);
const results = ref({
  qualitative: '',
  quantitative: '',
  valuation: ''
});
const loading = ref(false);

const scrollTo = (el) => {
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
  }
};

const toggleSidebar = () => {
  isOpen.value = !isOpen.value;
};

const fetchResults = async () => {
  loading.value = true;
  try {
    const response = await fetch('http://localhost:5000/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        ticker,
        qualitative,
        quantitative,
        valuation,
      }),
    });
    if (response.ok) {
      const data = await response.json();
      results.value = data;
    } else {
      console.error('Failed to fetch results');
    }
  } catch (error) {
    console.error('Error fetching results:', error);
  }
  loading.value = false;
};

// Fetch results on component mount
import { onMounted } from 'vue';
onMounted(() => {
  fetchResults();
});
</script>

<template>
  <div class="results-page">
    <!-- Sidebar -->
    <div class="sidebar" :class="{ open: isOpen }">
      <div class="toggle-area" @click="toggleSidebar">
        <span class="arrow">{{ isOpen ? '&lt;' : '&gt;' }}</span>
      </div>
      <div v-show="isOpen" class="nav-content">
        <h3>Navigate</h3>
        <ul>
          <li><a @click="scrollTo(overviewRef)">Overview</a></li>
          <li><a @click="scrollTo(qualitativeRef)">Qualitative</a></li>
          <li><a @click="scrollTo(quantitativeRef)">Quantitative</a></li>
          <li><a @click="scrollTo(valuationRef)">Valuation</a></li>
        </ul>
        <button @click="$router.push('/')">Back to Home</button>
      </div>
    </div>
    <div class="content">
      <h1>Research Results for {{ ticker.toUpperCase() }}</h1>
      <div ref="overviewRef" class="section">
        <h2>Overview</h2>
        <p>Summary of the research for {{ ticker.toUpperCase() }}.</p>
      </div>
      <div v-if="qualitative" ref="qualitativeRef" class="section">
        <h2>Qualitative Data</h2>
        <p v-if="loading">Loading...</p>
        <p v-else>{{ results.qualitative || 'Placeholder for qualitative analysis (e.g., company news, management quality).' }}</p>
      </div>
      <div v-if="quantitative" ref="quantitativeRef" class="section">
        <h2>Quantitative Data</h2>
        <p v-if="loading">Loading...</p>
        <p v-else>{{ results.quantitative || 'Placeholder for quantitative metrics (e.g., financial ratios, charts).' }}</p>
      </div>
      <div v-if="valuation" ref="valuationRef" class="section">
        <h2>Valuation Models</h2>
        <p v-if="loading">Loading...</p>
        <p v-else>{{ results.valuation || 'Placeholder for valuation results (e.g., DCF, comparables).' }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.results-page {
  font-family: 'Inter', sans-serif;
  position: relative;
}

.content {
  padding: 20px;
  margin-left: 0;
  transition: margin-left 0.3s ease;
}

.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  width: 40px;
  height: 40px;
  background: #f8f9fa;
  border: 1px solid #ccc;
  border-radius: 4px;
  z-index: 1001;
  transition: all 0.3s ease;
}

.sidebar.open {
  width: 250px;
  height: 100vh;
  border: none;
  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
}

.toggle-area {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 20px;
}

.nav-content {
  padding: 20px;
  padding-top: 60px;
}

.nav-content h3 {
  margin-top: 0;
  color: #333;
}

.nav-content ul {
  list-style: none;
  padding: 0;
}

.nav-content li {
  margin: 10px 0;
}

.nav-content a {
  text-decoration: none;
  color: #007bff;
  font-weight: 600;
  cursor: pointer;
}

.nav-content a:hover {
  color: #0056b3;
}

.nav-content button {
  margin-top: 20px;
  padding: 10px 15px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.nav-content button:hover {
  background: #0056b3;
}

.section {
  margin-bottom: 40px;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.section h2 {
  color: #333;
}
</style>