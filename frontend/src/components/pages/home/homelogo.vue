<script setup>

</script>

<template>
    <div class = hero-logo>
      <img src="/homepagelogo.png" alt="STOCKFA Logo" class="logo"/>
    </div>
</template>

<style scoped>
  .logo {
      width: 100%;      
      height: auto;          
      image-rendering: -webkit-optimize-contrast;
      filter: drop-shadow(6px 6px 6px rgba(0, 0, 0, 0.5));
      margin-top: 20px;  
      max-width: 100;
    }

  .hero-logo {
      display: flex;
      justify-content: center;
      position: fixed;
      top: -150px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 1000;
      width: 600px;
      padding: 1rem;
}

</style>