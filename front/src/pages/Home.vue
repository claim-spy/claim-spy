<template>
<div>
  Home, bonjour {{ userStore.userToString() }}
</div>
</template>

<script setup>
import {useUserStore} from "@/stores/user.js";

const userStore = useUserStore()
</script>

<style scoped>

</style>