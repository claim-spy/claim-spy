<template>
  <div class="flex justify-center items-center h-[100%]">
    <Card class="w-[380px]">
      <CardHeader>
        <h2 class="text-2xl font-bold text-center">Create a ClaimSpy account</h2>
      </CardHeader>
      <CardContent>
          <form class="grid gap-4" @submit.prevent="handleSignup">
            <div class="grid gap-1">
              <Label for="email">Username</Label>
              <Input
                id="username"
                v-model="username"
                type="text"
                required
                placeholder="your_username"
              />
            </div>
            <div class="grid gap-1">
              <Label for="email">Email address</Label>
              <Input
                id="email"
                v-model="email"
                type="email"
                required
                placeholder="you@example.com"
              />
            </div>
            <div class="grid gap-1">
              <Label for="password">Password</Label>
              <Input
                id="password"
                v-model="password"
                type="password"
                required
                placeholder="••••••••"
              />
            </div>
            <Button type="submit" class="w-full" :disabled="loading">
              {{ loading ? 'Signing in...' : 'Login' }}
            </Button>
            <p v-if="error" class="text-red-500 text-sm text-center">
              {{ error }}
            </p>
          </form>
      </CardContent>
    </Card>
  </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { makeApiRequest } from '@/utils'
  
  import { Card, CardHeader, CardContent } from '@/components/ui/card'
  import { Input } from '@/components/ui/input'
  import { Label } from '@/components/ui/label'
  import { Button } from '@/components/ui/button'
  import { useRouter } from 'vue-router'
  import { useUser } from '@/composables/useUser'
  
  const email = ref('')
  const password = ref('')
  const loading = ref(false)
  const error = ref(null)
  
  const router = useRouter()
  const {setUser} = useUser()
  const handleSignup = async () => {
    error.value = null
    loading.value = true
    try {
      const response = await makeApiRequest({
        endpoint: 'users/',
        method: 'POST',
        body: { username: username.value, email: email.value, password: password.value },
        useAccessToken: false,
      })

      localStorage.setItem('access_token', response.access);
      localStorage.setItem('refresh_token', response.refresh);
      setUser(response.user)
      router.push({name:"Charts"})
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }
  </script>
  