<script setup>
import { useRouter } from 'vue-router';
import SidebarTrigger from '@/components/ui/sidebar/SidebarTrigger.vue';
import Separator from '@/components/ui/separator/Separator.vue';

const router = useRouter()

defineProps({
  title: String
})
</script>

<template>
    <div class="z-10 bg-white/100 sticky top-0 pt-1.5 ">
        <div class="flex mb-1.5 space-x-2">
            <SidebarTrigger class="ml-2 mt-1.5"/>
            <Separator class="min-h-9" orientation="vertical"/>
            <h1 class="text-3xl ">{{ title? title : router.currentRoute.value.meta.title }}</h1>
            </div>
        <Separator />
    </div>
</template>