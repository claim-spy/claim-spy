<script setup>
import AppSidebar from '@/components/AppSidebar.vue'
import { SidebarProvider } from '@/components/ui/sidebar'
import TopBar from './TopBar.vue';

import { ref, provide, watch } from 'vue'
import { useRoute } from 'vue-router';

const route = useRoute()

const pageTitle = ref('')
provide('pageTitle', pageTitle)

watch(() => route.fullPath, () => {
  pageTitle.value = ''
})
</script>

<template>
    <div class="w-[100%]">
        <SidebarProvider>
            <AppSidebar />
            <div class="flex-col w-[100%]">
                <TopBar :title="pageTitle"/>
                <main class="w-[100%]">
                    <RouterView  class="mx-13.5 my-5" />
                </main>
            </div>
        </SidebarProvider>
    </div>
</template>
