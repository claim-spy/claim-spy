<template>
<div>
  Value: {{ value }}
</div>
</template>

<script setup>
import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";

const value = ref(0)

onMounted((() => {
  value.value = useRoute().params
}))
</script>

<style scoped>

</style>