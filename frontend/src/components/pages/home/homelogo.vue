<script setup>

</script>

<template>
    <div class = hero-logo>
    <img src="/homepagelogo.png" alt="STOCKFA Logo" class="logo" />
    </div>
</template>

<style scoped>
  .logo {
        width: 100%;      
        max-width: 600px; 
        height: auto;          
        image-rendering: -webkit-optimize-contrast;
        filter: drop-shadow(6px 6px 6px rgba(0, 0, 0, 0.5));
        margin-top: 20px;      
    }

  .hero-logo {
   position: fixed;
  top: -170px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  width: 600px;
  max-width: 90vw;
}
</style>