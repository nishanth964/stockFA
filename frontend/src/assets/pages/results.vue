<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
const ticker = route.query.ticker || '';
const qualitative = route.query.qualitative === 'true';
const quantitative = route.query.quantitative === 'true';
const valuation = route.query.valuation === 'true';
</script>

<template>
  <div class="results-page">
    <h1>Research Results for {{ ticker.toUpperCase() }}</h1>
    <div v-if="qualitative" class="section">
      <h2>Qualitative Data</h2>
      <p>Placeholder for qualitative analysis (e.g., company news, management quality).</p>
    </div>
    <div v-if="quantitative" class="section">
      <h2>Quantitative Data</h2>
      <p>Placeholder for quantitative metrics (e.g., financial ratios, charts).</p>
    </div>
    <div v-if="valuation" class="section">
      <h2>Valuation Models</h2>
      <p>Placeholder for valuation results (e.g., DCF, comparables).</p>
    </div>
    <button @click="$router.push('/')">Back to Home</button>
  </div>
</template>

<style scoped>
.results-page {
  padding: 20px;
  font-family: 'Inter', sans-serif;
}

.section {
  margin-bottom: 20px;
}
</style>