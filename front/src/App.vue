<template>
  <Toaster />
  <RouterView />
</template>

<script setup>
import 'vue-sonner/style.css'
import { Toaster } from 'vue-sonner';
import './index.css';
</script>
<style>
#app {
  margin: 0;
  padding: 0;
  display: block; /* Or use any other display property based on your needs */
  width: 100%;
  height: 100vh; 
  max-width: none;
}
</style>
