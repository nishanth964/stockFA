<script setup>

</script>

<template>
    <div class = hero-logo>
    <img src="/homepagelogo.png" alt="STOCKFA Logo" class="logo" />
    </div>
</template>

<style scoped>
    .hero-logo {
        display: flex;
        flex-direction: column; 
        align-items: center;    
        justify-content: center;
        padding: 40px 20px;
        text-align: center;
    }
  .logo {
        width: 100%;      
        max-width: 600px; 
        height: auto;          
        image-rendering: -webkit-optimize-contrast;
        filter: drop-shadow(6px 6px 6px rgba(0, 0, 0, 0.5));
        margin-top: 20px;      
    }
</style>